import mysql.connector as sqlc
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Spacer
import smtplib
from email.message import EmailMessage

password = input("ENter MySQL Password: ")

mycon = sqlc.connect(host="localhost" , user="root" , password= password , database = "railway_employees")
cursor = mycon.cursor()
def availability():
    cursor.execute("select * from records")
seat_count={}
z=1
aa = 1
sll=1
lower3 = [1,4,9,12,17,20,25,28,33,36,41,44,49,52,57,60,65,68,73,76]
mid3 = [2,5,10,13,18,21,26,29,34,37,42,45,50,53,58,61,66,69,74,77]
upp3 = [3,6,11,14,19,22,27,30,35,38,43,46,51,54,59,62,67,70,75,78]
sidel3 = [7,15,23,31,39,47,55,63,71,79]
sideu3 = [8,16,24,32,40,48,56,64,72,80]
lower2 = [1,3,7,9,13,15,19,21,25,27,31,33,37,39,43,45,49,51]
upp2 = [2,4,8,10,14,16,20,22,26,28,32,34,38,40,44,46,50,52]
sidel2 = [5,11,17,23,29,35,41,47,53]
sideu2 = [6,12,18,24,30,36,42,48,54]
lower1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
upp1 = [2,4,6,8,10,12,14,16,18,20,22,24]
#FUNCTIONS


def chartout():
    take = int(input("Enter your PNR Number: "))
    cursor.execute("select * from chart where pnr = '%s' " %(take,) )
    out = cursor.fetchall()
    kn=0
    while kn<=4:
        print(out[0][kn], end="\n")
        kn+=1
    mycon.commit()

app_password = input("Enter email app password: ")
def send_ticket_email(pdf_path,receiver_email):
    sender_email = "srctc.ticket@gmail.com"
    app_password = app_password

    msg = EmailMessage()
    msg["Subject"] = "Your ticket PDF"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Dear Passenger,\n\n Your ticket is attached to this mail.\n\n Have a happy and safe journey")

    with open(pdf_path , "rb") as f:
        msg.add_attachment(f.read(), maintype="application",subtype="pdf",
        filename  = os.path.basename(pdf_path))
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(sender_email,app_password)
        server.send_message(msg)
    print("\t\tTicket sent successfully")





