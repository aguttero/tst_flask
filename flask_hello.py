#this runs in .venv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

print(__name__)

#if __name__ == "__main__":
#    app.run()

# to run
# Terminal
# >flask --app <filename> run
# or
# export FLASK_APP=<filename.py>
# flask run
# flask run --help for help