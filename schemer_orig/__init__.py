all_tables = set()

class Table:
    @classmethod
    def Field(cls, field_type_instance):
        print 'Field:', cls, field_type_instance

        def __str__(self):
            return "%s" % (self.name)

    fields = []


class FieldBase(object):
    def __init__(self, postgres):
        self.postgres = postgres
        self.name = ""

    def __str__(self):
        return "%s(%s)" % (self.postgres, self.name)

    def __repr__(self):
        return str(self)

    def __call__(self, calling_class, name):
        obj = {
            'name': name,
            'postgres': self.postgres,
        }

        calling_class.fields.append(obj)
        return obj


Table.SmallInt = classmethod(FieldBase('smallint'))
Table.Integer = classmethod(FieldBase('integer'))
Table.BigInt = classmethod(FieldBase('bigint'))
Table.Decimal = classmethod(FieldBase('decimal'))
Table.Numeric = classmethod(FieldBase('numeric'))
Table.Real = classmethod(FieldBase('real'))
Table.DoublePrecision = classmethod(FieldBase('doubleprecision'))
Table.SmallSerial = classmethod(FieldBase('smallserial'))
Table.Serial = classmethod(FieldBase('serial'))
Table.BigSerial = classmethod(FieldBase('bigserial'))

Table.Money = classmethod(FieldBase('money'))

Table.VarChar = classmethod(FieldBase('varchar(50)'))  ### REQUIRES LIMIT
Table.Char = classmethod(FieldBase('char'))  #### REQUIRES LEN
Table.Text = classmethod(FieldBase('text'))

Table.Boolean = classmethod(FieldBase('boolean'))
Table.Date = classmethod(FieldBase('date'))
Table.Json = classmethod(FieldBase('json'))
Table.TimeTz = classmethod(FieldBase('timetz'))
Table.TimeStamp = classmethod(FieldBase('timestamp'))
Table.TimeStampTz = classmethod(FieldBase('timestamptz'))
Table.Uuid = classmethod(FieldBase('uuid'))

# TODO: make this implicit
def AddTable(cls):
    all_tables.add(cls)

