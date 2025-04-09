def count_total_feedback_entries(feedback_file="feedback_data.txt"):
    count = 0
    try:
        with open(feedback_file, "r") as f:
            for line in f:
                count += 1
    except FileNotFoundError:
        return 0
    return count

if __name__ == "__main__":
    total_count = count_total_feedback_entries()
    print(f"Total number of feedback entries: {total_count}")
