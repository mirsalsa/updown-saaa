from tkinter import Widget
from django import forms
from .models import Files

class FilesForm(forms.ModelForm):
    # file_name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'input-height',
    #         }
    #     )
    # )
    # file_docs = forms.FileField()
    class Meta:
      model = Files
      fields = ['file_name', 'file_docs']
      widgets = {
            'file_name': forms.TextInput(),
            'file_docs': forms.FileInput(),
        }
    
