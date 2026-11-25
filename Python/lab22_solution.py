import os

def setup_file(filename):
    if not os.path.exists(filename):
        content = (
            "Annual Technology and AI Progress Report.\n"
            "The adoption of Artificial Intelligence accelerated across business units.\n"
            "AI algorithms improved diagnostic accuracy in healthcare operations.\n"
            "Data engineering pipelines were upgraded to support real-time data streaming.\n"
            "The company plans further investments in AI research and machine learning.\n"
        )
        with open(filename, "w") as f:
            f.write(content)

def search_keyword(filename, keyword):
    total_occurrences = 0
    print(f"--- Search Results for '{keyword}' ---")
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            clean_line = line.strip()
            count = clean_line.lower().count(keyword.lower())
            if count > 0:
                total_occurrences += count
                match_word = "match" if count == 1 else "matches"
                print(f"Line {line_num} ({count} {match_word}): {clean_line}")
    print(f"\n[FOUND] Total occurrences of '{keyword}': {total_occurrences}")

def display_document(filename):
    print(f"--- Full Report Document ({filename}) ---")
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            print(f"{line_num} | {line.strip()}")

def main():
    filename = "report.txt"
    setup_file(filename)
    
    print("================================")
    print("     KEYWORD SEARCH UTILITY     ")
    print("================================")
    
    while True:
        print("\nSelect an operation:")
        print("1. Search Keyword in Document")
        print("2. View Full Document")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == "1":
            keyword = input("Enter keyword to search: ")
            search_keyword(filename, keyword)
        elif choice == "2":
            display_document(filename)
        elif choice == "3":
            print("Thank you for using Keyword Search Utility. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()