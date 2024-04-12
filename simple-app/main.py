from flask import Flask, jsonify, render_template

app = Flask(__name__)

list_of_employees = [
    {
        '_id': '0skX4zgfbx4QHHuX1tl7',
        'name': 'Abby Bacchus',
        'email': 'abby.b@enso.com',
        'gender': 'male',
        'date_of_birth': '14-05-1989'
    },
    {
        '_id': 'xLylnafOcQufnkGf8r1h',
        'name': 'Dudley Gutierrez',
        'email': 'dudley.g@enso.com',
        'gender': 'male',
        'date_of_birth': '25-09-1975'
    },
    {
        '_id': 'P6sTbOGgtj8RpUtOdLC1',
        'name': 'Pansy Jenning',
        'email': 'pansy.j@enso.com',
        'gender': 'female',
        'date_of_birth': '10-05-1965'
    },
    {
        '_id': 'V1AtNWnAMLgfUml39Niy',
        'name': 'Samuel Castro',
        'email': 'samuel.c@enso.com',
        'gender': 'male',
        'date_of_birth': '18-03-1985'
    },
    {
        '_id': '6vwjMOYBGwMTLfRswYFx',
        'name': 'Toby Morrison',
        'email': 'toby.m@enso.com',
        'gender': 'male',
        'date_of_birth': '28-01-1995'
    }
]