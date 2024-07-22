from employees.models import Agency

class AgencyRepository:
    
    def save_bulk(data):
        return Agency.objects.bulk_create(data)
    
    def get_all():
        all_agency = Agency.objects.all()
    
        return list(all_agency)
    
    def get_all_names():
        all_agency = Agency.objects.all()
    
        return [agency.name for agency in all_agency]