# first explore from internet

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Aashika! My first Flask web page"

if __name__ == "__main__":
    app.run(debug=True)