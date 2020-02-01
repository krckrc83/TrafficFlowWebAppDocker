<?php
	
	$result_array = array();

    $mysqli = new mysqli("db", "user", "test", "trafikverket");
	if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
	$result = $mysqli->query("SELECT * FROM trafficflow ORDER BY id DESC LIMIT 12");
	
	if ($result->num_rows > 0) {
    		while($row = $result->fetch_assoc()) {
        	array_push($result_array, $row);
    		}
	}

	$mysqli->close();
	echo json_encode($result_array);
	
?>

