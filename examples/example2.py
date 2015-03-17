from schemer import *

Person = Table('Person')

Person.SmallInt('age')
Person.VarChar('firstname')
Person.VarChar('lastname')

print Person
print Person.name
print Person.fields

OutputAll()
