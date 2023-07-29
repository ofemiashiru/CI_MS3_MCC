document.addEventListener("DOMContentLoaded", function () {
    
    //Retrieves api key 
    const getKey = function(){
        return btoa(encodedKey());
    };

    // Get Movie cover - add_movie.html
    const fetchMovieCover = function(){
        // clear img src
        document.querySelector("#movie-img").src = "";
        document.querySelector("#poster").value = "";
        const movieName = document.querySelector("#title").value;
        document.querySelector(".preloader-wrapper").classList.remove("hidden");

        if(!movieName){
            document.querySelector(".movie-cover-container__header").innerHTML = "Please enter a title";
            document.querySelector("#poster").value = "Please enter a title";
            document.querySelector("#movie-img").setAttribute("src", "./static/images/no-image-solid.svg");
            document.querySelector(".preloader-wrapper").classList.add("hidden");
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
                document.querySelector("#movie-img").setAttribute("src", "./static/images/no-image-solid.svg");
                document.querySelector(".movie-cover-container__header").innerHTML = "Poster not found!";
                document.querySelector(".preloader-wrapper").classList.add("hidden");
                
            } else {
                const omdbMoviePoster = data.Poster;
                document.querySelector(".movie-cover-container__header").innerHTML = "Poster found";
                document.querySelector("#movie-img").setAttribute("src", omdbMoviePoster);
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