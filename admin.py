class Student:

    def __init__(self,name, pname, studentid, aadhar, phoneno, Class, section):
        self.name =  input("Enter your Student Name ")
        self.pname = input("Enter your Parent Name ")
        self.studentid = input("Enter your Student Id ")
        self.aadhar = input("Enter your Aadhar no ")
        self.phoneno = input("Enter your Phone no ")
        self.Class = input("Enter your Class ")
        self.section = input("Enter your Section ")
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

 #Add Function

    def accept(self,name, pname, studentid, aadhar, phoneno, Class, section):
        ob = Student(name, pname, studentid, aadhar, phoneno, Class, section)
        ls.append(ob)


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#View Function

    def display(self,ob):
        print("name : ", ob.name)
        print("pname : ", ob.pname)
        print("studentid : ", ob.studentid)
        print("aadhar : ", ob.aadhar)
        print("phoneno : ", ob.phoneno)
        print("Class : ", ob.Class)
        print("section : ", ob.section)
        print("\n")


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# Delete Function

    def delete(self, si):
        del ls[si]


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# Update Function

    def update(self, si, No):
        studentid = ls[No].Class
        ls[si].Class =  studentid


ls = []
obj = Student('','', 0, 0 ,0, 0,'')
ls.append(obj)
obj = Student('','', 0, 0 ,0, 0,'')
ls.append(obj)
obj = Student('','', 0, 0 ,0, 0,'')
ls.append(obj)


print("\n")
print("\n List of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

obj.update(1, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])

obj.delete(1)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
