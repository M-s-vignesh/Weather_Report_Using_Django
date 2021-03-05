from django import forms 
from report.models import weather_database
  
# create a ModelForm 

class weather_database1(forms.ModelForm): 
    
    class Meta: 
        model = weather_database 
        fields = "__all__"


