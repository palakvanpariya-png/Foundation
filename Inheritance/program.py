import hr 
import employee
import productivity

manager = employee.manager(1, "Mary Poppins", 3000)
secretary = employee.secretary(2, "John Smith", 1500)
sales_guy = employee.sales_person(3, "Kevin Bacon", 1000, 250)
factory_worker = employee.factory_worker(4, "Jane Doe", 40, 15)
temporary_secretary = employee.temporary_secretary(5, "Temporary Jane", 20, 10)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]


productivity_sys = productivity.ProductivitySystem()
productivity_sys.track(employees, 40)

payroll = hr.PayrollSystem()
payroll.calculate_payroll(employees)