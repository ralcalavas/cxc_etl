from employees.models import Ethnicity

class EthnicityRepository:
    
    def save_bulk(data):
        return Ethnicity.objects.bulk_create(data)
    
    def get_all():
        all_ethnicity = Ethnicity.objects.all()
    
        return list(all_ethnicity)
    
    def get_all_names():
        all_ethnicity = Ethnicity.objects.all()
    
        return [ethnicity.name for ethnicity in all_ethnicity]