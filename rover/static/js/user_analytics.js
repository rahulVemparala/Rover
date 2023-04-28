// First Pie Chart
var ctx1 = document.getElementById("chart1").getContext("2d");
var chart1 = new Chart(ctx1, {
    type: "pie",
    data: {
        labels: ["Pop", "Rock", "Dance", "Rap", "Hip-Hop", "Country", "EDM"],
        datasets: [
            {
                label: "View Count",
                data: [10, 20, 15, 5, 8, 12, 30],
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#1E90FF",
                    "#9400D3",
                    "#008000",
                    "#FF69B4",
                ],
                hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#1E90FF",
                    "#9400D3",
                    "#008000",
                    "#FF69B4",
                ],
            },
        ],
    },
});

// Second Pie Chart
var ctx2 = document.getElementById("chart2").getContext("2d");
var chart2 = new Chart(ctx2, {
    type: "pie",
    data: {
        labels: ["Pop", "Rock", "Dance", "Rap", "Hip-Hop", "Country", "EDM"],
        datasets: [
            {
                label: "Favorite Genre",
                data: [5, 15, 10, 20, 25, 8, 17],
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#1E90FF",
                    "#9400D3",
                    "#008000",
                    "#FF69B4",
                ],
                hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#1E90FF",
                    "#9400D3",
                    "#008000",
                    "#FF69B4",
                ],
            },
        ],
    },
});
