
var error = document.getElementById("error");

function init() {
    document.getElementById("login-form").addEventListener("submit", onFormSubmit);
}
function onFormSubmit(e) {
    e.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == null || username.length == 0) {
        error.style.display = "block";
        error.innerHTML = "Enter valid Username";
        return;
    }
    if (password == null || password.length == 0) {
        error.style.display = "";
        error.innerHTML = "Enter valid password.";
        return;
    }
    document.getElementById("p").style.display = 'block';
    data = { "username": username, "password": password, "csrfmiddlewaretoken": csrfToken };
    $.post("/login/", data, function (data) {
        document.getElementById("p").style.display = 'none';
        switch (data["result"]) {
            case "OK":
                window.location = "/";
                break;
            case "Confirm Email":
                window.location = "confirm_email";
                break;
            default:
                window.location = "/";
        }
        
    });
}

document.onload = init();