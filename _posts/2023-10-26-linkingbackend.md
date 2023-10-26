<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brawl Stars Player Tag</title>
</head>
<body>
    <label for="playerTag">Enter Your Player Tag:</label>
    <input type="text" id="playerTag" placeholder="e.g., #ABC123">
    <button onclick="sendPlayerTag()">Submit</button>

    <script>
        function sendPlayerTag() {
            // Get player tag from input
            const playerTag = document.getElementById('playerTag').value;

            // Prepare the request body
            const requestBody = {
                playerTag: playerTag
            };

            // Make a POST request to the backend
            fetch('your_backend_api_url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the backend
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
</body>
</html>