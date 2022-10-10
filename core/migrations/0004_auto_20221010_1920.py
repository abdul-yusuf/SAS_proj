# Generated by Django 3.1 on 2022-10-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221010_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_product',
            old_name='price',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, to='core.Images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_product',
            field=models.ManyToManyField(blank=True, to='core.Sub_Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_product',
            name='images',
            field=models.ManyToManyField(blank=True, to='core.Images'),
        ),
    ]
