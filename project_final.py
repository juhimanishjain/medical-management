import mysql.connector as sqlct
import datetime
def createdb():
    global mycn
    global mycur
    mycn=sqlct.connect(host="localhost",user="root",password="Juhijain05$",database="juhijain1234")
    if mycn.is_connected():
        print("\tThank you for choosing to shop with Apollo Medical Store.")
    mycur=mycn.cursor()
    cmd1="Create table if not exists _medicalproject(ProductCode integer primary key,name char(50) not null,Packing char(50),Expirydate date,"\
    "Company char(50),Batch char(10),Quantity integer,Rate integer)"
    mycur.execute(cmd1)
    cust1="Create table if not exists customertable(BillNumber integer,Customername varchar(50),Doctorname varchar(50),Productcode integer,"\
    "Quantity integer,foreign key(ProductCode) references _medicalproject(ProductCode))"
    mycur.execute(cust1)
#---------MEDICINE(SHOP OWNER)-------------------------
#FUNCTION TO ADD MEDICINES:-
def add_medicine():
    ProductCode=int(input("Enter the product code:"))               #PRODUCT CODE
    name=input("Enter name of the medicine:")                       #NAME OF THE MEDICINE
    Packing=input("Enter the packing details:")                     #PACKING DETAILS        
    ExpiryDate=input("Enter expiry date of medicine(yyyy/mm/dd):")  #EXPIRY DATE OF MEDICINES
    Company=input("Enter name of the company:")                     #COMPANY NAME OF MEDICINES
    Batch=int(input("Enter batch name of medicine:"))               #BATCH NUMBER
    Quantity=int(input("Enter quantity for your medicine:"))        #QUANTITY PURCHASED
    Rate=int(input("Enter rate of your medicine:"))                 #RATE OF THE MEDICINES
    cmd5 = "insert into _medicalproject values ("+str(ProductCode)+",'"+name+"','"+Packing+"','"+str(ExpiryDate)+"','"+Company+"',"+str(Batch)+","+str(Quantity)+","+str(Rate)+")"
    mycur.execute(cmd5)
    print("Record has been added successfully")
#FUNCTION TO DISPLAY MEDICINES:-
def display_medicine():
    cmd2 = "select * from _medicalproject"
    mycur.execute(cmd2)
    r2 = mycur.fetchall()
    print("=================================================================================================================")
    print("| PRODUCT CODE   MEDICINE NAME   PACKING DETAILS   EXPIRY DATE   COMPANY NAME   BILL NUMBER  QUANTITY     RATE  |")
    print("=================================================================================================================")
    for i in range(len(r2)):
        print("| ",end="")
        print(str(r2[i][0]).ljust(15," "),end="")
        print(r2[i][1].ljust(17," "),end="")
        print(r2[i][2].ljust(18," "),end="")
        print(str(r2[i][3]).ljust(14," "),end="")
        print(r2[i][4].ljust(15," "),end="")
        print(str(r2[i][5]).ljust(16," "),end="")
        print(str(r2[i][6]).ljust(10," "),end="")
        print(str(r2[i][7]).ljust(5," "),end="|")
        print()
    print("==================================================================================================================")



#FUNCTION FOR SEARCHING MEDICINES:-
def search_medicine():
    med_name= input("Enter medicine name for search: ")
    cmd4 = "select * from _medicalproject where name like '%"+med_name+"%'"
    mycur.execute(cmd4)
    r2 = mycur.fetchone()
    if r2 is None:
        print("No record has found ")
    else:
        print("PRODUCT CODE   MEDICINE NAME   PACKING DETAILS   EXPIRY DATE   COMPANY NAME   BILL NUMBER  QUANTITY     RATE")  
        print(str(r2[0]).ljust(15," "),end="")
        print(r2[1].ljust(17," "),end="")
        print(r2[2].ljust(18," "),end="")
        print(str(r2[3]).ljust(14," "),end="")
        print(r2[4].ljust(15," "),end="")
        print(str(r2[5]).ljust(16," "),end="")
        print(str(r2[6]).ljust(10," "),end="")
        print(str(r2[7]).ljust(15," "),end="")
        print()


        
        
