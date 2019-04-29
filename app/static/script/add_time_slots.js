var slotsRootContainer = document.getElementById("slots-root-container");
var slotsContainer = null;
var timeslotsContainer = document.getElementById('timeslots_container');
var numOfSlots = document.getElementById('number_of_time_slots');
var startTime = document.getElementById("start_time");
var endTime = document.getElementById("end_time");
var hideSlotsButton = document.getElementById("hide_slots_button");

function numSlotsChanged(node) {

    slotsRootContainer.innerHTML = "";
    slotsRootContainer.innerHTML += `<table style="table-layout: fixed; width: 100%;" id="timeslots_container" class="">`
        + `<caption>All time slots</caption><thead>`
        + `<tr><th class="">Time slot number</th><th class="">Start time</th><th class="">End Time</th>`
        + `<th class="">Total Time</th></tr></thead><tbody id="all_timeslots"><tbody></table>`;

    slotsContainer = document.getElementById("all_timeslots");

    var slots = getTimeSlots();

    for (var i = 0; i < slots.length; i++) {
        var slot = slots[i];
        slotsContainer.innerHTML += "<tr><td>" + (i + 1) + "</td><td>" + slot.start + "</td><td>" + slot.end + "</td><td>" + slot.slotTime + " minutes</td></tr>";
    }
    timeslotsContainer.style.display = "block";
    hideSlotsButton.style.display = "block";
}

function hideSlots() {
    slotsContainer.innerHTML = "";
    timeslotsContainer.style.display = "none";
    hideSlotsButton.style.display = "none";
}

function onFocusOnNumSlots() {
    var start = startTime.value;
    var end = endTime.value;
    if (start.length == 0) {
        startTime.focus();
    }
    if (end.length == 0) {
        endTime.focus();
    }
}

function addToTime(time, hourToAdd, minToAdd) {
    var h = parseInt(getHour(time));
    var m = parseInt(getMinutes(time));
    h += hourToAdd;
    m += minToAdd;
    while (m == 60 || m >= 60) {
        h += 1;
        m -= 60;
    }

    if (m == 60) {
        h += 1;
        m -= 60;
    }

    if (h < 10) {
        h = "0" + h;
    }
    if (m < 10) {
        m = "0" + m;
    }
    return h + ":" + m;
}

function getHour(time) {
    var listByColon = time.split(":");
    return listByColon[0];
}

function getTimeSlots() {
    var result = [];
    var slots = numOfSlots.value;
    var start = startTime.value;
    var end = endTime.value;
    var totalTime = getTimeDifference(start, end);
    var slotTime = totalTime / slots;

    var current = start;

    for (var i = 0; i < slots; i++) {
        result.push(new Timeslot(current, addToTime(current, 0, slotTime), slotTime));
        current = addToTime(current, 0, slotTime);
    }
    console.log(result);
    return result;
}

function Timeslot(start, end, slotTime) {
    this.start = start;
    this.end = end;
    this.slotTime = slotTime;
}

function getTimeDifference(low, higher) {
    var higherHour = parseInt(getHour(higher));
    var lowHour = parseInt(getHour(low));
    var higherMinute = parseInt(getMinutes(higher));
    var lowMinute = parseInt(getMinutes(low));
    var diff = 0;

    if ((higherHour - lowHour) >= 1) {
        diff += (higherHour - lowHour) * 60;
    }

    diff += higherMinute - lowMinute;

    return diff;
}

function getMinutes(time) {
    return time.split(":")[1];
}

function setUpSubmit() {

    var submitFunction = function () {

        document.getElementById("p").style.display = "block";
        document.getElementById("p-text").style.display = "block";
        document.getElementById("submit-button").style.display = "none";

        var slots = getTimeSlots();

        var startTimes = [];
        var endTimes = [];
        var timeSlot = 0;
        var first = true;

        var date = getSelectedDate();

        for (var i = 0; i < slots.length; i++) {
            startTimes.push(slots[i].start);
            endTimes.push(slots[i].end);
            if (first) {
                first = false;
                timeSlot = slots[i].timeSlot;
            }
        }
        $.post('/timeslots/', {
            "professor_email": PROFESSOR_EMAIL,
            "date": getSelectedDate(),
            "startTimes[]": startTimes,
            "endTimes[]": endTimes,
            "csrfmiddlewaretoken": csrfToken
        }, function (data, status) {
            document.getElementById("p-text").innerHTML = "Time Slots have been added.";
            setTimeout(function () {
                document.getElementById("p-text").style.display = "none";
                document.getElementById("p").style.display = "none";
                document.getElementById("submit-button").style.display = "block";
                setTimeout(function () {
                    window.location.href = "/all_timeslots/";
                }, 500);
            }, 500);
        }, 'json');
    };

    $('#submit-button').click(submitFunction);


}

document.onload = initialize();

function onCalendarDateClicked(data) {
    console.log("/--/");
}

function initialize() {
    setUpSubmit();
}