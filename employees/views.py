from django.http import HttpResponse
from employees.services.CatalogService import CatalogService
from employees.services.EmployeesService import EmployeesService

def index(request):
    return HttpResponse("ok")

def charge_catalog(request):
    agency_cant, profession_cant, ethnicity_cant, gender_cant = CatalogService.charge_data()
    return HttpResponse(f"Se cargaron correctamente agency={agency_cant}, profession={profession_cant}, ethnicity={ethnicity_cant}, gender_cant={gender_cant}")

def charge_employees(request):
    rows_read, rows_error = EmployeesService.charge_data()
    return HttpResponse(f"Se procesaron correctamente {rows_read} registros, errores: {rows_error}")