#FUNCTION TO CHECK WHICH MEDICINES HAVE EXPIRED:-
def expiry_stockmodule():
    expdate=datetime.date.today()
    y1=expdate.year
    cmd6 ="select ProductCode,name,Expirydate,Batch from _medicalproject where Expirydate <='"+str(expdate)+"'"
    mycur.execute(cmd6)
    r2=mycur.fetchall()
    print("PRODUCT CODE   NAME             EXPIRY DATE   BATCH")  
    for i in range(len(r2)):
        print(str(r2[i][0]).ljust(15," "),end="")
        print((r2[i][1]).ljust(17," "),end="")
        print(str(r2[i][2]).ljust(14," "),end="")
        print(str(r2[i][3]).ljust(15," "),end="")
        print()

           
#DISPLAY MEDICINES COMPANY-WISE:-
def display_companywise():
    company_name= input("Enter the company name you want to display:")
    cmd8=" select * from _medicalproject where Company = '"+company_name+"'"
    mycur.execute(cmd8)
    r4 = mycur.fetchall()
    if r4 is None:
        print("No record has found ")
    else:
        print(r4)

#DELETE MEDICINE RECORDS:-
def delete_medicine():
    delete_medicine=int(input("Enter the medicine product code that you want to delete:"))
    cmd3= "select count(*) from customertable where Productcode="+str(delete_medicine)+""
    mycur.execute(cmd3)
    r3 = mycur.fetchone()
    total_record=r3[0]
    if(total_record==0):
        cmd7="delete from _medicalproject where ProductCode="+str(delete_medicine)+""
        mycur.execute(cmd7)
        print("Record has been deleted")
    else:
        cmd7="update _medicalproject set quantity=0 where ProductCode="+str(delete_medicine)+""
        mycur.execute(cmd7)
        print("This medicine has already been sold,so it can't be deleted.Hence,the quantity of this medicine is set to zero.")
#-------------MEDICINE(BILLING)---------------
#FUNCTION TO FILL IN BILL DETAILS:-

def add_newbill():
    cmd3= "select max(BillNumber) from customertable "
    mycur.execute(cmd3)
    r3 = mycur.fetchone()
    BillNumber=r3[0]+1
    print("Your bill number is:",BillNumber)                            #BILL NUMBER              
    name=input("Enter your name:")                                      #NAME 
    DoctorName=input("Enter your doctor's name:")                       #DOCTOR'S NAME
    while(1):
        Productcode=int(input("Enter product code of your medicine:"))  #PRODUCT CODE OF MEDICINE
        Quantity=int(input("Enter quantity for your medicine:"))        #QUANTITY
        #print("Your order has been successfully placed")                
        cmd = "insert into customertable values ("+str(BillNumber)+",'"+name+"','"+DoctorName+"',"+str(Productcode)+","+str(Quantity)+")"
        mycur.execute(cmd)
        addmed=input("Do you want to add medicine(y/n)?")
        if(addmed=='n' or addmed=='N'):
            break
    print("Record has been added")   
    
    
#FUNCTION FOR DISPLAYING THE BILL:-
def display_bill():
    cmd1 = "select CT.BillNumber,CT.Customername,CT.DoctorName,CT.Productcode,MDT.name,CT.Quantity,MDT.Rate,CT.Quantity*MDT.Rate Amount "
    cmd1 = cmd1+ "from customertable CT,_medicalproject MDT where CT.Productcode=MDT.ProductCode"
    mycur.execute(cmd1)
    r = mycur.fetchall()
    print("BILL NUMBER      CUSTOMER NAME       DOCTOR NAME     PRODUCT CODE    MEDICINE NAME     QUANTITY       RATE     AMOUNT")  
    #print("BILLNO  DOCTOR NAME      PRODUCT CODE          MEDICINE NAME       QUANTITY        RATE         AMOUNT")
    for i in range(len(r)):
        print(str(r[i][0]).ljust(4," "),end=" ")
        print(r[i][1].rjust(24," "),end=" ")
        print(r[i][2].rjust(17," "),end=" ")
        print(str(r[i][3]).rjust(14," "),end=" ")
        print(str(r[i][4]).rjust(15," "),end=" ")
        print(str(r[i][5]).rjust(13," "),end=" ")
        print(str(r[i][6]).rjust(7," "),end=" ")
        print(str(r[i][7]).rjust(13," "),end=" ")
        print()        
