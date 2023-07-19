document.addEventListener("DOMContentLoaded", function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav, {edge:"right"});

    // tooltip initialization
    let tooltipped = document.querySelectorAll(".tooltipped");
    M.Tooltip.init(tooltipped);

    // drop down initialization
    let select = document.querySelectorAll("select");
    M.FormSelect.init(select);

    // modal initialisation
    let modal = document.querySelectorAll(".modal");
    M.Modal.init(modal);

    // collapsabile initialization
    let collapsible = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsible);

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
    fetch(`https://www.omdbapi.com/?t=${strMovieName}&apikey=a366f18e`)
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
    })

}
