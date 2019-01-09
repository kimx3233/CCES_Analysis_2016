var basemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap </a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox </a>",
    maxZoom: 18,
    id: "mapbox.outdoors",
    accessToken: API_KEY
});

var map = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});





function buildMetadata(sample) {
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
});
}

function buildMap(sample) {}

//   // Define a function we want to run once for each feature in the features array
//   // Give each feature a popup describing the place and time of the earthquake
//   function onEachFeature(feature, layer) {
//       layer.bindPopup("<h3> Magnitude: " + feature.properties.mag + "<br> Location: " + feature.properties.place +
//       "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
//   }
//   // Create a GeoJSON layer containing the features array on the earthquakeData object
//   // Run the onEachFeature function once for each piece of data in the array
//   var earthquakes = L.geoJSON(earthquakeData, {
//       pointToLayer: function(feature, place) {
//           return L.circleMarker(place);
//         },
//       style: styleInfo,
//       onEachFeature: onEachFeature
//   });

//   // Sending our earthquakes layer to the createMap function
//   createMap(earthquakes);
//   }





function createMap(earthquakes) {
  // // Creating map object
  // var myMap = L.map("map", {
  //     center: [39.8283, -98.5795],
  //     layers: [lightmap, earthquakes],
  //     zoom: 11
  //   });
    
  // // Adding tile layer
  // L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  //   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  //   maxZoom: 18,
  //   id: "mapbox.streets",
  //   accessToken: API_KEY
  // }).addTo(myMap);

  // // Map layers 
  // var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  //     attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  //     maxZoom: 18,
  //     id: "mapbox.light",
  //     accessToken: API_KEY
  // });

  // // Define a baseMaps object to hold our base layers
  // var baseMaps = {
  //   "Grayscale": lightmap
  // };
  // // Create overlay object to hold our overlay layer
  // var overlayMaps = {
  //   Earthquakes: earthquakes
  // };









