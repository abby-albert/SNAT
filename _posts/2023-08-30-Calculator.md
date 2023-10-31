
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator Background</title>
    <style>
        body {
            background-color: lightgreen;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .calculator {
            background-color: white;
            border: 5px solid black;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 5px;
            padding: 20px;
            border-radius: 10px;
        }

        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 20px;
            text-align: center;
            text-decoration: none;
            font-size: 20px;
            border-radius: 5px;
            cursor: pointer;
        }

        .button:hover {
            background-color: #45a049;
        }

        .output {
            grid-column: span 4;
            padding: 10px;
            font-size: 20px;
            border: 5px solid black;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <div class="output" id="output">0</div>
        <div class="button">1</div>
        <div class="button">2</div>
        <div class="button">3</div>
        <div class="button">+</div>
        <div class="button">4</div>
        <div class="button">5</div>
        <div class="button">6</div>
        <div class="button">-</div>
        <div class="button">7</div>
        <div class="button">8</div>
        <div class="button">9</div>
        <div class="button">*</div>
        <div class="button">A/C</div>
        <div class="button">0</div>
        <div class="button">.</div>
        <div class="button">=</div>
    </div>
</body>
</html>
