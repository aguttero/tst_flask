from flask import Flask
import random as rd

# html decorator functions
def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

app = Flask(__name__)

def generate_random_int(max_number):
    return rd.randint(0,max_number)
    

@app.route("/")
def home():
    return f"<h1>Guess a number between 0 and 9</h1>"\
            "{generate_random_int(100)}"\
            "<a href='/bye'> Bye Page.</a>"\
            "<h2>This is a text line </h2>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:user_guess>")
def check_guess(user_guess):
    if user_guess < random_choice:
        return f"Too Low"
    elif user_guess > random_choice:
        return f"Too High"
    else:
        return f"Yeahhh {user_guess} is the right answer!!!"


@app.route("/bye")
@make_bold
def say_bye():
    return "<p>Bye!</p>"


# code to run the flask local server:

random_choice = generate_random_int(9)
print("generate_random_int:", random_choice)
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