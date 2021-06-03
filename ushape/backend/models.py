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
    # class Meta:
    #     ordering = ['created']