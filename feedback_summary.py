def summarize_feedback(students):
    feedback_types = ["very poor", "poor", "good", "very good", "excellent"]

    for student, subjects in students.items():
        print(f"\nSummary for {student}:")
        total_feedback_count = 0
        feedback_count = {ftype: 0 for ftype in feedback_types}

        for subject, feedbacks in subjects.items():
            total_feedback_count += len(feedbacks)
            for feedback in feedbacks:
                if feedback in feedback_count:
                    feedback_count[feedback] += 1

        print(f"Subjects with feedback: {len(subjects)}")
        print(f"Total feedback entries: {total_feedback_count}")
        print("Feedback distribution:")
        for ftype in feedback_types:
            print(f"  {ftype.title()}: {feedback_count[ftype]}")

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

    summarize_feedback(students)

if __name__ == "__main__":
    main()
