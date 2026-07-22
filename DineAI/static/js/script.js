console.log("DineAI Loaded");

// Initialize AOS only if it exists
if (typeof AOS !== "undefined") {
    AOS.init({
        duration: 1000,
        once: true
    });
}

const goSearch = document.getElementById("goSearch");

function scrollToSearch() {

    const search = document.getElementById("search");

    if (!search) return;

    const navbar = document.querySelector(".navbar");

    const navbarHeight = navbar ? navbar.offsetHeight + 30 : 110;

    const position =
        search.getBoundingClientRect().top +
        window.pageYOffset -
        navbarHeight;

    window.scrollTo({
        top: position,
        behavior: "smooth"
    });

}

if (goSearch) {

    goSearch.addEventListener("click", function (e) {

        e.preventDefault();

        if (window.location.pathname === "/") {

            scrollToSearch();

        } else {

            window.location.href = "/?search=1";

        }

    });

}

window.addEventListener("load", function () {

    const params = new URLSearchParams(window.location.search);

    if (params.get("search")) {

        history.replaceState({}, "", "/");

        setTimeout(scrollToSearch, 300);

    }

});



const goFooter = document.getElementById("goFooter");

function scrollToFooter() {

    const footer = document.getElementById("footer");

    if (!footer) return;

    const navbar = document.querySelector(".navbar");

    const navbarHeight = navbar ? navbar.offsetHeight + 20 : 100;

    const position =
        footer.getBoundingClientRect().top +
        window.pageYOffset -
        navbarHeight;

    window.scrollTo({

        top: position,

        behavior: "smooth"

    });

}

if (goFooter) {

    goFooter.addEventListener("click", function (e) {

        if (window.location.pathname === "/") {

            e.preventDefault();

            scrollToFooter();

        }

    });

}