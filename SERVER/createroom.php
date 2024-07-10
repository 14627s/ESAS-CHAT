<?php
// createroom.php

function generateRoomId() {
    return uniqid();
}

$roomId = generateRoomId();
$chatLogFile = "chat_logs/" . $roomId . ".txt";

// Create a directory for chat logs if it doesn't exist
if (!is_dir('chat_logs')) {
    mkdir('chat_logs', 0777, true);
}

// Create an empty chat log file for the new room
file_put_contents($chatLogFile, "");

// Return the room ID as JSON response
$response = array($roomId);
echo json_encode($response);
?>
