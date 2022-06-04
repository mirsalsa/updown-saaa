import os
from django.db import models

# Create your models here.
def create_name(instance, filename):
  path = 'documents/'
  filename, fileextensions = os.path.splitext(filename)
  return os.path.join(path, f"{filename}{fileextensions}")

class Files(models.Model):
    file_name = models.CharField(max_length=100)
    file_docs = models.FileField(upload_to=create_name)
    file_date = models.DateTimeField(auto_now_add=True)
