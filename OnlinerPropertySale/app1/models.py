from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()


class State(models.Model):
    state_idno = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)


class City(models.Model):
    city_idno = models.IntegerField(primary_key=True)
    state_name = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)


class Locality(models.Model):
    locality_idno = models.IntegerField(primary_key=True)
    locality_name = models.CharField(max_length=50)
    state_name = models.ForeignKey(City,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    pincode = models.CharField(max_length=150)


class SalesRegistration(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


class Transaction(models.Model):
    Order_id = models.IntegerField()
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)


class Suggestions(models.Model):
    tittle = models.CharField(max_length=150)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)





