def search_feedback_by_name_and_count(feedback_file="feedback_data.txt"):
    matching_feedback = []
    total_entries = 0
    try:
        with open(feedback_file, "r") as f:
            for line in f:
                total_entries += 1
                name, _, comment = line.strip().split(",", 2)
                if search_term.lower() in name.lower():
                    matching_feedback.append(line.strip())
    except FileNotFoundError:
        return [], 0
    return matching_feedback, total_entries

def main():
    global search_term
    search_term = input("Enter name to search (leave blank for all): ")
    if search_term.strip() == "":
        search_term = ""  # Ensure empty string for all feedback
    results, total = search_feedback_by_name_and_count()
    print(f"\nTotal Feedback Entries: {total}")
    if search_term:
        print(f"Feedback matching '{search_term}':")
        if results:
            for entry in results:
                print(f"- {entry}")
        else:
            print("No feedback found for that name.")
    else:
        print("All Feedback:")
        for entry in results:
            print(f"- {entry}")

if __name__ == "__main__":
    main()
