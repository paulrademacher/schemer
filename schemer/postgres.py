from collections import namedtuple
import os
import subprocess

import db

def parse_postgres_output(output, has_name_row, has_separator_row):
    lines = output.split('\n')
    first_row_line = 2 if has_separator_row else 1
    if has_name_row:
        name_row = lines[0].strip()
        headers_raw = lines[1].strip()
        first_row_line += 1
    else:
        name_row = ''
        headers_raw = lines[0].strip()

    lines = lines[first_row_line:]

    headers = [h.strip() for h in headers_raw.split('|')]
    rows = []
    for line in lines:
        if (line.count('|') + 1) != len(headers):
            print 'THIS IS NOT FIELDS:', line
            print (line.count('|') + 1), '!=', len(headers)
            break
        fields = [f.strip() for f in line.split('|')]
        row_object = {}
        for (index, field) in enumerate(fields):
            if field != '':
                row_object[headers[index]] = field
        rows.append(row_object)

    return {'headers': headers, 'rows': rows}


class Row():
    pass

Table = namedtuple('Table', ['headers', 'rows'])


def parse_examine_script_output(output):
    lines = output.split('\n')
    headers = lines[0].split('|')
    rows = []
    for line in lines[1:]:
        fields = line.split('|')
        if len(fields) != len(headers):
            # We're done parsing.
            break
        row = Row()
        for (index, field) in enumerate(fields):
            setattr(row, headers[index], field)
        rows.append(row)
    return Table(headers=headers, rows=rows)


def parse_examine_script_database_output(output):
    return parse_examine_script_output(output)


def parse_examine_script_table_output(output):
    return parse_examine_script_output(output)


def exec_examine(database_name, table_name):
    this_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(this_path, "scripts/examine-db.sh")

    if table_name:
        output = subprocess.check_output([script_path, database_name, table_name])
        parsed = parse_examine_script_table_output(output)
    else:
        output = subprocess.check_output([script_path, database_name])
        parsed = parse_examine_script_database_output(output)
    return parsed


def add_column_to_table(table, column_name, postgres_type):
    if postgres_type == 'smallint':
        table.SmallInt(column_name)
    if postgres_type == 'integer':
        table.Integer(column_name)
    if postgres_type == 'bigint':
        table.BigInt(column_name)
    if postgres_type == 'numeric':
        table.Numeric(column_name)
    if postgres_type == 'real':
        table.Real(column_name)
    if postgres_type == 'double precision':
        table.DoublePrecision(column_name)
#        if row.Type == 'smallint': # TODO: serial
#        if row.Type == 'integer': # TODO: serial
#        if row.Type == 'bigint': # TODO: serial
    if postgres_type == 'money':
        table.Money(column_name)
    if postgres_type == 'character varying(50)': # TODO: parse width
        table.VarChar(column_name)
    if postgres_type == 'character(1)':  # TODO: parse width
        table.Char(column_name)
    if postgres_type == 'text':
        table.Text(column_name)
    if postgres_type == 'boolean':
        table.Boolean(column_name)
    if postgres_type == 'date':
        table.Date(column_name)
    if postgres_type == 'json':
        table.Json(column_name)
    if postgres_type == 'time with time zone':
        table.TimeTz(column_name)
    if postgres_type == 'timestamp without time zone':
        table.TimeStamp(column_name)
    if postgres_type == 'timestamp with time zone':
        table.TimeStampTz(column_name)
    if postgres_type == 'uuid':
        table.Uuid(column_name)

def parse_existing_db(db_name):
    database = db.Database(db_name)
    parsed = exec_examine(db_name, None)
    for row in parsed.rows:
        if row.Type == 'table':
            table = database.Table(row.Name)
            for table_row in exec_examine(db_name, row.Name).rows:
                add_column_to_table(table, table_row.Column, table_row.Type)

    return database
