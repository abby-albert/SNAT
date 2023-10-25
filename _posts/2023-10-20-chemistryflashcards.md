---
toc: false
comments: true
layout: post
title: Chem flashcards
description: flashcards for chem
type: plans
courses: { compsci: {week: 1} }
permalink: /plans/week3
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AP Chemistry Flashcards</title>
</head>
<body>
    <div id="flashcard">
        <h2 id="question">Question</h2>
        <p id="answer" style="display: none;">Answer</p>
        <button onclick="showAnswer()">Show Answer</button>
        <button onclick="nextCard()">Next Card</button>
    </div>

    <script>
        const flashcards = [
            { question: "What is the atomic number of hydrogen", answer: "1" },
            { question: "what is the atomic number of helium", answer: "2" },
            { question: "what is the atomic number of lithium", answer: "3" }
            // Add more flashcards as needed
        ];

        let currentCard = 0;
        const questionElement = document.getElementById('question');
        const answerElement = document.getElementById('answer');

        function showAnswer() {
            answerElement.style.display = 'block';
        }

        function nextCard() {
            if (currentCard < flashcards.length - 1) {
                currentCard++;
                questionElement.textContent = flashcards[currentCard].question;
                answerElement.textContent = flashcards[currentCard].answer;
                answerElement.style.display = 'none';
            } else {
                alert('You have reached the end of the flashcards.');
            }
        }

        // Display the first flashcard on page load
        window.onload = function() {
            questionElement.textContent = flashcards[currentCard].question;
            answerElement.textContent = flashcards[currentCard].answer;
        };
    </script>
</body>
</html>
