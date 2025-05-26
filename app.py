from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Harness App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }
            .message {
                display: inline-block;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="message">
            <h1>Hello from <span style="color:#007bff;">Harness</span>!</h1>
            <p>This is a styled HTML response from your Flask app.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
