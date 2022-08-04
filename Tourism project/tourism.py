# Tourism database management system
import mysql.connector 

mydb=mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="12345",
    database="tourism", 
)
mycursor=mydb.cursor()
#***************-------******************

print("Welcome to Tourism data management system")

register_username = "ragul"
register_password = "12345"

login_username = "ragul"
login_password = "12345"

db_username = "ragul"
db_password = "12345"

def register_login():
    if not (not register_username and not register_password):
        print("Register Succcessfully") 
        if db_username==login_username and db_password==login_password:
            print("Login Successfully")
        else:
            print("please check your username and password")
    else:
        print("please enter the value to  register the username and password")
                        
register_login()

def select_destination():
    global travel_place
    print("1.Ooty \n2.Maldives \n3.Andaman \n4.Goa \n5.Kodaikanal")
    travel_place = int(input("select the your tourism place:"))
    if travel_place == 1:
        global amount
        amount = 3000
        travel_place = "Ooty"
        print(f"your are selected Ooty")
    elif travel_place == 2:
        amount = 10000
        travel_place = "Maldives"
        print(f"your are selected Maldives")
    elif travel_place == 3:
        amount = 8000
        travel_place = "Andaman"
        print(f"your are selected Andaman")
    elif travel_place == 4:
        amount = 5000
        travel_place = "Goa"
        print(f"your are selected Goa")
    elif travel_place == 5:
        amount = 3000
        travel_place = "Kodaikanal"
        print(f"your are selected Kodaikanal")   
    else:
        print("please choose the option between 1 to 5:")   
        select_destination()  
select_destination()

def package_manage():
    global total_members
    total_members =int(input("how many members:"))
    global total_staydays
    total_staydays= int(input("enter the days you want to stay:"))   
    print("you have 2 options to pay: \n 1. if you pay online payment you have 20%' discount \n 2. Cash on hand no discount")
    global payment_method
    payment_method  = int(input("Enter your payment method:"))
    global total_amount
    total_amount = (total_members * amount * total_staydays)
    if payment_method == 1:
        payment_method = "Online payment"
        total = total_amount * 20 // 100
        total_amount -= total
        print("you have 20%' discount")
        print(f"your total cost for {total_members} person with {total_staydays}days stay in {travel_place} total cost is Rs:{total_amount}")
    elif payment_method == 2:
        payment_method = "cash on hand"
        print(f"your total cost for {total_members} person with {total_staydays}days stay in {travel_place} total cost is Rs:{total_amount}")
    else:
        print("please enter 1 or 2 there is only 2 option:") 
        package_manage()      
package_manage()
    

def payment():
        recipt = input("you want payment recipt yes or no:")
        if recipt == "yes":
            f = open("Tourism project/text.txt","w")
            f.write(f"Welcome mam/sir \n  your total cost for {total_members} person \n  with {total_staydays}days stay in {travel_place} total cost is Rs:{total_amount}\n*****Thank you sir/mam*****")
            f.close()
            print("your payment recipt stored in text file")
        else:
            print("ok Thank you ")
payment()                

#sql commands
#mycursor.execute("create table tourism_database(travel_place varchar(100),total_members int,total_amount int,payment_method varchar(200))")
# mycursor.execute("create database tourism")
sql="insert into tourism_database(travel_place,total_staydays,total_members,total_amount,payment_method) values (%s,%s,%s,%s,%s)" 
val=(travel_place,total_staydays,total_members,total_amount,payment_method) 
mycursor.execute(sql,val) 
mydb.commit()
print("your data are stored in database")     








