import output

class Database(object):
    def __init__(self, name):
        self.name = name
        self.tables = []

    def Table(self, name):
        table = Table(name)
        self.tables.append(table)
        return table

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "db(%s):\n  %s" % (self.name, '\n  '.join([str(t) for t in self.tables]))

    def write_script(self, file):
        output.write_script(self, file)


class Table(object):
    def __init__(self, name):
        self.name = name
        self.fields = []

    def AddField(self, obj):
        self.fields.append(obj)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "table(%s): %s" % (self.name, self.fields)


def CreateFieldMethod(postgres):
    def FieldMethod(self, name):
        self.AddField({'name': name, 'postgres': postgres})
    return FieldMethod


Table.SmallInt = CreateFieldMethod('SMALLINT')
Table.Integer = CreateFieldMethod('INTEGER')
Table.BigInt = CreateFieldMethod('BIGINT')
Table.Decimal = CreateFieldMethod('DECIMAL')
Table.Numeric = CreateFieldMethod('NUMERIC')
Table.Real = CreateFieldMethod('REAL')
Table.DoublePrecision = CreateFieldMethod('DOUBLE PRECISION')
Table.SmallSerial = CreateFieldMethod('SMALLSERIAL')
Table.Serial = CreateFieldMethod('SERIAL')
Table.BigSerial = CreateFieldMethod('BIGSERIAL')
Table.Money = CreateFieldMethod('MONEY')
Table.VarChar = CreateFieldMethod('VARCHAR(50)')  ### REQUIRES LIMIT
Table.Char = CreateFieldMethod('CHAR')  #### REQUIRES LEN
Table.Text = CreateFieldMethod('TEXT')
Table.Boolean = CreateFieldMethod('BOOLEAN')
Table.Date = CreateFieldMethod('DATE')
Table.Json = CreateFieldMethod('JSON')
Table.TimeTz = CreateFieldMethod('TIMETZ')
Table.TimeStamp = CreateFieldMethod('TIMESTAMP')
Table.TimeStampTz = CreateFieldMethod('TIMESTAMPTZ')
Table.Uuid = CreateFieldMethod('UUID')

