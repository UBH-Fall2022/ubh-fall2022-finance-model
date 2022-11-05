import bottle
import processing
import json

#routing static files
@bottle.route("/")
def index():
  return bottle.static_file("index.html",".")
@bottle.route("/index.html")
def index():
  return bottle.static_file("index.html",".")
@bottle.route("/dashboard.html")
def dashboard():
  return bottle.static_file("dashboard.html",".")
@bottle.route("/about_us.html")
def aboutus():
  return bottle.static_file("about_us.html",".")
@bottle.route('/<filename>.css')
def stylesheets(filename):
    return bottle.static_file('{}.css'.format(filename),root="")
@bottle.route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return bottle.static_file(filename, root='images/', mimetype='image/png')
@bottle.route("/ajax.js")
def javascript():
  return bottle.static_file("ajax.js",".")
@bottle.route("/frontend.js")
def graphJavascript():
  return bottle.static_file("frontend.js",".")
#serving graphs
@bottle.post("/piegraph")
def sendPieGraph():
    content=bottle.request.body.read().decode()
    textbox=json.loads(content)
    data = processing.portions(float(textbox))
    pie_values = [{
    "values": [data[0], data[1], data[2]],
    "labels": ['Needs', 'Wants', 'Savings'],
    "type": 'pie'
    }]
    return json.dumps(pie_values)
@bottle.post("/linegraph")
def sendLineGraph():
    content=bottle.request.body.read().decode()
    textbox=json.loads(content)
    xvalues= range(2022, 2033)
    yvalues= processing.annualAmount(float(textbox[0]),float(textbox[1]))
    line_values = [{"x":xvalues,"y":yvalues,"type":"line"}]
    return json.dumps(line_values)

bottle.run(host = "0.0.0.0",port = 8080)