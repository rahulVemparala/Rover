function filterObjects(c) {
    var x, i;
    x = document.getElementsByClassName("song");
    if (c == "all") c = "";
    for (i = 0; i < x.length; i++) {
        if (x[i].className.indexOf(c) > -1) {
            x[i].style.display = "block";
        } else {
            x[i].style.display = "none";
        }
    }

    // Smoothly scroll to the song-section element
    var songSection = document.getElementById("song-section");
    if (songSection) {
        songSection.scrollIntoView({ behavior: "smooth" });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});


// Or with jQuery

$(document).ready(function () {
    $('.fixed-action-btn').floatingActionButton();
});



var instance = M.FloatingActionButton.getInstance(elem);


$(document).ready(function () {
    $('.tabs').tabs();
});

$(document).ready(function () {
    $('.tooltip').tooltip();
});