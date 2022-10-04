#Python Student and Course Management System:

print("Welcome to course management system\n")
#roll=[10001,10002,10003]
#grades=["A+","A","A-","B+","B","B-","C+","C","C-","D","F","E"]
#mandate course
courses=["Python","Java","C","C++"]
courses_grades={"Python":"","Java":"","C":"","C++":""}


students={10001:{"name":"Kartik", "age":"24", "course":courses,"Grades":courses_grades},
          10002:{"name":"Anish", "age":"24", "course":courses,"Grades":courses_grades},
          10003:{"name":"Krish", "age":"24", "course":courses,"Grades":courses_grades}}
roll=list(students.keys())
print(roll)
print(type(roll))
#print(students[10001]["course"])
#names={"Abhinav","Kartik","Rakshit"]

#print(grades[-1],"\n", grades[-len(grades)])

class student:
    #students=[]
    def search_student(rollNo):
        if rollNo in roll:
            print("Student found or Already existss! Below mentioned are his details")
            obj2.details_student(rollNo)
            dsc9=int(input("For more functionalities of same student press 1\n or anything else to exit"))
            if dsc9==1:
                obj2.student_access(rollNo)
            else:
                print("Invalid Input")
        else:
            print("Student not found!! \n To register yourself as a student, press 1")
            dcsn1=int(input())
            if dcsn1==1:
                obj2.register_student(rollNo)
                
    def student_access(rollNo):
        loop=True
        while loop==True:
            y=int(input("Enter 1 to view student details\n2 to enroll a student in course\n3 to remove student from a course \n anything else to exit"))
            if y==1:obj2.details_student(rollNo),
            elif y==2:obj3.enroll_student(rollNo),
            elif y==3:obj3.unenroll_student(rollNo)
            else:
                print("invalid selection")
                loop=False
            
    def delete_student(rollNo):  
         if rollNo in students:
             students.pop(rollNo)
             print("Now this student has been removed")
             
    # adding or registering student           
    def add_student():
        rollNum=obj2.roll_validate()
#         roll.append(rollNo)
#         name=input("Enter student name")
#         age=input("enter student age")
#         course=courses
#         grades=courses_grades
#         students[rollNo]={"name":name,"age":age,"course":course,"Grades":grades}
#         inp1=int(input("To operate more functions for this student, press 1"))
#         if inp1==1:
#             obj2.student_access(rollNo)
#         else:
#             print ("Thanks for using this system")
    
    def register_student(rollNo):
        #rollNo=obj2.roll_validate()
        roll.append(rollNo)
        name=input("Enter student name")
        age=input("enter student age")
        course=courses
        grades=courses_grades
        students[rollNo]={"name":name,"age":age,"course":course,"Grades":grades}
        inp1=int(input("To operate more functions for this student, press 1"))
        if inp1==1:
            obj2.student_access(rollNo)
        else:
            print ("Thanks for using this system")
            
    def roll_validate():
        cnt=1
        while cnt==1:
            rollNum=str(input("Enter 5 digit roll number of student"))
            if len(rollNum)!=5:
                print("Invalid! Enter your input again of 5 digits only\n")
                cnt=1
            else:
                try:
                    rollNum=int(rollNum)
                    obj2.search_student(rollNum)
                    cnt=0
                    return rollNum
                           
                except Exception as e:
                    print("Invalid! Enter your roll number in digits only\n")
                    print(e)
                    cnt=1
                    
    def details_student(rollNo):
        if rollNo in students:
            print("Details for roll number ",rollNo," are:\n")
            print(students[rollNo])
        
#     def add_student(rollNo):
#         roll.append(rollNo)
#         name=input("enter student name")
#         names.append(name)
        
obj2= student

