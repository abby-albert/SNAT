
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickable Cards</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .card {
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
            width: 200px;
            padding: 20px;
            margin: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        a {
            text-decoration: none;
            color: #ADD8E6;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <a href="http://127.0.0.1:4200/student/2023/10/19/Flashcards.html">Ap Calc AB</a>
        <p>Flashcards to help student with the basics of AP Calc AB</p>
    </div>
    <div class="card">
        <a href="http://127.0.0.1:4200/student/2023/10/27/chemFlashcards.html">AP Chemistry</a>
        <p>Flashcards to help students with the material in AP Chemistry</p>
    </div>
    <div class="card">
        <a href="http://127.0.0.1:4200/student/2023/10/27/bioflahsa.html">AP Biology</a>
        <p>Flashcards to help students with the material in AP Biology</p>
    </div>
        <div class="card">
        <a href="page3.html">AP Computer Science Principals</a>
        <p>Flashcards to help students with the material in AP CSP</p>
    </div>
</body>
</html>
