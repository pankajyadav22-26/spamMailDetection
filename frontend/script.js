async function checkSpam() {
    const message = document.getElementById('message').value;

    if (!message) {
        alert("Please enter a message!");
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    document.getElementById('result').textContent = data.result;
}

// Dark mode toggle functionality
const toggleDarkModeButton = document.getElementById("toggleDarkMode");

toggleDarkModeButton.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
});

// Simple spam check function (You can extend this with more complex logic)
function checkSpam() {
    const message = document.getElementById("message").value;
    const resultDiv = document.getElementById("result");

    // Simple spam detection: looking for common spam phrases
    const spamKeywords = ["buy now", "free", "limited time offer", "act fast", "urgent"];
    const foundSpam = spamKeywords.some(keyword => message.toLowerCase().includes(keyword));

    if (foundSpam) {
        resultDiv.textContent = "This message may be spam.";
        resultDiv.style.color = "red";
    } else {
        resultDiv.textContent = "This message seems clean.";
        resultDiv.style.color = "green";
    }
}