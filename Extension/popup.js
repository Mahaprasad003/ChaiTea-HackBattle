// popup.js
document.getElementById('analyze-url').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentUrl = tabs[0].url;
        // Open a new page with the current URL as a query parameter
        chrome.tabs.create({ url: `analysis.html?url=${encodeURIComponent(currentUrl)}` });
    });
});
