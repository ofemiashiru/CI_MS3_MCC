document.addEventListener("DOMContentLoaded", function () {
    
    //Retrieves api key from html page 
    const getKey = function(){
        return document.querySelector(".omdb_key").value;
    }

    // Get Movie cover - add_movie.html
    const fetchMovieCover = function(){
        // clear img src
        document.querySelector("#movie-img").src = "";
        document.querySelector("#poster").value = "";
        const movieName = document.querySelector("#title").value;


        if(!movieName){
            document.querySelector(".movie-cover-container__header").innerHTML = "Please enter a title";
            document.querySelector("#poster").value = "Please enter a title";
            return;  
        }
        // split movie name by space
        const arrMovieName = movieName.split(" ");
        // join movie name as a string with + between
        const strMovieName = arrMovieName.join("+");

        // fetch request
        fetch(`https://www.omdbapi.com/?t=${strMovieName}&apikey=${getKey()}`)
        .then(response => response.json())
        .then(data => {
            if(data.Response === "False"){
                document.querySelector("#poster").value = "Poster not found!";
                document.querySelector("#movie-img").src = "";
                document.querySelector(".movie-cover-container__header").innerHTML = "Poster not found!";
                document.querySelector(".preloader-wrapper").classList.remove("hidden");
                
            } else {
                const omdbMoviePoster = data.Poster;
                document.querySelector(".movie-cover-container__header").innerHTML = "Poster found";
                document.querySelector("#movie-img").src = omdbMoviePoster;
                document.querySelector("#poster").value = omdbMoviePoster;
                document.querySelector(".preloader-wrapper").classList.add("hidden");
            }

        })
        .catch((error) => {
            console.error(error);
        });

    };

    document.querySelector("#title").addEventListener("input", function(){
        fetchMovieCover();
    });

});