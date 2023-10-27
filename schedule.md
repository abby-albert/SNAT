
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Schedule</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 50px;
        }
        .schedule {
            width: 300px;
        }
        input[type="text"], input[type="time"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .event {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="schedule">
        <h2>Enter Your Schedule</h2>
        <input type="text" id="event" placeholder="Event Name">
        <input type="time" id="time" name="appt" placeholder="Select Time">
        <button onclick="addEvent()">Add Event</button>
        <div id="eventList"></div>
    </div>

    <script>
        function addEvent() {
            var event = document.getElementById("event").value;
            var time = document.getElementById("time").value;
            var eventList = document.getElementById("eventList");
            var newEvent = document.createElement("div");
            newEvent.className = "event";
            newEvent.innerHTML = "<h3>" + event + "</h3><p>Time: " + time + "</p>";
            eventList.appendChild(newEvent);
            document.getElementById("event").value = "";
            document.getElementById("time").value = "";
        }
    </script>
</body>
</html>
