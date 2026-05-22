// Tool-Calling Agent - Frontend JavaScript
// =========================================

let history = [];

// Initialize on page load
document.addEventListener("DOMContentLoaded", function() {
    setupToolButtons();
    loadHistory();
});

// Setup tool button click handlers
function setupToolButtons() {
    const toolButtons = document.querySelectorAll(".tool-btn");

    toolButtons.forEach(button => {
        button.addEventListener("click", function() {
            const tool = this.getAttribute("data-tool");
            switchTool(tool);
        });
    });
}

// Switch between tools
function switchTool(toolName) {
    // Update button states
    document.querySelectorAll(".tool-btn").forEach(btn => {
        btn.classList.remove("active");
    });
    document.querySelector(`[data-tool="${toolName}"]`).classList.add("active");

    // Update interface visibility
    document.querySelectorAll(".tool-interface").forEach(iface => {
        iface.classList.remove("active");
    });
    document.getElementById(`${toolName}-interface`).classList.add("active");
}

// Execute Calculator
async function executeCalculator() {
    const operation = document.getElementById("calc-operation").value;
    const num1 = parseFloat(document.getElementById("calc-num1").value);
    const num2 = parseFloat(document.getElementById("calc-num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        showError("Please enter valid numbers");
        return;
    }

    const data = { operation, num1, num2 };

    try {
        const response = await fetch("/api/calculator", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        displayResult(result);
        addToHistory("calculator", result.success);

    } catch (error) {
        showError("Failed to connect to server: " + error.message);
    }
}

// Execute Time
async function executeTime() {
    try {
        const response = await fetch("/api/time");
        const result = await response.json();
        displayResult(result);
        addToHistory("get_time", result.success);

    } catch (error) {
        showError("Failed to connect to server: " + error.message);
    }
}

// Execute Weather
async function executeWeather() {
    const city = document.getElementById("weather-city").value.trim();

    if (!city) {
        showError("Please enter a city name");
        return;
    }

    try {
        const response = await fetch("/api/weather", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ city })
        });

        const result = await response.json();
        displayResult(result);
        addToHistory("weather", result.success);

    } catch (error) {
        showError("Failed to connect to server: " + error.message);
    }
}

// Execute Text Analyzer
async function executeAnalyzer() {
    const text = document.getElementById("analyzer-text").value.trim();

    if (!text) {
        showError("Please enter some text to analyze");
        return;
    }

    try {
        const response = await fetch("/api/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const result = await response.json();
        displayResult(result);
        addToHistory("text_analyzer", result.success);

    } catch (error) {
        showError("Failed to connect to server: " + error.message);
    }
}

// Display result in the results section
function displayResult(result) {
    const container = document.getElementById("results-container");

    const resultDiv = document.createElement("div");
    resultDiv.className = `result-item ${result.success ? "" : "error"}`;

    const header = document.createElement("div");
    header.className = "result-header";

    const toolName = document.createElement("span");
    toolName.className = "result-tool";
    toolName.textContent = result.tool_name || "Unknown Tool";

    const timestamp = document.createElement("span");
    timestamp.className = "result-time";
    timestamp.textContent = new Date(result.timestamp).toLocaleTimeString();

    header.appendChild(toolName);
    header.appendChild(timestamp);

    const content = document.createElement("div");
    content.className = "result-content";

    if (result.success) {
        content.innerHTML = formatSuccessResult(result);
    } else {
        content.innerHTML = `<strong>Error:</strong> ${result.error}`;
    }

    resultDiv.appendChild(header);
    resultDiv.appendChild(content);

    const placeholder = container.querySelector(".placeholder");
    if (placeholder) {
        placeholder.remove();
    }

    container.insertBefore(resultDiv, container.firstChild);

    while (container.children.length > 5) {
        container.removeChild(container.lastChild);
    }
}

// Format success result based on tool type
function formatSuccessResult(result) {
    const tool = result.tool_name;

    if (tool === "calculator") {
        return `<strong>Result:</strong> ${result.result}<br>
                <small>Operation: ${result.operation} | Inputs: ${result.inputs.num1}, ${result.inputs.num2}</small>`;
    }

    if (tool === "get_time") {
        return `<strong>Time:</strong> ${result.time}<br>
                <strong>Date:</strong> ${result.date}<br>
                <strong>Day:</strong> ${result.day}`;
    }

    if (tool === "weather") {
        return `<strong>City:</strong> ${result.city}<br>
                <strong>Temperature:</strong> ${result.temperature}°${result.unit}<br>
                <strong>Condition:</strong> ${result.condition}<br>
                <strong>Humidity:</strong> ${result.humidity}%`;
    }

    if (tool === "text_analyzer") {
        return `<strong>Words:</strong> ${result.word_count}<br>
                <strong>Characters:</strong> ${result.character_count} (${result.character_count_no_spaces} without spaces)<br>
                <strong>Sentences:</strong> ${result.sentence_count}<br>
                <strong>Uppercase:</strong> ${result.uppercase_count} | <strong>Lowercase:</strong> ${result.lowercase_count}`;
    }

    return "<pre>" + JSON.stringify(result, null, 2) + "</pre>";
}

// Show error message
function showError(message) {
    const container = document.getElementById("results-container");

    const errorDiv = document.createElement("div");
    errorDiv.className = "result-item error";
    errorDiv.innerHTML = `
        <div class="result-header">
            <span class="result-tool">Error</span>
            <span class="result-time">${new Date().toLocaleTimeString()}</span>
        </div>
        <div class="result-content">${message}</div>
    `;

    const placeholder = container.querySelector(".placeholder");
    if (placeholder) {
        placeholder.remove();
    }

    container.insertBefore(errorDiv, container.firstChild);
}

// Add to history
function addToHistory(toolName, success) {
    const historyItem = {
        tool: toolName,
        success: success,
        timestamp: new Date().toISOString()
    };

    history.unshift(historyItem);

    if (history.length > 20) {
        history = history.slice(0, 20);
    }

    saveHistory();
    renderHistory();
}

// Render history
function renderHistory() {
    const container = document.getElementById("history-container");

    if (history.length === 0) {
        container.innerHTML = "<p class='placeholder'>No history yet</p>";
        return;
    }

    container.innerHTML = "";

    history.slice(0, 10).forEach(item => {
        const historyDiv = document.createElement("div");
        historyDiv.className = "history-item";

        const time = new Date(item.timestamp).toLocaleTimeString();
        const statusClass = item.success ? "success" : "error";
        const statusText = item.success ? "✓" : "✗";

        historyDiv.innerHTML = `
            <span><span class="tool-name">${item.tool}</span> - ${time}</span>
            <span class="status ${statusClass}">${statusText}</span>
        `;

        container.appendChild(historyDiv);
    });
}

// Save history to localStorage
function saveHistory() {
    try {
        localStorage.setItem("agent_history", JSON.stringify(history));
    } catch (e) {
        console.error("Failed to save history:", e);
    }
}

// Load history from localStorage
function loadHistory() {
    try {
        const saved = localStorage.getItem("agent_history");
        if (saved) {
            history = JSON.parse(saved);
            renderHistory();
        }
    } catch (e) {
        console.error("Failed to load history:", e);
    }
}

// Clear history
function clearHistory() {
    if (confirm("Are you sure you want to clear the history?")) {
        history = [];
        saveHistory();
        renderHistory();
    }
}
