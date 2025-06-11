const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Debugging - Task 4</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                text-align: center;
            }
            .success {
                color: green;
                font-size: 24px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <h1>Docker Debugging Assignment</h1>
        <h2>Day 1 - Task 4</h2>
        <div class="success">
            Success! You've fixed the command issue!
        </div>
        <p>
            You successfully fixed the Dockerfile to use the correct start command.
        </p>
    </body>
    </html>
  `);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
}); 