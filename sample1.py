import random

print("=== Number Guessing Game ===")

best_score = None

while True:

    print("\nChoose Difficulty")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter choice: ")

    if choice == "1":
        max_num = 10
    elif choice == "2":
        max_num = 50
    elif choice == "3":
        max_num = 100
    else:
        print("Invalid choice! Using Easy level.")
        max_num = 10

    number = random.randint(1, max_num)
    attempts = 0

    print("Guess the number between 1 and", max_num)

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct! You guessed it in", attempts, "attempts")
            break

    if best_score == None or attempts < best_score:
        best_score = attempts
        print("New Best Score!")

    print("Best Score:", best_score)

    again = input("Play again? (yes/no): ")

    if again != "yes":
        print("Thanks for playing!")
        break