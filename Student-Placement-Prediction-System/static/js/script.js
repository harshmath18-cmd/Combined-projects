// ==============================
// Loading Button
// ==============================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            document.getElementById("btnText").style.display = "none";
            document.getElementById("loading").style.display = "inline-block";
            document.getElementById("predictBtn").disabled = true;

        });

    }

});

// ==============================
// Counter Animation
// ==============================

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    counter.innerText = "0";

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const current = +counter.innerText;

        const increment = target / 60;

        if (current < target) {

            counter.innerText = `${Math.ceil(current + increment)}`;

            setTimeout(updateCounter, 25);

        }

        else {

            counter.innerText = target;

        }

    }

    updateCounter();

});