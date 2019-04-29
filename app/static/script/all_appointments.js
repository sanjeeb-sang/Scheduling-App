// appointment object needs date, start_time, end_time, email_contact, id, title

var all_appointments = new Map();
var appointmentContainer = document.getElementById("appointment-container");

function initAppointments() {
    appointmentContainer.innerHTML = "";
}

document.onload = initAppointments();

function displayOneAppointment(appointment) {

    if (STATUS == "professor") {
        appointmentContainer.innerHTML += getHtmlForOneAppointmentForProfessor(appointment);
    } else {
        appointmentContainer.innerHTML += getHtmlForOneAppointment(appointment);
    }
}


function getHtmlForOneAppointment(appointment) {
    var html = getAHeading(appointment.title, appointment.id, true);
    html += `<h5 style="padding-left: 16px;"><i class="material-icons" style="font-size: 24px; margin-right: 8px;">calendar_today</i>` + appointment.date + `</h5>`;
    html += `<h5 style="padding-left: 16px;"><i class="material-icons" style="font-size: 24px; margin-right: 8px;">access_time</i>` + appointment.start_time + " to " + appointment.end_time + `</h5><span></span><hr />`;
    html += `<div style="padding-left: 16px;">`;
    html += getAButton("mailto:" + appointment.email_contact, "Send Email", "email");
    html += getAButton ("appointments/delete/" + appointment.id, "Delete", "delete");
    html += `</div><hr /></div>`;
    return html;
}

function getAHeading(title, id, enableDelete) {
    var html = `<div class="change-background mdl-color--white mdl-shadow--4dp"><h4 style="padding: 16px;" class="mdl-color--blue mdl-color-text--white">`;
    html += `<div style="display: inline-block; width: 95%;"><i class="material-icons" style="color: white; font-size: 24px; margin-right: 8px;">account_box</i>`
        + title + `</div>`;
    if (enableDelete) {
        html += `<div style="display: inline-block; width: 3%;"><a href="appointments/delete/` + id + `"><i class="material-icons" style="color: white; font-size: 36px;">delete_forever</i></a></div>`;
    }
    return html + `</h4>`;
}

function getAButton (link, text, icon) {
    return `<a style='margin-right: 16px;' href=` + link + `><button class="mdl-button mdl-js-button mdl-button--raised mdl-color--blue mdl-color-text--white">`
        + `<i class="material-icons" style="margin-right: 8px;">` + icon + "</i>" + text + "</button></a>";
}

function getHtmlForOneAppointmentForProfessor(appointment) {   
    var html = `<div style='padding: 0px;' class="change-background mdl-shadow--2dp">`;
    html += `<h5 class="mdl-color--blue mdl-color-text--white" style="padding: 8px 8px 24px 8px;"><i class="material-icons" style="font-size: 24px; margin-right: 8px;">access_time</i>` + appointment.start_time + " to " + appointment.end_time + `</h5><span></span>`;
    html += `<h5 style="padding-left: 48px; padding-bottom: 8px;">` + appointment.title + `</h5>`;
    html += `<div style="padding-left: 48px;">`;
    html += getAButton("mailto:" + appointment.email_contact, "Send Email", "email");
    html += getAButton("appointments/delete/" + appointment.id, "Delete", "delete");
    html += `</div><hr /></div>`;
    return html;
}


function onCalendarDateClicked(data) {

    var date = MONTHS[data.month] + " " + data.date + ", " + data.year;
    handleDate(date);
}

function handleTime(slot) {
    var appointment = all_appointments.get(slot.id);
    displayOneAppointment(appointment);
}

function onHandleDate() {
    appointmentContainer.innerHTML = "";
}

function Appointment(timeslot, emailContact, title, status) {
    this.date = timeslot.date;
    this.id = timeslot.id;
    this.start_time = timeslot.startTime;
    this.end_time = timeslot.endTime;
    this.email_contact = emailContact;
    this.title = title;
    this.status = status;
}