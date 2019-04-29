var linksContainer = document.getElementById('drawer-links-container');

function addMainLink(icon, name, url) {
    var html = `<a class="nav-link" href="` + url + `"><div><i class="drawer-icons material-icons mdl-color-text--white">`
    + icon + `</i><span class="drawer-text">` + name + `</span></div></a>`;

    linksContainer.innerHTML += html;
}


function addSubLinks() {

}

function init() {
    addMainLink();
    addMainLink();
    addMainLink();
}

document.onload = init();