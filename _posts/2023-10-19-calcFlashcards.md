---
toc: true
comments: true
layout: post
title: Flashcards
description: calc flashcards
type: flashcards
courses: { compsci: {week: 0} }
---
---
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2e6ff; /* Light Purple background color */
            display: grid;
            place-items: center;
            min-height: 100vh;
        }

        /* Style for the question containers */
        .question-container {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
            max-width: 400px;
            margin: 10px;
            padding: 20px;
            text-align: left;
        }

        /* Style for question titles */
        .question h2 {
            font-size: 18px;
            color: #333;
        }

        /* Style for answer choices */
        .question ul {
            list-style-type: none;
            padding: 0;
        }

        .question li {
            padding: 8px 0;
        }

        /* Style for the correct answer reveal */
        .question details {
            margin-top: 15px;
            cursor: pointer;
        }

        .question summary {
            font-weight: bold;
            color: #333;
        }

        /* Style for the correct answer */
        .question details p {
            margin: 0;
            color: #009900; /* Green color for correct answer */
        }

        /* Arrange questions in two rows using grid layout */
        .questions-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
    </style>
</head>
<body>
    <div class="questions-grid">
        <div class="question-container">
            <div class="question">
                <h2>Biology Question 1</h2>
                <p>What is the powerhouse of the cell?</p>
                <ul>
            <li>A) 1</li>
            <li>B) 63</li>
            <li>C) 0</li>
            <li>D) indeterminate</li>
                </ul>
                <details>
                    <summary>Click to reveal the correct answer</summary>
                    <p>The correct answer is B) Mitochondria</p>
                </details>
            </div>
        </div>

        <div class="question-container">
            <div class="question">
                <h2>Biology Question 2</h2>
                <p>Which gas do plants absorb from the atmosphere during photosynthesis?</p>
                <ul>
            <li>A) infinity</li>
            <li>B) negative infinity</li>
            <li>C) 1</li>
            <li>D) none of the above</li>
                </ul>
                <details>
                    <summary>Click to reveal the correct answer</summary>
                    <p>The correct answer is C) Carbon dioxide</p>
                </details>
            </div>
        </div>

        <div class="question-container">
            <div class="question">
                <h2>Biology Question 3</h2>
                <p>What is the process by which organisms maintain a stable internal environment?</p>
                <ul>
            <li>A) sin x</li>
            <li>B) cos x</li>
            <li>C) -cos x</li>
            <li>D) tan x</li>
                </ul>
                <details>
                    <summary>Click to reveal the correct answer</summary>
                    <p>The correct answer is A) Homeostasis</p>
                </details>
            </div>
        </div>
    </div>
</body>
</html>

