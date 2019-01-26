function buildMetadata(sample) {
  // Complete the following function that builds the metadata panel
  // Use `d3.json` to fetch the app.py metadata for a sample (Flask Route)
  d3.json(`/metadatatotals${sample}`).then((data) => {
    // Use d3 to select the html panel with id of `#sample-metadata`
      var Panel = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
      Panel.html("");
    // Use `Object.entries` to add each key and value pair to the panel
      Object.entries(data).forEach(([key, value]) => {
          Panel.append("h6").text(`${key}: ${value}`);
          console.log(key, value);
          console.log('this is a key: ', key);
          console.log('this is a value: ', value);
          console.log('this is data:', data);
          console.log('this is the sample variable', sample);
      });
});
}

// Map Function Attempt 1
function buildMap(sample) {
  console.log('starting BuildMap Function', sample);
  var url = `/metadata_states${sample}`;
  console.log(url);
 
  console.log(d3.json(url));

  d3.json(url).then(function(data){
    console.log(data[0]);
    console.log(data[0]['state']['StateName']);
    var stateAbb = [];
    var stateVote = [];
    var voteSupport = [];
    var voteOppose = [];
    var percSupport = [];
    var percOppose = [];
    
     // console.log('crash before map data?')
    var mapData = [{
      type: 'choropleth',
      locationmode: 'USA-states',
      locations: (stateAbb),
      z: (stateVote),
      text: (stateAbb),
      colorscale:[['support', 'rgb(242,240,247)'], ['oppose','rgb(84,39,143)']],
    }];

    var layout = {
      title: 'Map of US test lable',
      geo: {
        scope: 'usa',
        autosize: true,
        showlegend: false}
        };

    for (var i = 0; i < data.length; i++) {
      stateAbb.push(data[i]['state']['StateAbb']);
      stateVote.push(data[i]['voteTotal']['Overall']);
      voteSupport.push(data[i]['voteTotal']['Support']);
      voteOppose.push(data[i]['voteTotal']['Oppose']);
      percSupport.push(data[i]['voteTotal']['Support_%']);
      percOppose.push(data[i]['voteTotal']['Oppose_%']);
    };
    // console.log(stateAbb);
    // console.log(stateVote);
    // console.log(voteSupport);
    // console.log(voteOppose);
    // console.log(percSupport);
    // console.log(percOppose);
  

  console.log('Please Plot Map!')
  Plotly.plot("map", mapData, layout, {responsive: true});
    
  }); 
}

// PIE CHART FOR THE SURVEY TOTALS ONLY
function pieChart(sample) {

    d3.json(`/metadatatotals${sample}`).then((data) => {
        var labels = [];
        var values = [];
        Object.entries(data).forEach(([key, value]) => {
          labels.push(key);
          values.push(value);
          console.log('pieChart labels array: ', labels);
          console.log('pieChart values array: ', values);
   
    // Build a Pie Chart
        var pieData = [{
                values : values,
                labels : labels,
                hovertext : labels,
                hoverinfo: "hovertext",
                type: "pie"
            }];
        
        var pieLayout = {
            margin: {t:0, l:0}
        };
        
        // insert in the html div ID = pie
        Plotly.plot("pie", pieData, pieLayout);       
      });
    });
  }

// Create Dropdown Menu, Populate first tables and visuals
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  console.log('test test test')
  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    const firstSample = sampleNames[0];
    buildMetadata(firstSample);
    pieChart(firstSample);
    buildMap(firstSample);
    console.log('This is the first sample used to build dashboard:  ',firstSample);
  });
}

// On Dropdown Menu Change - Update Tables and Charts
function optionChanged(newSample) {
  buildMetadata(newSample);
  pieChart(newSample);
  buildMap(newSample);
  console.log('This is the new sample passed when the dropdown selection changes',newSample);
}

// Initialize the dashboard
init();
