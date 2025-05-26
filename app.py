from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False  # disables CSRF
csrf = CSRFProtect(app)

@app.route("/")
def hello():
    return "Hello with Harness"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
