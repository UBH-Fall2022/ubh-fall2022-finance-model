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
  
function getGraphs(){
    let id=document.getElementById("annual");
    let id2=document.getElementById("sc");
    let string=JSON.stringify([id["value"],id2["value"]]);
    ajaxPostRequest('/linegraph', string, sendLineGraph);
    id = document.getElementById("weekly");
    string=JSON.stringify(id["value"]);
    ajaxPostRequest('/piegraph', string, sendPieGraph);
}