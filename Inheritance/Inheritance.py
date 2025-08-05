class Payroll:

    def calculate_payroll(self, employees):
        for employee in employees:
            print(f"{employee.name} Payroll: ")
            print(f"{employee.Calculate_payroll()}")


class employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class salary_employee(employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def Calculate_payroll(self):
        return self.salary
    
class hourly_employee(employee):
    def __init__(self, id, name, hourly_rate, hours_worked):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def Calculate_payroll(self):
        return self.hourly_rate * self.hours_worked
    
class commission_employee(employee):
    def __init__(self, id, name, sales_amount, commission_rate):
        super().__init__(id, name)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def Calculate_payroll(self):
        return self.sales_amount * self.commission_rate


