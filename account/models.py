from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class  Adress(models.Model):
    pincode = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    city = models.TextField(max_length=200, verbose_name='City')
    area = models.TextField(max_length=1000, verbose_name='Locality')
    
    

    def __str__(self):
        return self.pincode