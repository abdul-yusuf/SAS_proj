# Generated by Django 3.1 on 2022-10-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timeframe',
            field=models.CharField(choices=[('L', 'Lifetime'), ('M', 'Monthly'), ('Y', 'Yearly')], default='Y', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('R', 'Rent'), ('S', 'Sell')], default='R', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
