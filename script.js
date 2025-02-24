function calculateScore() {
    let score = 0;
    let answers = document.querySelectorAll("input[type='radio']:checked");

    answers.forEach((answer) => {
        score += parseInt(answer.value);
    });

    document.getElementById("result").innerText = score + " / 60";

    // Send data to Flask backend
    fetch('/submit', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "score": score })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.log("Error:", error));
}