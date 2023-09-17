from django.db import models

# Create your models here.
class customers(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    current_balance=models.FloatField()
    address=models.CharField(max_length=150)
    phone_number=models.IntegerField()
    def _str_(self):
        return self.name

class history(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=100)
    reciever=models.CharField(max_length=100)
    amount=models.FloatField()
    date_transfer=models.DateTimeField()
    def _str_(self):
        return self.sender