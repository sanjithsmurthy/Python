class employee:

    def __init__(self):
        self.name = input("Enter Name: ")
        self.emp_id = int(input("Enter Employee ID: "))
        self.dept = input("Enter Department: ")
        self.salary = float(input("Enter Salary: "))
    def display(self):
        print("Name: {0}\t | Employee ID: {1}\t | Department: {2}\t | Salary: {3}".format(self.name,self.emp_id,self.dept,self.salary))

    def update_salary(self,deapartment,new_salary):
            if self.dept == department:
                self.salary = new_salary

n=int(input("Enter number of employess: "))
e=[]
for i in range(0,n):
    e.append(employee())
for obj in e:
    obj.display()
department = input("\nEnter department: ")
new_salary = float(input("Enter new salary: "))
for obj in e:
    obj.update_salary(department,new_salary)
print("New Updated Salary:")
for obj in e:
    obj.display()