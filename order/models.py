import random
import string
from django.db import models
import uuid
from product.models import  Product
# Create your models here.


class Status():
   
    def tolist():

        NOT_STARTED = 'NS'
        IN_PROGRESS = 'IP'
        COMPLETED = 'CP'
        DELIVERED = 'DE'
        RETURNED_BACK = 'RB'
        CANCELLED = 'CA'

        CHOICES = [
            (NOT_STARTED, 'Not Started'),
            (IN_PROGRESS, 'In Progress'),
            (COMPLETED, 'Completed'),
            (DELIVERED, 'Delivered'),
            (RETURNED_BACK, 'Returned Back'),
            (CANCELLED, 'Cancelled'),
        ]

        return CHOICES

class OrderItem(models.Model):
    choices = Status.tolist()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=False) 
    quantity =  models.IntegerField(default=0, null=False, verbose_name="Quantity")
    status = models.CharField(max_length=50,choices=choices,default=choices[0],verbose_name="Status",null=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(null=True,auto_now_add=True)
    def __str__(self) -> str:
        return '{} x {}'.format(self.product, self.quantity)
    def natural_key(self):
        return (self.quantity, self.created_at)

class Order(models.Model):
    
    def generateOrderNo(id):
        from datetime import datetime

        size=4
        chars=string.ascii_uppercase + string.digits
        date = datetime.now()
        randomstr = "".join(random.choice(chars) for _ in range(size))
        return '{}-{}'.format(date.strftime("%Y"),randomstr)
   
    choices = Status.tolist()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_no = models.CharField(editable=False,unique=True,max_length=50,null=True,verbose_name="Order No")
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)  
    items = models.ManyToManyField(OrderItem) 
    status = models.CharField(max_length=50,choices=choices,default=choices[0], verbose_name="Status",null=False)
    note= models.TextField(default="", blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(null=True,auto_now_add=True)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.order_no, self.status)
    
    def save(self, *args, **kwargs):
        self.order_no = self.generateOrderNo()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        
    
    class Meta:
        verbose_name_plural = "Orders"

    