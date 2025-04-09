def calculate_average_score(students):
    feedback_scores = {
        "very poor": 1,
        "poor": 2,
        "good": 3,
        "very good": 4,
        "excellent": 5
    }

    for student, subjects in students.items():
        print(f"Average scores for {student}:")
        for subject, feedbacks in subjects.items():
            valid_feedbacks = [feedback for feedback in feedbacks if feedback in feedback_scores]
            if valid_feedbacks:
                total_score = sum(feedback_scores[feedback] for feedback in valid_feedbacks)
                average_score = total_score / len(valid_feedbacks)
                print(f"{subject}: {average_score:.2f}")
            else:
                print(f"No valid feedback for '{subject}' found for '{student}'.")
        print()  # Empty line for better readability

def calculate_average_score_for_all_subjects(students):
    feedback_scores = {
        "very poor": 1,
        "poor": 2,
        "good": 3,
        "very good": 4,
        "excellent": 5
    }

    for student, subjects in students.items():
        all_feedbacks = [feedback for subject_feedbacks in subjects.values() for feedback in subject_feedbacks]
        valid_feedbacks = [feedback for feedback in all_feedbacks if feedback in feedback_scores]
        if valid_feedbacks:
            total_score = sum(feedback_scores[feedback] for feedback in valid_feedbacks)
            average_score = total_score / len(valid_feedbacks)
            print(f"Overall average score for {student}: {average_score:.2f}")
        else:
            print(f"No valid feedback found for '{student}'.")

def main():
    students = {
        "Alice": {
            "Math": ["good", "very good", "excellent"],
            "Science": ["poor", "good"]
        },
        "Bob": {
            "Math": ["very poor", "poor"],
            "Science": ["good", "very good"]
        }
    }

    calculate_average_score(students)
    calculate_average_score_for_all_subjects(students)

if __name__ == "__main__":
    main()
