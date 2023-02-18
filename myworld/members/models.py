from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  # after to field join 
  phone = models.IntegerField(null = True)
  joined_date = models.DateField(null = True)

# after create model we have run
# python manage.py makemigrations members
# python manage.py migrate
# python manage.py sqlmigrate members 0001   :- for see the schema 
