from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello")
def hello_world():
    return "Hello, World!"

print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
