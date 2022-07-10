from flask import Flask
from tangled_up_in_unicode import name

app = Flask(__name__)

mcu = {}
mcu['films'] = [{'name': 'Iron Man'}, {'name': 'Incredible Hulk'}]
mcu['shows'] = [{'name': 'Wandavisions'}]

@app.route("/")
def hello_world():
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <h1>Welcome to the MCU!</h1>
        <h2>Feature Films</h2>
            <ul>
            <li><a href = '/properties/films'>Films</a></li>
            <li><a href = '/properties/shows'>TV Shows</a></li>
            </ul>
      </body>
    </html>
    '''



@app.route('/properties/<property_type>')
def properties(property_type):
  html = f'<h1>List of {property_type}</h1>'
  html += '<ul>'
  for idx, property in enumerate(mcu[property_type]):
    html += f'''<li><a href = '/properties/{property_type}/{idx}'>{property["name"]}</a></li>'''
  html += '</ul>'
  return html

@app.route('/properties/<property_type>/<int:property_id>')
def property(property_type, property_id):
  property = mcu[property_type][property_id]
  html = f'''<h1>{property["name"]}</h1>'''

  return html
#To run this:
#~export FLASK_APP = {{file_name.py}}~
#~flask run~