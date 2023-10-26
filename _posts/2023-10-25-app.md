<!DOCTYPE html>
<html>
<head>
    <title>Frontend App</title>
</head>
<body>
    <h1>Frontend App</h1>
    <div id="data"></div>
    <script>
        fetch('/api/get_data')
            .then(response => response.json())
            .then(data => {
                document.getElementById('data').textContent = data.message;
            })
            .catch(error => {
                console.error('API request error:', error);
            });
    </script>
</body>
</html>
