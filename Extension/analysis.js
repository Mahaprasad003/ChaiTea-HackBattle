// analysis.js
window.onload = function() {
    // Get the URL from the query string
    const urlParams = new URLSearchParams(window.location.search);
    const pageUrl = urlParams.get('url');

    // Log to console for debugging
    console.log("Retrieved URL:", pageUrl);

    // Display the URL or a message if none is found
    const resultDiv = document.getElementById('result');
    if (pageUrl) {
        resultDiv.innerText = `Analyzing URL: ${decodeURIComponent(pageUrl)}`;
    } else {
        resultDiv.innerText = 'No URL provided for analysis.';
    }

    // Additional debugging: Check if the resultDiv is accessible
    if (resultDiv) {
        console.log("Result div is accessible");
    } else {
        console.log("Result div is not accessible");
    }
};
