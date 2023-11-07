function cambiarIdioma() {
    var selectIdioma = document.getElementById("idioma");
    var idiomaSeleccionado = selectIdioma.value;

    if (idiomaSeleccionado === "English") {
        document.getElementById("titulo").textContent = "Registration Form";
        document.getElementById("labelIdioma").textContent = "Language Selection:";
        document.getElementById("opcionEspañol").textContent = "Spanish";
        document.getElementById("opcionEnglish").textContent = "English";
        document.getElementById("labelSucursal").textContent = "Branch Selection:";
        document.getElementById("opcionEverett").textContent = "Everett";
        document.getElementById("opcionLynnwood").textContent = "Lynnwood";
        document.getElementById("labelFecha").textContent = "Date:";
        document.getElementById("labelClases").textContent = "Classes:";
        document.getElementById("opcionMaquillaje").textContent = "Makeup";
        document.getElementById("opcionReposteria").textContent = "Bakery";
        document.getElementById("opcionPlaza").textContent = "Community Plaza";
        document.getElementById("opcionCostura").textContent = "Sewing";
        document.getElementById("opcionNegocio").textContent = "Business-Finance";
        document.getElementById("opcionEspañolNinos").textContent = "Spanish for Kids";
        document.getElementById("labelNombre").textContent = "First Name:";
        document.getElementById("labelApellido").textContent = "Last Name:";
        document.getElementById("labelCP").textContent = "Zip Code:";
        document.getElementById("labelSalario").textContent = "Annual Income:";
        document.getElementById("opcionSalario1").textContent = "> $10,000";
        document.getElementById("opcionSalario2").textContent = "$10,001 - $30,000";
        document.getElementById("opcionSalario3").textContent = "$30,001 - $50,000";
        document.getElementById("opcionSalario4").textContent = "$50,001 - $70,000";
        document.getElementById("opcionSalario5").textContent = "$70,001 - $90,000";
        document.getElementById("opcionSalario6").textContent = "+$90,001";
        document.getElementById("labelComentario").textContent = "Comments:";
        document.getElementById("botonEnviar").value = "Submit";
        document.getElementById("botonRestablecer").value = "Reset";
    } else {
        // Restablecer el formulario a español
        // (Puedes agregar aquí los textos en español)
    }
}