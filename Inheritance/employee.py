from hr import HourlyPolicy, SalaryPolicy, CommissionPolicy
from productivity import ManagerRole, SecretaryRole, SalesRole, FactoryRole

class employee():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class manager(employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class secretary(employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class sales_person(employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)


class factory_worker(employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
        super().__init__(id, name)

class temporary_secretary(employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hourly_rate, hours_worked):
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
        super().__init__(id, name) 
