class Table:
    pass

all_fields = []

class Field(object):
    def __init__(self, postgres):
        self.postgres = postgres

        global all_fields
        all_fields.append(self)

    def __str__(self):
        return self.postgres

    def __repr__(self):
        return str(self)

SmallIntField = Field("smallint")
Integer = Field("integer")
BigInt = Field("bigint")
Decimal = Field("decimal")
Numeric = Field("numeric")
Real = Field("real")
DoublePrecision = Field("doubleprecision")
SmallSerial = Field("smallserial")
Serial = Field("serial")
BigSerial = Field("bigserial")

print all_fields
