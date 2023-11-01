
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grammar Checker</title>
    <style>
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Grammar Checker</h1>
    <textarea id="textInput" placeholder="Enter text here..."></textarea>
    <br>
    <button onclick="checkGrammar()">Check Grammar</button>
    <h2>Grammar Errors:</h2>
    <ul id="errorList"></ul>
    <script>
        function checkGrammar() {
            const textToCheck = document.getElementById('textInput').value;
            // Send a POST request to the grammar checking API
            fetch('http://localhost:8086/grammar-check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: textToCheck }),
            })
            .then(response => response.json())
            .then(errors => {
                // Display grammar errors on the page
                const errorList = document.getElementById('errorList');
                errorList.innerHTML = '';
                errors.forEach(error => {
                    const listItem = document.createElement('li');
                    listItem.textContent = error;
                    errorList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>

<html lang="en">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Light Green Background</title>
    <style>
        body {
            background-color: lightgreen;
        }
        .container {
            width: 50%;
            margin: auto;
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
</div>
</body>
</html>
