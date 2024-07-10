<?php
// sendmessage.php

// Get the POST data
$roomId = $_POST['roomId'];
$message = $_POST['message'];

$chatLogFile = "chat_logs/" . $roomId . ".txt";

if (!file_exists($chatLogFile)) {
    http_response_code(404);
    echo json_encode(array("error" => "Room ID not found"));
    exit();
}

// Append the message to the chat log file
file_put_contents($chatLogFile, $message . PHP_EOL, FILE_APPEND);

$response = array("status" => "success");
echo json_encode($response);
?>
