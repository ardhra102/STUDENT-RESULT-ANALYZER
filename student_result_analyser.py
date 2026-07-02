#                             STUDENT RESULT ANALYSER

#add student
def add_std(details):
    l=[]
    s = input(f"Enter student ID:")
    details[s]={}
    for i,j in details["STD001"].items():
            if i=="Mark":
                    print("Enter marks out of 100")
                    m1 = int(input("Enter the mark of Maths:"))
                    m2 = int(input("Enter the mark of Hindi:"))
                    m3 = int(input("Enter the mark of English:"))
                    m4 = int(input("Enter the mark of Science:"))
                    m5 = int(input("Enter the mark of Social:"))
                    l.extend([m1,m2,m3,m4,m5])
                    details[s][i]=l

            elif i=="Name":
                    n=input(f"Enter {i} of the student:")
                    details[s][i]=n

            elif i=="Place":
                    n=input(f"Enter {i} of the student:")
                    details[s][i]=n
            elif i=="Total":
                    details[s][i]=sum(details[s]["Mark"])

            else:
                    num=int(input(f"Enter {i} of the student:"))
                    details[s][i]=num


    return details[s]


#delete student
def delete(details):
    d=input("Enter ID of the student:")
    if d in details:
        name=details[d]["Name"]
        details.pop(d)
        return d,name

    else:
        return None,None

#update student
def update_std(details,s):
    m=input("Enter ID of Student to Update:")
    if m in details:
        if s=="Name":
            l=input("Enter new Name:")
            details[m][s]=l
        elif s=="Age":
            l=input("Enter new Age:")
            details[m][s]=l
        elif s=="Mark":
            print("Enter new Mark:")
            j = 0
            for i in details[m][s]:
                l=["Maths","Hindi","English","Science","Social"]
                h=int(input(f"{l[j]}:"))
                details[m]["Mark"][j]=h
                j += 1
            details[m]["Total"] = sum(details[m]["Mark"])
        elif s=="Place":
            l = input("Enter new Place:")
            details[m][s] = l
        return f"\nUpdated Successfully....\n"
    else:
        return None



def search_std(details):
    ids=input("Enter the ID of the student:")
    for i in details:
        if i==ids:
            return details[i]
    else:
        return None



#calculate grade
def cal_grade(details):
    s=""
    for k,v in details.items():
            per=(v["Total"]/500)*100
            if per>=90:
                grade="A+"
                s += f"{k}-{grade}\n"
            elif per>=80 and per<90:
                grade="A"
                s += f"{k}-{grade}\n"
            elif per>=70 and per<80:
                grade="B"
                s += f"{k}-{grade}\n"
            elif per<70 and per>=60:
                grade="C"
                s += f"{k}-{grade}\n"
            elif per<60 and per>=50:
                grade="D"
                s += f"{k}-{grade}\n"
            else:
                grade="E (FAIL)"
                s += f"{k}-{grade}\n"

    return s


#topper
def topper(details):
    high=0
    m=0
    top=""
    for k,v in details.items():
                if v["Total"] > high:
                    high=v["Total"]
                    top=details[k]["Name"]
                    m=details[k]["Total"]
    return f"Topper is: {top}\nTotal    :{m}"


#low mark
def lower(details):
    low=500
    lowest=0
    for k,v in details.items():
                if v["Total"] < low:
                    low=v["Total"]
                    lowest=details[k]
    return lowest


#class average
def cls_avg(details):
    avg=0
    subjects=0
    for k,v in details.items():
            tot=sum(v["Mark"])
            subjects=len(v["Mark"])
            details[k]["Total"]=tot
            avg += tot
    average= avg/(len(details)*subjects)
    return round(average)


#pass fail count
def pass_fail(details):
    p_l=[]
    f_l=[]
    pass_count=0
    fail_count=0
    for k,v in details.items():
        for i in v["Mark"]:
            if i<50:
                fail_count+=1
                f_l.append(v["Name"])
                break
        else:
            pass_count+=1
            p_l.append(v["Name"])
    return pass_count,fail_count,p_l,f_l #f"Passed:{pass_count}\nStudents Passed:{p_l}\nFailed:{fail_count}\nStudents Failed:{f_l}"


print("="*80)
print(" "*25,"STUDENT RESULT ANALYSER"," "*25)
print("="*80)
# print()
print(" "*25,"STUDENT MANAGEMENT"," "*25)
print("-"*80)
print("1. Add Student\n2. Delete Student\n3. Update Student\n4. View All Students\n5. Search Student\n")
print(" "*25,"RESULT ANALYSIS"," "*25)
print("-"*80)
print("6. Calculate Grade\n7. Class Topper\n8. Lowest Scorer\n9. Class Average\n10. Pass / Fail Report\n0. Exit")
print("="*80)

