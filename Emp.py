class Employee(object):
    """
    base class for all employees
    """

    Empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.Empcount +=1

    def display_count(self):
        print("the number of employees is ",Employee.Empcount)

    def display_employee(self):
        print('the name of employee is {}, and the salary is {}'.format(self.name, self.salary))


print(Employee.Empcount)
emp1 = Employee('Aman', 54)
print(Employee.Empcount)
emp2 = Employee('Pankaj', 58)
print(Employee.Empcount)

emp1.display_count()
emp2.display_employee()
print(emp2.Empcount)
print(emp1.Empcount)

print('######################')
print (Employee.__doc__)

print(Employee.__getattribute__(emp1, 'name'))
print(getattr(emp2,'name'))
print(hasattr(emp2,'salary'))
print(emp2.salary)
setattr(emp2,'salary',30)
print(emp2.salary)
emp2.salary =58
print(emp2.salary)

print('##########')
print('testing del attr')
delattr(emp2,'name')
print(hasattr(emp2, 'name'))
emp2.name = 'kamal'
print(hasattr(emp2, 'name'))
print(emp2.name)

print('#####################')
print('checking buitin attributes')

print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)


print('#################### Destroying Objects #####################')
print(emp2.name)
del emp2
#print(emp2.name)

print('################ data hiding ###########################')


class JustCounter(object):
    __s = 0

    def __init__(self):
        self.__s += 1
        print('inside init',self.__s)

    def disp(self):
        print(self.__s)


j1 = JustCounter()
j1.disp()
j2 = JustCounter()
j2.disp()

print(j2.__s)


