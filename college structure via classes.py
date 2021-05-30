'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Teacher:
    def __init__(self, subject):
        self._subject = subject
        print ("Primary subject Teacher teaches : ", subject)
    
    def name(self):
        """return name of teacher"""
        name = input("Name of the teacher: ")
        print ("Teacher Name : ", name)
    
    def year(self):
        year = int(input("Year of starting: "))
        Experience = 2020-year
        print ("Experience: ", Experience,"years")
class Student:
    def __init__(self, batch):
        self._batch = batch
    def admit(self, program):
        """return name of program"""
        if program == "B.tech":
            print(" ")  
            print("Stream: Computer Science and Engineering")
        elif program == "B.des":
            print(" ") 
            print("Stream: UI/UX Design")
        else:
            print(" ") 
            print("Invalid Program")
    def subjects(self):
        """returns list of subjects"""
        if self._batch == "Engineering":
            Semester = int(input("In which semester are you in: "))
            if Semester == 1:
                print("Subjects: Introduction To Design")
                print("          Critical And Creative Thinking")
                print("          Joy Of Making")
                print("          Engineering Physics")
                print("          Engineering Mathematics")
            elif Semester == 2:
                print("Subjects: Nature and Design")
                print("          Design Methodology")
                print("          Introduction to Computing")
                print("          Principles of Engineering")
            else:
                print("\nNot Released Yet")
            
        elif self._batch == "Designing":
            Semester = int(input("In which semester are you in: "))
            if Semester == 1:
                print("Subjects: Introduction To Design")
                print("          Critical And Creative Thinking")
                print("          Understanig Modelling")
                print("          Working In Workshop")
            elif Semester == 2:
                print("Subjects: Creative Visualization")
                print("          Semiotics")
                print("          Photography")
                print("          Critical and Creative Thinking 2") 
            else:
                print("\nNot Released Yet")
        else:
            print("\nInvalid Batch")
class StudentOffice(Student):
              
    def __init__(self, batch):     #Extending class Student
        super().__init__(batch)   
    def enrollment_status(self):   #returns enrollment status of batch
       
        Semester = int(input("Please enter one again, in which semester are you in: "))
        if Semester == 1:
            year = int(input("Enter enrolment year for B.Tech (2020 or 2021): "))
            if year == 2020:
                print("Enrolment Status: Inactive")
            elif year == 2021:
                print("Enrolment Status: Active")
            else:
                print("Enter a valid year")
        elif Semester == 2:
            year = int(input("Enter enrolment year for B.Des (2020 or 2021): "))
            if year == 2020:
                print("Enrolment Status: Active")
            elif year == 2021:
                print("Enrolment Status: Inactive")
            else:
                print("Enter a valid year")
        else:
            print("Invalid Batch")
    def attendance(self):
        """attendance status"""
        attend = int(input("Enter attendance (in %): "))
        return attend
class ExamOffice(StudentOffice):       #Extending class StudentOffice

    def __init__(self, batch, CGPA):
        super().__init__(batch)
        self._CGPA = CGPA
    def pass_exam(self):
    
        if self._CGPA > 5:              #returns pass if cgpa > 5
            print("Pass\n")
        else:
            return False
    def fail(self):
        """returns fail if cgpa < 5"""
        if self._CGPA < 5:
            print("Fail\n")
        else:
            return False
    def fr(self):
        """returns fail due to reason if attendance < 50%"""
        attend = super().attendance()
        if attend < 50 and self._CGPA < 5:
            print("Fail due to reason\n")
        else:
            pass
print("TECHNICAL BLOCK\n")    
teacher = Teacher("Mathematics")
teacher.name()
teacher.year()
print("\nFor Student Batch :")
student = Student("Engineering")
student.admit("B.tech")
student.subjects()
StudentExtension=StudentOffice("Engineering")
StudentExtension.enrollment_status()
cgpa=float(input("Enter your final CGPA: "))
StudentOfficeExtension=ExamOffice("Engineering", cgpa)
StudentOfficeExtension.pass_exam()
StudentOfficeExtension.fail()
StudentOfficeExtension.fr()
print("\n\nCREATIVE BLOCK\n")       
teacher = Teacher("Design Faculty")
teacher.name()
teacher.year()
print("\nFor Student Batch :")
student = Student("Designing")
student.admit("B.des")
student.subjects()
StudentExtension=StudentOffice("Designing")
StudentExtension.enrollment_status()
cgpa=float(input("Enter your final CGPA: "))
StudentOfficeExtension=ExamOffice("Designing", cgpa)
StudentOfficeExtension.pass_exam()
StudentOfficeExtension.fail()
StudentOfficeExtension.fr()

