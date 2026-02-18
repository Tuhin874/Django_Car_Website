from django.db import models

# Create your models here.

class BrandDb(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class CarsDb(models.Model):

    model_name = models.CharField(max_length=50)
    Top_Speed = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(BrandDb, on_delete= models.CASCADE,related_name='cars')
    image = models.ImageField(upload_to='car_images/')
    is_featured = models.BooleanField(default= False)
    def __str__(self):
        return f" {self.model_name}"