#FUNCTION TO SEARCH BILL:-
def search_bill():
    Bill_Number= int(input("Enter the bill number which you want to search :"))
    #cmd3= "select * from customertable where BillNumber= "+str(Bill_Number)+""
    cmd3 = "select CT.BillNumber,CT.Customername,CT.DoctorName,CT.Productcode,MDT.name,CT.Quantity,MDT.Rate,CT.Quantity*MDT.Rate Amount "
    cmd3 = cmd3+ "from customertable CT,_medicalproject MDT where CT.Productcode=MDT.ProductCode and "+" BillNumber= "+str(Bill_Number)+""
    mycur.execute(cmd3)
    r3 = mycur.fetchone()
    if r3 is None:
        print("no record found ")
    else:
        print(r3)
#FUNCTION FOR BILL DELETION:-
def delete_bill():
    Bill_Delete=int(input("Enter the bill number you want to delete:"))
    cmd4="delete from customertable where BillNumber="+str(Bill_Delete)+""
    mycur.execute(cmd4)
    print("The record has been deleted!")
#FUNCTION FOR EDITING BILL:-
def edit_bill():
    Bill_Number= int(input("Enter the bill number that you want to edit :"))
    product_code=int(input("Enter the product code that you want to edit :"))
    cmd3= "select Productcode,Quantity from customertable where BillNumber= "+str(Bill_Number)+" and Productcode="+str(product_code)+""
    mycur.execute(cmd3)
    r3 = mycur.fetchone()
    if r3 is None:
        print("no record found ")
    else:
        quantity_new=int(input("Enter the quantity for your medicine:"))  
        cmd5="update customertable set Quantity="+str(quantity_new)+" where BillNumber="+str(Bill_Number)+" and Productcode="+str(r3[0])+""
        mycur.execute(cmd5)
        print("Record has been updated")
 
#-------------THE MAIN MENU---------------------
print("\t\t\tApollo Medical Store")
createdb()
while True:
    print("\n\n-------------MAIN MENU--------------------")
    print("(1)Shop owner(Admin) (2)Customer(Billing)  (3)Exit")
    choice=int(input("Please enter your choice:"))
    if(choice==1):
        while True:
            print("\n\n----SHOP OWNER----\n")
            print("(1)ADD MEDICINE                  (2)DISPLAY ALL MEDICINE  (3)SEARCH MEDICINE")
            print("(4)DISPLAY MEDICINES COMPANYWISE (5)CHECK EXPIRY STOCK    (6)DELETE MEDICINE")
            print("(7)EXIT") 
            choice1=int(input("Please enter your choice:"))
            if(choice1==1):
                add_medicine()
            elif(choice1==2):
                display_medicine()
            elif(choice1==3):
                search_medicine()
            elif(choice1==4):
                display_companywise()
            elif (choice1==5):
                expiry_stockmodule()
            elif(choice1==6):
                delete_medicine()
            elif(choice1==7):
                break
                

    if(choice==2):
        while True:
            print("\n\n----BILLING---")
            print("\n(1)CUSTOMER BILLING(2)DISPLAY BILL(3)SEARCH BILL(4)EDIT BILL(5)DELETE BILL(6)EXIT")
            choice2=int(input("Enter your choice:"))
            if(choice2==1):
                add_newbill()
            elif(choice2==2):
                display_bill()
            elif(choice2==3):
                search_bill()
            elif(choice2==5):
                delete_bill()
            elif (choice2==4):
                edit_bill()
            elif(choice2==6):
                break
    if(choice==3):
        mycn.commit()
        break
    
