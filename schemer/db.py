import output

class Database(object):
    def __init__(self, name):
        self.name = name.lower()
        self.tables = []

    def Table(self, name):
        table = Table(name)
        self.tables.append(table)
        return table

#    def __repr__(self):
#        return str(self)

    def __str__(self):
        return "db(%s):\n  %s" % (self.name, '\n  '.join([str(t) for t in self.tables]))

    def serialize(self):
        db = {}
        db['name'] = self.name
        db['tables'] = [t.serialize() for t in self.tables]
        return db

    def write_script(self, file):
        output.write_script(self, file)


class Table(object):
    def __init__(self, name):
        self.name = name.lower()
        self.fields = []

    def AddField(self, obj):
        self.fields.append(obj)

        #    def __repr__(self):
        #        return str(self)

    def serialize(self):
        table = {}
        table['name'] = self.name
        table['fields'] = self.fields
        return table

    def __str__(self):
        return "table(%s): %s" % (self.name, self.fields)


def CreateFieldMethod(postgres, postgres_code):
    def FieldMethod(self, name):
        self.AddField({'name': name.lower(), 'postgres': postgres})
    return FieldMethod


# See http://doxygen.postgresql.org/include_2catalog_2pg__type_8h.html for postgres field codes.

Table.SmallInt = CreateFieldMethod('SMALLINT', 21)
Table.Integer = CreateFieldMethod('INTEGER', 23)
Table.BigInt = CreateFieldMethod('BIGINT', 20)
Table.Decimal = CreateFieldMethod('DECIMAL', 1700)
Table.Numeric = CreateFieldMethod('NUMERIC', 1700)
Table.Real = CreateFieldMethod('REAL', 700)
Table.DoublePrecision = CreateFieldMethod('DOUBLE PRECISION', 701)
Table.SmallSerial = CreateFieldMethod('SMALLSERIAL', 21)
Table.Serial = CreateFieldMethod('SERIAL', 23)
Table.BigSerial = CreateFieldMethod('BIGSERIAL', 20)
Table.Money = CreateFieldMethod('MONEY', 790)
Table.VarChar = CreateFieldMethod('VARCHAR(50)', 1043)  ### REQUIRES LIMIT
Table.Char = CreateFieldMethod('CHAR', 1042)  #### REQUIRES LEN
Table.Text = CreateFieldMethod('TEXT', 25)
Table.Boolean = CreateFieldMethod('BOOLEAN', 16)
Table.Date = CreateFieldMethod('DATE', 1082)
Table.Json = CreateFieldMethod('JSON', 114)
Table.TimeTz = CreateFieldMethod('TIMETZ', 1266)
Table.TimeStamp = CreateFieldMethod('TIMESTAMP', 1114)
Table.TimeStampTz = CreateFieldMethod('TIMESTAMPTZ', 1184)
Table.Uuid = CreateFieldMethod('UUID', 2950)
