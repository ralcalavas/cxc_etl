import pandas as pd
import hashlib
import logging
from employees.repositories.AgencyRepository import AgencyRepository
from employees.repositories.EthnicityRepository import EthnicityRepository
from employees.repositories.GenderRepository import GenderRepository
from employees.repositories.ProfessionRepository import ProfessionRepository
from employees.repositories.EmployeeRepository import EmployeeRepository
from employees.models import Employee

class EmployeesService:
    CSV_ROUTE = "employees\\data\\employees.csv"
    def charge_data(file_route = CSV_ROUTE):
        rows_read = 0
        rows_error = 0
        size = 10000
        cols = ["agency_name","last_name","first_name","class_title","ethnicity","gender","monthly"]
        df_chunk = pd.read_csv(file_route, sep = ',', chunksize=size, usecols=cols)
        dict_entitys = dict(agencys=EmployeesService.get_dict_from_table(AgencyRepository),
          ethnicity=EmployeesService.get_dict_from_table(EthnicityRepository),
          gender=EmployeesService.get_dict_from_table(GenderRepository),
          profession=EmployeesService.get_dict_from_table(ProfessionRepository))
        
        for df in df_chunk:
            data_for_save = []
            for index, row in df.iterrows():
                employee = EmployeesService.get_employee(dict_entitys, row)
                
                if employee:
                    data_for_save.append(employee)
                else:
                    rows_error += 1

            bulk_response = EmployeeRepository.save_bulk(data_for_save)
            rows_read += len(bulk_response)
            
        return rows_read, rows_error

    def get_employee(dict_entitys, row):
        result = None
        try:
            agency_id = dict_entitys['agencys'][row['agency_name']]
            ethnicity_id = dict_entitys['ethnicity'][row['ethnicity']]
            gender_id = dict_entitys['gender'][row['gender']]
            profession_id = dict_entitys['profession'][row['class_title']]
            concat = f'{row['first_name']}_{row['last_name']}_{profession_id}_{ethnicity_id}_{gender_id}'
            md5 = hashlib.md5(concat.encode()).hexdigest()
            
            result = Employee(
                name=row['first_name'],
                last_name=row['last_name'],
                agency_id=agency_id,
                profession_id=profession_id,
                gender_id=gender_id,
                ethnicity_id=ethnicity_id,
                monthly_salary=row['monthly'],
                md5=md5,
            )
        except Exception as e: 
            logging.warning(f"ERROR: {e} data:{row}")
        
        return result

    def get_dict_from_table(repo):
        data_db = repo.get_all()

        return {obj.name: obj.id for obj in data_db}
       