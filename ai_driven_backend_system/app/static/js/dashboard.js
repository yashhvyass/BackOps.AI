// dashboard.js
import { VoiceRecorder } from './voiceRecorder.js';
import { APIHandler } from './api.js';
import { MessageHandler } from './messageHandler.js';

class Dashboard {
    constructor() {
        this.messageLimit = 50; // Maximum number of messages to show
        this.activityUpdateInterval = null;
        this.initializeElements();
        this.initializeCharts();
        this.initializeCalendar();
        this.setupEventListeners();
        this.loadInitialData();
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

        // Initialize handlers
        this.messageHandler = new MessageHandler(this.chatMessages);
        this.voiceRecorder = new VoiceRecorder(this.handleTranscription.bind(this));
        this.voiceRecorder.initialize();
    }

    initializeCharts() {
        // Activity Chart
        const ctx = document.getElementById('activityChart').getContext('2d');
        this.activityChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                datasets: [{
                    label: 'Queries',
                    data: [1, 2, 2, 2, 2, 2, 2],
                    backgroundColor: '#4CAF50',
                    borderColor: '#4CAF50',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 3,
                        ticks: {
                            stepSize: 1
                        }
                    }
                },
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0 // Disable animations for better performance
                }
            }
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

    setupEventListeners() {
        this.sendBtn.addEventListener('click', () => this.handleSendMessage());
        this.voiceBtn.addEventListener('click', () => this.handleVoiceRecording());
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.handleSendMessage();
        });

        document.getElementById('viewLogsBtn').addEventListener('click', () => {
            // Implement logs view functionality
            console.log('View logs clicked');
        });
    }

    async handleSendMessage() {
        const message = this.userInput.value.trim();
        if (!message) return;

        // Clear old messages if limit is reached
        const messages = this.chatMessages.children;
        if (messages.length >= this.messageLimit) {
            this.chatMessages.removeChild(messages[0]);
        }

        this.messageHandler.addMessage(message, true);
        this.messageHandler.clearInput(this.userInput);
        this.sendBtn.disabled = true;

        try {
            const response = await APIHandler.sendChatMessage(message);
            this.messageHandler.addMessage(response, false);
            this.updateMetrics(false); // Pass false to prevent continuous updates
        } catch (error) {
            this.messageHandler.addMessage('Error: Could not get response', false);
        }

        this.sendBtn.disabled = false;
        
        // Scroll to bottom after new message
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    handleVoiceRecording() {
        const isRecording = this.voiceRecorder.toggleRecording();
        this.voiceBtn.classList.toggle('recording', isRecording);
    }

    handleTranscription(text) {
        if (text) {
            this.userInput.value = text;
            this.handleSendMessage();
        }
    }

    updateMetrics(updateChart = true) {
        // Update overview metrics
        const currentQueries = parseInt(this.totalQueriesElement.textContent);
        this.totalQueriesElement.textContent = currentQueries + 1;
        
        // Update response time (simulated)
        const responseTime = (Math.random() * 0.5 + 0.1).toFixed(2);
        this.avgResponseTimeElement.textContent = `${responseTime}s`;
        
        // Update success rate
        const successRate = (Math.random() * 2 + 97).toFixed(1);
        this.successRateElement.textContent = `${successRate}%`;

        // Randomly Update Metrics
        const RandomFact = (Math.random() * 2 + 97).toFixed(1);
        this.randomvizElement.textContent = `${RandomFact}%`;

        // Only update chart if specified
        if (updateChart) {
            const dayOfWeek = new Date().getDay();
            const newData = [...this.activityChart.data.datasets[0].data];
            newData[dayOfWeek] = Math.min(newData[dayOfWeek] + 1, 3); // Cap at 3
            this.activityChart.data.datasets[0].data = newData;
            this.activityChart.update('none'); // Use 'none' mode for better performance
        }
    }

    loadInitialData() {
        // Set initial values
        this.totalQueriesElement.textContent = '156';
        this.avgResponseTimeElement.textContent = '0.3s';
        this.successRateElement.textContent = '98.5%';
        this.randomvizElement.textContent = '70.5%';
    }
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