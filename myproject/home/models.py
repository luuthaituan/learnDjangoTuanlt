from django.db import models

# Create your models here.
class home(models.Model):
    first_column = models.CharField(max_length=255)
    second_column = models.CharField(max_length=255)

    #tạo ra bảng với 2 trường first_column và second_column
    #Python manage.py makemigrations
    #python manage.py migrate