<?php
// joinroom.php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get room ID from POST data
    $roomId = $_POST['roomId'];
    
    // Function to fetch messages from a chat log
    function fetchMessages($roomId) {
        $chatLogFile = "chat_logs/" . $roomId . ".txt";
        
        // Check if the chat log file exists
        if (file_exists($chatLogFile)) {
            // Read and return all messages
            $messages = file_get_contents($chatLogFile);
            return $messages;
        } else {
            return "No messages found for room ID: " . $roomId;
        }
    }
    
    // Fetch messages for the specified room ID
    $messages = fetchMessages($roomId);
    
    // Return response with messages
    $response = array("status" => "success", "messages" => $messages);
    echo json_encode($response);
} else {
    // Handle incorrect request method (optional)
    http_response_code(405); // Method Not Allowed
    echo json_encode(array("error" => "Method Not Allowed"));
}
?>
