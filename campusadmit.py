import time
import random
import mysql.connector as mycon
import csv
from datetime import date
import re
from tabulate import tabulate
import pandas as pd

con = mycon.connect(host="localhost", user="root", password="IamGroot3007#", database="projects")
cursor = con.cursor()

cursor.execute("SELECT * FROM accounts")
accounts = cursor.fetchall() 

global stud
#noglobal date
global today
global stud_count

def create_id():
    cursor.execute("SELECT * FROM accounts")
    accounts1 = cursor.fetchall()
    if(accounts1==[]):
        stud_count=0
        timestamp = int(time.time() * 1000)
        counter = random.randint(0, 999)
        unique_id = f"{timestamp:013d}{counter:03d}"
        stud = int(unique_id)
        return stud
    else:
        stud=accounts1[-1][0]
        #stud_count=1
        return stud+1

def create_account():
    #stud_count=0
    i=create_id()
    username = input("\tEnter the username: ")
    password = input("\tEnter a strong password: ")
    s_id = i
    acc_query = "INSERT INTO accounts (id, username, password) VALUES ({}, '{}', '{}')".format(s_id,username,password)
    cursor.execute(acc_query)
    con.commit()
    #stud_count += 1
    print("\tAccount created")
    print("Your ID is:", s_id)

def find_college():
    answer = "yes"
    while answer.lower() == "yes":
        print("\t____________________________________________________________________________")
        print("\tEnter 1 to search by fee range")
        print("\tEnter 2 to search by cutoff range")
        print("\tEnter 3 to search by field")
        print("\tEnter 4 to search by college ID")
        print("\t____________________________________________________________________________")
        choice = int(input("\tEnter your choice: "))
        if choice == 1:
            amt = int(input("\tEnter your maximum fee range: "))
            query = f"SELECT * FROM colleges WHERE fee <= {amt}"
            cursor.execute(query)
            colleges=cursor.fetchall()
            print("\t__________________________________HERE ARE THE LIST OF COLLEGES___________________________")
            '''college_dict = {'COLLEGE ID': [clgs[0] for clgs in colleges],'COLLEGE NAME': [clgs[1] for clgs in colleges],'FEE': [clgs[5] for clgs in colleges]}
            df = pd.DataFrame(college_dict)
            print(df)'''
            print(f"{'COLLEGE ID':<20}{'COLLEGE NAME':<60}{'FEE':<15}")
            for clgs in colleges:
                    print(f"{clgs[0]:<20}{clgs[1]:<60}{clgs[5]:<15}")
        
        elif choice == 2:
            cutoff = int(input("\tEnter your cut off: "))
            print(f"{'COLLEGE ID':<20}{'COLLEGE NAME':<60}{'cutoff':<15}")
            query = f"SELECT * FROM colleges WHERE cutoff <= {cutoff}"
            cursor.execute(query)
            colleges=cursor.fetchall()
            for clgs in colleges:
                    print(f"{clgs[0]:<20}{clgs[1]:<60}{clgs[4]:<15}")
        elif choice == 4:
            clg_id = int(input("\tEnter college ID: "))
            query=f"SELECT * FROM colleges WHERE clg_id = {clg_id}"
            cursor.execute(query)
            colleges = cursor.fetchone()
            print(f"{'COLLEGE ID':<20}{'COLLEGE NAME':<30}{'field':<20}{'location':<20}{'cutoff':<15}{'fee':<10}")
            for i in colleges:
                print(i,end="\t"*2)
            print()
        else:
            field = int(input("\tEnter field of study:\n1. Engineering and Technology\n2. Medical\n3. Arts and Science\nYour choice:"))
            if field==3:
                cursor.execute("SELECT * FROM colleges WHERE field = 'arts and science'")
                colleges = cursor.fetchall()
                headers = ["collegeID"+("\t"*2), "college Name"+("\t"*5),"Field"+("\t"),"Location"+("\t"*2),"cutoff"+("\t"),"fee"+("\t")]
                for head in headers:
                    print(head,end="")
                print()
                col_widths = [max(len(str(item)) for item in column) for column in zip(*colleges)]
                for row in colleges:
                    print(" | "+"\t".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

            elif field==2:
                cursor.execute("SELECT * FROM colleges WHERE field = 'Medical'")
                colleges = cursor.fetchall()
                headers = ["collegeID"+("\t"*2), "college Name"+("\t"*2),"Field"+("\t"),"Location"+("\t"*2),"cutoff"+("\t"),"fee"+("\t")]
                for head in headers:
                    print(head,end="")
                print()
                col_widths = [max(len(str(item)) for item in column) for column in zip(*colleges)]
                for row in colleges:
                    print(" | "+"\t".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))
            else:
                cursor.execute("SELECT * FROM colleges WHERE field = 'engineering and technology'")
                colleges = cursor.fetchall()
                headers = ["collegeID"+("\t"*2), "college Name"+("\t"*5),"Field"+("\t"*2),"Location"+("\t"*2),"cutoff"+("\t"),"fee"+("\t")]
                for head in headers:
                    print(head,end="")
                print()
                col_widths = [max(len(str(item)) for item in column) for column in zip(*colleges)]
                for row in colleges:
                    print(" | "+"\t".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

        answer = input("Do you want to continue searching? ")

def is_valid_email(email):
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def is_valid_contact(contact):
    # Regular expression for contact number validation
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, contact))

