# Student Score Tracker with predefined subjects

students = {}
subjects = []

def setup_subjects():
    global subjects
    print("Enter the list of subjects to track (type 'done' to finish):")
    while True:
        subject = input("Subject name: ").strip()
        if subject.lower() == "done":
            break
        elif subject == "":
            print("Subject name cannot be empty.")
        elif subject in subjects:
            print("Subject already added.")
        else:
            subjects.append(subject)
    if not subjects:
        print("No subjects entered. Exiting.")
        exit()

def add_student():
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists. Updating their scores.")
    else:
        students[name] = {}
    
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter {name}'s score for {subject} (0-100): "))
                if 0 <= score <= 100:
                    students[name][subject] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

def calculate_averages():
    if not students:
        print("No students to calculate averages.")
        return
    print("\nAverage Scores:")
    for name, subject_scores in students.items():
        if subject_scores:
            avg = sum(subject_scores.values()) / len(subjects)
            print(f"- {name}: {avg:.2f}")
        else:
            print(f"- {name}: No subjects recorded.")

def find_top_students():
    if not students:
        print("No students available.")
        return
    
    averages = {}
    for name, scores in students.items():
        if scores:
            averages[name] = sum(scores.values()) / len(subjects)
    
    if not averages:
        print("No subject scores to calculate top student.")
        return

    max_avg = max(averages.values())
    top_students = [name for name, avg in averages.items() if avg == max_avg]

    print(f"\nTop student(s) with average {max_avg:.2f}:")
    for name in top_students:
        print(f"- {name}")

def list_failing_students():
    if not students:
        print("No students available.")
        return
    
    print("\nFailing Students (average < 50):")
    found = False
    for name, scores in students.items():
        if scores:
            avg = sum(scores.values()) / len(subjects)
            if avg < 50:
                print(f"- {name}: {avg:.2f}")
                found = True
    if not found:
        print("No failing students.")

def show_menu():
    print("\n--- Student Score Tracker ---")
    print("1. Add Student Scores")
    print("2. Calculate Average Scores")
    print("3. Find Top Student(s)")
    print("4. List Failing Students")
    print("5. Exit")

def main():
    setup_subjects()  # Prompt for subjects first
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            calculate_averages()
        elif choice == '3':
            find_top_students()
        elif choice == '4':
            list_failing_students()
        elif choice == '5':
            print("Exiting Student Score Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()