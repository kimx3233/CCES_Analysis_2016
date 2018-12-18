function buildMetadata(sample) {

  // Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the app.py metadata for a sample (Flask Route)
  d3.json(`/metadata/${sample}`).then((data) => {
      
    // Use d3 to select the html panel with id of `#sample-metadata`
      var Panel = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
      Panel.html("");
    // Use `Object.entries` to add each key and value pair to the panel
      Object.entries(data).forEach(([key, value]) => {
          Panel.append("h6").text(`${key}: ${value}`);
          console.log(key, value);
      });
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
});
}


function buildCharts(sample) {

  // Use `d3.json` to fetch the sample data for the plots
    d3.json(`/samples/${sample}`).then((data) => {
        const otu_ids = data.otu_ids;
        const otu_labels = data.otu_labels;
        const sample_values = data.sample_values;
        
        // console.log the otu ids, labels, and sample value
        console.log(otu_ids, otu_labels, sample_values);
   
    // Build a Bubble Chart using the sample data
        var bubbleLayout = {
            margin: { t: 0},
            hovermode: "closest",
            xaxis: { title: "OTU ID"}
        };
        
        var bubbleData = [
            {
                x : otu_ids,
                y : sample_values,
                text : otu_labels,
                mode : "markers",
                marker: {
                    size: sample_values,
                    color: otu_ids,
                    colorscale: "Earth"
                }
            }
        ];
        
        // Link the Plotly.plot to the html ID = bubble
        Plotly.plot("bubble", bubbleData, bubbleLayout);
        
        
    // Build a Pie Chart
        var pieData = [{
                values : sample_values.slice(0, 10),
                labels : otu_ids.slice(0, 10),
                hovertext : otu_labels.slice(0, 10),
                hoverinfo: "hovertext",
                type: "pie"
            }];
        
        var pieLayout = {
            margin: {t:0, l:0}
        };
        
        // insert in the html div ID = pie
        Plotly.plot("pie", pieData, pieLayout);
        
 });
}


function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

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
