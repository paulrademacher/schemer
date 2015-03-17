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


Table.SmallInt = CreateFieldMethod('smallint')
Table.Integer = CreateFieldMethod('integer')
Table.BigInt = CreateFieldMethod('bigint')
Table.Decimal = CreateFieldMethod('decimal')
Table.Numeric = CreateFieldMethod('numeric')
Table.Real = CreateFieldMethod('real')
Table.DoublePrecision = CreateFieldMethod('doubleprecision')
Table.SmallSerial = CreateFieldMethod('smallserial')
Table.Serial = CreateFieldMethod('serial')
Table.BigSerial = CreateFieldMethod('bigserial')
Table.Money = CreateFieldMethod('money')
Table.VarChar = CreateFieldMethod('varchar(50)')  ### REQUIRES LIMIT
Table.Char = CreateFieldMethod('char')  #### REQUIRES LEN
Table.Text = CreateFieldMethod('text')
Table.Boolean = CreateFieldMethod('boolean')
Table.Date = CreateFieldMethod('date')
Table.Json = CreateFieldMethod('json')
Table.TimeTz = CreateFieldMethod('timetz')
Table.TimeStamp = CreateFieldMethod('timestamp')
Table.TimeStampTz = CreateFieldMethod('timestamptz')
Table.Uuid = CreateFieldMethod('uuid')

