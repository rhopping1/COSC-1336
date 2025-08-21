#Rachel Hopping
#Complete
#Create 3 instances of Employee class
#Get information from the user then display for the 3 individuals

import employee

def main():

    employee_list = []

    #For 3 employees
    for count in range(1,4):
        #Get employee data
        print(f'Employee {count}:')
        empl_name = input('Enter the employee\'s name: ')
        empl_id = int(input('Enter the employee\'s ID number: '))
        empl_dept = input('Enter the employee\'s department: ')
        empl_title = input('Enter the employee\'s job title: ')

        #Create new Employee object 
        person = employee.Employee(empl_name, empl_id, empl_dept, empl_title)

        #Add to employee list
        employee_list.append(person)


    #Display the employees' info
    print('Here are the three employees\' information entered: ')
    for person in employee_list:
        print(f'Name: {person.get_name()}')
        print(f'ID Number: {person.get_id_num()}')
        print(f'Department: {person.get_dept()}')
        print(f'Title: {person.get_job_title()}')
        print()

main()
