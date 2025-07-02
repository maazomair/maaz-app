from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure Web App using Python 3.9!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
