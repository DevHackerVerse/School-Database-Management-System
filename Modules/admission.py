import main_menu
import admission
import mysql.connector as co

def adm_menu():
    while True:
        print("\t\t.................................................")
        print("\t\t.....*********School Management System***********")
        print("\t\t.................................................")
        print("\n**Admission**\n")
        print("*1. Add New Admission Details*")
        print("*2. Show Admission Details*")
        print("*3. Search Admission record*")
        print("*4. Deletion of Record")
        print("*5. Update Admission Details*")
        print("*6. Return*")
        print("\t\t-------------------------------------------------")
        choice=int(input("Enter your choice : "))
        if choice==1:
            admission.admin_details()
        elif choice==2:
            admission.show_admin_details()
        elif choice==3:
            admission.search_admin_details()
        elif choice==4:
            admission.delete_admin_details()
        elif choice==5:
            admission.edit_admin_details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice try again..")
            conti=input("press any key ti continue..")

def admin_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
        cursor=mycon.cursor()
        adno=input("Enter Admission No.: ")
        rno=input("Enter Role No.: ")
        sname=input("Enter Student Name.: ")
        address=input("Enter Address: ")
        phon=input("Enter Mobile No.: ")
        clas=input("Enter Class: ")
        query="insert into Admission(adno,rno,sname,address,phon,clas) value('{}','{}','{}','{}','{}','{}')".format(adno,rno,sname,address,phon,clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')
    except:
        print('error')
            
def show_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    cursor.execute("Select * from Admission")
    data = cursor.fetchall()
    for row in data:
        print(row)

def search_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    adn=input("Enter Admission Number: ")
    st="select * from Admission where adno='%s'"%(adn)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)
    
def delete_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    adn=input("Enter Admission Number: ")
    st="delete from Admission where adno='%s'"%(adn)
    cursor.execute(st)
    mycon.commit()
    print("Record has been deleted")

def edit_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    print("1: Edit Name: ")
    print("2: Edit Address: ")
    print("3: Phone number: ")
    print("4: Return: ")
    print("\t\t-----------------------------------------------------")
    choice = int(input("Enter your choise: "))    
    if choice == 1:
        admission.edit_name()
    elif choice == 2:
        admission.edit_address()
    elif choice == 3:
        admission.edit_phno()
    elif choice == 4:
        return
    else:
        print("Error: Invalid Choise try again.....")
        conti="Press any key to return to "

def edit_name():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Admission no: ")
    nm=input("Enter Correct nlName: ")
    st = "update Admission set sname='%s' where adno = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
    
def edit_address():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Admission no: ")
    nm=input("Enter Correct Address: ")
    st = "update Admission set address='%s' where adno = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
    
def edit_phno():
    mycon =co.connect(host="localhost",user="root",passwd="KARAN&vivo99", database="mps")
    cursor=mycon.cursor()
    ac=input("Enter Admission no: ")
    nm=input("Enter Correct Phone: ")
    st = "update Admission set phon='%s' where adno = '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
