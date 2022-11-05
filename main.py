import bottle

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
  load=data.load_data("saved_data.csv")  
  dates=processing.max_value(load,'date')
  jan_val=processing.sum_matches(load,'date',dates,'administered_janssen')
  mod_val=processing.sum_matches(load,'date',dates,'administered_moderna') 
  pfi_val=processing.sum_matches(load,'date',dates,'administered_pfizer') 
  unk_val=processing.sum_matches(load,'date',dates,'administered_unk_manuf')

  pie_values = [{
  "values": [jan_val,mod_val,pfi_val,unk_val],
  "labels": ['Janssen', 'Moderna', 'Pfizer', 'Other'],
  "type": 'pie'
  }];
  return json.dumps(pie_values)

sendPieGraph()

@bottle.post("/linegraph")
def sendLineGraph():
  content=bottle.request.body.read().decode()
  textbox=json.loads(content)
  print(textbox)
  load=data.load_data("saved_data.csv")
  location=processing.copy_matching(load,'location',textbox)
  location.sort(key=sort_Date)
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

