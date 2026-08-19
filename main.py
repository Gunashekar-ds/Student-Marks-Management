from operation import *

while True:
    print("\n------ STUDENT MENU ------")
    print("1. Add Students")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Remove Failed Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = input("Enter number of students: ")
        if n.isdigit():
            write_students(int(n))
        else:
            print("Invalid number")

    elif choice == "2":
        read_students()

    elif choice == "3":
        delete_students()

    elif choice == "4":
        remove_failed_students()

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid choice")