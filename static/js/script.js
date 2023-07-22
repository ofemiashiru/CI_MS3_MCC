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

    // Get year for footer
    const now = new Date();
    const year = now.getFullYear();
    const footer = document.querySelector(".footer-copyright .container span");
    footer.innerHTML = `© ${year} Movie Crazy Club`;

});


