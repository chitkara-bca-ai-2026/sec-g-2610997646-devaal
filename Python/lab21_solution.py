import os

def setup_sample_file(filename):
    if not os.path.exists(filename):
        sample_text = (
            "Artificial Intelligence is transforming modern industries.\n"
            "Python provides powerful libraries for text processing and data analysis.\n"
            "Developers use file handling to store and retrieve persistent records.\n"
            "Modular programming ensures code is clean, reusable, and easy to maintain.\n"
        )
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sample_text)

def get_document_statistics(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    
    return (line_count, word_count, char_count)

def display_document(filename):
    print(f"\n--- Document Preview ({filename}) ---")
    with open(filename, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index} | {line.rstrip()}")

def main():
    filename = "document.txt"
    setup_sample_file(filename)
    
    print("========================================")
    print("      DOCUMENT STATISTICS ANALYZER      ")
    print("========================================")
    
    while True:
        print("\nSelect an operation:")
        print("1. Calculate Document Statistics")
        print("2. Display Document Content")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            if os.path.exists(filename):
                lines, words, chars = get_document_statistics(filename)
                print("\n----------------------------------------")
                print("            DOCUMENT REPORT             ")
                print("----------------------------------------")
                print(f"Target File      : {filename}")
                print(f"Total Lines      : {lines}")
                print(f"Total Words      : {words}")
                print(f"Total Characters : {chars}")
                print("----------------------------------------")
            else:
                print(f"\nError: '{filename}' not found.")
                
        elif choice == "2":
            if os.path.exists(filename):
                display_document(filename)
            else:
                print(f"\nError: '{filename}' not found.")
                
        elif choice == "3":
            print("Thank you for using Document Statistics Analyzer. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()