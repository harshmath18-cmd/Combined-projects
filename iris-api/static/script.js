// ===========================================
// IRIS AI - JavaScript
// ===========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("🌸 Iris AI Loaded Successfully!");

    // -----------------------------
    // Smooth Scroll for Navigation
    // -----------------------------
    const links = document.querySelectorAll(".nav-links a");

    links.forEach(link => {

        link.addEventListener("click", function (e) {

            e.preventDefault();

            const targetId = this.getAttribute("href");

            const targetSection = document.querySelector(targetId);

            if (targetSection) {

                window.scrollTo({
                    top: targetSection.offsetTop - 70,
                    behavior: "smooth"
                });

            }

        });

    });

    // -----------------------------
    // Predict Button Loading Effect
    // -----------------------------
    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const predictButton =
                document.querySelector(".button-group button[type='submit']");

            if (predictButton) {

                predictButton.innerHTML = "⏳ Predicting...";

                predictButton.disabled = true;

            }

        });

    }

    // -----------------------------
    // Input Focus Animation
    // -----------------------------
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {

        input.addEventListener("focus", function () {

            this.style.transform = "scale(1.02)";

        });

        input.addEventListener("blur", function () {

            this.style.transform = "scale(1)";

        });

    });

    // -----------------------------
    // Scroll Reveal Animation
    // -----------------------------
    const observer = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {
        threshold: 0.15
    });

    const hiddenElements = document.querySelectorAll(
        ".prediction-card, .result-card, .card, .about-section"
    );

    hiddenElements.forEach(el => {

        el.classList.add("hidden");

        observer.observe(el);

    });

    // -----------------------------
    // Active Navbar Highlight
    // -----------------------------
    const sections = document.querySelectorAll("section");

    window.addEventListener("scroll", () => {

        let current = "";

        sections.forEach(section => {

            const sectionTop = section.offsetTop - 120;

            if (pageYOffset >= sectionTop) {

                current = section.getAttribute("id");

            }

        });

        links.forEach(link => {

            link.classList.remove("active");

            if (link.getAttribute("href") === "#" + current) {

                link.classList.add("active");

            }

        });

    });

});