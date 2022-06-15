from datetime import date
import os
from django.db import models

# Create your models here.
def create_name(instance, filename):
  path = 'documents/'
  filename, fileextensions = os.path.splitext(filename)
  day = instance.file_date.strftime("%A").upper()
  tanggal = instance.file_date.timestamp()
  second, milisecond = str(tanggal).split(".")
  file_name = "%s-%s" % (day, second)
  return os.path.join(path, f"{file_name}{fileextensions}")

class Files(models.Model):
    file_name = models.CharField(max_length=100)
    file_date = models.DateTimeField(auto_now_add=True)
    file_docs = models.FileField(upload_to=create_name)
