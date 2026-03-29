import random
import time

LEADERBOARD_FILE = "leaderboard.txt"

def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            return 50, 10
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 200, 5
        else:
            print("Invalid choice!")

def save_score(name, score, time_taken, status):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name},{score},{time_taken:.2f},{status}\n")

def show_leaderboard():
    print("\n🏆 Leaderboard:")

    try:
        with open(LEADERBOARD_FILE, "r") as f:
            lines = f.readlines()

            if not lines:
                print("No records yet.")
                return

            data = []
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    data.append(parts)

            data.sort(key=lambda x: int(x[1]), reverse=True)

            for i, entry in enumerate(data[:5], start=1):
                name, score, time_taken, status = entry
                print(f"{i}. {name} | Score: {score} | {status} | Time: {time_taken}s")

    except FileNotFoundError:
        print("No leaderboard yet.")

def play_game():
    max_range, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_range)

    attempts = 0
    score = 100

    print(f"\n🎯 Guess between 1 and {max_range}")
    print(f"You have {max_attempts} attempts.\n")

    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Invalid input!\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low!\n")
            score -= 10
        elif guess > secret_number:
            print("📈 Too high!\n")
            score -= 10
        else:
            end_time = time.time()
            time_taken = end_time - start_time

            print(f"\n🎉 Correct! Number was {secret_number}")
            print(f"🏆 Attempts: {attempts}")
            print(f"⭐ Score: {score}")
            print(f"⏱️ Time: {time_taken:.2f} seconds")

            name = input("Enter your name: ")
            save_score(name, score, time_taken, "WIN")
            return

    end_time = time.time()
    time_taken = end_time - start_time

    print(f"\n💀 Game Over! Number was {secret_number}")
    print(f"⭐ Score: {score}")

    name = input("Enter your name: ")
    save_score(name, score, time_taken, "LOSE")

def main():
    print("🎮 Ultimate Number Guessing Game")

    while True:
        print("\n1. Play Game")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_leaderboard()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()