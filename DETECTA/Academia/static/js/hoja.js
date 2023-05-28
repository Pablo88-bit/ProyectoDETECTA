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

/*Código de los cursos
window.onload = function() {
    var cursos = document.getElementsByClassName("col-4");
    var currentIndex = 0;
    var maxIndex = cursos.length - 1;
    var interval = setInterval(changeCursos, 30000);

    function changeCursos() {
        cursos[currentIndex].style.display = "none";
        cursos[currentIndex + 1].style.display = "none";
        currentIndex = (currentIndex + 3) % maxIndex;
        cursos[currentIndex].style.display = "block";
        cursos[currentIndex + 1].style.display = "block";
    }
};


window.onload = function () {
    var galeria = document.getElementById("curso");
    if (galeria) {
        var imgs = galeria.getElementsByTagName("card-curso");
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


window.onload = function () {
    var galeria = document.getElementById("galeria2");
    var row = galeria.querySelector(".row");
    var prevBtn = galeria.querySelector(".carousel-prev");
    var nextBtn = galeria.querySelector(".carousel-next");
    var cursos = galeria.querySelectorAll(".col-4");
    var currentIndex = 0;
    var maxIndex = cursos.length - 1;
    var interval = setInterval(changeCursos, 40000);

    function changeCursos() {
        currentIndex = (currentIndex + 3) % maxIndex;
        row.style.transform = `translateX(-${currentIndex * 33.33}%)`;
    }

    function prevCursos() {
        currentIndex = (currentIndex - 3 + maxIndex) % maxIndex;
        row.style.transform = `translateX(-${currentIndex * 33.33}%)`;
    }

    function nextCursos() {
        currentIndex = (currentIndex + 3) % maxIndex;
        row.style.transform = `translateX(-${currentIndex * 33.33}%)`;
    }

    prevBtn.addEventListener("click", prevCursos);
    nextBtn.addEventListener("click", nextCursos);
};*/