while True:
    print("Welcome to Railway Management System")
    print("Logging in as: ")
    print("1. Official Employee")
    print("2. Passenger")
    print("3. Leave Program")
    a = int(input("Enter your Choice: "))
    if a==1:
        while True:
            a = random.randrange(111111,999999)
            print("CAPTCHA:",a)
            captcha = int(input("Enter the given CAPTCHA: "))
            if a==captcha:
                
                print("Logged IN Successfully as Official")
                while True:
                    print("1.Show LOCO-PILOT LIST")
                    print("2.Assign LOCO-PILOT")
                    print("3.Back to Main menu")
                    opt = int(input("Enter Operation to be Carried out: "))
                    if opt==1:
                        cursor.execute("select * from records")
                        data = cursor.fetchall()
                        for rec in data:
                            print(rec , end="\n")
                            continue
                    elif opt==2:
                       stn1 = input("Enter Railway Station Code: ")
                       stn = stn1.upper()
                       
                       print("The list of available Loco-Pilots is as follows: ")
                       cursor.execute("select * from records where source_station = '%s' " %(stn,))
                       lst = cursor.fetchall()
                       for i in lst:
                           print(i , end="\n")
                       st = int(input("Enter Employee Number: "))
                       cursor.execute("select empname from records where empno = '%s' " %(st,))
                       loco=cursor.fetchall()
                       print("Select the Train from given list: ")
                       cursor.execute("select * from train")
                       train=cursor.fetchall()
                       for k in train:
                           print(k , end="\n")
                       sel = int(input("Enter Train no.: ")) 
                       cursor.execute("select train_name from train where train_no = '%s' " %(sel,))
                       rail = cursor.fetchall()
                       print("Name: ",loco[0][0])
                       print("Train: ",rail[0][0])
                       cursor.execute("update records set no_of_duties = no_of_duties+1 where empno='%s' " %(st,))
                       continue
                       
                           
                    elif opt==3:
                        break
                    
                    
                    
                    
                break
            else:
                print("Invalid captcha!!!")
                print("Please Try Again.")
                continue
    elif a==2:
        while True:
            print("1.Login with Password")
            print("2.Register as New User")
            us = int(input("Enter your choice: "))
            if us==2:
                name = input("Enter your Username: ")
                passw = input("Enter your Password: ")
                cursor.execute("insert into users values('%s','%s')" %(name,passw))
                print("Registered Successfully!!!")
                continue
            elif us==1:
                cursor.execute("select * from users")
                user = cursor.fetchall()
                name1 = input("Enter you Username: ")
                passw1 = input("Enter your password: ")
               
                for o in user:
                   if (name1,passw1)==o:
                        print("Login Successfully")
                        print("1.Book Ticket")
                        print("2.Check PNR")
                        tk = int(input("Enter your Choice: "))
                        if tk==1:
                            abj = []
                            for j in range(1,73):
                                abj.append(j)
                            abj.reverse()
                            abk=abj
                        
                            
                            abo = []
                            for u in range(1,7):
                                abo.append(u)
                            abo.reverse()
                            abi=abo

                            aba = []
                            for e in range(1,5):
                                aba.append(e)
                            aba.reverse()
                            abii=aba

                            absl=[]
                            for t in range(1,11):
                                absl.append(t)
                            absl.reverse()
                            abss=absl

                            sa=[]
                            for c in range(1,49):
                                sa.append(c)
                            sa.reverse()
                            saa=sa

                            sh=[]
                            for q in range(1,25):
                                sh.append(q)
                            sh.reverse()
                            shh=sh

                            sl=[]
                            for y in range(1,81):
                                sl.append(y)
                            sl.reverse()
                            slll=sl
                            
                            

                            while True:
                                print("List of Trains is as follows:")
                                cursor.execute("select * from reserved")
                                r = cursor.fetchall()
                                for v in r:
                                    print(v, end="\n")
                                
                                tr = int(input("Enter Train no.: "))
                                if tr not in seat_count:
                                    seat_count[tr] = 0
                                cursor.execute("select * from reserved where train_no='%s' " %(tr,))
                                p = cursor.fetchall()
                                for h in p:
                                    print(h, end="\n")
                                nm = input("Enter name: ")
                                ag = int(input("Enter your Age: "))
                                fr = input("From: ")
                                to = input("To: ")
                                dt = input("Enter Date of Journey: ")
                                cl = input("Enter Travelling Class: ")
                                receiver_email = input("Enter your E-Mail ID: ")
                                pnr = random.randrange(2222222222,9999999999)
                                cursor.execute("select train_name from reserved where train_no='%s'" %(tr,))
                                tnn = cursor.fetchall()
                                print()
                                print()
                                print()
                                print()
                                print()
                                
                                
                                
                                print('''\t\t********************Ticket Details:********************''')
                                print("\t\tName: ",nm)
                                print("\t\tAge: ",ag)
                                print("\t\tTrain Number: ",tr)
                                print("\t\tTrain Name: ",tnn[0][0])
                                print("\t\tPNR Number: ", pnr)
                                print("\t\tReserved from:", fr)
                                print("\t\tReserved Upto: ", to)
                                print("\t\tDate of Journey: ",dt)
                                print("\t\tClass[3A/2A/1A/SL]: ", cl)
                                

                                file_name = 'Ticket.pdf'
                                doc = SimpleDocTemplate(file_name)
                                styles = getSampleStyleSheet()
                                content =[]
                                content.append(Paragraph("<b>Railway Ticket Details</b>", styles['Title']))
                                content.append(Spacer(1,12))
                                
                                if cl.lower()=="3a":
                                     coach = abi[0]
                               
                                     print("\t\tCoach No.: B",coach )
                                     seat = abk[seat_count[tr]]
                                     seat_count[tr] += 1

                                     print("\t\tSeat No.: ", seat)
                                     if seat in lower3:
                                         berth = "Lower berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in mid3: 
                                         berth = "Middle berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in upp3:
                                         berth = "Upper berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sidel3:
                                         berth = "Side Lower"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sideu3:
                                         berth = "Side Upper"
                                         print("\t\tBerth: ",berth)
                                     cursor.execute("update reserved set AC_3=AC_3 - 1 where train_no='%s' " %(tr,))
                                     cursor.execute("insert into chart values('%s','%s','%s','%s','%s')" %(pnr,nm,tr,seat,dt))
                                     qr_data = f"""
                                        PNR: {pnr}
                                        Name: {nm}
                                        Train: {tr}
                                        From: {fr}
                                        To: {to}
                                        Seat: {berth}
                                        Coach: B {coach}
                                        Seat No.: {seat}
                                        Date: {dt}"""
                                     qr_code = qr.QrCodeWidget(qr_data)
                                     bounds = qr_code.getBounds()
                                     width = bounds[2] - bounds[0]
                                     height = bounds[3] - bounds[1]

                                     size =120
                                     drawing = Drawing(size,size,transform=[size/width,0,0,size/height,0,0])
                                     drawing.add(qr_code)
                                                                        
                                            

                                    
                                     details = [
                                         f"Name: {nm}",
                                         f"Age: {ag}",
                                         f"Train Number: {tr}",
                                         f"Train Name: {tnn[0][0]}",
                                         f"PNR Number: {pnr}",
                                         f"From: {fr}",
                                         f"TO: {to}",
                                         f"Date Of Journey: {dt}",
                                         f"Class: {cl}",
                                         f"Coach No.: B {coach}",
                                         f"Seat No.: {seat}",
                                         f"Berth: {berth}"
                                     ]
                                     

                                     for d in details:
                                         content.append(Paragraph(d,styles['Normal']))
                                         content.append(Spacer(1,8))
                                     content.append(Spacer(1,10))
                                    
                                     content.append(drawing)
                                     doc.build(content)
                                     os.startfile(file_name)
                                     pdf_file = "Ticket.pdf"
                                     receiver = receiver_email
                                     send_ticket_email(pdf_file, receiver)


                                     
                                     
                                elif cl.lower()=="2a":
                                     coach = abii[0]

                               
                                     print("\t\tCoach No.: A", coach )
                                     
                                     seat = saa[seat_count[tr]]
                                     seat_count[tr] += 1
                                     print("\t\tSeat No.: ", seat)
                                     if seat in lower2:
                                        berth = "Lower berth"
                                        print("\t\tBerth: ",berth)
                                     elif seat in upp2:
                                         berth = "Upper berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sidel2:
                                         
                                         berth = "Side Lower"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sideu2:
                                         berth = "Side Upper"
                                         print("\t\tBerth: ",berth)
                                     cursor.execute("update reserved set AC_2=AC_2 - 1 where train_no='%s' " %(tr,))
                                     cursor.execute("insert into chart values('%s','%s','%s','%s','%s')" %(pnr,nm,tr,seat,dt))

                                     qr_data = f"""
                                        PNR: {pnr}
                                        Name: {nm}
                                        Train: {tr}
                                        From: {fr}
                                        To: {to}
                                        Seat: {berth}
                                        Coach: A {coach}
                                        Seat No.: {seat}
                                        Date: {dt}"""
                                     qr_code = qr.QrCodeWidget(qr_data)
                                     bounds = qr_code.getBounds()
                                     width = bounds[2] - bounds[0]
                                     height = bounds[3] - bounds[1]

                                     size =120
                                     drawing = Drawing(size,size,transform=[size/width,0,0,size/height,0,0])
                                     drawing.add(qr_code)
                                     

                                     details = [
                                         f"Name: {nm}",
                                         f"Age: {ag}",
                                         f"Train Number: {tr}",
                                         f"Train Name: {tnn[0][0]}",
                                         f"PNR Number: {pnr}",
                                         f"From: {fr}",
                                         f"TO: {to}",
                                         f"Date Of Journey: {dt}",
                                         f"Class: {cl}",
                                         f"Coach No.: A {coach}",
                                         f"Seat No.: {seat}",
                                         f"Berth: {berth}"
                                     ]

                                     for d in details:
                                         content.append(Paragraph(d,styles['Normal']))
                                         content.append(Spacer(1,8))
                                     content.append(Spacer(1,10))
                                     content.append(drawing)
                                     doc.build(content)
                                     os.startfile(file_name)
                                     pdf_file = "Ticket.pdf"
                                     receiver = receiver_email
                                     send_ticket_email(pdf_file, receiver)

                                elif cl.lower()=="1a":
                               
                                     print("\t\tCoach No.: H1" )
                                     
                                     seat = shh[seat_count[tr]]
                                     seat_count[tr] += 1
                                     print("\t\tSeat No.: ", seat)
                                     if seat in lower1:
                                         berth = "Lower berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in upp1:
                                         berth = "Upper berth"
                                         print("\t\tBerth: ",berth)
                                     cursor.execute("update reserved set AC_1=AC_1 - 1 where train_no='%s' " %(tr,))
                                     cursor.execute("insert into chart values('%s','%s','%s','%s','%s')" %(pnr,nm,tr,seat,dt))

                                     qr_data = f"""
                                        PNR: {pnr}
                                        Name: {nm}
                                        Train: {tr}
                                        From: {fr}
                                        To: {to}
                                        Seat: {berth}
                                        Coach: H1
                                        Seat No.: {seat}
                                        Date: {dt}"""
                                     qr_code = qr.QrCodeWidget(qr_data)
                                     bounds = qr_code.getBounds()
                                     width = bounds[2] - bounds[0]
                                     height = bounds[3] - bounds[1]

                                     size =120
                                     drawing = Drawing(size,size,transform=[size/width,0,0,size/height,0,0])
                                     drawing.add(qr_code)

                                     details = [
                                         f"Name: {nm}",
                                         f"Age: {ag}",
                                         f"Train Number: {tr}",
                                         f"Train Name: {tnn[0][0]}",
                                         f"PNR Number: {pnr}",
                                         f"From: {fr}",
                                         f"TO: {to}",
                                         f"Date Of Journey: {dt}",
                                         f"Class: {cl}",
                                         f"Coach No.: H 1",
                                         f"Seat No.: {seat}",
                                         f"Berth: {berth}"
                                     ]

                                     for d in details:
                                         content.append(Paragraph(d,styles['Normal']))
                                         content.append(Spacer(1,8))
                                     content.append(Spacer(1,10))
                                     content.append(drawing)
                                     doc.build(content)
                                     os.startfile(file_name)
                                     pdf_file = "Ticket.pdf"
                                     receiver = receiver_email
                                     send_ticket_email(pdf_file, receiver)


                                elif cl.lower()=="sl":
                                     coach = abss[0]
                               
                                     print("\t\tCoach No.: S", coach )
                                     seat = slll[seat_count[tr]]
                                     seat_count[tr] += 1
                                     
                                     print("\t\tSeat No.: ", seat)
                                     if seat in lower3:
                                         berth = "Lower berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in mid3: 
                                        berth = "Middle berth"
                                        print("\t\tBerth: ",berth)
                                     elif seat in upp3:
                                         berth = "Upper berth"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sidel3:
                                         berth = "Side Lower"
                                         print("\t\tBerth: ",berth)
                                     elif seat in sideu3:
                                         berth = "Side Upper"
                                         print("\t\tBerth: ",berth)

                                     cursor.execute("update reserved set SL=SL - 1 where train_no='%s' " %(tr,))
                                     cursor.execute("insert into chart values('%s','%s','%s','%s','%s')" %(pnr,nm,tr,seat,dt))

                                     qr_data = f"""
                                        PNR: {pnr}
                                        Name: {nm}
                                        Train: {tr}
                                        From: {fr}
                                        To: {to}
                                        Seat: {berth}
                                        Coach: B {coach}
                                        Seat No.: {seat}
                                        Date: {dt}"""
                                     qr_code = qr.QrCodeWidget(qr_data)
                                     bounds = qr_code.getBounds()
                                     width = bounds[2] - bounds[0]
                                     height = bounds[3] - bounds[1]

                                     size =120
                                     drawing = Drawing(size,size,transform=[size/width,0,0,size/height,0,0])
                                     drawing.add(qr_code)

                                     details = [
                                         f"Name: {nm}",
                                         f"Age: {ag}",
                                         f"Train Number: {tr}",
                                         f"Train Name: {tnn[0][0]}",
                                         f"PNR Number: {pnr}",
                                         f"From: {fr}",
                                         f"TO: {to}",
                                         f"Date Of Journey: {dt}",
                                         f"Class: {cl}",
                                         f"Coach No.: S {coach}",
                                         f"Seat No.: {seat}",
                                         f"Berth: {berth}"
                                     ]

                                     for d in details:
                                         content.append(Paragraph(d,styles['Normal']))
                                         content.append(Spacer(1,8))
                                     content.append(Spacer(1,10))
                                     content.append(drawing)
                                     doc.build(content)
                                     os.startfile(file_name)
                                     pdf_file = "Ticket.pdf"
                                     receiver = receiver_email
                                     send_ticket_email(pdf_file, receiver)

                                print()
                                print()
                                print()
                                z+=1
                                
                            
                                break
                        elif tk ==2:

                            chartout()
                             
                            
                        break
                   else:
                       
                        
                        continue
            break
    elif a==3:
        print("Program terminated successfully")
        break
mycon.commit()