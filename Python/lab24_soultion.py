import csv
import os

def setup_file(filename):
    if not os.path.exists(filename):
        data = [
            ["RollNo", "Name", "Subject", "Marks"],
            [101, "Aman", "Python", 85],
            [102, "Riya", "Python", 92],
            [103, "Karan", "Python", 45],
            [104, "Neha", "Python", 78],
            [105, "Rohit", "Python", 38],
            [106, "Pooja", "Python", 62]
        ]
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

def read_all_students(filename):
    print("\n---------------------------------------------")
    print("            ALL ENROLLED STUDENTS            ")
    print("---------------------------------------------")
    print(f"{'Roll No':<10} {'Name':<12} {'Subject':<12} {'Marks'}")
    print("---------------------------------------------")
    count = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['RollNo']:<10} {row['Name']:<12} {row['Subject']:<12} {row['Marks']}")
            count += 1
    print("---------------------------------------------")
    print(f"Total Records: {count}")

def filter_students_above_threshold(filename, threshold=50):
    print("\n---------------------------------------------")
    print(f"         STUDENTS WITH MARKS > {threshold}            ")
    print("---------------------------------------------")
    print(f"{'Roll No':<10} {'Name':<12} {'Subject':<12} {'Marks'}")
    print("---------------------------------------------")
    qualified_count = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Marks"]) > threshold:
                print(f"{row['RollNo']:<10} {row['Name']:<12} {row['Subject']:<12} {row['Marks']}")
                qualified_count += 1
    print("---------------------------------------------")
    print(f"Qualified Students Count: {qualified_count}")

def main():
    filename = "students_data.csv"
    setup_file(filename)

    print("=============================================")
    print("       STUDENT RESULT ANALYSIS SYSTEM        ")
    print("=============================================")

    while True:
        print("\nSelect an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ")

        if choice == "1":
            read_all_students(filename)
        elif choice == "2":
            filter_students_above_threshold(filename)
        elif choice == "3":
            print("Thank you for using Student Result Analysis System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()