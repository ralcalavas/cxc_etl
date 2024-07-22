from employees.models import Profession

class ProfessionRepository:
    
    def save_bulk(data):
        return Profession.objects.bulk_create(data)
    
    def get_all():
        all_profession = Profession.objects.all()
    
        return list(all_profession)
    
    def get_all_names():
        all_profession = Profession.objects.all()
    
        return [profession.name for profession in all_profession]