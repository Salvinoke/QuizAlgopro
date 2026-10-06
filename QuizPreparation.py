import random as rand
import datetime

registered = False

name = ""
gender = ""
birthyear = 0
email = ""
studentAge = 0
studentID = ""

while True:
    menuInput = input("""=== Student Registration ====
1. Input New Data
2. View Student Data
3. Update Student
4. Delete Student
5. Exit Program
-> """)

    if menuInput == "1":
        while True:
            name = input("Input Name: ")
            nospace_Name = name.replace(" ","")

            if len(nospace_Name) <= 5:
                print("Name must contains more than 5 characters!")
                continue
            elif not nospace_Name.isalpha():
                print("Name must only contains alphabetical characters!")
                continue
            elif nospace_Name != name.title().replace(" ",""):
                print("Name needs to be in Title format!")
                continue
            break

        while True:
            gender = input("Input Gender: ").upper()

            if gender not in ("M","F"):
                print("Gender must be either M or F!")
                continue
            elif gender == "M":
                gender = "Male"
            elif gender == "F":
                gender = "Female"
            break

        while True:
            try:
                birthyear = int(input("Input Birthyear: "))
            except ValueError:
                print("Birth year must be numeric!")
                continue
            if birthyear < 1900 or birthyear > 2008:
                print("Birth year is between 1900 and 2008 inclusive!")
                continue
            break

        while True:
            email = input("Input email: ")

            if email != email.lower():
                print("email must be in lowercase!")
                continue
            elif email.count("@") != 1:
                print("Email must contain exactly one @ symbol!")
                continue
            elif not email.endswith("binus.ac.id"):
                print("Email must ends with binus.ac.id!")
                continue
            break

        studentAge = datetime.datetime.now().year - birthyear
        studentID = "BN" + str(rand.randint(100,999))

        input("New student registered!\n")
        registered = True
        continue

    elif menuInput == "2":
        if registered:
            print(f"""Current Student Data

ID: {studentID}
Name: {name}
Gender: {gender}
Age: {studentAge}
Email: {email}

Student number: {studentID.replace("BN","")}
Last digit of ID: {studentID[-1]}
Done-viewing!
""")
            input("Press Enter to continue...")
            continue
        elif not registered:
            print("""Current Student Data
            
No data""")
            continue
    elif menuInput == "3": 
        if registered:
            while True:
                print(f"""Current Student Data
                    
ID: {studentID}
Name: {name}
Gender: {gender}
Age: {studentAge}
Email: {email}

Student number: {studentID.replace("BN","")}
Last digit of ID: {studentID[-1]}
Done-viewing!
""")

                updateInput = input("Update: 1. Name    2. Gender   3. Birth Year   4. Email (0 to exit): ")
                if updateInput == "1":
                    while True:
                        name = input("Input new name: ")
                        nospace_Name = name.replace(" ","")
            
                        if len(nospace_Name) <= 5:
                            print("Name must contains more than 5 characters!")
                            continue
                        elif not nospace_Name.isalpha():
                            print("Name must only contains alphabetical characters!")
                            continue
                        elif nospace_Name != name.title().replace(" ",""):
                            print("Name needs to be in Title format!")
                            continue
                        break

                elif updateInput == "2":
                     while True:
                        gender = input("Input new Gender: ").upper()
            
                        if gender not in ("M","F"):
                            print("Gender must be either M or F!")
                            continue
                        elif gender == "M":
                            gender = "Male"
                        elif gender == "F":
                            gender = "Female"
                        break
                elif updateInput == "3":
                    while True:
                        try:
                            birthyear = int(input("Input new Birthyear: "))
                        except ValueError:
                            print("Birth year must be numeric!")
                            continue
                        if birthyear < 1900 or birthyear > 2008:
                            print("Birth year is between 1900 and 2008 inclusive!")
                            continue
                        break
                    studentAge = datetime.datetime.now().year - birthyear
                elif updateInput == "4":
                    while True:
                        email = input("Input new email: ")
            
                        if email != email.lower():
                            print("email must be in lowercase!")
                            continue
                        elif email.count("@") != 1:
                            print("Email must contain exactly one @ symbol!")
                            continue
                        elif not email.endswith("binus.ac.id"):
                            print("Email must ends with binus.ac.id!")
                            continue
                        break
                elif updateInput == "0":
                    break
                else:
                    print("Choice must be 1 to 4")
                    input("Press ENTER to continue...")
                    continue

                input("Student Updated! ")
                continue
        else:
            print("No data")
            input("Press ENTER to continue...")
            continue

    elif menuInput == "4":
        if registered:
            print(f"""Current Student Data
                                
ID: {studentID}
Name: {name}
Gender: {gender}
Age: {studentAge}
Email: {email}

Student number: {studentID.replace("BN","")}
Last digit of ID: {studentID[-1]}
Done-viewing!
""")
            confirmation = input("Are you sure? [y/n]: ").lower()
            if confirmation == "y":
                name = ""
                gender = ""
                birthyear = 0
                email = ""
                studentAge = 0
                studentID = ""
                registered = False
                
                print("Student Deleted!")
                input("Press ENTER to continue...")
            else:
                print("Delete cancelled!")
                input("Press ENTER to continue...")
            
        else:
            print("No data")
            input("Press ENTER to continue...")
            continue
    
    elif menuInput == "5":
        print("Thank you for using this program!")
        break
    else:
        print("Choice must be 1 to 5!")
        continue