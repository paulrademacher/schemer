all_tables = []

class Table(object):
    def __init__(self, name):
        self.name = name
        self.fields = []

        global all_tables
        all_tables.append(self)

    def AddField(self, obj):
        self.fields.append(obj)


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

def OutputAll():
    print all_tables
