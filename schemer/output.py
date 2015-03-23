from __future__ import print_function
import os

import jinja2

import diff

# http://stackoverflow.com/a/4060259
__location__ = os.path.realpath(os.path.join(os.getcwd(),
    os.path.dirname(__file__)))


def write_template(template_name, data):
    contents = open(os.path.join(__location__, template_name)).read()
    template = jinja2.Template(contents)
    return template.render(**data)


def test():
    print("TEST")


def write_script(db, file):
    print("WRITING", db, file)
    data = {
        'dbname': db.name,
        'tables': db.tables,
    }
    print(write_template("postgres-main.tmpl", data), file=file)
