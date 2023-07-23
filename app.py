import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash
import re

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def valid_object_id(id):
    """
    Function that checks that the id being passed is 24 characters long
    and contains only letters and numbers. This is used to validate the
    ids being used and returns a boolean value
    """
    check = re.search("[0-9a-zA-Z]{24}", id)

    return bool(check)


@app.route("/")
@app.route("/show_movies")
def show_movies():
    """
    Route for home and show_movies
    """
    movies = list(mongo.db.movies.find().sort("rating", -1))
    return render_template("movies.html", movies=movies)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Route for search functionality to allow users to search for movies
    """
    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Route for user registration to allow users to sign up
    """
    if request.method == "POST":
        # Check if passwords are matching
        if request.form.get("password") != request.form.get("passwordCheck"):
            flash("The passwords do not match")
            return redirect(url_for("register"))

        # Check if the username exists
        existing_user = mongo.db.users.find_one_or_404(
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


def delete_user_entirely(id):
    """
    Function to purge user, all associated movies
    and reviews from mongodb based upon id
    """
    # Grab user to delete associated movies and reviews
    user_to_delete = mongo.db.users.find_one_or_404(
        {"_id": ObjectId(id)})["username"]
    # Find all reviews associated with user and delete
    mongo.db.reviews.delete_many({"created_by": user_to_delete})
    # Find all movies associated with user and delete
    mongo.db.movies.delete_many({"created_by": user_to_delete})
    # Finally find the user and delete them
    mongo.db.users.find_one_and_delete({"_id": ObjectId(id)})


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    Route handles the deletion of a user from the site
    from both the admin and user themselves
    """
    if session["user"] == "admin":
        delete_user_entirely(user_id)

        flash("User has been succesfully deleted.")
        return redirect(url_for("profile", username=session["user"]))

    if "user" in session and session["user"].lower() != "admin":
        delete_user_entirely(user_id)

        session.pop("user")
        flash("Your account has been succesfully deleted.")
        return redirect(url_for("show_movies"))


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    """
    Route for user to log in to app
    """
    if "user" in session:
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        #  check if the user exists in our database
        existing_user = mongo.db.users.find_one_or_404(
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
                flash("The credentials you have entered are incorrect.")
                return redirect(url_for("sign_in"))
        else:
            # if the username is incorrect
            flash("The credentials you have entered are incorrect.")
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
        user_info = mongo.db.users.find_one_or_404(
            {"username": session["user"]})
        # Bring back all the users movies
        users_movies = list(
            mongo.db.movies.find({"created_by": user_info["username"]}))
        # bring back all reviews for the users movie
        reviews = list(mongo.db.reviews.find())

        return render_template(
            "profile.html",
            user_info=user_info,
            users_movies=users_movies,
            reviews=reviews,
            all_users=list(mongo.db.users.find())
            if session["user"].lower() == "admin" else []
        )

    flash("You are not currently logged in.")
    return redirect(url_for("sign_in"))


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


@app.errorhandler(404)
def page_not_found(e):
    """
    Route for all 404 errors
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Route for all 500 errors
    """
    return render_template("500.html"), 500


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    """
    Route to allow users to add movies
    """
    if "user" in session:
        if request.method == "POST":

            movie = {
                "genre_name": request.form.get("genre_name"),
                "title": request.form.get("title"),
                "year": int(request.form.get("year")),
                "plot": request.form.get("plot"),
                "rating": int(request.form.get("rating")),
                "director": request.form.get("director"),
                "poster": request.form.get("poster"),
                "created_by": session["user"]
            }
            mongo.db.movies.insert_one(movie)
            flash("Your movie has been succesfully added.")
            return redirect(url_for("show_movies"))

        genres = list(mongo.db.genres.find().sort("genre_name", 1))
        return render_template("add_movie.html", genres=genres)

    flash("You need to be logged in to add a movie.")
    return redirect("sign_in")


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    """
    Route to allow users to edit and update movie
    """
    if "user" in session:
        movie = mongo.db.movies.find_one_or_404(
            {"_id": ObjectId(movie_id)})

        if session["user"].lower() == movie["created_by"]:

            if request.method == "POST":
                updated_movie = {
                    "genre_name": request.form.get("genre_name"),
                    "title": request.form.get("title"),
                    "year": int(request.form.get("year")),
                    "plot": request.form.get("plot"),
                    "rating": int(request.form.get("rating")),
                    "director": request.form.get("director"),
                    "poster": request.form.get("poster"),
                    "created_by": session["user"]
                }
                mongo.db.movies.update_one(
                    {"_id": ObjectId(movie_id)}, {"$set": updated_movie})
                flash("Your movie has been succesfully updated.")
                return redirect(url_for("show_movies"))

            movie = mongo.db.movies.find_one_or_404(
                {"_id": ObjectId(movie_id)})
            genres = list(mongo.db.genres.find().sort("genre_name", 1))
            return render_template(
                "edit_movie.html", movie=movie, genres=genres)

        flash("Only the user who submitted this movie can edit it.")
        return redirect(url_for("show_movies"))

    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    """
    Route allows logged in users to delete their own movies
    """
    if "user" in session:
        movie = mongo.db.movies.find_one_or_404(
            {"_id": ObjectId(movie_id)})
        if session["user"].lower() == movie["created_by"].lower():
            mongo.db.movies.find_one_and_delete({"_id": ObjectId(movie_id)})
            flash("Movie has been successfully deleted.")
            return redirect(url_for("show_movies"))
        flash("Only the user who submitted this movie can delete it.")
        return redirect(url_for("show_movies"))

    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/show_genres")
def show_genres():
    """
    Route used to display all genres
    """
    if "user" in session:
        if session["user"].lower() == "admin":
            genres = list(mongo.db.genres.find().sort("genre_name", 1))
            return render_template("genres.html", genres=genres)
        flash("Only admin can access this page.")
        return redirect(url_for("sign_in"))
    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """
    Route used to add genres
    """
    if "user" in session:
        if session["user"].lower() == "admin":
            if request.method == "POST":
                genre = request.form.get("genre_name")
                mongo.db.genres.insert_one({"genre_name": genre})
                flash("Genre successfully added.")
                return redirect("show_genres")
            return render_template("add_genre.html")
        flash("Only admin can access this page.")
        return redirect(url_for("sign_in"))
    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    """
    Route used to edit a single genre
    """
    if "user" in session:
        if session["user"].lower() == "admin":
            # Grabs the previous genre and stores it
            prev_genre = mongo.db.genres.find_one_or_404(
                {"_id": ObjectId(genre_id)})["genre_name"]
            if request.method == "POST":
                updated_genre = {
                    "genre_name": request.form.get("genre_name")
                }
                # Update genre
                mongo.db.genres.update_one(
                    {"_id": ObjectId(genre_id)}, {"$set": updated_genre})
                # Uses the previous genre to update all associated movies
                mongo.db.movies.update_many(
                    {"genre_name":  prev_genre}, {"$set": updated_genre})

                flash("Genre succesfully updated and all associated movies.")
                return redirect(url_for("show_genres"))
            genre = mongo.db.genres.find_one_or_404(
                {"_id": ObjectId(genre_id)})
            return render_template("edit_genre.html", genre=genre)

        flash("Only admin can access this page.")
        return redirect(url_for("sign_in"))
    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    """
    Route allows admin user to delete genre
    """
    if "user" in session:
        if session["user"].lower() == "admin":
            # Grab genre name to delete associated movies
            genre = mongo.db.genres.find_one_or_404(
                {"_id": ObjectId(genre_id)})["genre_name"]
            # Find all movies associated with genre and delete
            mongo.db.movies.delete_many({"genre_name": genre})
            # Finally find the genre and delete it
            mongo.db.genres.find_one_and_delete({"_id": ObjectId(genre_id)})
            flash("Genre succesfully deleted and all associated movies.")
            return redirect(url_for("show_genres"))
        flash("Only admin can access this page.")
        return redirect(url_for("sign_in"))
    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/show_reviews/<movie_id>")
def show_reviews(movie_id):
    """
    Route used to show reviews for specific movie
    """
    if not valid_object_id(movie_id):
        return redirect(url_for("show_reviews", movie_id=""))

    # Grab all the movie information
    movie = mongo.db.movies.find_one_or_404({"_id": ObjectId(movie_id)})
    # Grab all reviews associated with the movie
    reviews = list(mongo.db.reviews.find({"title": movie["title"]}))
    return render_template("reviews.html", movie=movie, reviews=reviews)


@app.route("/add_review/<movie_id>", methods=["GET", "POST"])
def add_review(movie_id):
    """
    Route used to allow user to add a review for specific movie
    """
    if not valid_object_id(movie_id):
        return redirect(url_for("add_reviews", movie_id=""))
        
    if "user" in session:
        movie = mongo.db.movies.find_one_or_404({"_id": ObjectId(movie_id)})
        if request.method == "POST":
            new_review = {
                "review": request.form.get("review"),
                "title": movie["title"],
                "created_by": session["user"]
            }
            mongo.db.reviews.insert_one(new_review)
            flash("Your review has been succesfully added")
            return redirect(
                url_for("show_reviews", movie_id=ObjectId(movie_id)))
        return render_template("add_review.html", movie=movie)
    flash("You need to be logged in.")
    return redirect(url_for("sign_in"))


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Route allows user to edit their own review
    """
    if not valid_object_id(movie_id):
        return redirect(url_for("edit_review", review_id=""))

    # Check if the review writer is logged in.
    if "user" in session:
        review = mongo.db.reviews.find_one_or_404(
            {"_id": ObjectId(review_id)})
        movie = mongo.db.movies.find_one_or_404(
            {"title": review["title"]})

        if session["user"].lower() == review["created_by"].lower():
            if request.method == "POST":
                updated_review = {
                    "review": request.form.get("review")
                }
                mongo.db.reviews.update_one(
                    {"_id": ObjectId(review_id)}, {"$set": updated_review})
                flash("Review succesfully updated.")
                return redirect(url_for("show_reviews", movie_id=movie["_id"]))

            return render_template(
                "edit_review.html", review=review, movie=movie)

        flash("Only the user who submitted this review can edit it.")
        return redirect(url_for("show_reviews", movie_id=movie["_id"]))

    flash("You need to be logged in")
    return redirect(url_for("sign_in"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    Route used to delete reviews
    """
    if "user" in session:
        review = mongo.db.reviews.find_one_or_404(
            {"_id": ObjectId(review_id)})
        movie = mongo.db.movies.find_one_or_404(
            {"title": review["title"]})
        if session["user"].lower() == review["created_by"]:
            mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
            flash("Review sucessfully deleted")
            return redirect(url_for("show_reviews", movie_id=movie["_id"]))
        flash("Only the user who submitted this review can delete it.")
        return redirect(url_for("show_reviews", movie_id=movie["_id"]))

    flash("You need to be logged in")
    return redirect(url_for("sign_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
