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

class Recycle_Plant(models.Model):
    RP_Id =  models.IntegerField(primary_key=True,null=False)
    JC_Name =  models.CharField(max_length = 100)
    Contact_no =  models.CharField(max_length = 100)
    Adress =  models.CharField(max_length = 100)
    Email =  models.CharField(max_length = 100)
    JC_Location =  models.CharField(max_length = 100)
    Ver_Proof = models.IntegerField()
    Vehicle =  models.CharField(max_length = 100)
    Location =  models.CharField(max_length = 100)

class Ewaste(models.Model):
    Ewaste_Id = models.IntegerField(primary_key=True,null=False)
    Name = models.CharField(max_length = 100)
    Dimensions = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Size = models.CharField(max_length = 100)
    Weight = models.CharField(max_length = 100)
    Donator_Id =models.ForeignKey()
    JC_Id =models.ForeignKey()
    Booking_Id =models.ForeignKey()
    JD_Id = models.ForeignKey()
    RP_Id = models.ForeignKey()
    Status = models.CharField(max_length = 20)

class Pickup_Booking(models.Model):
     Booking_Id =  models.IntegerField(primary_key=True,null=False)
     Pickup_location = models.CharField(max_length = 100)
     Ewaste_Id = models.ForeignKey()
     Booking_Status =  models.CharField(max_length = 20)
     Startof_pickup = models.CharField(max_length = 100)
     Endof_Pickup = models.CharField(max_length = 100)
