from urls import commands, paths
from helpers import create_tables

def main_menu():
    create_tables()
    active_user = None
    active = True
    while active:
        print("\nPlease select an option:")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            paths[1]()
        elif choice == '2':
            active_user = paths[2]()
        elif choice == '3':
            print("Exiting the program.")
            active = False
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
