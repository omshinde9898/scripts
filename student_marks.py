student_list = []

class student:
    def __init__(self,name,department,marks):
        self.name = name
        self.department = department
        self.marks = marks
        
    def percentage_calc(self):
        if len(self.marks) == 0:
            return 0
        else: 
            return sum(self.marks)/5
        
    def show_res(self):
        print("Name : ",self.name)
        if self.department == 1:
            print("Department : Computer Science")
        elif self.department == 2:
            print("Department : Information Technology")
        elif self.department == 3:
            print("Department : Artificial Intelligence")
        else:
            print("Other Department")
        for i in range(len(self.marks)):
            print("Subject : ",i+1," Marks : ",self.marks[i])
        print("\nPercentage : ",self.percentage_calc())
        per = self.percentage_calc()
        if per > 75:
            print("Class : Distinction")
        elif per >=60 and per < 75:
            print("Class : First")
        elif per >=50 and per <60:
            print("Class : Second")
        elif per >= 40 and per <50:
            print("Class : Third")
        else:
            print("Fail")
        
    
def getData():
    n = input("Enter Name : ")
    print("Choose department\nCS : 1\nIT : 2\nAI : 3")
    dep = int(input(" : "))
    lst = []
    i = 0
    while i <5:
        i = i+1
        m = int(input("Enter Marks Of Subject "+str(i)+" : "))
        if m <40:
            print(n," : Result : ",end="")
            print("Failed")
            lst.clear()
            break
        elif m >100:
            print("Marks can't be above 100")
            i = i-1
            continue
        lst.append(m)
        
    sdt = student(n,dep,lst)
    student_list.append(sdt)
    

def basic_op():
    print("\nChoose Action")
    print("Add Students           : 1")
    print("Search Student Result  : 2")
    print("Get All Results        : 3")
    print("Exit                   : 4")
    ip = int(input(":"))
    if ip == 1:
        j = int(input("Enter Number of Students : "))
        for i in range(j):
            print("\nUpdate ",i+1," Student : ")
            getData()
    elif ip == 2:
        nm = input("Enter Student Name :(Case Sensitive): ")
        for i in student_list:
            if nm != i.name:
                continue
            else:
                i.show_res()
        
            

    elif ip == 3:
        for i in student_list:
            print("\n")
            print("   :Result:   ")
            print("\n")
            i.show_res()
    elif ip == 4:
        exit()
    else:
        print("Choose correct option")
    
while True:
    basic_op()