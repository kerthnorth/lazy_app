import os


user_input = input("Enter something: ").strip().lower()


if "terminal" in user_input:
    os.system("python3 terminal.py")  # Run the terminal script
else:
    print("No action taken.")
