# Generated by Django 3.1 on 2022-10-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchant', '0006_auto_20221013_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate1',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate3',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate4',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate5',
            field=models.IntegerField(default=1),
        ),
    ]
