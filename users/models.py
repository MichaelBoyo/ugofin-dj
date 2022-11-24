from djongo import models


class Vendor(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name


class Store(models.Model):
    store_name = models.CharField(max_length=100, primary_key=True)
    store_address = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)



class Product(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.CharField(max_length=100)
    product_image_url = models.TextField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)