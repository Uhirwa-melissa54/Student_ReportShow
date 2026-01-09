print("Welcome to StudentReportShow")
print("How many student do you have?")
numberOfStudent=int(input())
student={}
def viewStudent():
    for x in student:
        print(x)
for x in range(numberOfStudent):
    print("Enter Student's Name")
    name=input()
    print("Enter Physic's Marks")
    physMarks=int(input())
    print("Enter English's Marks")
    engMarks=int(input())
    print("Enter Math's Marks")
    mathMarks=int(input())
    print("Enter Java's Marks")
    javaMarks=int(input())
    print("Enter DSA's Marks")
    dsaMarks=int(input())
    student[name]=[physMarks,engMarks,mathMarks,javaMarks]
else:
    print("You have entered all Students");
print("Choose to continue")
print("1.Continue]\n 0.exit")
decision=int(input())
if decision==1:
    print("Choose what you want to do:\n 1.View Students \n 2. View Studn2.Find each student average\n3.Find each subject Marks \n")
    choice=int(input())
    match choice:
        case 1:
            viewStudent()
elif decision==0:
    print("Bye")
    exit()

