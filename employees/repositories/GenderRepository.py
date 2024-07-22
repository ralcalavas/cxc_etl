from employees.models import Gender

class GenderRepository:
    
    def save_bulk(data):
        return Gender.objects.bulk_create(data)
    
    def get_all():
        all_gender = Gender.objects.all()
    
        return list(all_gender)
    
    def get_all_names():
        all_gender = Gender.objects.all()
    
        return [gender.name for gender in all_gender]