class course:
    def admin_access():
        loop1=True
        rollNo=obj2.roll_validate()
        while loop1==True:
            y=int(input("Enter 1 to assign grades to same student\n 2 to add your new student\n 3 to delete the existing student details\n 4 to Add new course\n 5 to modify course\n 6 to delete the existing course\n 7 to modify grades of same student\n 8 to view all student details\n anything else to exit"))
            if y==1:obj1.assign_grades(rollNo)
            elif y==2:obj2.add_student()
            elif y==3:obj2.delete_student(rollNo)
            elif y==4:obj1.add_course(rollNo)
            elif y==5:obj1.modify_course()
            elif y==6:obj1.delete_course(rollNo)
            elif y==7:obj1.modify_grades(rollNo)
            elif y==8:print(students)
            else:
                print("Invalid selection")
                loop1=False

    def add_course(rollNo):
        dsc3=int(input("press 1 if it's mandate course or 2 if it's for specific student"))
        course_name=input("Enter the course name")
        loop3=True
        while loop3==True:
            if course_name in courses:
                course_name=input("Enter different course name, as this already exists")
            else:
                loop3=False
        if dsc3==1:
            courses.append(course_name)
            for x in students.keys():
                students[x]["Grades"][course_name]=""
        elif dsc3==2:
            obj3.enroll_student(rollNo)
                #students[x]["Grades"][course_name]=grade
        else:
            print("Enter Valid input")
        print("")
    def delete_course(rollNo):
        dsc4=int(input("press 1 if it's mandate course or 2 if it's for specific student"))
        course_name=input("Enter the course name")
        if dsc4==1:
            courses.remove(course_name)
            for x in students.keys():
                ###students[x]["course"].remove(course_name)
                students[x]["Grades"].pop(course_name)
        elif dsc4==2:
            obj3.unenroll_student(rollNo)
                #students[x]["Grades"][course_name]=grade
        else:
            print("Enter Valid input")

    def modify_course():
        course_name=input("Enter the old course name")
        course_name_new=input("Enter the old course name")
        courses[course_name]=course_name_new
        for x in students:
            if course_name in students[x]["Grades"].keys():
                students[x]["Grades"][course_name_new]= dictionary.pop(course_name)

    def assign_grades(rollNum):
        course_name1=input("Enter the course name")
        grade=input("Enter the grades to be assigned")
        if course_name1 in students[rollNum]["Grades"].keys():
            #students[rollNum]["course"].append(course_name)
            students[rollNum]["Grades"][course_name1]=grade
        else:
            inp=int(input("This course doesn't exists\n to add this course, press 1 or anything else to exit"))
            if inp==1:
                obj1.add_course(rollNum)

    def modify_grades(rollNum):
        course_name=input("Enter the course name")
        grade=input("Enter the grades to be modified")
        if course_name in students[rollNum]["Grades"].keys():
            students[rollNum]["Grades"][course_name]=grade
        else:
            inp=int(input("This course doesn't exists\n to add this course, press 1 or anything else to exit"))
            if inp==1:
                obj1.add_course(rollNum)

obj1= course

class course_student:
    def enroll_student(rollNo):
        #roll_number=obj2.roll_validate()
        course_name=input("Enter the course name")
        loop2=True
        while loop2==True:
            if course_name in courses:
                course_name=input("Enter different course name, as this already exists")
            else:
                loop2=False
        roll_number=rollNo
        if roll_number in students:
#         for x in students:
#             if course_name in students[x]["Grades"].keys():
            students[roll_number]["course"].append(course_name)
            students[roll_number]["Grades"][course_name]=""

    def unenroll_student(rollNo):
        #roll_number=obj2.roll_validate()
        course_name=input("Enter the course name")
        roll_number=rollNo
        if roll_number in students:
#         for x in students:
#             if x==roll_number:
            if course_name in students[roll_number]["course"]:
                students[roll_number]["course"].remove(course_name)
                students[roll_number]["Grades"].pop(course_name)
            else:
                print("course not present")
        
obj3= course_student

ps0=1
while ps0==1:
    input1=int(input("Please enter 1 if you are student and 2 for admin\n"))
    if input1==1:
        obj2.roll_validate()
        #obj2.search_student(rollNo)
        #print("Login Successfull!")
        #obj2.student_access() 
        ps0=0
    elif input1==2:
        ps1=1
        while ps1==1:
            name=input("Enter your username")
            pswrd=input("Enter your password")
            if((name=="Admin" or name=="admin") and pswrd=="Admin@1"):
                print("Login Successfull!")
                obj1.admin_access()
                ps1=0
            else:
                print("Credentials didn't Match!! Enter your credentials again")
                ps1=1
        ps0=0
    else:
        print("Enter a valid input")
        ps0=1