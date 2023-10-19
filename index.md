
---
layout: default
title: Student Blog
---




## SNAT Team homepage
Welcome to our homepage ;)

![Alt text](6410C3B2-B590-4460-8DF8-A3C00334A06F_1_105_c.jpeg)

## Who are we?


SNAT Scrum Master: Sreeja
- Hi im sreeja. I am a junior and the scrum master of the team.


SNAT backend: Tanvi
- Hi!! I'm Tanvi and I am in 10th grade at Del Norte High School. I like to dance, run, learn, and hang out with my friends. This year I am taking AP Computer Science Principles, AP Calculus, AP Chemistry, Honors Humanities, and Honors Principles of Engineering.


SNAT backend: Nupur
- Hi, I'm Nupur and I am in 10th grade at Del Norte High School. I like to play tenis and hang out with my friends.


SNAT frontend: Abby
- Hi, I'm Abby and I am in 10th grade at Del Norte High School. I like to read, listen to music, and sleep. 


## Our project
We aim to create a "study buddy" for our passion project this year. As students at Del Norte, we have a lot to juggle and sometimes it can be overwhelming. With the help of the study buddy, it will allow us to input our schedules and get daily reminders, create flashcards to study with, and have study sessions with an AI.


## Our plan deadlines


| The date to be finished by | Task to be completed |
|------|-------|
|10/8| Create shared repositiories, deploy backend on AWS and front end |
|10/10 | Create the homepage and do a small about-SNAT and add our goal, with study buddy-Frontend assignment. Add in pictures of the crew|
|10/18 |Create the backend code for the inputting of schedules and the code so that it will send notifications and reminders |
| 10/25| Create code for making flashcards, organize it based on subject, and input guideline basics for each subject. Ex. for calc, add flashcards of the basic derivatives of trig functions. For che,: add in solubility rules. We can also consider adding in AI.|
|11/1 |Do a final run-through of the study buddy to make sure everything is running smootly and nothing is glitching. If possible, add a video on the homepage about us. We can add an ad that shows how to use the study buddy and create a user-friendly guide.  |

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
        <p>What is the capital of France?</p>
        <button onclick="showAnswer(this)">Show Answer</button>
        <p style="display:none;"><strong>Answer:</strong> Paris</p>
    </div>

    <div class="flashcard">
        <h2>Question 2</h2>
        <p>What is the largest planet in our solar system?</p>
        <button onclick="showAnswer(this)">Show Answer</button>
        <p style="display:none;"><strong>Answer:</strong> Jupiter</p>
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
