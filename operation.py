from module import Student, Sportsstudent
import datetime
def get_student():
    while True:
        try:
            print("1. Regular Student")
            print("2. Sports Student")
            student_choice = input("Enter student type: ")

            name = input("Enter student name: ")
            if not name.isalpha():
                raise ValueError("Invalid name")

            roll = input("Enter roll number: ")

            branch = input("Enter branch: ")
            if not branch.isalpha():
                raise ValueError("Invalid branch")
            
            sem = input("Enter sem: ")
            if not sem.isdigit(): 
                raise ValueError("Semester must be numeric")
            sem = int(sem)

            m1 = input("Enter marks of subject 1: ")
            if not m1.isdigit():
                raise ValueError("Marks must be numeric")
            m1 = int(m1)
            if not (0 <= m1 <= 100):
                raise ValueError("Marks must be between 0 and 100")

            m2 = input("Enter marks of subject 2: ")
            if not m2.isdigit():
                raise ValueError("Marks must be numeric")
            m2 = int(m2)
            if not (0 <= m2 <= 100):
                raise ValueError("Marks must be between 0 and 100")


            if student_choice == "1":
                return Student(name, roll, branch, sem, m1, m2)

            elif student_choice == "2":
                sports = int(input("Enter sports marks: "))
                return Sportsstudent(name, roll, branch, sem, m1, m2, sports)

            else:
                print("Invalid type")

        except ValueError as e:
            print("inavlid input:", e)

 
def write_students(n):
    with open("student.txt", "w") as file:
        x = datetime.datetime.now()

        file.write("---Student Report Card---".center(120) + "\n")
        file.write("Time: " + x.strftime("%c") + "\n")
        file.write("Name\tRoll\tBranch\tSem\tTotal\tAverage\tGrade\tSports\n")

        for i in range(n):
            s = get_student()
            file.write(s.display() + "\n")


def read_students():
    try:
        with open("student.txt", "r") as file:
            print("\n----- Student Records -----")
            print(file.read())
    except FileNotFoundError:
        print("No records found.")
        
        
def delete_students():
    roll = input("Enter roll number to delete: ")

    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()

        found = False

        with open("student.txt", "w") as file, open("deleted.txt", "a") as dfile:
            for line in lines:
                data = line.strip().split("\t")

                
                if len(data) > 1 and data[1] == roll:
                    dfile.write(line)   
                    found = True
                else:
                    file.write(line)    

        if found:
            print("Record deleted and stored in deleted.txt")
        else:
            print("Roll number not found.")

    except FileNotFoundError:
        print("student.txt file not found.")
    
    
def remove_failed_students():
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()

        with open("student.txt", "w") as file, open("failed.txt", "a") as ffile:
            for line in lines:
                data = line.strip().split("\t")

               
                if len(data) < 7 or data[0] == "Name":
                    file.write(line)
                    continue

                grade = data[6]   

                if grade == "F":
                    ffile.write(line)   
                else:
                    file.write(line)    

        print("Failed students removed and stored in failed.txt")

    except FileNotFoundError:
        print("student.txt file not found.")