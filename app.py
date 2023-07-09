import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ROUTE FOR HOME PAGE AND SHOW MOVIES
@app.route("/")
@app.route("/show_movies")
def show_movies():
    """
    Route for home and show_movies
    """
    movies = list(mongo.db.movies.find().sort("title", 1))
    return render_template("movies.html", movies=movies)


# ROUTE FOR REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Route for user registration
    """
    if request.method == "POST":
        # Check if passwords are matching
        if request.form.get("password") != request.form.get("passwordCheck"):
            flash("The passwords do not match")
            return redirect(url_for("register"))

        # Check if the username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # If user name does not exist add new user
        new_user = {
            "username": request.form.get("username").lower(),
            # generate hash for users password
            "password": generate_password_hash(request.form.get("password"))
        }

        # add new user to mongo database
        mongo.db.users.insert_one(new_user)

        # put the new user in session
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        #  redirect user to profile on successful registration
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("register.html")


# ROUTE FOR SIGN IN
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    """
    Route for user to log in to app
    """
    if "user" in session:
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        #  check if the user exists in our database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the existing user is truthy
        if existing_user:
            #  compare the password in the db with entered password
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                # create session for logged in user
                session["user"] = request.form.get("username").lower()
                flash(f"Hey, {existing_user['username']} you are logged in!")

                #  redirect user to profile on successful log in
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # if the password is incorrect
                flash("The credentials you have entered are incorrect")
                return redirect(url_for("sign_in"))
        else:
            # if the username is incorrect
            flash("The credentials you have entered are incorrect")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


# USER PROFILE ROUTE WITH CUSTOM
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        # Use this section to pull other data through based on username
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("profile.html", username=username)

    flash("You are not currently logged in")
    return redirect(url_for("sign_in"))


# SIGN OUT ROUTE
@app.route("/sign_out")
def sign_out():
    if "user" in session:
        # remove user from session cookie
        session.pop("user")
        flash("You have been logged out")
        return redirect(url_for("sign_in"))
    return redirect(url_for("sign_in"))


# 404 Route - https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


# ADD MOVIE ROUTE
@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():

    if request.method == "POST":
        if "user" in session:
            movie = {
                "genre_name": request.form.get("genre_name"),
                "title": request.form.get("title"),
                "year": request.form.get("year"),
                "plot": request.form.get("plot"),
                "rating": request.form.get("rating"),
                "director": request.form.get("director"),
                "poster": request.form.get("poster"),
                "created_by": session["user"]
            }
            mongo.db.movies.insert_one(movie)
            flash("Your movie has been succesfully added")
            return redirect(url_for("show_movies"))

    if "user" in session:
        genres = list(mongo.db.genres.find().sort("genre_name", 1))
        return render_template("add_movie.html", genres=genres)

    flash("You need to be logged in to add a movie.")
    return redirect("sign_in")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
