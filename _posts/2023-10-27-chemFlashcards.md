---
toc: true
comments: true
layout: post
title: chem Flashcards
description: chem flashcards
type: flashcards
courses: { compsci: {week: 0} }
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
    <div class="question">
        <h2>Chemistry Question 1</h2>
        <p>What is the chemical formula for water?</p>
        <ul>
            <li>A) H2O</li>
            <li>B) CO2</li>
            <li>C) CH4</li>
            <li>D) O2</li>
        </ul>
        <details>
            <summary>Click to reveal the correct answer</summary>
            The correct answer is A) H2O
        </details>
    </div>

    <div class="question">
        <h2>Chemistry Question 2</h2>
        <p>Which element is the most abundant in the Earth's crust?</p>
        <ul>
            <li>A) Oxygen</li>
            <li>B) Silicon</li>
            <li>C) Carbon</li>
            <li>D) Iron</li>
        </ul>
        <details>
            <summary>Click to reveal the correct answer</summary>
            The correct answer is A) Oxygen
        </details>
    </div>

    <div class="question">
        <h2>Chemistry Question 3</h2>
        <p>What is the pH of a neutral solution?</p>
        <ul>
            <li>A) 0</li>
            <li>B) 7</li>
            <li>C) 14</li>
            <li>D) -1</li>
        </ul>
        <details>
            <summary>Click to reveal the correct answer</summary>
            The correct answer is B) 7
        </details>
    </div>
</body>
</html>
