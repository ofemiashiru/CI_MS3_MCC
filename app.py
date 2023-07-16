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
    movies = list(mongo.db.movies.find().sort("rating", 1))
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
    """
    Route for the user profile route with additional custom route
    """
    if "user" in session:
        # Use this section to pull other data through based on username
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Bring back all the users movies
        users_movies = list(mongo.db.movies.find({"created_by": username}))
        # bring back all reviews for the users movie
        reviews = list(mongo.db.reviews.find())

        return render_template(
            "profile.html",
            username=username,
            users_movies=users_movies,
            reviews=reviews
        )

    flash("You are not currently logged in")
    return redirect(url_for("sign_in"))


# SIGN OUT ROUTE
@app.route("/sign_out")
def sign_out():
    """
    Route to allow user to sign out of their account
    """
    if "user" in session:
        # remove user from session cookie
        session.pop("user")
        flash("You have been logged out")
        return redirect(url_for("sign_in"))
    return redirect(url_for("sign_in"))


# 404 Route - https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    """
    Route for all 404 errors
    """
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


# ADD MOVIE ROUTE
@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    """
    Route to allow isers to add movies
    """
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


# EDIT MOVIE ROUTE
@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    """
    Route to allow users to edit and update movie
    """
    if request.method == "POST":
        updated_movie = {
            "genre_name": request.form.get("genre_name"),
            "title": request.form.get("title"),
            "year": request.form.get("year"),
            "plot": request.form.get("plot"),
            "rating": request.form.get("rating"),
            "director": request.form.get("director"),
            "poster": request.form.get("poster"),
            "created_by": session["user"]
        }
        mongo.db.movies.update_one(
            {"_id": ObjectId(movie_id)}, {"$set": updated_movie})
        flash("Your movie has been succesfully updated")
        return redirect(url_for("show_movies"))

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("edit_movie.html", movie=movie, genres=genres)


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    if "user" in session:
        mongo.db.movies.find_one_and_delete({"_id": ObjectId(movie_id)})
        flash("Movie has been successfully deleted")
        return redirect(url_for("show_movies"))


@app.route("/show_genres")
def show_genres():
    """
    Route used to display all genres
    """
    if "user" in session and session["user"].lower() == "admin":
        genres = list(mongo.db.genres.find().sort("genre_name", 1))
        return render_template("genres.html", genres=genres)
    flash("You need to be logged in as admin")
    return redirect(url_for("sign_in"))


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """
    Route used to add genres
    """
    if "user" in session and session["user"].lower() == "admin":
        if request.method == "POST":
            genre = request.form.get("genre_name")
            mongo.db.genres.insert_one({"genre_name": genre})
            flash("Genre successfully added")
            return redirect("show_genres")
        return render_template("add_genre.html")
    flash("You need to be logged in as admin")
    return redirect(url_for("sign_in"))

@app.route("/edit_genre/<genre_id>", methods=["GET","POST"])
def edit_genre(genre_id):
    """
    Route used to edit a single genre
    """  
    if "user" in session and session["user"].lower() == "admin":
        # Grabs the previous genre and stores it
        prev_genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
        if request.method == "POST":
            updated_genre = {
                "genre_name" : request.form.get("genre_name")
            }
            mongo.db.genres.update_one(
                {"_id": ObjectId(genre_id)}, {"$set": updated_genre})
            # Uses the previous genre to update all associated movies
            mongo.db.movies.update_many(
                {"genre_name" :  prev_genre['genre_name']}, {"$set" : updated_genre})

            flash("Your genre has been succesfully updated and all associated movies")
            return redirect(url_for("show_genres"))
        genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
        return render_template("edit_genre.html", genre=genre)

    flash("You need to be logged in as admin")
    return redirect(url_for("sign_in"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
