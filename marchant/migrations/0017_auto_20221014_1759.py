# Generated by Django 3.1 on 2022-10-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchant', '0016_auto_20221014_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(blank=True, to='marchant.Reviews'),
        ),
    ]
