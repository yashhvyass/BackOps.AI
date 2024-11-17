class Dashboard {
    constructor() {
        this.messageLimit = 50; // Maximum number of messages to show
        this.activityUpdateInterval = null;
        this.initializeElements();
        this.initializeCharts();
        this.initializeCalendar();
        // this.loadInitialData();
    }

    initializeElements() {
        // Overview metrics
        this.totalQueriesElement = document.getElementById('totalQueries');
        this.avgResponseTimeElement = document.getElementById('avgResponseTime');
        this.successRateElement = document.getElementById('successRate');
        this.randomvizElement = document.getElementById('RandomFact');

        // Chat elements
        this.userInput = document.getElementById('userInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.voiceBtn = document.getElementById('voiceBtn');
        this.chatMessages = document.getElementById('chatMessages');
    }

    initializeCharts() {
        // Activity Chart
        const ctx = document.getElementById('activityChart').getContext('2d');
        this.activityChart = new Chart(ctx, {
          type: "bar",
          data: {
            labels: [
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Sunday",
            ],
            datasets: [
              {
                label: "Queries",
                data: [1, 3, 2, 1, 2, 0, 2],
                backgroundColor: "#BA5370",
                borderColor: "#BA5370",
                borderWidth: 1,
                fontFamily: "Cinzel",
              },
            ],
          },
          options: {
            scales: {
              x: {
                grid: {
                  color: "#f8f7ff", // Color of the grid lines for the x-axis
                  lineWidth: 1, // Thickness of the grid lines
                },
                ticks: {
                  color: "#f8f7ff", // Color of the labels for the x-axis
                },
              },
              y: {
                beginAtZero: true,
                max: 3,
                ticks: {
                  stepSize: 1,
                  color: "#f8f7ff", // Color of the labels for the y-axis
                },
                grid: {
                  color: "#f8f7ff", // Color of the grid lines for the y-axis
                  lineWidth: 1, // Thickness of the grid lines
                },
              },
            },
            plugins: {
              legend: {
                labels: {
                  color: "#f8f7ff", // Color for the "Queries" label
                  font: {
                    size: 14, // Font size for the legend label
                    weight: "bold", // Font weight for the legend label
                  },
                },
              },
            },
          },
        });
    }

    // Clean up method to prevent memory leaks
    destroy() {
        if (this.activityUpdateInterval) {
            clearInterval(this.activityUpdateInterval);
        }
        if (this.activityChart) {
            this.activityChart.destroy();
        }
    }

    initializeCalendar() {
        const calendar = document.getElementById('calendar');
        const currentDate = new Date();
        const month = currentDate.toLocaleString('default', { month: 'long' });
        
        // Create calendar header
        const header = document.createElement('div');
        header.className = 'header';
        header.textContent = month;
        calendar.appendChild(header);

        // Create days grid
        const daysContainer = document.createElement('div');
        daysContainer.className = 'days';
        
        // Add days
        const daysInMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();
        for (let i = 1; i <= daysInMonth; i++) {
            const day = document.createElement('div');
            day.className = 'day';
            day.textContent = i;
            daysContainer.appendChild(day);
        }
        
        calendar.appendChild(daysContainer);
    }

    // loadInitialData() {
    //     // Set initial values
    //     this.totalQueriesElement.textContent = '156';
    //     this.avgResponseTimeElement.textContent = '0.3s';
    //     this.successRateElement.textContent = '98.5%';
    //     this.randomvizElement.textContent = '70.5%';
    // }
}

// Initialize dashboard when DOM is loaded and handle cleanup
let dashboardInstance;
document.addEventListener('DOMContentLoaded', () => {
    dashboardInstance = new Dashboard();
});

window.addEventListener('beforeunload', () => {
    if (dashboardInstance) {
        dashboardInstance.destroy();
    }
});