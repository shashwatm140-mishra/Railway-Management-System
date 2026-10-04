import mysql.connector as sqlc
import random
password = input("Enter MySQL Password")
mycon = sqlc.connect(host="localhost" , user="root" , password= password , database = "railway_employees")
cursor = mycon.cursor()
while True:
    a = int(input("Enter train no. "))
    b = input("Enter train name: ")
    c = input("from: ")
    d = input("to: ")
    e = input("via: ")
    f = input("3A: ")
    g = int(input("Seats: "))
    h = input("2A: ")
    i = int(input("Seats: "))
    j = input("SL: ")
    k = int(input("Seats: "))
    l = input("1A: ")
    m = int(input("Seats: "))
    cursor.execute("insert into reserved values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(a,b,c,d,e,f,g,h,i,j,k,l,m))
    print()
    print("Records added successfully")
    mycon.commit()
    n = input("Enter more records: ")
    if n.lower() == "y":
        continue
    else:
        print("Program Terminated successfully")
        break
