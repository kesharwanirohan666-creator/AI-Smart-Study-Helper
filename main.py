import sys
from database import init_db, add_note, get_all_notes
from nlp_engine import summarize_text, generate_questions

def display_menu():
    """Displays the main menu of the application."""
    print("\n" + "="*30)
    print("   AI Smart Study Helper")
    print("="*30)
    print("1. Add Study Note")
    print("2. Summarize Text")
    print("3. Generate Questions")
    print("4. View Saved Notes")
    print("5. Exit")
    print("="*30)

def main():
    # Initialize the database
    init_db()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter note title: ")
            print("Enter note content (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = "\n".join(lines)
            
            if title and content:
                add_note(title, content)
                print("\n[SUCCESS] Note saved successfully!")
            else:
                print("\n[ERROR] Title and content cannot be empty.")

        elif choice == '2':
            print("\nEnter the text you want to summarize (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            
            if text:
                summary = summarize_text(text)
                print("\n" + "-"*20)
                print("SUMMARY:")
                print(summary)
                print("-"*20)
            else:
                print("\n[ERROR] Text cannot be empty.")

        elif choice == '3':
            print("\nEnter text to generate study questions (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            
            if text:
                questions = generate_questions(text)
                print("\n" + "-"*20)
                print("STUDY QUESTIONS:")
                for i, q in enumerate(questions, 1):
                    print(f"{i}. {q}")
                print("-"*20)
            else:
                print("\n[ERROR] Text cannot be empty.")

        elif choice == '4':
            notes = get_all_notes()
            if not notes:
                print("\nNo notes found in the database.")
            else:
                print("\n" + "-"*30)
                print("SAVED NOTES:")
                for title, content, date in notes:
                    print(f"\nTitle: {title}")
                    print(f"Date: {date}")
                    print(f"Content: {content[:100]}..." if len(content) > 100 else f"Content: {content}")
                print("-"*30)

        elif choice == '5':
            print("\nExiting AI Smart Study Helper. Happy studying!")
            sys.exit()

        else:
            print("\n[ERROR] Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()
