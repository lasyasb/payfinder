
document.querySelectorAll(".tag").forEach(tag => {
  tag.addEventListener("click", () => {
    document.getElementById("job").value = tag.textContent;
  });
});

document.getElementById("salaryForm").onsubmit = async (e) => {
  e.preventDefault();

  const job = document.getElementById("job").value;
  const location = document.getElementById("location").value;
  const education = document.getElementById("education").value;
  const experience = parseInt(document.getElementById("experience").value);

  const res = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ job, location, education, experience })
  });

  const data = await res.json();
  const predicted = parseFloat(data.predicted_salary);
  const min = (predicted * 0.85).toFixed(2);
  const max = (predicted * 1.15).toFixed(2);

  // Hide form and show result
  document.getElementById("salaryForm").style.display = "none";
  document.getElementById("resultSection").style.display = "block";

  // Set text
  document.getElementById("summaryText").innerText = `Salary Prediction for ${job} in ${location}`;
  document.getElementById("predictedAmount").innerText = `Predicted Annual Salary: $${predicted}`;

  // Chart rendering
  new Chart(document.getElementById("salaryChart"), {
    type: 'bar',
    data: {
      labels: ['Min', 'Your Estimate', 'Max'],
      datasets: [{
        label: 'Annual Salary ($)',
        data: [min, predicted, max],
        backgroundColor: ['#d1d5db', '#3b82f6', '#d1d5db']
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
};

function startNewPrediction() {
  document.getElementById("salaryForm").reset();
  document.getElementById("experience").value = 0;
  document.getElementById("expVal").textContent = 0;
  document.getElementById("salaryForm").style.display = "block";
  document.getElementById("resultSection").style.display = "none";
}
