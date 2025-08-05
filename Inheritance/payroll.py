import Inheritance

salary_employee = Inheritance.salary_employee(1, "John Smith", 1500)
hourly_employee = Inheritance.hourly_employee(2, "Jane Doe", 40, 15)
commission_employee = Inheritance.commission_employee(3, "Kevin Bacon", 100, 250)

payroll = Inheritance.Payroll()
payroll.calculate_payroll([salary_employee, hourly_employee, commission_employee])

