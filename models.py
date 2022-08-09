from email.headerregistry import Address
from ssl import VERIFY_CRL_CHECK_LEAF
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    phone =  models.CharField(max_length= 122)
    email =  models.CharField(max_length = 12)
    text =  models.TextField()
    def __str__(self):
        return self.name
    
class Donator(models.Model):
    Donator_Id = models.IntegerField(primary_key=True,null=False)
    Name = models.CharField(max_length = 100)
    Contact_No = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 50)
    Don_location = models.CharField(max_length = 100)
    Ver_Prrof = models.IntegerField()
    Ewaste_Id = models.ForeignKey()
    
class Collector(models.Model):
    JC_Id = models.IntegerField(primary_key=True,null=False)
    JC_Name = models.CharField(max_length = 100)
    Contact_No = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 50)
    JC_Location = models.CharField(max_length = 100)
    Ver_Proof =  models.IntegerField()
    Vehicle = models.CharField(max_length = 100)
    Ewaste_Id = models.ForeignKey()

class Dealer(models.Model):
    JD_Id =  models.IntegerField(primary_key=True,null=False)
    DC_Name = models.CharField(max_length = 100)
    Contact_No = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 50)
    JD_Location = models.CharField(max_length = 100)
    Ver_Proof =  models.IntegerField()
    Vehicle = models.CharField(max_length = 100)
    Location_Shop = models.CharField(max_length = 100)
    Shop_Regno = models.CharField(max_length = 100)
    Ewaste_Id = models.ForeignKey()
    