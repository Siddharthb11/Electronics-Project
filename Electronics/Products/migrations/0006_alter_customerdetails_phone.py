# Generated by Django 5.0.1 on 2024-03-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_customerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
