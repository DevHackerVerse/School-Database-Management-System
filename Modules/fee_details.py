import main_menu
import fee_details
import mysql.connector

def fee_menu():
	while True:
		print("\t\t.................................................")
		print("\t\t.....*********SCHOOL MANAGEMENT SYSTEM***********")
		print("\t\t.................................................")
		print("\n **FEE DETAILS**\n")
		print("*1 : Deposit Fee*")
		print("*2 : View Fee of All Students*")
		print("*3 : View Fee of a Particular Student*")
		print("*4 : Return*")
		try:
			userInput = int(input("Please Select An Above Option: "))
		except ValueError:
			exit("\nHy! That's Not A Number")
		else:
			print("\n")
			if (userInput==1):
				fee_details.feeDeposit()
			elif (userInput==2):
				fee_details.feeView()
			elif (userInput==3):
				fee_details.feeViewPart()
			elif (userInput==4):
				return
		print("-------------------------------------------------")


def feeDeposit():
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="KARAN&vivo99",database="mps")
	mycursor=mydb.cursor()
	L=[]
	roll=int(input("Enter the Admission number : "))
	L.append(roll)
	feedeposit=int(input("Enter the Fee to be deposited : "))
	L.append(feedeposit)
	month=input("Enter month of fee : ")
	L.append(month)
	fee=(L)
	sql="insert into Fees (adno,FeeDeposit,Month) values (%s,%s,%s)"
	mycursor.execute(sql,fee)
	mydb.commit()
	print ("Fee has been Deposited Succefully!!!")

def feeView():
	print ("*ALL FEE DETAILS*")
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="KARAN&vivo99",database="mps")
	mycursor=mydb.cursor()
	sql="Select Admission.adno, Admission.sname, Admission.clas, sum(Fees.FeeDeposit), count(Fees.month) from Admission,Fees where Admission.adno=Fees.adno Group by adno"
	mycursor.execute(sql)
	res=mycursor.fetchall()
	month = ['April','May','June','July','August','September','October','November','December','January', 'February','March']
	for x in res:
		x = list(x)
		a = x.pop()
		x.append(month[a-1])
		print(x,end = ' ')
		print (f"  Fee left from {month[a]}")
	print('\n','\n')

def feeViewPart():
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="KARAN&vivo99",database="mps")
	mycursor=mydb.cursor()
	admno=int(input("Enter the Admission number of the Student : "))
	sql="Select Admission.adno, Admission.sname, Admission.clas, sum(Fees.FeeDeposit), count(Fees.month) from Admission INNER JOIN Fees ON Admission.adno=Fees.adno and Fees.adno = %s"
	adm=(admno,)
	mycursor.execute(sql,adm)
	res=mycursor.fetchall()
	month = ['April','May','June','July','August','September','October','November','December','January', 'February','March']
	for x in res:
		x = list(x)
		a = x.pop()
		x.append(month[a-1])
		print('\n',x,'\n')
		print (f"Fee left from {month[a]}")
	print('\n','\n')
