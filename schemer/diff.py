from __future__ import print_function

import output

class FieldDiff(object):
    def __init__(self, table_name, field):
        self.table_name = table_name
        self.field = field

    def serialize(self):
        return {
            'table_name': self.table_name,
            'field': self.field,
        }


class Rename(object):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def serialize(self):
        return {
            'old_name': self.old_name,
            'new_name': self.new_name,
        }


class SchemaDiff(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.tables_added = []  # Array of Table.
        self.tables_deleted = []  # Array of Table.
        self.tables_changed = []
        self.tables_renamed = []  # Array of Rename.
        self.fields_added = []  # Array of FieldDiff.
        self.fields_deleted = []  # Array of FieldDiff.
        self.fields_changed = []

    def serialize(self):
        return {
            'db_name': self.db_name,

            'tables_added': [t.serialize() for t in self.tables_added],
            'tables_deleted': [t.serialize() for t in self.tables_deleted],

            'tables_renamed': [t.serialize() for t in self.tables_renamed],

            'fields_added': [f.serialize() for f in self.fields_added],
            'fields_deleted': [f.serialize() for f in self.fields_deleted],

            # TODO: fields renamed
        }

    def write_script(self, file):
        serialized = self.serialize()
        data = {
            'diff': serialized,
        }
        print(output.write_template('schema-diff.tmpl', data), file=file)


def compare_databases(db_old, db_new):
    different = False

    diff = SchemaDiff(db_new.name)

    tables_db_old = dict((t.name, t) for t in db_old.tables)
    tables_db_new = dict((t.name, t) for t in db_new.tables)

    for name in tables_db_old:
        if name not in tables_db_new:
            print("Table '%s' not in db '%s'" % (name, db_new.name))
            diff.tables_deleted.append(tables_db_old[name])
            different = True
        else:
            tables_diff = compare_tables(tables_db_old[name], tables_db_new[name], diff)
            if tables_diff:
                different = True
    for name in tables_db_new:
        if name not in tables_db_old:
            print("Table '%s' not in db '%s'" % (name, db_old.name))
            different = True
            diff.tables_added.append(tables_db_new[name])

    # If the any tables added/deleted were actually a rename.
    for added_index in reversed(range(len(diff.tables_added))):
        added = diff.tables_added[added_index]
        for deleted_index in reversed(range(len(diff.tables_deleted))):
            deleted = diff.tables_deleted[deleted_index]
            dummy_diff = SchemaDiff('')
            diff_bool = compare_tables(deleted, added, dummy_diff)
            if not diff_bool:
                print('RENAME: %s -> %s' % (deleted.name, added.name))
                print(added_index, deleted_index)
                diff.tables_renamed.append(Rename(deleted.name, added.name))
                diff.tables_deleted.pop(deleted_index)
                diff.tables_added.pop(added_index)
                break

            # TODO: detect renames in presence of field addition/deletion.

    if different:
        print("DBs are different")
    else:
        print("DBs are same")

    return diff


def compare_tables(table_old, table_new, diff):
    table_old_field_names = {f['name'] for f in table_old.fields}
    table_new_field_names = {f['name'] for f in table_new.fields}

    table_old_fields_by_name = dict((f['name'], f) for f in table_old.fields)
    table_new_fields_by_name = dict((f['name'], f) for f in table_new.fields)

    table_old_field_names_not_in_table_new = table_old_field_names - table_new_field_names
    table_new_field_names_not_in_table_old = table_new_field_names - table_old_field_names

    for field_name in table_old_field_names_not_in_table_new:
        field = table_old_fields_by_name[field_name]
        diff.fields_deleted.append(FieldDiff(table_old.name, field))

    for field_name in table_new_field_names_not_in_table_old:
        field = table_new_fields_by_name[field_name]
        diff.fields_added.append(FieldDiff(table_new.name, field))

    if len(table_old_field_names_not_in_table_new) > 0 or \
       len(table_new_field_names_not_in_table_old) > 0:
        print("Tables '%s' do not have same fields (%d vs %d)" % \
            (table_old.name, len(table_old.fields), len(table_new.fields)))

        if len(table_old_field_names_not_in_table_new) > 0:
            print("  Fields in table_old:", [f for f in table_old_field_names_not_in_table_new])
        if len(table_new_field_names_not_in_table_old) > 0:
            print("  Fields in table_new:", [f for f in table_new_field_names_not_in_table_old])
        return True
    return False
