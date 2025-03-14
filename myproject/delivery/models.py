from django.db import models

class Customer(models.Model):
    username = models.CharField( max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=12,default=90)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username}, {self.password}"
    
class Restaurants(models.Model):
    res_name = models.CharField(max_length=100)
    food_cat = models.CharField(max_length=100)
    rating = models.FloatField()
    img = models.URLField(default="",max_length=500)
    res_address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.res_name}"
    
class Menu(models.Model):
    res = models.ForeignKey(
        Restaurants,
        on_delete= models.CASCADE
    )
    
    item_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_avial = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.res.res_name } - {self.res.food_cat}"
    
    
    
    
class Cart(models.Model):
    customer = models.ForeignKey (
        Customer,
        on_delete = models.CASCADE
    )
    items = models.ManyToManyField(Menu)
    
    def total_price(self):
        return sum(item.price for item in self.items.all())
    
    def __str__(self):
        return f"{self.customer} {self.total_price()}"