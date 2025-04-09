# feedback_entry.py

import score_calculator

def add_feedback(students, student_name, subject, feedback):
    if student_name not in students:
        students[student_name] = {}
    
    if subject not in students[student_name]:
        students[student_name][subject] = []
    
    students[student_name][subject].append(feedback)
    print(f"Feedback added for '{student_name}' in '{subject}'.")

def view_feedback(students, student_name=None, subject=None):
    if student_name:
        if student_name in students:
            if subject:
                if subject in students[student_name]:
                    print(f"Feedback for {student_name} in {subject}:")
                    for i, feedback in enumerate(students[student_name][subject], start=1):
                        print(f"{i}. {feedback}")
                else:
                    print(f"No feedback for '{subject}' found for '{student_name}'.")
            else:
                print(f"Feedback for {student_name}:")
                for subj, feedbacks in students[student_name].items():
                    print(f"{subj}:")
                    for i, feedback in enumerate(feedbacks, start=1):
                        print(f"{i}. {feedback}")
                    print()  # Empty line for better readability
        else:
            print(f"Student '{student_name}' does not exist.")
    else:
        for name, subjects in students.items():
            print(f"Feedback for {name}:")
            for subj, feedbacks in subjects.items():
                print(f"{subj}:")
                for i, feedback in enumerate(feedbacks, start=1):
                    print(f"{i}. {feedback}")
                print()  # Empty line for better readability

def calculate_average_score(students):
    # Example calculation; implement actual logic here
    for student, subjects in students.items():
        print(f"Average score for {student}:")
        for subject, feedbacks in subjects.items():
            print(f"{subject}:")
            # Implement score calculation based on feedback levels
            # For simplicity, assume scores are based on feedback levels
            scores = {
                "very poor": 1,
                "poor": 2,
                "good": 3,
                "very good": 4,
                "excellent": 5
            }
            total_score = sum(scores[feedback] for feedback in feedbacks)
            average_score = total_score / len(feedbacks) if feedbacks else 0
            print(f"Average score: {average_score:.2f}")
            print()  # Empty line for better readability

def main():
    students = {}

    # Adding default feedback for testing
    default_students = [
        {"name": "Alice", "subject": "Math", "feedback": "excellent"},
        {"name": "Alice", "subject": "Science", "feedback": "very good"},
        {"name": "Bob", "subject": "Math", "feedback": "good"},
        {"name": "Bob", "subject": "Science", "feedback": "poor"},
        {"name": "Charlie", "subject": "Math", "feedback": "very poor"},
        {"name": "Charlie", "subject": "Science", "feedback": "good"},
    ]

    for student in default_students:
        add_feedback(students, student["name"], student["subject"], student["feedback"])

    # Viewing feedback
    print("\nDefault Feedback:")
    view_feedback(students)

    # Calculating average scores
    print("\nCalculating Average Scores:")
    calculate_average_score(students)

if __name__ == "__main__":
    main()
