from schemer import *


class Person(Table):
    name = "Table"

print dir(type(Person))
print dir(Table)
print dir(Person)

Person.VarChar("firstname")
Person.VarChar("lastname")

print "fields: ------"
print Person.fields

AddTable(Person)

print all_tables

