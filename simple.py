from flask import Flask, render_template
from tangled_up_in_unicode import name
import pandas as pd

app = Flask(__name__)


d = pd.read_csv("marvel_cinematic_universe.csv", header = 0)

mcu = {}

mcu['shows'] = []
mcu['films'] = []

for film in d[d['media'] == "Film"].property:
    mcu['films'].append({'name': film})

for show in d[d['media'] == 'Series'].property:
    mcu['shows'].append({'name': show})


@app.route("/")
def index():
  return render_template("index.html")



@app.route('/properties/<property_type>')
def properties(property_type):
  html = f'<h1>List of {property_type}</h1>'
  html += '<ul>'
  for idx, property in enumerate(mcu[property_type]):
    html += f'''<li><a href = '/properties/{property_type}/{idx}'>{property['name']}</a></li>'''
  html += '</ul>'
  return html

@app.route('/properties/<property_type>/<int:property_id>')
def property(property_type, property_id):
  property = mcu[property_type][property_id]
  html = f'''<h1>{property['name']}</h1>'''

  return html
#To run this:
#~export FLASK_APP={{file_name.py}}~
#~flask run~