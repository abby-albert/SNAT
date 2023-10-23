---
toc: false
comments: true
layout: post
title: flashcards
description: flashcards for calc AB
type: plans
courses: { compsci: {Units in Calculus, week: 0} }
permalink: /plans/week3
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .flashcard {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            max-width: 300px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .flashcard h2 {
            color: #333;
        }
    </style>
</head>
<body>

    <div class="flashcard">
        <h2>Question 1</h2>
        <p>What is the derivative of sin(x)?</p>
        <button onclick="showAnswer(this)">Show Answer</button>
        <p style="display:none;"><strong>Answer:</strong> cos(x)dx</p>
    </div>

    <div class="flashcard">
        <h2>Question 2</h2>
        <p>what is the derivative of sin(u)?</p>
        <button onclick="showAnswer(this)">Show Answer</button>
        <p style="display:none;"><strong>Answer:</strong> cos(u)du/dx</p>
    </div>

    <!-- Add more flashcards as needed -->

    <script>
        function showAnswer(button) {
            var answer = button.nextElementSibling;
            answer.style.display = (answer.style.display === 'none' || answer.style.display === '') ? 'block' : 'none';
        }
    </script>

</body>
</html>
