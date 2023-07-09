document.addEventListener("DOMContentLoaded", function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav, {edge:"right"});

    // tooltip initialization
    let tooltipped = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(tooltipped);

    // drop down initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);
/*
    vanilla JavaScript for validating the materialize dropdown - 
    taken from https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js
*/
    
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
        let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
        let selectValidate = document.querySelector("select.validate");
        let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
        if (selectValidate.hasAttribute("required")) {
            selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
        }
        selectWrapperInput.addEventListener("focusin", (e) => {
            e.target.parentNode.addEventListener("change", () => {
                ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                for (let i = 0; i < ulSelectOptions.length; i++) {
                    if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                        e.target.style.cssText = classValid;
                    }
                }
            });
        });
        selectWrapperInput.addEventListener("click", (e) => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
            for (let i = 0; i < ulSelectOptions.length; i++) {
                if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                    e.target.style.cssText = classValid;
                } else {
                    e.target.addEventListener("focusout", () => {
                        if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                            if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                e.target.style.cssText = classInvalid;
                            }
                        }
                    });
                }
            }
        });
    }
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
            
        } else {
            const omdbMoviePoster = data.Poster;
            document.querySelector(".movie-cover-container__header").innerHTML = "Poster found";
            document.querySelector("#movie-img").src = omdbMoviePoster;
            document.querySelector("#poster").value = omdbMoviePoster;
        }

    })
    .catch((error) => {
        console.error(error);
    })

}
