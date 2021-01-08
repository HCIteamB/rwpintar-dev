from django.db import models

class Umkm(models.Model):
     title = models.CharField(max_length=200)
     descript = models.TextField(blank=True)
     photo_main = models.ImageField(upload_to='photos/%Y%m/%d/')
     photo_1 = models.ImageField(upload_to='photos/%Y%m/%d/')
     photo_2 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
     photo_3 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
     photo_4 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)

     def __str__(self):
        return self.title
