TEST = """ table_catalog | table_schema | table_name | column_name | ordinal_position | column_default | is_nullable |     data_type     | character_maximum_length | character_octet_length | numeric_precision | numeric_precision_radix | numeric_scale | datetime_precision | interval_type | interval_precision | character_set_catalog | character_set_schema | character_set_name | collation_catalog | collation_schema | collation_name | domain_catalog | domain_schema | domain_name | udt_catalog | udt_schema | udt_name | scope_catalog | scope_schema | scope_name | maximum_cardinality | dtd_identifier | is_self_referencing | is_identity | identity_generation | identity_start | identity_increment | identity_maximum | identity_minimum | identity_cycle | is_generated | generation_expression | is_updatable
---------------+--------------+------------+-------------+------------------+----------------+-------------+-------------------+--------------------------+------------------------+-------------------+-------------------------+---------------+--------------------+---------------+--------------------+-----------------------+----------------------+--------------------+-------------------+------------------+----------------+----------------+---------------+-------------+-------------+------------+----------+---------------+--------------+------------+---------------------+----------------+---------------------+-------------+---------------------+----------------+--------------------+------------------+------------------+----------------+--------------+-----------------------+--------------
 schemer       | public       | commits    | shalong     |                1 |                | YES         | character varying |                       50 |                    200 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |                |                |               |             | schemer     | pg_catalog | varchar  |               |              |            |                     | 1              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
 schemer       | public       | commits    | shashort    |                2 |                | YES         | character varying |                       50 |                    200 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |                |                |               |             | schemer     | pg_catalog | varchar  |               |              |            |                     | 2              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
 schemer       | public       | commits    | comment     |                3 |                | YES         | text              |                          |             1073741824 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |               |                |               |             | schemer     | pg_catalog | text     |               |              |            |                     | 3              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
(3 rows)"""

TEST_WITH_NAME_ROW = """                                Table "public.commits"
  Column  |         Type          | Modifiers | Storage  | Stats target | Description
----------+-----------------------+-----------+----------+--------------+-------------
 shalong  | character varying(50) |           | extended |              |
 shashort | character varying(50) |           | extended |              |
 comment  | text                  |           | extended |              |
Has OIDs: no
"""

def parse_postgres_output(output, has_name_row):
    lines = output.split('\n')
    if has_name_row:
        name_row = lines[0].strip()
        headers_raw = lines[1].strip()
        lines = lines[3:]  # Skip the ---+----+---- divider
    else:
        name_row = ''
        headers_raw = lines[0].strip()
        lines = lines[2:]  # Skip the ---+----+---- divider

    headers = [h.strip() for h in headers_raw.split('|')]
    print headers
    print len(lines)
    data = []
    for line in lines:
        if (line.count('|') + 1) != len(headers):
            print "THIS IS NOT FIELDS:", line
            print (line.count('|') + 1), "!=", len(headers)
            break
        fields = [f.strip() for f in line.split('|')]
        row_object = {}
        for (index, field) in enumerate(fields):
            row_object[headers[index]] = field
        data.append(row_object)

    print "----"
    return data

print parse_postgres_output(TEST, False)
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print parse_postgres_output(TEST_WITH_NAME_ROW, True)
