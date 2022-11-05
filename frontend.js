function sendPieGraph(jsonBlob){
    let loadData=JSON.parse(jsonBlob)
    let layout = {
      title: 'Weekly Financial Savings Pie Chart',
      height: 400,
      width: 500
    };
  Plotly.newPlot('piegraph',loadData,layout)
}
function sendLineGraph(jsonBlob) {
    let location=document.getElementById("locText").value
    let loadData=JSON.parse(jsonBlob)
    let layout = {
        title: 'Annual Financial Savings Graph',
        xaxis: {title: "Years"},
        yaxis: {title: "Amount of Money"},
        type:'scatter'
    };
    Plotly.newPlot('linegraph', loadData, layout);
}

function getData(){
    ajaxGetRequest('/piegraph',sendPieGraph);
    ajaxGetRequest('/barchart',graphBarChart);
  }
  
  function getLocData(){
    let id=document.getElementById("locText")
    let string=JSON.stringify(id["value"])
    ajaxPostRequest('/linegraph', string, sendLineGraph);
  }