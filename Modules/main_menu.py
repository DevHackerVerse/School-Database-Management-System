import main_menu
import admission
import student_data
import fee_details

while True:
    print("\t\t.................................................")
    print("\t\t.....*********SCHOOL MANAGEMENT SYSTEM***********")
    print("\t\t.................................................")
    print("\n\t\t*****************VIKAS VIDYALAYA BEGUSARAI*******************")
    print("*1. Admission*")
    print("*2. Student Data*")
    print("*3. Fee Details*")
    print("*4. Exit*")
    print("\t\t.................................................")
    print("\t\t-------------------------------------------------")
    choice=int(input("Enter your choice : "))
    if choice==1:
        admission.adm_menu()
    elif choice==2:
        student_data.stu_menu()
    elif choice==3:
        fee_details.fee_menu()
    elif choice==4:
        break
    else:
        print("Error: Invalid Choice try again..")
        conti=input("press any key ti continue..")
