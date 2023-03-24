from django.db import models
from django .contrib.auth.models import User

class Profile(models.Model):
    CHOICES=(
    ("ADMIN","ADMIN"),
    ("STAFF","STAFF"),
    ("CUSTOMER","CUSTOMER"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    type = models.CharField(max_length=150, choices = CHOICES, default = "STAFF")
class Category(models.Model):
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Product(models.Model):
    product_name = models.TextField()
    cost = models.IntegerField()
    type = models.TextField()
    product_Description = models.TextField()
    Category =models.ForeignKey(Category,on_delete=models.CASCADE)
   

class Order(models.Model):
    # productid = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    # order_by = models.ForeignKey(User,on_delete=models.CASCADE)


    
    
