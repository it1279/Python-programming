n=int(input("enter the number of employees:"))
employees={}
for i in range(n):
    name=input("enter the name of the employee:")
    emp_id=input("enter employee Id:")
    phno=int(input("enter the employee phn no:"))
    address=input("enter the employee address:")
    employees[name]=[emp_id,phno,address]
while True:
    name=input("enter employee name:")
    info=employees.get(name,-1)
    if info==-1:
        print("employee does not exist")
    else:
        print('employee details are:\n employee Id:',emp_id,'\n phone:',phno,'\n address:',address)
    exit_choice=input('do you want to exit[yes/no]:')
    if exit_choice=='yes' or exit_choice=='no':
        break