def findname(colleges, clg_id):
    while True:
        for codes in colleges:
            if codes[0] == clg_id:
                return codes[1]
        
        print("Invalid college id. Please try again.")
        clg_id = input("Enter college id: ")

            
def apply_admission():
    query = "select * from colleges"
    cursor.execute(query)
    colleges = cursor.fetchall()
    
    cursor.execute("SELECT * FROM accounts")
    accnt = cursor.fetchall()
    
    print("\t______________________________________Application____________________________________")
    
    std_id = int(input("\tEnter the student id: "))
    found = False
    for user in accnt:
        if user[0] == std_id:
            print(user)
            found = True
            acc = user
            break
    if found:
        password = input("\tEnter your password: ")
        if password != acc[2]:
            print("\tIncorrect password. Please try again.")
            return

        while True:
            clg_id = int(input("\tEnter college id: "))
            cname = findname(colleges, clg_id)
            name = input("\tEnter your name: ")
            clg_name = cname
            email = input("\tEnter your email id: ")
            if not is_valid_email(email):
                print("\tInvalid email address. Please try again.")
                continue

            contact = input("\tEnter your contact no: ")
            if not is_valid_contact(contact):
                print("\tInvalid contact number. Please try again.")
                continue
            break
        m_name = input("\tEnter Mother's name: ")
        f_name = input("\tEnter father's name: ")
        add = input("\tEnter address: ")
        print("\t_______________choose your course________________________")
        see_courses()
        major =input("Enter course name:")
        today = date.today()
        duration = int(input("\tEnter course duration: "))
        l=[std_id,name,clg_id,cname,m_name,f_name,add,major,today,duration,email,contact]
        detquery = "insert into student_details values({},'{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{})".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11])
        cursor.execute(detquery)
        con.commit()
        print("\t________________________________HERE IS YOUR APPLICATION FORM_______________________________")
        
        query = "select * from student_details where std_id = {}".format(std_id)
        cursor.execute(query)
        details = cursor.fetchall()
        for i in details:
            print(f"Student ID: {i[0]}\nName: {i[1]}\nCollege ID: {i[2]}\nCollege Name: {i[3]}\nMother's Name: {i[4]}\nFather's Name: {i[5]}\nAddress: {i[6]}\nMajor: {i[7]}\nDate of Admission: {i[8]}\nCourse Duration: {i[9]}\nEmail: {i[10]}\nContact: {i[11]}")
        print("successfully applied for", i[3])
    else:
        print("\tAccount not found. Please create a new account.")

