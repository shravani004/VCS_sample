import score_calculator

# Function to add feedback to students data
def add_feedback(students, student_name, subject, feedback):
    if student_name not in students:
        students[student_name] = {}
    
    if subject not in students[student_name]:
        students[student_name][subject] = []
    
    students[student_name][subject].append(feedback)
    print(f"Feedback added for '{student_name}' in '{subject}'.")

# Function to view feedback based on student name and subject
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

# Default main function without user input
def main():
    # Sample default data for students
    students = {
        "Alice": {
            "Math": ["good", "very good"],
            "Science": ["excellent", "good"]
        },
        "Bob": {
            "Math": ["poor", "very poor"],
            "History": ["good", "excellent"]
        }
    }

    print("\nStudent Feedback Manager")
    print("1. Add Feedback")
    print("2. View All Feedback")
    print("3. Calculate Average Scores")
    print("4. Exit")

    # We can simulate a choice by directly assigning a value to `choice`
    choice = "2"  # For example, let's simulate the option to "View All Feedback"

    if choice == "1":
        # Default data for adding feedback
        student_name = "Charlie"
        subject = "Math"
        feedback_choice = "4"  # "Very Good"
        
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
                return
        
        add_feedback(students, student_name, subject, feedback)
    elif choice == "2":
        if not students:
            print("No feedback available.")
        else:
            # Simulating parameters for viewing feedback
            student_name = "Alice"  # Specific student
            subject = "Math"        # Specific subject
            view_feedback(students, student_name, subject)
    elif choice == "3":
        if not students:
            print("No feedback available.")
        else:
            score_calculator.calculate_average_score(students)
            score_calculator.calculate_average_score_for_all_subjects(students)
    elif choice == "4":
        print("Exiting program.")
        return
    else:
        print("Invalid choice. Please choose again.")

# Function to get an empty student dictionary
def get_empty_students_dict():
    return {}

if __name__ == "__main__":
    main()
