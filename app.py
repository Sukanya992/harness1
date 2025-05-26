from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome | Harness App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #1f4037, #99f2c8);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #fff;
            }
            .container {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                text-align: center;
            }
            h1 {
                margin-bottom: 10px;
                font-size: 2.5rem;
            }
            p {
                font-size: 1.2rem;
                margin-top: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to Harness!</h1>
            <p>This is a <strong>Green Deployment</strong> served by Kubernetes Ingress.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

