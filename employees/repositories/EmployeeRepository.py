from employees.models import Employee

class EmployeeRepository:
    
    def save_bulk(data):
        return Employee.objects.bulk_create(data, ignore_conflicts=True)