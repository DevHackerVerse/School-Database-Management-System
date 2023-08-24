import main_menu
import student_data
import mysql.connector as co

def stu_menu():
    while True:
        print("\t\t.................................................")
        print("\t\t.....*********SCHOOL MANAGEMENT SYSTEM***********")
        print("\t\t.................................................")
        print("\n\t\t*******************STUDENT DATA*******************")
        print("*1. Add Student Record*")
        print("*2. Show Student Records*")
        print("*3. Search Student record*")
        print("*4. Deletion of Record")
        print("*5. Update Student Record*")
        print("*6. Return*")
        print("\t\t-------------------------------------------------")
        choice=int(input("Enter your choice : "))
        if choice==1:
            student_data.add_record()
        elif choice==2:
            student_data.show_stu_details()
        elif choice==3:
            student_data.search_stu_details()
        elif choice==4:
            student_data.delete_stu_details()
        elif choice==5:
            student_data.edit_stu_details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice try again..")
            conti=input("press any key ti continue..")

def add_record():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
        cursor=mycon.cursor()
        session=input("Enter Session: ")
        stname=input("Enter Student Name: ")
        stclass=input("Enter Class: ")
        stsec=input("Enter Section: ")
        stroll=input("Enter Roll No.: ")
        sub = []
        for i in range(3):
            sb = input(f"Enter subject {i+1}: ")
            sub.append(sb)
        query="insert into Student() value('{}','{}','{}','{}','{}','{}','{}','{}')".format(session,stname,stclass,stsec,stroll,sub[0],sub[1],sub[2])
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')
    except:
        print('error')
            
def show_stu_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    cursor.execute("Select * from Student")
    data = cursor.fetchall()
    for row in data:
        print(row)

def search_stu_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    adn=input("Enter Admission Number: ")
    st="select * from Student where stroll='%s'"%(adn)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)
    
def delete_stu_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    adn=input("Enter Admission Number: ")
    st="delete from Student where stroll='%s'"%(adn)
    cursor.execute(st)
    mycon.commit()
    print("Record has been deleted")

def edit_stu_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    print("*1: Edit Name* ")
    print("*1: Edit First Subject* ")
    print("*3: Edit Second Subject* ")
    print("*4: Edit Third Subject* ")
    print("*5: Return* ")
    print("\t\t-----------------------------------------------------")
    choice = int(input("Enter your choise: "))    
    if choice == 1:
        student_data.edit_name()
    elif choice == 2:
        student_data.edit_sub1()
    elif choice == 3:
        student_data.edit_sub2()
    elif choice == 4:
    	student_data.edit_sub3()
    elif choice == 5:
        return
    else:
        print("Error: Invalid Choise try again.....")
        conti="Press any key to return to "

def edit_name():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Roll no: ")
    nm=input("Enter Correct name: ")
    st = "update Student set stname='%s' where stroll = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
def edit_sub1():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Roll no: ")
    nm=input("Enter Correct Subject: ")
    st = "update Student set sub1='%s' where stroll = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
def edit_sub2():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Roll no: ")
    nm=input("Enter Correct Subject: ")
    st = "update Student set sub2='%s' where stroll = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
def edit_sub3():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Roll no: ")
    nm=input("Enter Correct Subject: ")
    st = "update Student set sub3='%s' where stroll = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
