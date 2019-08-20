function dictionary(list) {
  var map = {};
  for (var i = 0; i < list.length; ++i) {
    var ID = list[i].ID
    if (!map[ID]) {
      map[ID] = [];
      map[ID].push(list[i])
    } 

  } return map;
}


function buildMetadata(Year) {
  d3.selectAll("p").remove();
  // @TODO: Complete the following function that builds the metadata panel
  var femaleURL = `/female/years/${Year}`;
  var input = d3.select("#female-year"); 
  d3.json(femaleURL).then((data) => {
    // console.log(data)
    data.forEach((Help) => {
      // var row = d3.select("#female-year").append("p");
      //   row.text(`${Help.Name}`);  
        buildGauge(Help.Count);
      })
      
  
    // for (var i = 0; i < data.length; ++i) {
    // var d = dictionary(data)
    // console.log(d)
    // var row = input.append("p");
    // row.text((`${key}`))
    // }




      
      // console.log(data)
  });
}
    // BONUS: Build the Gauge Chart

function buildGauge(Year) {

var level = (Year * 20);

var degrees = 180 - level,
  radius = .5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);


var data = [{ type: 'scatter',
x: [0], y:[0],
 marker: {size: 28, color:'850000'},
 showlegend: false,
 name: 'Frequency of Washes',
 text: level,
 hoverinfo: 'text+name'},
{ values: [50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50],
rotation: 90,
text: ['8-9', '7-8', '6-7', '5-6', '4-5', '3-4', '2-3',
         '1-2', '0-1', ''],
textinfo: 'text',
textposition:'inside',
marker: {colors:[ 'rgba(0,128,0, .9)', 'rgba(0,128,0, .8)', 'rgba(0,128, 0, .7)', 
                  'rgba(0,128, 0, .6)', 'rgba(0,128, 0, .5)',	'rgba(0,128, 0, .4)',
                  'rgba(0,128, 0, .3)', 'rgba(0,128, 0, .2)', 'rgba(0,128, 0, .1)',
                  'rgba(255, 255, 255, 0)']},
labels: ['8-9', '7-8', '6-7', '5-6', '4-5', '3-4', '2-3',
'1-2', '0-1', ''],
hoverinfo: 'label',
hole: .5,
type: 'pie',
showlegend: false
}];

var layout = {
shapes:[{
   type: 'path',
   path: path,
   fillcolor: '850000',
   line: {
     color: '850000'
   }
 }],
title: '<b>Frequency of Belly Button Washing</b> <br> Washes per Week',
xaxis: {zeroline:false, showticklabels:false,
          showgrid: false, range: [-1, 1]},
yaxis: {zeroline:false, showticklabels:false,
          showgrid: false, range: [-1, 1]}
};

Plotly.newPlot('gauge', data, layout);
}
 
// d3.json(femaleURL).then((data) => {
//   console.log(data)
//   data.forEach((Help) => {
//     var row = d3.select("#female-year").append("p");
//       row.text(`${Help.Name}`);  
//   })


function buildCharts(Year) {
  var Names = []
  var Counts = []
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var femaleYRURL = `/female/years/${Year}`;
  d3.json(femaleYRURL).then((requests) => {
    requests.forEach((response) => {
      Names.push(response.Name)
      Counts.push(response.Count)
    var trace1 = {
      x: Names,
      y: Counts,
      mode: "markers",
      text: Names,
      marker: { size: Counts/100,
      color: Names,
      colorscale: 'Earth'}
    } 
    var data1 = [trace1]   
    Plotly.newPlot("bubble", data1);
    
  }) 

})
}

    // var topValues = response.Count.slice(0,10);
    // var topLabels = response.Name.slice(0,10);
    // var topIDs = response.Rank.slice(0,10);
    // // console.log(topVsalues)
    // var trace2 = {
    //   values: topValues,
    //   labels: topIDs,
    //   hovertext: topLabels,
    //   hoverinfo: 'hovertext',
    //   type: "pie"
    // }
    // var data2 = [trace2]

    // Plotly.newPlot("pie", data2)
  


function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  console.log(selector);
  // Use the list of sample names to populate the select options
  d3.json("/female/years").then((femaleYears) => { 
    console.log(femaleYears)
    femaleYears.forEach((Year) => {
      selector
        .append("option")
        .text(Year)
        .property("value", Year);
    });

    // Use the first sample from the list to build the initial plots
    const firstYear = femaleYears;
    buildCharts(firstYear);
    buildMetadata(firstYear);
  });
}

function optionChanged(newYear) {
  // Fetch new data each time a new sample is selected
  buildCharts(newYear);
  buildMetadata(newYear);
}

// Initialize the dashboard
init();
