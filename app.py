from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    subject = request.form["subject"]
    hours = int(request.form["hours"])
    level = request.form["level"]

    # Topic logic
    if subject.lower() == "mathematics":
        topics = ["Algebra", "Calculus", "Geometry"]
    elif subject.lower() == "python":
        topics = ["Basics", "Functions", "Loops"]
    else:
        topics = ["Concept 1", "Concept 2", "Concept 3"]

    # Smart distribution
    if level == "Easy":
        split = [0.4, 0.35, 0.25]
    elif level == "Medium":
        split = [0.35, 0.35, 0.30]
    else:
        split = [0.3, 0.4, 0.3]

    plan = []
    for i in range(3):
        plan.append((topics[i], round(hours * split[i], 1)))

    recommendation = f"Based on your {level} difficulty and {hours} hours input, EduAI recommends this optimized study plan."

    return render_template("quiz.html",
                           plan=plan,
                           subject=subject,
                           level=level,
                           recommendation=recommendation)

@app.route("/result", methods=["POST"])
def result():
    score = 0
    feedback = []

    if request.form["q1"] == "4":
        score += 1
    else:
        feedback.append("Revise basic arithmetic.")

    if request.form["q2"].lower() == "3x^2":
        score += 1
    else:
        feedback.append("Revise derivatives.")

    if request.form["q3"] == "1":
        score += 1
    else:
        feedback.append("Revise trigonometry.")

    if score == 3:
        message = "Excellent Performance!"
    elif score == 2:
        message = "Good Performance, Minor improvements needed."
    else:
        message = "You need more focused practice."

    return render_template("result.html",
                           score=score,
                           message=message,
                           feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)



