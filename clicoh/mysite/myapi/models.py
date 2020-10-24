from django.db import models

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    date_time = models.DateTimeField()

    #class Meta:
    #    ordering = ['created']

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cuantity = models.IntegerField()
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)