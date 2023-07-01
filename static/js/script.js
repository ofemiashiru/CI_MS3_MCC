document.addEventListener("DOMContentLoaded", function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav, {edge:"right"});
});

// Get year for footer
const now = new Date();
const year = now.getFullYear()
const footer = document.querySelector(".footer-copyright .container span");
footer.innerHTML = `© ${year} Movie Crazy Club`;
