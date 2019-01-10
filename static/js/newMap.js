var link = `/metadata_states/${sample}`;

function buildMap() {
    /* data route */
  d3.json(link, function(response) {

    console.log(response);

    stateInfo = response[3];
    console.log(stateInfo);

    var states = [];

    for (var i = 0; i < 1000; i++) {
      states.push(
        L.marker([state.Lat[i], state.Long[i]]).bindPopup("<h2>" + state.StateName + "</h2><br><h3> Oppose" + response.voteTotal.Oppose + "</h3><h3> Support:" + response.voteTotal.Support + "</h3>")
      );
    }

    var stateLayer = L.layerGroup(states);

    var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.light",
      accessToken: API_KEY
    });

    var baseMap = {
        light: light,
      };
  
    var overlayMap = {
    "Sample": sample
    };
    var map = L.map("map", {
        center: [39.8283, -98.5795],
        layers: [light, sample],
        zoom: 11
    });

    L.control.layers(baseMap, overlayMap).addTo(map);
  })
};

buildMap();