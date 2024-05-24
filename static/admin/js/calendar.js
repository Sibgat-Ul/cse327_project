document.addEventListener('DOMContentLoaded', function() {
    let events = {};

    // Fetch events from the Django backend API
    fetch('/api/events/')
        .then(response => response.json())
        .then(data => {
            // Store events in a dictionary with dates as keys
            data.forEach(event => {
                const eventDate = event.date;
                if (!events[eventDate]) {
                    events[eventDate] = [];
                }
                events[eventDate].push(event.name);
            });
            initCalendar(events);
        });

    function initCalendar(events) {
        let today = new Date();
        let currentMonth = today.getMonth();
        let currentYear = today.getFullYear();

        let calendar = document.getElementById("calendar");
        let lang = calendar.getAttribute('data-lang');

        let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        let days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

        let $dataHead = "<tr>";
        for (let dhead in days) {
            $dataHead += "<th data-days='" + days[dhead] + "'>" + days[dhead] + "</th>";
        }
        $dataHead += "</tr>";

        document.getElementById("thead-month").innerHTML = $dataHead;

        let monthAndYear = document.getElementById("monthAndYear");
        showCalendar(currentMonth, currentYear);

        document.getElementById("previous").addEventListener('click', function() {
            currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
            currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
            showCalendar(currentMonth, currentYear);
        });

        document.getElementById("next").addEventListener('click', function() {
            currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
            currentMonth = (currentMonth + 1) % 12;
            showCalendar(currentMonth, currentYear);
        });

        function showCalendar(month, year) {
            let firstDay = (new Date(year, month)).getDay();
            let tbl = document.getElementById("calendar-body");
            tbl.innerHTML = "";
            monthAndYear.innerHTML = months[month] + " " + year;

            showMonthlyEvents(year, month);

            let date = 1;
            for (let i = 0; i < 6; i++) {
                let row = document.createElement("tr");
                for (let j = 0; j < 7; j++) {
                    if (i === 0 && j < firstDay) {
                        let cell = document.createElement("td");
                        let cellText = document.createTextNode("");
                        cell.appendChild(cellText);
                        row.appendChild(cell);
                    } else if (date > daysInMonth(month, year)) {
                        break;
                    } else {
                        let cell = document.createElement("td");
                        cell.setAttribute("data-date", date);
                        cell.setAttribute("data-month", month + 1);
                        cell.setAttribute("data-year", year);
                        cell.setAttribute("data-month_name", months[month]);
                        cell.className = "date-picker";
                        cell.innerHTML = "<span>" + date + "</span>";
                        cell.onclick = () => showEvents(year, month + 1, date, cell);

                        if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
                            cell.className = "date-picker selected";
                        }
                        row.appendChild(cell);
                        date++;
                    }
                }
                tbl.appendChild(row);
            }
        }

        function daysInMonth(iMonth, iYear) {
            return 32 - new Date(iYear, iMonth, 32).getDate();
        }

        function showEvents(year, month, date, cell) {
            const eventList = document.getElementById("event-list");
            const selectedDate = `${year}-${String(month).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
            eventList.innerHTML = "";

            document.querySelectorAll(".date-picker").forEach(cell => cell.classList.remove("clicked"));
            cell.classList.add("clicked");

            if (events[selectedDate]) {
                events[selectedDate].forEach(event => {
                    const eventDiv = document.createElement("div");
                    eventDiv.className = "event";
                    eventDiv.textContent = event;
                    eventList.appendChild(eventDiv);
                });
            } else {
                eventList.innerHTML = "<p>No events for this day.</p>";
            }
        }

        function showMonthlyEvents(year, month) {
            const eventList = document.getElementById("event-list");
            eventList.innerHTML = `<h3>Events for ${months[month]} ${year}</h3>`;

            const monthString = String(month + 1).padStart(2, '0');
            const yearString = String(year);

            let hasEvents = false;

            for (const date in events) {
                if (date.startsWith(`${yearString}-${monthString}`)) {
                    hasEvents = true;
                    events[date].forEach(event => {
                        const eventDiv = document.createElement("div");
                        eventDiv.className = "event";
                        eventDiv.textContent = `${date}: ${event}`;
                        eventList.appendChild(eventDiv);
                    });
                }
            }

            if (!hasEvents) {
                eventList.innerHTML += "<p>No events for this month.</p>";
            }
        }
    }
});
