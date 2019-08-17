function buildMetadata(Year) {
  d3.selectAll("p").remove();
  // @TODO: Complete the following function that builds the metadata panel
  var femaleYRURL = `/female/years/${Year}`;
  d3.json(femaleYRURL).then(function(data) {
    var input = d3.select("#female-year");
      Object.entries(data).forEach(function ([key, value]) {
        var row = input.append("p");
        row.text(`${key}: ${value}`);
      })
      buildGauge(data.WFREQ);
      console.log(data.WFREQ)
  });

    // BONUS: Build the Gauge Chart

    
}
function buildGauge(sample) {

var level = (sample * 20);

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


function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var sampleURL = `/samples/${sample}`;
  d3.json(sampleURL).then(function(response){
    console.log(response)
    var trace1 = {
      x: response.otu_ids,
      y: response.sample_values,
      mode: "markers",
      text: response.otu_labels,
      marker: { size: response.sample_values,
      color: response.otu_ids,
      colorscale: 'Earth'}
    }
    var data1 = [trace1]
    
    Plotly.newPlot("bubble", data1);

    var topValues = response.sample_values.slice(0,10);
    var topLabels = response.otu_labels.slice(0,10);
    var topIDs = response.otu_ids.slice(0,10);
    console.log(topValues)
    var trace2 = {
      values: topValues,
      labels: topIDs,
      hovertext: topLabels,
      hoverinfo: 'hovertext',
      type: "pie"
    }
    var data2 = [trace2]

    Plotly.newPlot("pie", data2)
  })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  console.log(selector);
  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
