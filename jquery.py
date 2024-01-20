#!/usr/bin/env python
# coding: utf-8

# In[3]:


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Changing Box</title>
    <style>
        colorBox {
            width: 100px;
            height: 100px;
            background-color: lightblue;
        }
    </style>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>
<body>

<div id="colorBox"></div>
<button id="changeColorBtn">Change Color</button>

<script>
    (/, jQuery, code, to, change, the, color, of, the, box)
    $(document).ready(function() {
        (/, Initial, color)
        var currentColor = "lightblue";

        (/, Function, to, generate, a, random, color)
        function getRandomColor() {
            var letters = '0123456789ABCDEF';
            var color = '#';
            for (var i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        (/, Event, handler, for, button, click)
        $("#changeColorBtn").on("click", function() {
            (/, Generate, a, random, color)
            var newColor = getRandomColor();

            (/, Change, the, background, color, of, the, box)
            $("#colorBox").css("background-color", newColor);

            (/, Update, the, current, color)
            currentColor = newColor;
        });
    });
</script>

</body>
</html>


# In[ ]:




