/*document.addEventListener("DOMContentLoaded", function() {
    const toggleButtonBtn = document.getElementById("toggleButton");
    const formularioContacto = document.getElementById("formularioContacto");

    toggleButtonBtn.addEventListener("click", function() {
        formularioContacto.style.display = "block";
    });
});*/

document.addEventListener("DOMContentLoaded", function() {
    const toggleButtonBtn = document.getElementById("toggleButton");
    const formularioContacto = document.getElementById("formularioContacto");

    toggleButtonBtn.addEventListener("click", function() {
        if (formularioContacto.style.display === "none") {
            formularioContacto.style.display = "block";
            toggleButtonBtn.textContent = "Hide Form";
        } else {
            formularioContacto.style.display = "none";
            toggleButtonBtn.textContent = "Show Form";
        }
    });
});
