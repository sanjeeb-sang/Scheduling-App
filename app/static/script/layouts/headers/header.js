



function headerHtml(title, link, icon, name) {
    var html = `<div class="mdl-grid mdl-color--indigo-400 mdl-color-text--white mdl-shadow--4dp center" style="margin-bottom: 16px; padding: 16px; background-color: #EEEEEE;">`
         + `<div class="mdl-cell mdl-cell--10-col"><h3>` + title + `</h3></div><div class="mdl-cell mdl-cell--2-col" style="padding-top: 16px;">`
         + `<a href="` + link + `"><button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"><i class="material-icons" style="margin-right: 8px;">` + icon + `</i>` + name + `</button></a>`
         + `</div></div>`;
    return html;
}

function setHeader(title, link, icon, name) {
    var headerContainer = document.getElementById("title-header");
    headerContainer.innerHTML = headerHtml(title, link, icon, name);
}
