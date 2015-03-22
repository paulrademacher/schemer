import json
import pprint

import postgres

PSQL_OUTPUT = """ table_catalog | table_schema | table_name | column_name | ordinal_position | column_default | is_nullable |     data_type     | character_maximum_length | character_octet_length | numeric_precision | numeric_precision_radix | numeric_scale | datetime_precision | interval_type | interval_precision | character_set_catalog | character_set_schema | character_set_name | collation_catalog | collation_schema | collation_name | domain_catalog | domain_schema | domain_name | udt_catalog | udt_schema | udt_name | scope_catalog | scope_schema | scope_name | maximum_cardinality | dtd_identifier | is_self_referencing | is_identity | identity_generation | identity_start | identity_increment | identity_maximum | identity_minimum | identity_cycle | is_generated | generation_expression | is_updatable
---------------+--------------+------------+-------------+------------------+----------------+-------------+-------------------+--------------------------+------------------------+-------------------+-------------------------+---------------+--------------------+---------------+--------------------+-----------------------+----------------------+--------------------+-------------------+------------------+----------------+----------------+---------------+-------------+-------------+------------+----------+---------------+--------------+------------+---------------------+----------------+---------------------+-------------+---------------------+----------------+--------------------+------------------+------------------+----------------+--------------+-----------------------+--------------
 schemer       | public       | commits    | shalong     |                1 |                | YES         | character varying |                       50 |                    200 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |                |                |               |             | schemer     | pg_catalog | varchar  |               |              |            |                     | 1              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
 schemer       | public       | commits    | shashort    |                2 |                | YES         | character varying |                       50 |                    200 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |                |                |               |             | schemer     | pg_catalog | varchar  |               |              |            |                     | 2              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
 schemer       | public       | commits    | comment     |                3 |                | YES         | text              |                          |             1073741824 |                   |                         |               |                    |               |                    |                       |                      |                    |                   |                  |               |                |               |             | schemer     | pg_catalog | text     |               |              |            |                     | 3              | NO                  | NO          |                     |                |                    |                  |                  |                | NEVER        |                       | YES
(3 rows)"""

PSQL_OUTPUT_WITH_NAME_ROW = """                                Table "public.commits"
  Column  |         Type          | Modifiers | Storage  | Stats target | Description
----------+-----------------------+-----------+----------+--------------+-------------
 shalong  | character varying(50) |           | extended |              |
 shashort | character varying(50) |           | extended |              |
 comment  | text                  |           | extended |              |
Has OIDs: no
"""

EXAMINE_DATABASE_OUTPUT = """Schema|Name|Type|Owner
public|commits|table|paulrademacher
public|oids|table|paulrademacher
public|repos|table|paulrademacher
public|users|table|paulrademacher"""

EXAMINE_TABLE_OUTPUT ="""Column|Type|Modifiers|Storage|Stats target|Description
smallint_field|smallint||plain||
integer_field|integer||plain||
bigint_field|bigint||plain||
decimal_field|numeric||main||
numeric_field|numeric||main||
real_field|real||plain||
doubleprecision_field|double precision||plain||
smallserial_field|smallint|not null default nextval('oids_smallserial_field_seq'::regclass)|plain||
serial_field|integer|not null default nextval('oids_serial_field_seq'::regclass)|plain||
bigserial_field|bigint|not null default nextval('oids_bigserial_field_seq'::regclass)|plain||
money_field|money||plain||
varchar_field|character varying(50)||extended||
char_field|character(1)||extended||
text_field|text||extended||
boolean_field|boolean||plain||
date_field|date||plain||
json_field|json||extended||
timetz_field|time with time zone||plain||
timestamp_field|timestamp without time zone||plain||
timestamptz_field|timestamp with time zone||plain||
uuid_field|uuid||plain||"""


print postgres.parse_postgres_output(PSQL_OUTPUT, False, True)
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print postgres.parse_postgres_output(PSQL_OUTPUT_WITH_NAME_ROW, True, True)

print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print postgres.parse_examine_script_database_output(EXAMINE_DATABASE_OUTPUT)
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print postgres.parse_examine_script_table_output(EXAMINE_TABLE_OUTPUT)

print "###"
print postgres.exec_examine('schemer', None)

print "###"
print postgres.parse_existing_db('schemer')

print "----------"
print pprint.pprint(postgres.parse_existing_db('schemer').serialize())
print json.dumps(postgres.parse_existing_db('schemer').serialize())
