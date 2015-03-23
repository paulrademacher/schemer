import pprint

from schemer import Database
from schemer import postgres
from schemer import diff

db = Database('schemer')

repos = db.Table('repos')
repos.VarChar('Name')
repos.VarChar('UserName')
repos.VarChar('Url')  # len
repos.VarChar('RemoteOriginUrl')
repos.Boolean('Private')

users = db.Table('users')
users.VarChar('UserName')
users.VarChar('Email')

commits = db.Table('commits2')
commits.VarChar('ShaLong')
commits.VarChar('ShaShort')
commits.Text('Comment')

oids = db.Table('oids')
oids.SmallInt('SmallInt_field')
oids.Integer('Integer_field')
oids.BigInt('BigInt_field')
oids.Decimal('Decimal_field')
oids.Numeric('Numeric_field')
oids.Real('Real_field')
oids.DoublePrecision('DoublePrecision_field')
oids.SmallSerial('SmallSerial_field')
oids.Serial('Serial_field')
oids.BigSerial('BigSerial_field')
oids.Money('Money_field')
oids.VarChar('VarChar_field')
oids.Char('Char_field')
oids.Text('Text_field')
oids.Boolean('Boolean_field')
#oids.Date('Date_field')
oids.Json('Json_field')
oids.TimeTz('TimeTz_field')
oids.TimeStamp('TimeStamp_field')
oids.TimeStampTz('TimeStampTz_field')
oids.Uuid('Uuid_field')

print db

output = file('output/output.sh', 'w')
db.write_script(output)

db_from_disk = postgres.parse_existing_db('schemer')
d = diff.compare_databases(db_from_disk, db)

new_table = db.Table('new_table')
new_table.Boolean("some_new_boolean")
new_table.Integer("some_new_int")
new_table2 = db.Table('new_table2')
new_table2.Boolean("some_new_boolean")
oids.Text("yet_another_field")
d = diff.compare_databases(db_from_disk, db)

print "\nDIFF:"
pprint.pprint(d.serialize())
