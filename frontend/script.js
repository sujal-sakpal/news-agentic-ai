document.addEventListener('DOMContentLoaded', () => {
    const topicInput = document.getElementById('topic-input');
    const searchButton = document.getElementById('search-button');
    const resultsContainer = document.getElementById('results-container');

    // API endpoint for the backend
    const API_URL = 'http://localhost:8000/get-news-summary';

    const showLoader = () => {
        resultsContainer.innerHTML = `
            <div class="loader">
                <div class="spinner"></div>
                <p>The AI crew is assembling...</p>
                <small>This may take a minute.</small>
            </div>
        `;
    };

    const displayResults = (summary) => {
        // Use the 'marked' library to convert markdown to HTML
        // This makes sure the formatting from the agent looks good.
        const htmlContent = marked.parse(summary);
        resultsContainer.innerHTML = `<div class="summary-content">${htmlContent}</div>`;
    };

    const displayError = (errorMessage) => {
        resultsContainer.innerHTML = `
            <div class="error-message">
                <h3>An Error Occurred</h3>
                <p>${errorMessage}</p>
            </div>
        `;
    };

    const handleSearch = async () => {
        const topic = topicInput.value.trim();
        if (!topic) {
            displayError("Please enter a topic to analyze.");
            return;
        }

        showLoader();

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic: topic }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            displayResults(data.summary);

        } catch (error) {
            console.error('Error fetching news summary:', error);
            displayError('Failed to fetch the news summary. Make sure the backend server is running and accessible.');
        }
    };

    searchButton.addEventListener('click', handleSearch);

    // Allow pressing Enter to search
    topicInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    });
});
