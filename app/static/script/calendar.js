
const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

var container = document.getElementById("calendar");
var month = null;
var year = null;
var daysToHighlight = new Map();
var previousClickedDate = 0;
var alwaysHighlightDays = [];
var selectedDate = 0;

function initCalendar() {

    container.innerHTML = `<div id="calendar-root"><table style='width: 100%;' class='mdl-shadow--4dp'><caption>` + getHeaders() + `</caption><thead><th>Sunday</th><th>Monday</th><th>Tuesday</th>` +
        `<th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th></thead><tbody id="c-body"></tbody></table></div>`;
    month = document.getElementById("month");
    year = document.getElementById("year");
}


function loadCalendar(date) {
    y = date.getFullYear(), m = date.getMonth();
    var firstDay = new Date(y, m, 1);
    var lastDay = new Date(y, m + 1, 0);

    document.getElementById("month").value = m;
    document.getElementById("year").value = y;

    var monthName = MONTHS[m];
    var year = y;

    var startDay = firstDay.getDay();

    var stop = false;
    var current = 1;
    var d = 1;
    var addFirst = false;
    var html = "<tr>";

    while (!stop) {
        if (!addFirst) {
            if (current == startDay) {
                addFirst = true;
            } 
            html += "<td></td>";
        } else {
            html += "<td onclick='onDateClick(" + d + ")' id='date-" + d + "'>" + d + "</td>";
            if (d >= lastDay.getDate()) {
                stop = true;
                html += "</tr>";
            }
            d++;
            if (!stop && current % 7 == 0) {
                html += "</tr><tr>";
            }
        }
        current++;
    }
    document.getElementById("c-body").innerHTML = html;
    handleTodaysDate();
    handleHighlights();
}

function handleTodaysDate() {
    if (isCurrentMonth()) {
        var today = new Date();
        highlightThisDate(today.getDate());
        alwaysHighlightDays.push(today.getDate());
    }
}

function isCurrentMonth() {
    var y = parseInt(year.value);
    var m = parseInt(month.value);
    var today = new Date();
    if (today.getYear() + 1900 == y) {
        if (today.getMonth() == m) {
            return true;
        }
    }
    return false;
}


function handleHighlights() {
    previousClickedDate = 0;
    alwaysHighlightDays = [];
    var y = parseInt(year.value);
    var m = parseInt(month.value);
    if (daysToHighlight != null && daysToHighlight.size > 0) {
        if (daysToHighlight.has(y)) {
            var months = new Map(daysToHighlight.get(y));
            if (months.has(m)) {
                var daysArray = Array.from(months.get(m));
                for (var i = 0; i < daysArray.length; i++) {
                    highlightDate(daysArray[i].getDate());
                }
            }
        }
    }
}

function highlightDate(date) {
    alwaysHighlightDays.push(date);
    var focus = document.getElementById("date-" + date);
    if (isCurrentMonth() && date == (new Date()).getDate()) {
        focus.style.backgroundColor = '#6A1B9A';
    } else {
        focus.style.backgroundColor = '#C2185B';
    }
    focus.style.color = 'white';
}


function highlightClickedDate(date) {
    if (previousClickedDate != 0) {
        var p = document.getElementById("date-" + previousClickedDate);
        p.style.backgroundColor = '#FAFAFA';
        p.style.color = 'black';
        previousClickedDate = 0;
    }
    if (alwaysHighlightDays.includes(date)) {
        return;
    }
    var focus = document.getElementById("date-" + date);
    focus.style.backgroundColor = '#0D47A1';
    focus.style.color = 'white';
    previousClickedDate = date;
}

function highlightThisDate(date) {
    selectedDate = date;
    var focus = document.getElementById("date-" + date);
    focus.style.backgroundColor = '#006064';
    focus.style.color = 'white';
}

function getHeaders() {
    var select = `<select id='year' onchange="onYearChange()">`;
    for (var i = 2019; i < 2030; i++) {
        select += "<option value='" + i + "'>" + i + "</option>";
    }
    select += "</select>";
    var year = `<div id='year-box'>` + select + `</div>`;

    var months = `<select id='month' onchange="onMonthChange()"><option value="0">January</option><option value="1">February</option><option value="2">` +
        `March</option><option value="3">April</option><option value="4">May</option><option value="5">` +
        `June</option><option value="6">July</option><option value="7">August</option><option value="8">` + 
        `September</option><option value="9">October</option><option value="10">November</option><option value="11">` + 
        `December</option></select>`;
    var month = `<div id='month-box'>` + months + `</div>`;
    return month + year;
}

function setDaysToHighlight(datesArray) {
    daysToHighlight.clear();
    var dates = Array.from(datesArray);
    for (var i = 0; i < dates.length; i++) {
        var d = new Date(dates[i]);
        if (daysToHighlight.has(d.getYear() + 1900)) {
            var monthMap = new Map(daysToHighlight.get(d.getYear() + 1900));
            if (monthMap.has(d.getMonth())) {
                var daysArray = Array.from(monthMap.get(d.getMonth()));
                daysArray.push(d);
                monthMap.set(d.getMonth(), daysArray);
                daysToHighlight.set(d.getYear() + 1900, monthMap);
            } else {
                var daysArray = [];
                daysArray.push(d);
                monthMap.set(d.getMonth(), daysArray);
                daysToHighlight.set(d.getYear() + 1900, monthMap);
            }
        } else {
            var monthMap = new Map();
            var daysArray = [];
            daysArray.push(d);
            monthMap.set(d.getMonth(), daysArray);
            daysToHighlight.set(d.getYear() + 1900, monthMap);
        }
    }
    handleHighlights();
}

function getSelectedDate(date) {
    return year.value + "-" + (parseInt(month.value) + 1) + "-" + selectedDate;
}

function onDateClick(d) {
    highlightClickedDate(d);
    selectedDate = d;
    onCalendarDateClicked({year: year.value, month: month.value, date: d});
}


function onMonthChange() {
    loadCalendar(new Date(year.value, month.value, 1));
}

function onYearChange() {
    loadCalendar(new Date(year.value, month.value, 1));
}
   
document.onload = initialize();


function initialize() {
    initCalendar();
    loadCalendar(new Date());
}

    