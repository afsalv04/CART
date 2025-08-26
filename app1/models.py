from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()
    phone = models.IntegerField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    pincode = models.IntegerField()


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    brand = models.CharField(max_length=50)  # Brand name
    category = models.CharField(max_length=50)  # Category of product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g. 99999999.99
    size = models.CharField(max_length=20, blank=True, null=True)  # For clothing/shoes, can be S, M, L, XL
    # color = models.CharField(max_length=30, blank=True, null=True)  # Optional
    stock = models.PositiveBigIntegerField()  # Stock quantity
    image = models.ImageField(upload_to="product/")  # Product image
    
    def __str__(self):
        return f"{self.name} ({self.brand})"






class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)


class contactus(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.user.get_full_name() or self.user.username

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def total(self):
        return self.product.price * self.quantity

    
# def __str__(self):
#         return self.name