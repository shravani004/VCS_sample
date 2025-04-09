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

def main():
    students = {}

    while True:
        try:
            print("\nStudent Feedback Manager")
            print("1. Add Feedback")
            print("2. View All Feedback")
            print("3. Calculate Average Scores")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                student_name = input("Enter student name: ")
                subject = input("Enter subject: ")
                print("Choose feedback level:")
                print("1. Very Poor")
                print("2. Poor")
                print("3. Good")
                print("4. Very Good")
                print("5. Excellent")
                feedback_choice = input("Enter choice (1-5): ")
                
                match feedback_choice:
                    case "1":
                        feedback = "very poor"
                    case "2":
                        feedback = "poor"
                    case "3":
                        feedback = "good"
                    case "4":
                        feedback = "very good"
                    case "5":
                        feedback = "excellent"
                    case _:
                        print("Invalid choice. Please choose again.")
                        continue
                
                add_feedback(students, student_name, subject, feedback)
            elif choice == "2":
                if not students:
                    print("No feedback available.")
                else:
                    student_name = input("Enter student name (leave blank for all): ")
                    subject = input("Enter subject (leave blank for all): ")
                    if student_name.strip() == "":
                        student_name = None
                    if subject.strip() == "":
                        subject = None
                    view_feedback(students, student_name, subject)
            elif choice == "3":
                if not students:
                    print("No feedback available.")
                else:
                    score_calculator.calculate_average_score(students)
                    score_calculator.calculate_average_score_for_all_subjects(students)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please choose again.")
        except EOFError:
            # Handle EOFError gracefully
            print("\nEOFError detected: No input provided. Exiting program.")
            break

if __name__ == "__main__":
    main()

def get_empty_students_dict():
    return {}
