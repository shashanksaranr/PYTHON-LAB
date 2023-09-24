class Employee:
    def __init__(self,name,emp_id,department,salary):
        self.name=name
        self.emp_id=emp_id
        self.department=department
        self.salary=salary

    def update_salary(self,department,new_salary):
        if self.department==department:
            self.salary=new_salary

employee_list=[Employee("Bob",1,"Sales",50000),
               Employee("Mikey",2,"HR",60000),
               Employee("Nike",3,"Sales",55000),
               Employee("David",4,"IT",65000),
               Employee("Hasbullah",5,"IT",70000)]

for employee in employee_list:
    print(f"{employee.name} ({employee.emp_id}) works in {employee.department} and earns {employee.salary} per year.")

for employee in employee_list:
    employee.update_salary("Sales",66000)

print("\n After Salary Update:")
for employee in employee_list:
    print(f"{employee.name} ({employee.emp_id}) works in {employee.department} and earns {employee.salary} per year.")