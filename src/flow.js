document.body.onload = setup;

var y_flow=[];
var x_time=[];


function setup() {
        getdata();
}

function getdata() {


    $.ajax({
        type:     "get",
        url:      "mysql.php",
	aysnc : false,
	success: function(result) {
	console.log("Success");
	var data=$.parseJSON(result);
	console.log(data);
	for (var i = 0; i < data.length; i++) {
   		 y_flow[i]= parseInt(data[i].flow);
		 x_time[i]= data[i].time;
	}
	console.log(y_flow);
	console.log(x_time);
	plot();
	},
	error: function(a,exception){
	console.log("error");
	}
});
}


function plot() {
GRAPH = document.getElementById('graph');
var data = [
{
    x: x_time,
    y: y_flow,
    type: 'bar',
    name: '90%',
    marker: {}
}
];

var layout = {
      title: {
        text:'The last 12  instances.',
        font: {
          family: 'Courier New, monospace',
          size: 24
        },
        xref: 'paper',
        x: 0.5,
      },
      xaxis: {
        title: {
          text: 'Time',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
        type: 'category'
      },
      yaxis: {
        title: {
          text: 'Hourly Flow Rate',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        }
      }

}


Plotly.newPlot(GRAPH, data, layout);
}