def check_eligibility():
    clg_file = open("C:/Users/Vishwaridha/Downloads/Colleges_Dataset.csv", "r")
    colleges = list(csv.reader(clg_file))

    mat = int(input("\tEnter your math score: "))
    phy = int(input("\tEnter your physics score: "))
    chem = int(input("\tEnter your chemistry score: "))
    marks = mat + (phy / 2) + (chem / 2)
    cut_off = round(marks, 2)
    print("\tYour cutoff:",cut_off)

    found = False
    while not found:
        college_id = int(input("\tEnter the college id: "))
        for clg in colleges:
            if int(clg[0]) == college_id:
                coll = clg
                found = True
                break
        if not found:
            print("\tCollege ID not found. Please try again.")

    if cut_off >= float(coll[4]):
        print(f"Eligible for {coll[0]} {coll[1]}")
    else:
        print("Not Eligible for",coll[1])
        
def see_courses():
    f=open("C:/Users/Vishwaridha/Downloads/Courses_Dataset.csv","r")
    course=csv.reader(f)
    c=0
    for crs in course:
        print(c,end="\t")
        print(crs[0],crs[1],sep="\t"*2)
        c+=1
            
def get_details(scholarships, answer):
    for scls in scholarships:
        if scls[0].lower() == answer.lower():
            print("_____________________" + scls[0] + "_______________________")
            print("Scholarship Amount: ", scls[1])
            print("Scholarship Details: ", scls[2])
            print("link: ", scls[3])
            print("______________________________________________________")

def get_scholarship():
    with open("C:/Users/Vishwaridha/Downloads/scholorships.csv", "r") as sclr_file:
        scholarships = list(csv.reader(sclr_file))
        
        amount = int(input("\tEnter scholarship amount: "))
        
        found = False
        print("\n\tScholarships matching the amount:")
        print("\t______________________HERE ARE THE LIST OF SCHOLORSHIPS AVAILABLE_______________________ ")
        c=1
        for scholarship in scholarships:
            if float(scholarship[1]) >= amount: 
                found = True
                print("\t"*3)
                print(c,scholarship[0],sep="\t"*2)
                c+=1
        if not found:
            print("\tNo scholarships found for the specified amount.")
        print("\t_______________________________________________________________")
        y = input("\tDo you want to check details of scholarship? ")
        if y.lower() == "yes":
            answer = input("\tEnter scholarship name to see details: ")
            get_details(scholarships, answer)


def check_account():
    answer = input("Do you have an account? (yes/no): ")
    if answer.lower() == "yes":
        found = False
        u_name = input("\tEnter your username: ")
        for user in accounts:
            if user[1] == u_name:
                found = True
                acc = user
                break
        if found:
            password = input("\tEnter your password: ")
            while password != acc[2]:
                print("\tIncorrect password. Please try again.")
                password = input("Enter your password: ")
            print("\tAuthentication successful. Welcome back!")
            return True
        else:
            print("\tAccount not found. Please create a new account or create new account")
            check_account()
    elif answer.lower()=="no":
        print("Lets create an account")
        create_account()
        return True
    else:
        print("enter valid choice")
        check_account()
        return True

print("\t________________________Welcome to Campus Admit_________________________")
created=False  
created=check_account()
choice = 1
#print(created)
if created:
    while (choice != 0 and created==True):
        print("\t_________________________________________________________________________________________")
        print("\tEnter 1 to create a student account")
        print("\tEnter 2 to find colleges")
        print("\tEnter 3 to apply for admission")
        print("\tEnter 4 to check eligibility")
        print("\tEnter 5 to see scholorship details")
        print("\tEnter 6 to see list of courses")
        print("\tEnter 0 to EXIT")
        print("\t_________________________________________________________________________________________")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            find_college()
        elif choice == 3:
            apply_admission()
        elif choice == 4:
            check_eligibility()
        elif choice == 5: 
            get_scholarship()
        elif choice==6:
            loc=see_courses()
        elif choice == 0:
            print("\t______________________Thanks for using Campus Admit. Goodbye_________________________________")
            break
        else:
            print("\tInvalid choice. Please select a valid option.")
