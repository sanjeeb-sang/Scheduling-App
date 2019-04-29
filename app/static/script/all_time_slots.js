
// csrf_token is defined in html
var slots = [];
var dates = [];
var datesToSlotsMap = new Map();
var slotsMap = new Map();

function Slot(d, s, e, id) {
    this.date = d;
    this.startTime = s;
    this.endTime = e;
    this.id = id;
}

function timeSlotClicked(d, s, e, id) {
    var p = document.getElementById("p");
    p.style.display = "block";
    $.post('/appointments/', {
        "date": d,
        "start_time": s,
        "end_time": e,
        "timeslot_id": id,
        "csrfmiddlewaretoken": csrfToken
    }, function (data, status) {
        p.style.display = "none";
        setTimeout(function () {
            window.location.href = "/all_appointments/";
        }, 300);
    }, 'json');
}
function handleDate(date) {
    onHandleDate();
    var root = document.getElementById('root');
    if (root != null) {
        root.innerHTML = `<div id="` + date + `" class="change-background mdl-color--white mdl-shadow--4dp"><h5 style="padding: 32px 16px 32px 32px;" class="mdl-color--blue mdl-color-text--white">` +
            `<div style="display: inline-block; width: 95%;"><i class="material-icons" style="color: white; font-size: 24px; margin-right: 8px;">account_box</i>` + date +
            `</div><div style="display: inline-block; width: 3%;"></div></h5></div>`;
    }
    var data = datesToSlotsMap.get(date);
    if (data == null) {
        return;
    }
    var arr = Array.from(data);
    arr.sort(compareTwoTimeslots);
    for (var j = 0; j < arr.length; j++) {
        var slot = arr[j];
        handleTime(slot);
    }
}

function compareTwoTimeslots(a, b) {
    var result = compareTwoTime(a.startTime, b.startTime);
    if (result == 0) {
        var endResult = compareTwoTime(a.endTime, b.endTime);
        return endResult < 0 ? -1 : 1;
    }
    return result < 0 ? -1 : 1;
}

function compareTwoTime(a, b) {
    if (a.includes("noon")) {
        a = "12 p.m.";
    }
    if (b.includes("noon")) {
        b = "12 p.m.";
    }
    var aTimeList = a.split(" ");
    var bTimeList = b.split(" ");
    if (aTimeList[1].includes("p")) {
        if (bTimeList[1].includes("a")) {
            return 1;
        }
    } else {
        if (bTimeList[1].includes("p")) {
            return -1;
        }
    }
    var aTime = a.split(" ")[0].split(":");
    var aHour = parseInt(aTime[0]);
    var aMins = 0;
    var bTime = b.split(" ")[0].split(":");
    var bHour = parseInt(bTime[0]);
    var bMins = 0;
    if (bTime.length > 1) {
        bMins = parseInt(bTime[1]);
    }
    if (aTime.length > 1) {
        aMins = parseInt(aTime[1]);
    }
    if (aHour == bHour) {
        return aMins - bMins;
    }
    return aHour - bHour;
}

function slotClicked(id) {
    var slot = slotsMap.get(id);
    timeSlotClicked(slot.date, slot.startTime, slot.endTime, slot.id);
}
function handleTime(slot) {
    var root = document.getElementById(slot.date);
    var onclick = `onclick="slotClicked('` + slot.id + `');"`;
    var html = `<div style='padding: 4px 8px 4px 32px;' id='` + slot.id + `'><h5><i class="material-icons" style="font-size: 24px; margin-right: 8px;">reorder</i>` + slot.startTime + ` to ` + slot.endTime + `<button style="margin-left: 32px;" class="mdl-button mdl-js-button mdl-button--raised" ` + onclick + `><i class="material-icons">done</i>Select</button>`;
    if (STATUS == "professor") {
        html += `<a href="/timeslots/delete/` + slot.id + `"><button style="margin-left: 16px;" class="mdl-button mdl-js-button mdl-button--raised"><i class="material-icons">delete_forever</i>Delete</button></a>`;
    }
    html += `</h5></div><hr />`;
    if (root != null) {
        root.innerHTML += html;
    }
}

function setDateTitle(slot) {
    var date = new Date(cleanDate(slot.date));
    var calendarDate = document.getElementById("date-" + date.getDate());
    var title = "\n" + slot.startTime + " to " + slot.endTime + "\n";
    calendarDate.title += title;
}

function handleSlots() {
    datesToSlotsMap.clear();
    slots.sort(compareTwoTimeslots);
    for (var i = 0; i < slots.length; i++) {
        var slot = slots[i];
        if (datesToSlotsMap.has(slot.date)) {
            var arr = Array.from(datesToSlotsMap.get(slot.date));
            arr.push(slot);
            datesToSlotsMap.set(slot.date, arr);
        } else {
            var arr = [];
            arr.push(slot);
            datesToSlotsMap.set(slot.date, arr);
            dates.push(slot.date);
        }
        setDateTitle(slot);
    }
    handleCalendarOptions();
}

function handleCalendarOptions() {
    var newArray = [];
    for (var i = 0; i < dates.length; i++) {
        var d = dates[i];
        d = cleanDate(d);
        newArray.push(d);
    }
    setDaysToHighlight(newArray);
}

function cleanDate(d) {
    var list = d.split(" ");
    var month = list[0];
    var day = list[1].replace(",", "");
    var year = list[2];
    return year + "-" + (MONTHS.indexOf(month) + 1) + "-" + day;
}

function onCalendarDateClicked(data) {
    var date = MONTHS[data.month] + " " + data.date + ", " + data.year;
    handleDate(date);
}

function init() {

}

// This function can be overridden in other scripts
function onHandleDate() {

}