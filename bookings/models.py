from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=15, decimal_places=2)


    def __str__(self):
        return self.title



class Appointment(models.Model):
    Firstname = models.CharField(max_length=25)
    Email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    choosen_time = models.DateTimeField()
    dept = models.ForeignKey(Department, on_delete=models.RESTRICT)
  
