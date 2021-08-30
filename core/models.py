from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self) -> str:
        return str(self.first_name)
    
    
    