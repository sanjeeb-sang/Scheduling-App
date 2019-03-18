
window.onloadstart = function () {

    var x = document.getElementById("content-div");
    x.style.display = "none";

}

window.onload = function () {

    var x = document.getElementById("content-div");
    var y = document.getElementById("loading-div");
    x.style.display = "block";

}



function deleteMessage() {
    var x = document.getElementById("message");
    x.style.display = "none";
}

