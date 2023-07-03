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
const year = now.getFullYear()
const footer = document.querySelector(".footer-copyright .container span");
footer.innerHTML = `© ${year} Movie Crazy Club`;
