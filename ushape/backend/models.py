from django.db import models

class Calorielist (models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    calories = models.TextField(max_length=100, default='')
    fat = models.TextField(max_length=100, default='')
    carbs = models.TextField(max_length=100, default='')
    protein = models.TextField(max_length=100, default='')
    sodium = models.TextField(max_length=100, default='')
    calcium = models.TextField(max_length=100, default='')
    iron = models.TextField(max_length=100, default='')
    isType = models.TextField(max_length=100, default='')

def imageFile(instance, filename):
    return '/'.join( ['images', str(instance.id), filename] )


class Image (models.Model):
    username = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(
        upload_to=imageFile,
        max_length=254, blank=True, null=True
    )