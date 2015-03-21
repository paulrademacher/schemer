#!/bin/bash

DBNAME=$1
TABLE=$2

function usage() {
    echo USAGE: `basename $0` dbname \(table\)
    echo "  If 'table' is specified, will return columns of table."
    echo "  Otherwise, returns list of tables in db."
    exit 0
}

if [[ -z $DBNAME ]]; then usage; fi

if [[ -n $TABLE ]]
then
COMMAND="\d+ $TABLE"
else
COMMAND="\dt"
fi

echo $COMMAND | psql $DBNAME | grep \| | sed  -e 's/ *| */|/g' -e 's/  */ /g' -e 's/^ //' -e 's/ $//'
