class Employee(object):
    """
    base class for all employees
    """

    empCount = 0

    def __init__(self, name, salary):
        """
        Constructor method
        :param name: name of the employee
        :param salary: salary of the employee
        """

        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_employee(self):
        """
        Displays the information of Employee
        """
        print(f'name of the employee is {self.name} and age of employee is {self.age}')

    def display_emplaoyee_count(self):
        """
        Displays total number of employees
        :return:
        """
        print(f'number of employees are {Employee.empCount}')


if __name__ == '__main__':
    print(Employee.__doc__)
    e1 = Employee('Aman', 2000)
    e2 = Employee('Pankaj', 4000)

    print(e1.name,e1.salary)
    print(e2.name, e2.salary)
    print(Employee.empCount)
    Employee.empCount =100
    print(e2.empCount)
    print(e1.empCount)


    # getattr, hasttr, setattr, delattr

    print('e1 has name : ', hasattr(e1, 'name'))
    print('e1  has age : ', hasattr(e1, 'age'))
    print('name in e1', getattr(e1, 'name'))
    print('deleting e1.name', delattr(e1, 'name'))
    e1.name = 'Kamal'
    print('name in e1: ', e1.name)
    setattr(e1, 'name', 'aman again')
    print('name in e1 :', getattr(e1, 'name'))

    # buit in class attributes
    # __doc__
    # __name__
    # __dict__ (dictionary containing class namespace)
    # __module__ (module name in which class is defined)
#   __ bases__ base classes

    print('############ built in attributes ###########')
    print(Employee.__doc__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__bases__)
    print(Employee.__dict__)

