<?php
$servername = "199.231.93.162";
$username = "software";
$password = "B7BEE6B36BD35B773132D4E3A74C2BB5";
$db= "python";
// Create connection
$conn = new mysqli($servername, $username, $password,$db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

?>
