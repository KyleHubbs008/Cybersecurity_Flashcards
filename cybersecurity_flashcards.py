import json
import random

#Load flashcards from a file
def load_flashcards(filename):
  try:
    with open(filename, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []
  
#Save flashcards to a file
def save_flashcards(filename, flashcards):
  with open(filename, 'w') as file:
    json.dump(flashcards, file, indent = 4)
    
    
#List of flashcards
flashcards = load_flashcards('flashcards.json')

def show_flashcards(flashcards):
  random.shuffle(flashcards)  # Shuffle flashcards to randomize order
  for card in flashcards:
    print("\nQuestion: " + card["question"])
    response = input("Press Enter to show the answer or type exit to quit: ").strip().lower()
    if response == 'exit':
      print("Exiting flashcards...")
      break
    print("Answer: " + card["answer"])
    response = input("Press Enter to move on to the next flashcard or type exit to quit: ").strip().lower()
    if response == 'exit':
      print("Exiting flashcards...")
      break
    

def main():
  print("Welcome to the Cybersecurity Flashcard App!")
  while True: 
    print("\nMenu:")
    print("1. Start Flashcards")
    print("2. Add a Flashcard")
    print("3. Save and Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
      show_flashcards(flashcards)
    elif choice == "2":
      question = input("Enter the question: ")
      answer = input("Enter the answer: ")
      flashcards.append({"question": question, "answer": answer})
      print("Flashcard added!")
    elif choice == "3":
      save_flashcards('flashcards.json', flashcards)
      print("Flashcards saved!  Exiting...")
      break
    else:
      print("Please select a valid option!")
      
if __name__ == "__main__":
  main()
      
      
