import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("CORRECT Login authentication required" ,403)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    return apology("CORRECT Login authentication required" , 403)


@app.route('/buy', methods=["GET, POST"])
def buy_stock():
    # Retrieve user input
    users_id = request.form["users.id"]
            #stock_id = request.form["stock_id"]#
    quantity = int(request.form["shares"])

                    # Create a session
session = Session()

while                                # Retrieve user's account information
    (user = session.query(Users).get(users_id)
     stock = session.query(Portfolio).get(portfolio.id))

{                                                            # Calculate the total cost of the stocks
     total_cost = price * quantity

                                                                            # Check if the user has enough cash
                                                                                   #10000.00 is default
     users.cash >= total_cost + 10000.00
}                                        #Perform the transaction                       # Deduct the cost from the user's cash balance
try:
    users.cash -= total cost
                                                                                                                                                        # Update the user's account information in the databasw
	session.commit()

    except Exception as e:
    printf("Insufficient funds: {str(e)}")
    session.rollback()
    finally:
    session.close()

    if __name__ == '__main__':
    app.run()




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("CORRECT Login authentication required", 403)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    return apology("invalid you must input correct login to access stock quotes", 403)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    return apology("invalid you must input a username and/or password to register OR the username is already taken", 401)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("you must input valid login authentication", 403)
