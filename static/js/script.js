document.addEventListener("DOMContentLoaded", function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav, {edge:"right"});

    // tooltip initialization
    let tooltipped = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(tooltipped);
});

// Get year for footer
const now = new Date();
const year = now.getFullYear();
const footer = document.querySelector(".footer-copyright .container span");
footer.innerHTML = `© ${year} Movie Crazy Club`;


// Get Movie cover - add_movie.html
const fetchMovieCover = function(){
    // clear img src
    document.querySelector("#movie-img").src = "";
    const movieName = document.querySelector("#move_title").value;

    if(!movieName){
        document.querySelector('.movie-cover-container__header').innerHTML = "Please Enter a Title";
        return;  
    }
    // split movie name by space
    const arrMovieName = movieName.split(" ");
    // join movie name as a string with + between
    const strMovieName = arrMovieName.join("+");

    // fetch request
    fetch(`https://www.omdbapi.com/?t=${strMovieName}&apikey=a366f18e`)
    .then(response => response.json())
    .then(data => {
        if(data.Response === "False"){
            document.querySelector('.movie-cover-container__header').innerHTML = "Poster not Found!";
            document.querySelector("#movie-img").src = "";
        } else {
            const omdbMoviePoster = data.Poster;
            document.querySelector('.movie-cover-container__header').innerHTML = "Poster Found";
            document.querySelector("#movie-img").src = omdbMoviePoster;
        }

    })
    .catch((error) => {
        console.error(error);
    })

}
