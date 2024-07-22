import pandas as pd
from employees.repositories.AgencyRepository import AgencyRepository
from employees.repositories.EthnicityRepository import EthnicityRepository
from employees.repositories.GenderRepository import GenderRepository
from employees.repositories.ProfessionRepository import ProfessionRepository
from employees.models import Agency, Profession, Ethnicity, Gender

class CatalogService:
    CSV_ROUTE = "employees\\data\\catalogos.csv"
    def charge_data(file_route = CSV_ROUTE):
        df = pd.read_csv("employees\\data\\catalogos.csv", sep = ';')
        agency_cant = CatalogService.charge_entity_data(df, 'agency_name', AgencyRepository, Agency)
        profession_cant = CatalogService.charge_entity_data(df, 'class_title', ProfessionRepository, Profession)
        ethnicity_cant = CatalogService.charge_entity_data(df, 'ethnicity', EthnicityRepository, Ethnicity)
        gender_cant = CatalogService.charge_entity_data(df, 'gender', GenderRepository, Gender)
        
        return agency_cant, profession_cant, ethnicity_cant, gender_cant
        
    def charge_entity_data(df, column, repo, model):
        data_db = repo.get_all_names()
        unique_df_data = df[column].dropna().drop_duplicates()
        df_to_charge_data = unique_df_data[~unique_df_data.isin(data_db)]
        
        list_objs = []
        for item in df_to_charge_data:
            list_objs.append(model(name = item))
            
        rows_read = repo.save_bulk(list_objs)
        
        return len(rows_read)