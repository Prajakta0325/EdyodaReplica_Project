from Admin_Panel import *
import sys
admin=Admin_Panel()
while True:
    print("Press 1--For Admin Login")
    print("Press 2--For Student Login")
    print("Press 3--For Trainer Login")
    print("Press 4--For Exit")
    choice=int(input("Enter Your Choice :"))

    if choice==1:
        print("*"*100)
        username=input("Enter Username")
        password=input("Enter Password")
        temp=admin.admin_login(username,password)
        if temp:
            print("**********************Welcom To Admin Module*************************8")
            print("Press 1-- For Add Module")
            print("Press 2-- For Add Trainer")
            print("Press 3-- For Add Student")
            print("Press 4-- For Add Batch")
            print("Press 5-- For Remove Module")
            print("Press 6-- For Update Trainer")
            print("Press 7-- For Get Student Details")
            print("Press 8-- For Get Trainer Details")
            print("Press 9-- For Get Batch Details")
            opt=int(input("Enter Your Choice : "))
            
            if opt==1:
                print("*"*50)
                module_name=input("Enter Module Name : ")
                duration=input("Enter Module Duration :")
                admin.add_module(module_name,duration)

            elif opt==2:
                print("*"*50)
                admin.add_trainer()
            elif opt==3:
               print("*"*50)
               admin.add_student()
            elif opt==4:
                print("*"*50)
                modules=input("Enter Module Name: ")
                trainers=input("Enter Trainer Name :")
                student=input("Enter Student Name: ")
                admin.add_batch(modules,trainers,student)
            elif opt==5:
                print("*"*50)
                admin.remove_module()
            elif opt==6:
                print("*"*50)
                admin.update_trainer()
            elif opt==7:
                admin.get_student_details()
                print("*"*50)
            elif opt==8:
                admin.get_trainer_details()
                print("*"*50)
            elif opt==9:
                 admin.get_batch_details()
                 print("*"*50)
            else:
                print("Please Enter Correct Choice")
        else:
          print("Incorrect Username and Password")

    elif choice==2:
        print("**********************Welcom To Student Panel*************************")
        print("Press 1-- For Get Student Details")
        print("Press 2-- For Get Trainer Details")
        print("Press 3-- For Get Batch Details")
        opt=int(input("Enter Your Choice : "))

        if opt==1:
            admin.get_student_details()
            print("*"*50)
        elif opt==2:
            admin.get_trainer_details()
            print("*"*50)
        elif opt==3:
            admin.get_batch_details()
            print("*"*50)
        else:
            print("Please Enter Correct Choice")

    elif choice==3:
        print("**********************Welcom To Trainer Panel*************************")
        print("Press 1-- For Get Student Details")
        print("Press 2-- For Get Trainer Details")
        print("Press 3-- For Update Trainer")
        print("Press 4-- For Get Batch Details")
        opt=int(input("Enter Your Choice : "))

        if opt==1:
            admin.get_student_details()
            print("*"*50)
        elif opt==2:
            admin.get_trainer_details()
            print("*"*50)
        elif opt==3:
            admin.update_trainer()
            print("*"*50)
        elif opt==4:
            admin.get_batch_details()
            print("*"*50)
        else:
            print("Please Enter Correct Choice")

    elif choice==4:
        sys.exit
        print("Thankyou for Visiting....")
        break