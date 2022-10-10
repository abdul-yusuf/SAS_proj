# Generated by Django 3.1 on 2022-10-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20221010_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='specialization',
            field=models.CharField(choices=[('R', 'Rent'), ('S', 'Sell'), ('B', 'Sell & Rent'), ('C', 'Customer')], default='C', max_length=1),
        ),
    ]
