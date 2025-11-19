#this runs in .venv
from flask import Flask

# html decorator functions
def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"

@app.route("/bye")
@make_underlined
@make_emphasis
@make_bold
def say_bye():
    return "<p>Bye!</p>"

#variable rules <variable name>
# also has a converter to handle stings conversions and path
@app.route("/username/<name>/<int:age>")
def greet(name,age):
    return f"Hello there {name}! You are {age} years old!"

# code to run the flask local server:
print(__name__)
if __name__ == "__main__":
    app.run(debug=True)

#debugger mode on
## activates debugger
## activates automatic code reloader
## enables debug mode on the Flask application
## app.run(debug=True)


# to run
# Terminal
# >flask --app <filename> run
# or
# export FLASK_APP=<filename.py>
# flask run
# flask run --help for help