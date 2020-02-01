document.body.onload = setup;

var y_speed=[];
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
   		 y_speed[i]= parseInt(data[i].speed);
		 x_time[i]= data[i].time;
	}
	console.log(y_speed);
	console.log(x_time);
	plot();
	},
	error: function(a,exception){
	console.log("error");
	}
});
}


function plot() {
GRAPH = document.getElementById('graph2');
var data = [
{
    x: x_time,
    y: y_speed,
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
          text: 'Avergage speed',
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

