function sendPieGraph(jsonBlob){
    let loadData=JSON.parse(jsonBlob)
    let layout = {
      title: 'Weekly Financial Savings Pie Chart',
      height: 400,
      width: 500
    };
    Plotly.newPlot('pie',loadData,layout)
}
function sendLineGraph(jsonBlob) {
    let loadData = JSON.parse(jsonBlob)
    let layout = {
        title: 'Annual Financial Savings Graph',
        xaxis: {title: "Years"},
        yaxis: {title: "Amount of Money"},
        type:'line'
    };
    Plotly.newPlot('line', loadData, layout);
}
function getGraphs(){
    let id=document.getElementById("annual");
    let id2=document.getElementById("sc");
    let string=JSON.stringify([id["value"],id2["value"]]);
    let id3 = document.getElementById("weekly");
    let string3 =JSON.stringify(id3["value"]);
    ajaxPostRequest('/linegraph', string, sendLineGraph);
    ajaxPostRequest("/piegraph", string3, sendPieGraph);
  }