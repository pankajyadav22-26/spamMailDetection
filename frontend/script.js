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