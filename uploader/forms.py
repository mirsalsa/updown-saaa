from django import forms
from .models import Files

class FilesForm(forms.ModelForm):
    class Meta:
      model = Files
      fields = ['file_name', 'file_docs']
      widgets = {
            'file_name': forms.TextInput(),
            'file_docs': forms.FileInput(),
        }
    
