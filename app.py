from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Disable CSRF protection via config
app.config['WTF_CSRF_ENABLED'] = False

csrf = CSRFProtect(app)

@app.route("/")
def hello():
    return "Hello, world from Dockerized Flask app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
