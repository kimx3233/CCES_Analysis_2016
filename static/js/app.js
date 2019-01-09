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

// PIE CHART FOR THE SURVEY TOTALS ONLY
function pieChart(sample) {
//   // Use `d3.json` to fetch the sample data for the plots
    d3.json(`/metadatatotals${sample}`).then((data) => {
        var labels = [];
        var values = [];
        Object.entries(data).forEach(([key, value]) => {
          labels.push(key);
          console.log(key, ' was added to the labels array');
          values.push(value);
          console.log(value, ' was added to the values array');
          console.log('labels array: ', labels);
          console.log('values array: ', values);
   

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

// MAP FOR THE SURVEY

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

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    console.log('is this working');
    console.log('this is the firstSample variable:', firstSample);
  
    // buildCharts(firstSample);
    console.log(firstSample);
    
    buildMetadata(firstSample);
    pieChart(firstSample);
    
  });
}

// On Dropdown Menu Change - Update Tables and Charts
function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildMetadata(newSample);
  pieChart(newSample);
  console.log(newSample);
}

// Initialize the dashboard
init();
