from django.db import models
from django.contrib.auth.models import User

# Create your models here.

contry=[('America','America'),('Germany','Germany'),('Australia','Australia'),
('France','France')]
class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name=models.DateField(auto_now_add=True)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    mobile = models.CharField(max_length=40)
    telophone = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    portal_zip = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country= models.CharField(max_length=10,choices=contry,default='select')
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

contry=[('America','America'),('Germany','Germany'),('Australia','Australia'),
('France','France')]
class Bidder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name=models.DateField(auto_now_add=True)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    mobile = models.CharField(max_length=40)
    telophone = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    portal_zip = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country= models.CharField(max_length=10,choices=contry,default='select')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class TokenData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    start_date = models.DateField()
    expiry_date = models.DateField()
    user_type = models.CharField(max_length=100)
