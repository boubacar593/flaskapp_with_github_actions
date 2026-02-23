from flask import Flask, render_template

app = Flask(__name__)

# Données simulées RH
stats = {
    "employees": 42,
    "departments": 5,
    "open_positions": 3,
    "turnover": 8
}

employees = [
    {"name": "Awa Ndiaye", "department": "IT", "role": "Data Analyst", "status": "Active"},
    {"name": "Moussa Diop", "department": "RH", "role": "HR Manager", "status": "Active"},
    {"name": "Fatou Fall", "department": "Finance", "role": "Accountant", "status": "On leave"},
    {"name": "Ibrahima Sow", "department": "IT", "role": "Backend Developer", "status": "Active"},
    {"name": "Aminata Ba", "department": "Marketing", "role": "Content Manager", "status": "Active"},
]

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        stats=stats,
        employees=employees
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)