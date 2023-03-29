from django.db import models

# Create your models here.
class SuperType(models.Model):
    type = models.CharField(max_length=255)

s = SuperType.objects.create(type='my_type')