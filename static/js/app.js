function buildMetadata(sample) {

  // Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the app.py metadata for a sample (Flask Route)
  d3.json(`/metadatatotals/${sample}`).then((data) => {
      
    // Use d3 to select the html panel with id of `#sample-metadata`
      var Panel = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
      Panel.html("");
    // Use `Object.entries` to add each key and value pair to the panel
      Object.entries(data).forEach(([key, value]) => {
          Panel.append("h6").text(`${key}: ${value}`);
          console.log(key, value);
          console.log('this is data:', data)
          console.log('this is the sample variable', sample)
      });
    
});
}


// function buildCharts(sample) {

//   // Use `d3.json` to fetch the sample data for the plots
//     d3.json(`/samples/${sample}`).then((data) => {
//         const otu_ids = data.otu_ids;
//         const otu_labels = data.otu_labels;
//         const sample_values = data.sample_values;
        
//         // console.log the otu ids, labels, and sample value
//         console.log(otu_ids, otu_labels, sample_values);
   
//     // Build a Bubble Chart using the sample data
//         var bubbleLayout = {
//             margin: { t: 0},
//             hovermode: "closest",
//             xaxis: { title: "OTU ID"}
//         };
        
//         var bubbleData = [
//             {
//                 x : otu_ids,
//                 y : sample_values,
//                 text : otu_labels,
//                 mode : "markers",
//                 marker: {
//                     size: sample_values,
//                     color: otu_ids,
//                     colorscale: "Earth"
//                 }
//             }
//         ];
        
//         // Link the Plotly.plot to the html ID = bubble
//         Plotly.plot("bubble", bubbleData, bubbleLayout);
        
        
//     // Build a Pie Chart
//         var pieData = [{
//                 values : sample_values.slice(0, 10),
//                 labels : otu_ids.slice(0, 10),
//                 hovertext : otu_labels.slice(0, 10),
//                 hoverinfo: "hovertext",
//                 type: "pie"
//             }];
        
//         var pieLayout = {
//             margin: {t:0, l:0}
//         };
        
//         // insert in the html div ID = pie
//         Plotly.plot("pie", pieData, pieLayout);
        
//  });
// }


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
    
    buildMetadata(firstSample);                 // temp hard coded to Gun BackgroundChecks_16 for trouble shooting
    
    
  });
}

function optionChanged(newSample) {

  console.log(newSample);
  

  // Fetch new data each time a new sample is selected
  
  buildMetadata(newSample);
  
  
}

// Initialize the dashboard
init();

// # GunBackgroundChecks_16 = Cces.GunBackgroundChecks_16
// # ProhibitPublication_16 = Cces.ProhibitPublication_16
// # BanAssultWeapons_16 = Cces.BanAssultWeapons_16
// # MakeCCPEasier_16 = Cces.MakeCCPEasier_16

// # # Abortion Questions
// # AlwaysAllowChoice_16 = Cces.AlwaysAllowChoice_16
// # RapeIncestorHealth_16 = Cces.RapeIncestorHealth_16
// # ProhibitMoreThan20Weeks_16 = Cces.ProhibitMoreThan20Weeks_16
// # Employersdeclinebenefits_16 = Cces.Employersdeclinebenefits_16
// # ProhibitFedFunds_16 = Cces.ProhibitFedFunds_16

// # # Gay Marriage Question
// # GayMarriage = Cces.GayMarriage