from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=255)
    Stock_price = models.IntegerField(default=0, null=True, blank=True)
    stock_cost = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)
    stock_branch = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Sale(models.Model):
    #associating property item with the name of the stock being kept in the stock table/model.
    item = models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        #we want abstract values for change
        return abs(int(change))
    
    def __str__(self):
       return self.item.item_name
    

  

class Branch(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name