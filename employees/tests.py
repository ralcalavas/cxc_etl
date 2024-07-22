from django.test import TestCase
from employees.services.CatalogService import CatalogService
from employees.services.EmployeesService import EmployeesService

# Create your tests here.

class CatalogTests(TestCase):
    def test_charge_catalogos(self):
        agency_cant, profession_cant, ethnicity_cant, gender_cant = CatalogService.charge_data("employees\\data_test\\catalogos.csv")
        self.assertEqual(agency_cant, 113)
        self.assertEqual(ethnicity_cant, 6)
        self.assertEqual(gender_cant, 2)
        self.assertEqual(profession_cant, 1726)

class EmployeesTests(TestCase):
    def test_charge_employees(self):
        CatalogService.charge_data("employees\\data_test\\catalogos.csv")
        rows_read, rows_error = EmployeesService.charge_data("employees\\data_test\\employees.csv")
        self.assertEqual(rows_read, 99)
        self.assertEqual(rows_error, 1)
