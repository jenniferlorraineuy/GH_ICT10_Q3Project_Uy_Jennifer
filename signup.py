# sign up confirmation
from pyscript import display, document


def account_signup(e):
    document.getElementById('output').innerHTML = ' '
    username = document.getElementById('username').value
    password = document.getElementById('password').value

    if len(username) < 7:
        display("Username must be at least 7 characters long", target="output")

    elif len(password) < 10:
        display("Password must be at least 10 characters long", target="output")

    elif password.isdigit():
        display("Password must contain at least one letter", target="output")

    elif password.isalpha():
        display("Password must contain at least one number", target="output")

    else:

        display("You have successfully signed up", target="output")
