import bottle
import processing
import json

@bottle.route("/")
def index():
  return bottle.static_file("index.html",".")

@bottle.route("/ajax.js")
def javascript():
  return bottle.static_file("ajax.js",".")

@bottle.route("/graphs.js")
def graphJavascript():
  return bottle.static_file("graphs.js",".")

@bottle.route("/piegraph")
def sendPieGraph():
    content=bottle.request.body.read().decode()
    textbox=json.loads(content)
    data = processing.portions(textbox)
    pie_values = [{
    "values": [data[0],data[1],data[2]],
    "labels": ['Needs', 'Wants', 'Savings'],
    "type": 'pie'
    }]
    return json.dumps(pie_values)

sendPieGraph()

@bottle.post("/linegraph")
def sendLineGraph():
  content=bottle.request.body.read().decode()
  textbox=json.loads(content)
  print(textbox)
  xvalues=[]
  yvalues=[]
  print(textbox)
  for key in location:
    xvalues.append(key['date'])
    yvalues.append(key['series_complete_pop_pct'])
  line_values = [{
    "x": xvalues,
    "y": yvalues,
    "type": 'scatter'
  }];
  print(line_values)
  return json.dumps(line_values)