dicts = {
         "STD001": {
        "Name": "Rahul",
        "Age": 14,
        "Place": "Palakkad",
        "Mark": [78, 85, 69, 91, 80],
        "Total": 403
    },

    "STD002": {
        "Name": "Arya",
        "Age": 14,
        "Place": "Kottayam",
        "Mark": [65, 72, 81, 77, 70],
        "Total": 365
    },

    "STD003": {
        "Name": "Anjali",
        "Age": 15,
        "Place": "Thrissur",
        "Mark": [95, 90, 96, 92, 94],
        "Total": 467
    },

    "STD004": {
        "Name": "Adithya",
        "Age": 14,
        "Place": "Ernakulam",
        "Mark": [40, 55, 60, 48, 52],
        "Total": 255
    },

    "STD005": {
        "Name": "Meera",
        "Age": 15,
        "Place": "Kozhikode",
        "Mark": [88, 84, 79, 91, 86],
        "Total": 428
    },

    "STD006": {
        "Name": "Nikhil",
        "Age": 14,
        "Place": "Malappuram",
        "Mark": [30, 45, 50, 28, 60],
        "Total": 213
    },

    "STD007": {
        "Name": "Sneha",
        "Age": 15,
        "Place": "Kannur",
        "Mark": [70, 75, 68, 80, 74],
        "Total": 367
    }
}

while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        print(f"\n-----ADDING STUDENT DETAILS-----\n")
        value=add_std(dicts)

        print("\nStudent Details Added!!\n")
        print("Name      :",value["Name"])
        print("Age       :",value["Age"])
        print("\nMarks:\n---------")
        print("Maths     :",value["Mark"][0])
        print("Hindi     :",value["Mark"][1])
        print("English   :",value["Mark"][2])
        print("Science   :",value["Mark"][3])
        print("Social    :",value["Mark"][4])
        print()
        print("Total     :",value["Total"])
        print("Place     :",value["Place"])
        print()
    elif ch==2:
        print(f"\n-----DELETE A STUDENT-----\n")
        d,name=delete(dicts)
        if d is None:
            print("Student doesn't exist.\n")
        else:
            print(f"\nID    :{d}")
            print(f"Name  :{name}")
            print("Student Deleted Successfully....")
            print()

    elif ch==3:
        print(f"\n-----UPDATE STUDENT-----\n")
        print(f"1. Update Name\n2. Update Age\n3. Update Marks\n4. Update Place\n")
        n=int(input("Enter a option:"))
        if n==1:
            s="Name"
            data=update_std(dicts,s)
            if data is None:
                print("\nDoesn't Exist\n")
            else:
                print(data)
        elif n==2:
            s="Age"
            data = update_std(dicts, s)
            if data is None:
                print("\nDoesn't Exist\n")
            else:
                print(data)
        elif n==3:
            s = "Mark"
            data = update_std(dicts, s)
            if data is None:
                print("\nDoesn't Exist\n")
            else:
                print(data)
        elif n==4:
            s = "Place"
            data = update_std(dicts, s)
            if data is None:
                print("\nDoesn't Exist\n")
            else:
                print(data)

    elif ch==4:
        print(f"\n-----STUDENT DETAILS-----\n")

        for k,v in dicts.items():
            value=dicts[k]
            print("ID        :",k)
            print("Name      :", value["Name"])
            print("Age       :", value["Age"])
            print("\nMarks:\n")
            print("Maths     :", value["Mark"][0])
            print("Hindi     :", value["Mark"][1])
            print("English   :", value["Mark"][2])
            print("Science   :", value["Mark"][3])
            print("Social    :", value["Mark"][4])
            print()
            print("Total     :", value["Total"])
            print("Place     :", value["Place"])
            print("-"*20)
        print()
    elif ch==5:
        print(f"\n-----STUDENT SEARCH-----\n")

        value=search_std(dicts)
        if value is None:
            print("Invalid ID.\n")
        else:
            print()
            print("Name      :", value["Name"])
            print("Age       :", value["Age"])
            print("\nMarks:\n---------")
            print("Maths     :", value["Mark"][0])
            print("Hindi     :", value["Mark"][1])
            print("English   :", value["Mark"][2])
            print("Science   :", value["Mark"][3])
            print("Social    :", value["Mark"][4])
            print()
            print("Total     :", value["Total"])
            print("Place     :", value["Place"])

            print()
    elif ch==6:
        print(f"\n-----STUDENT GRADE-----\n")
        print(cal_grade(dicts))

    elif ch==7:
        print(f"\n-----CLASS TOPPER-----\n")
        print(topper(dicts))
        print()
    elif ch==8:
        print(f"\n-----LOWEST SCORER-----\n")
        v=lower(dicts)
        print("Name      :", v["Name"])
        print("Total     :", v["Total"])
        print()
    elif ch==9:
        print(f"\n-----CLASS AVERAGE-----")
        print(cls_avg(dicts))
        print()
    elif ch==10:
        print(f"\n-----PASS/FAIL COUNT-----")
        pass_count,fail_count,p_l,f_l =pass_fail(dicts)
        print(f"Passed     : {pass_count}\nPassed Students:")
        for i in p_l:
            print(i)
        print(f"\nFailed    : {fail_count}\nFailed Students:")
        for i in f_l:
            print(i)
        print()

    elif ch==0:
        print("-"*80)
        print(" "*25,"Thank you for using\n"," "*22,"STUDENT RESULT ANALYZER"," "*25)
        break
    else:
        print("Invalid choice\n")












