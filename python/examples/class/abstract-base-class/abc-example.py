# Required imports to create an abstract base class
# with abstract methods
from abc import ABC
from abc import abstractmethod


class Employee(ABC):
    """Employee will serve as the blueprint that all
    derived classes that inherit from it.

    A class with an @abstractmethod on it's function
    cannot be instatiated (created) only used as a 
    base class. These abstract method functions do
    not supply code, but instead use the "pass" keyword
    to indicate that no operations are present. Functions
    with these decorators MUST be implmeneted in derived
    classes.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @abstractmethod
    def get_salary(self):
        pass


class FulltimeEmployee(Employee):


    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    # Since this class inherits from Employee we MUST 
    # implmenet the abstract method get_salary()
    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):


    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    # Notice how full time employees and houly employees
    # both implement the get_salary function, but each
    # needs to calculate the amount in a different way.
    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:


    def __init__(self):
        self.employee_list = []


    def add(self, employee):
        self.employee_list.append(employee)

    # The advantage to using the abstract base class
    # is that it enforces the need for all derived
    # classes to share the get_salary function. We can
    # reliably call this function on any of the classes
    # that derive from Employee and are guaranteed to have
    # access to that function. I can now create an unlimited
    # number of different employee designations, but still
    # be able to get my payroll report with their salary
    # calculation.
    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")

            
def main():
    payroll = Payroll()
    payroll.add(FulltimeEmployee('John', 'Doe', 6000))
    payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
    payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
    payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
    payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

    payroll.print()


if __name__ == "__main__":
    main()