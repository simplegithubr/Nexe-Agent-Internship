const queryInput = document.getElementById('queryInput');
const calculateBtn = document.getElementById('calculateBtn');
const resultContainer = document.getElementById('resultContainer');
const loadingIndicator = document.getElementById('loadingIndicator');
const errorContainer = document.getElementById('errorContainer');
const memoryList = document.getElementById('memoryList');
const clearMemoryBtn = document.getElementById('clearMemoryBtn');
const closeResultBtn = document.getElementById('closeResult');

calculateBtn.addEventListener('click', handleCalculate);
queryInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleCalculate();
    }
});

document.querySelectorAll('.quick-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const query = btn.getAttribute('data-query');
        queryInput.value = query;
        handleCalculate();
    });
});

clearMemoryBtn.addEventListener('click', clearMemory);
closeResultBtn.addEventListener('click', () => {
    resultContainer.style.display = 'none';
});

async function handleCalculate() {
    const query = queryInput.value.trim();

    if (!query) {
        showError('Please enter a calculation query');
        return;
    }

    hideError();
    hideResult();
    showLoading();

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });

        const data = await response.json();

        hideLoading();

        if (data.success) {
            displayResult(data.data);
            loadMemory();
        } else {
            showError(data.error || 'Calculation failed');
        }
    } catch (error) {
        hideLoading();
        showError('Network error: ' + error.message);
    }
}

function displayResult(data) {
    document.getElementById('resultExpression').textContent = data.expression || 'N/A';
    document.getElementById('resultAnswer').textContent = data.result || 'N/A';

    const stepsList = document.getElementById('resultSteps');
    stepsList.innerHTML = '';
    if (data.steps && data.steps.length > 0) {
        data.steps.forEach(step => {
            const li = document.createElement('li');
            li.textContent = step;
            stepsList.appendChild(li);
        });
    } else {
        stepsList.innerHTML = '<li>No steps available</li>';
    }

    document.getElementById('resultExplanation').textContent = data.explanation || 'No explanation available';

    resultContainer.style.display = 'block';
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function showLoading() {
    loadingIndicator.style.display = 'block';
}

function hideLoading() {
    loadingIndicator.style.display = 'none';
}

function showError(message) {
    document.getElementById('errorMessage').textContent = message;
    errorContainer.style.display = 'flex';
    setTimeout(() => {
        hideError();
    }, 5000);
}

function hideError() {
    errorContainer.style.display = 'none';
}

function hideResult() {
    resultContainer.style.display = 'none';
}

async function loadMemory() {
    try {
        const response = await fetch('/memory');
        const data = await response.json();

        if (data.success && data.memory.length > 0) {
            displayMemory(data.memory);
        } else {
            displayEmptyMemory();
        }
    } catch (error) {
        console.error('Failed to load memory:', error);
    }
}

function displayMemory(memory) {
    memoryList.innerHTML = '';

    memory.reverse().forEach(item => {
        const memoryItem = document.createElement('div');
        memoryItem.className = 'memory-item';
        memoryItem.innerHTML = `
            <div class="memory-item-header">
                <div class="memory-query">${escapeHtml(item.query)}</div>
                <button class="memory-delete" onclick="deleteMemoryItem(${item.id})">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
            <div class="memory-result">${escapeHtml(String(item.result))}</div>
            <div class="memory-timestamp">
                <i class="fas fa-clock"></i>
                ${item.timestamp}
            </div>
        `;
        memoryList.appendChild(memoryItem);
    });
}

function displayEmptyMemory() {
    memoryList.innerHTML = `
        <div class="empty-state">
            <i class="fas fa-inbox"></i>
            <p>No calculations yet. Start by asking a math question!</p>
        </div>
    `;
}

async function clearMemory() {
    if (!confirm('Are you sure you want to clear all calculation history?')) {
        return;
    }

    try {
        const response = await fetch('/memory/clear', {
            method: 'POST'
        });

        const data = await response.json();

        if (data.success) {
            displayEmptyMemory();
            showTemporaryMessage('Memory cleared successfully', 'success');
        }
    } catch (error) {
        showError('Failed to clear memory: ' + error.message);
    }
}

async function deleteMemoryItem(id) {
    try {
        const response = await fetch(`/memory/${id}`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if (data.success) {
            loadMemory();
            showTemporaryMessage('Calculation deleted', 'success');
        }
    } catch (error) {
        showError('Failed to delete calculation: ' + error.message);
    }
}

function showTemporaryMessage(message, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `temp-message temp-message-${type}`;
    messageDiv.innerHTML = `
        <i class="fas fa-check-circle"></i>
        <span>${message}</span>
    `;
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        display: flex;
        align-items: center;
        gap: 10px;
        z-index: 1000;
        animation: slideInRight 0.3s ease;
    `;

    document.body.appendChild(messageDiv);

    setTimeout(() => {
        messageDiv.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(messageDiv);
        }, 300);
    }, 3000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

loadMemory();
