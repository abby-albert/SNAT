import os

flashcards = {}

def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards[question] = answer
    print("Flashcard added!")

def view_flashcards():
    if not flashcards:
        print("No flashcards available.")
    else:
        for question, answer in flashcards.items():
            print(f"Question: {question}")
            print(f"Answer: {answer}")
            print("--------")

def delete_flashcard():
    if not flashcards:
        print("No flashcards available to delete.")
    else:
        question = input("Enter the question to delete: ")
        if question in flashcards:
            del flashcards[question]
            print("Flashcard deleted!")
        else:
            print("Flashcard not found.")

def main():
    while True:
        print("\nFlashcard System")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Delete Flashcard")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_flashcard()
        elif choice == '2':
            view_flashcards()
        elif choice == '3':
            delete_flashcard()
        elif choice == '4':
            print("Exiting the flashcard system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
flashcards = {}

def add_flashcard():
    term = input("Enter the term: ")
    definition = input("Enter the definition: ")
    flashcards[term] = definition
    print("Flashcard added!")

def view_flashcards():
    if not flashcards:
        print("No flashcards available.")
    else:
        print("Available Flashcards:")
        for term, definition in flashcards.items():
            print(f"Term: {term}")
            print(f"Definition: {definition}")
            print("--------")

def delete_flashcard():
    if not flashcards:
        print("No flashcards available to delete.")
    else:
        term = input("Enter the term to delete: ")
        if term in flashcards:
            del flashcards[term]
            print("Flashcard deleted!")
        else:
            print("Flashcard not found.")

def main():
    while True:
        print("\nComputer Science Flashcards")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Delete Flashcard")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_flashcard()
        elif choice == '2':
            view_flashcards()
        elif choice == '3':
            delete_flashcard()
        elif choice == '4':
            print("Exiting the flashcard system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
