async function predictPerformance() {

    const data = {
        study_hours: parseFloat(document.getElementById("study_hours").value),
        attendance_percentage: parseInt(document.getElementById("attendance").value),
        previous_score: parseFloat(document.getElementById("previous_score").value),
        assignments_completed: parseInt(document.getElementById("assignments").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
    
        document.getElementById("resultBox").style.display = "block";
        document.getElementById("score").innerText = result.predicted_score;

        const categorySpan = document.getElementById("category");
        categorySpan.innerText = result.performance_category;

        categorySpan.className = "";
        if (result.performance_category === "Excellent") {
            categorySpan.classList.add("excellent");
        } else if (result.performance_category === "Average") {
            categorySpan.classList.add("average");
        } else {
            categorySpan.classList.add("needs");
        }

    } catch (error) {
        alert("Error connecting to prediction API");
    }
}