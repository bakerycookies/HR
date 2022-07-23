from imp import create_dynamic
from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
        )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    salary = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note =  models.TextField()
    created_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Jason
    def get_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'occupation': self.occupation,
            'salary': self.salary,
            'gender': self.gender,
        }
        