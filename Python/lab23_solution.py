import os

def setup_file(filename):
    if not os.path.exists(filename):
        content = (
            "Aman,85\n"
            "Riya,92\n"
            "Karan,78\n"
        )
        with open(filename, "w") as f:
            f.write(content)

def store_student(filename, name, marks):
    with open(filename, "a") as f:
        f.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")

def display_and_calculate_average(filename):
    if not os.path.exists(filename):
        print("No student records found.")
        return

    marks_list = []
    print("\n---------------------------------------")
    print("          STUDENT MARKS LEDGER         ")
    print("---------------------------------------")
    print(f"{'No.':<5} {'Student Name':<20} {'Marks Obtained'}")
    print("---------------------------------------")

    with open(filename, "r") as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                parts = line.split(",")
                name = parts[0]
                marks = int(parts[1])
                marks_list.append(marks)
                print(f"{idx:<5} {name:<20} {marks}")

    print("---------------------------------------")
    if marks_list:
        total_students = len(marks_list)
        total_marks = sum(marks_list)
        average = total_marks / total_students
        print(f"Total Students : {total_students}")
        print(f"Total Marks    : {total_marks}")
        print(f"Class Average  : {average:.2f}")
    else:
        print("No records to calculate average.")

def main():
    filename = "student_marks.txt"
    setup_file(filename)

    print("=======================================")
    print("     STUDENT MARKS FILE HANDLING TOOL  ")
    print("=======================================")

    while True:
        print("\nSelect an operation:")
        print("1. Add & Store Student Marks")
        print("2. Display Records & Class Average")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ")

        if choice == "1":
            name = input("Enter Student Name: ").strip()
            try:
                marks = int(input("Enter Marks (0-100): "))
                if 0 <= marks <= 100:
                    store_student(filename, name, marks)
                else:
                    print("Invalid marks! Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numeric marks.")
        elif choice == "2":
            display_and_calculate_average(filename)
        elif choice == "3":
            print("Thank you for using Student Marks Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()