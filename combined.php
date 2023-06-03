<?php

function loadJsonFromFile($filePath) {
    // Check if the file exists
    if (file_exists($filePath)) {
        // Read the file contents
        $jsonString = file_get_contents($filePath);

        // Decode the JSON string
        $jsonData = json_decode($jsonString, true);
        var_dump($jsonData);

        // Check if decoding was successful
        if ($jsonData !== null) {
            return $jsonData;
        } else {
            // JSON decoding failed
            throw new Exception('Failed to decode JSON from file: ' . $filePath);
        }
    } else {
        // File does not exist
        throw new Exception('File not found: ' . $filePath);
    }
}

loadJsonFromFile(app_path() . '/../resources/combined_data.json');


