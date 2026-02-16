# ===============================
# EduAI - Adaptive Study Scheduler
# ===============================

def classify(score):
    if score <= 40:
        return "Weak"
    elif score <= 70:
        return "Moderate"
    else:
        return "Strong"


def allocate_time(category):
    if category == "Weak":
        return 90
    elif category == "Moderate":
        return 60
    else:
        return 30


def analyze_student(name, subjects):
    print(f"\n===== {name} Report =====")
    schedule = {}

    for subject, scores in subjects.items():
        accuracy = (sum(scores) / len(scores)) * 100
        category = classify(accuracy)
        time_needed = allocate_time(category)

        schedule[subject] = time_needed

        print(f"\nSubject: {subject}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Category: {category}")
        print("Why scheduled today?")
        print(f"- Last score was {accuracy:.2f}%")

        if category == "Weak":
            print("- High forgetting risk")
        elif category == "Moderate":
            print("- Needs reinforcement")
        else:
            print("- Maintenance revision")

    return schedule


# -------------------------------
# Simulated Data
# -------------------------------

student_A = {
    "Math": [1,1,1,1,0],
    "Physics": [1,0,1,0,1],
    "Chemistry": [1,1,1,0,1]
}

student_B = {
    "Math": [0,0,1,0,0],
    "Physics": [1,1,1,1,0],
    "Chemistry": [0,1,0,1,0]
}


schedule_A = analyze_student("Student A", student_A)
schedule_B = analyze_student("Student B", student_B)

print("\n===== Study Time Comparison =====")
for subject in schedule_A:
    print(f"{subject}: Student A = {schedule_A[subject]} min | Student B = {schedule_B[subject]} min")
