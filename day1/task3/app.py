from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Debugging - Task 3</title>
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
        <h2>Day 1 - Task 3</h2>
        <div class="success">
            Success! You've fixed the dependency issue!
        </div>
        <p>
            You successfully fixed the Dockerfile to install Flask.
        </p>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000) 