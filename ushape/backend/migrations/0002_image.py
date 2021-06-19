# Generated by Django 3.1.7 on 2021-06-04 10:33

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to=backend.models.imageFile)),
            ],
        ),
    ]