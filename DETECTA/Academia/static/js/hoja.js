console.log("El documento Javascript se ha cargado correctamente.");

/*document.getElementById("hero").style.display = "none";*/

/*Código galeria de imagenes*/
window.onload = function () {
    var galeria = document.getElementById("galeria");
    if (galeria) {
        var imgs = galeria.getElementsByTagName("img");
        var i = 0;
        setInterval(function () {
            for (var j = 0; j < imgs.length; j++) {
                imgs[j].style.display = "none";
            }
            for (var k = 0; k < 3; k++) {
                imgs[i + k].style.display = "inline-block";
            }
            i = (i + 3) % imgs.length;
        }, 2000);
    }
};


/*Código iconos*/
var icons = document.querySelectorAll(".fas");

for (var i = 0; i < icons.length; i++) {
    icons[i].addEventListener("mouseover", function () {
        var sound = new Audio("sound.mp3");
        sound.play();
        this.style.transform = "translate(-10px, -10px)";
    });
    icons[i].addEventListener("mouseout", function () {
        this.style.transform = "translate(0, 0)";
    });
}

