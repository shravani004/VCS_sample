def search_feedback(students, query):
    """
    Searches for feedback matching the given query across all students and subjects.

    Parameters:
    - students (dict): Dictionary containing student feedback data.
    - query (str): Search query to look for in feedback strings.

    Returns:
    - list: List of dictionaries containing student name, subject, and matching feedback.
    """
    results = []
    for student, subjects in students.items():
        for subject, feedbacks in subjects.items():
            for feedback in feedbacks:
                if query.lower() in feedback.lower():
                    results.append({
                        "student": student,
                        "subject": subject,
                        "feedback": feedback
                    })
    return results

def main():
    # Example usage with sample data
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

    query = input("Enter search query:")
    results = search_feedback(students, query)
    
    if results:
        print(f"Search results for '{query}':")
        for result in results:
            print(f"Student: {result['student']}, Subject: {result['subject']}, Feedback: {result['feedback']}")
    else:
        print(f"No feedback found matching '{query}'.")

if __name__ == "__main__":
    main()
