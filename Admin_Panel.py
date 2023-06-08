#implement complete functionality
import random
import json
class Admin_Panel:
    student_list=[]
    def __init__(self):
        self.module_details={}
        self.trainer_details={}
        self.batch_details={}
        self.student_details={}

    def admin_login(self,username,password):
        if username=="admin" and password=="admin":
            return True
        else:
            return False
    
    def add_module(self,module_name,duration):
        self.module_name=module_name
        self.duration=duration

        Topic_list=[]
        key=random.randint(1,100)
        topic_size=int(input("Enter How Many Topics You Want To Add"))
        for i in range (1,topic_size+1):
            topic =input(f"Enter Topic Name {i} :")
            Topic_list.append(topic)

        module_data={"Module Name":module_name,"Duration":duration,"Topics":Topic_list}
        print(module_data)
        self.module_details[int(key)]=module_data
        #store in json
        with open("add_module.json","w")as f:
            json.dump(self.module_details,f,indent=4)
        return self.module_details
    
    def add_trainer(self):
        trainer_id=random.randint(1,100)
        name=input("Enter Trainer Name : ")
        gender=input("Enter Trainer Gender")
        mobile_no=int(input("Enter Trainer Mobile Number :"))
        qualification=input("Enter Trainer Qualification")
        emailid=input("Enter Trainer Email Id :")
        password=input("Enter Password :")

        trainer_data={"Name":name,"Gender":gender,"Mobile Number":mobile_no,"Qualification":qualification,
                      "Email ID":emailid,}
        self.trainer_details[trainer_id]=trainer_data
        print("Data Added Successfully...")

         #store in json
        with open("add_trainer.json","w")as f:
            json.dump(self.trainer_details,f,indent=4)
        return self.trainer_details
    
    def add_batch(self,modules,trainers,student):
        key=random.randint(1,100)
        batch_data={"Module":modules,"Trainers":trainers,"Student":student}

        self.batch_details[key]=batch_data

         #store in json
        with open("add_batch.json","w")as f:
            json.dump(self.batch_details,f,indent=4)
        return self.batch_details
    
    def add_student(self):
        student_list=[]
        batch={}
        student_size=int(input("Enter number of Student want to add :"))
        for i in range(1,student_size+1):
            student_id=random.randint(1,100)
            name=input("Enter Student Name : ")
            gender=input("Enter Student Gender")
            mobile_no=int(input("Enter Student Mobile Number :"))
            qualification=input("Enter Student Qualification")
            emailid=input("Enter Student Email Id :")
            password=input("Enter Password :")

            student_data={"Name":name,"Gender":gender,"Mobile Number":mobile_no,"Qualification":qualification,
                      "Email ID":emailid,}  
            Admin_Panel.student_list.append(student_data)
        self.student_details[student_id]=Admin_Panel.student_list
    
    #store in json
        with open("add_student.json","w")as f:
            json.dump(self.student_details,f,indent=4)
        return self.student_details
    
    def remove_module(self):
        #before remove print all module
        with open("add_module.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f"Module_ID:{k}   Data:{v}")
        module_key=str(input("Enter Module Id Which You Want To Delete"))
        del content1[module_key]
        print("Module Has been Deleted")

        for k,v in content1.items():
            print(f"Module_ID:{k}   Data:{v}")

        with open("add_module.json","w")as f:
            json.dump(content1,f,indent=4)

    def update_trainer(self):
        #before update print all trainer
        with open("add_trainer.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f,"Trainer_ID:{k},   Data:{v}")
        trainer_id=str(input("Enter Trainer Id You Want to Update :"))
        trainer_edit=input("Enter Field You Want To Update")
        trainer_updated_value=input("Enter Updated Value :")
        content1[trainer_id][trainer_edit]=trainer_updated_value
        print("Trainer Details are Updated...")

        for k,v in content1.items():
            print(f"Trainer_ID:{k}   Data:{v}")
        
        #need to update data in json
        with open("add_trainer.json","w")as f:
            json.dump(content1,f,indent=4)

    def get_student_details(self):
        with open("add_student.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f,"Student_ID:{k},   Data:{v}")
            print("\n")
    
    def get_trainer_details(self):
        with open("add_trainer.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f,"Trainer ID:{k}     Data:{v}")
            print("\n")
    
    def get_batch_details(self):
        with open("add_batch.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f,"Batch ID :{k}     Data:{v}")
            print("\n")


#a=Admin_Panel()
#a.add_batch()
#a.add_module("AAA","8 week")
#a.add_module("ABC","8 week")
#a.get_student_details()
#a.get_trainer_details()