# Generated by Django 3.1 on 2022-10-13 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marchant', '0005_auto_20221012_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_product',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='23333', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('H', 'House'), ('A', 'Apartment'), ('O', 'Office'), ('R', 'Room')], default='R', max_length=1),
        ),
        migrations.DeleteModel(
            name='SubProduct',
        ),
        migrations.AddField(
            model_name='review',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marchant.reviewreply'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]