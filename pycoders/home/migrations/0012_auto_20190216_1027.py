# Generated by Django 2.1.7 on 2019-02-16 10:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/brand'),
        ),
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/avatar'),
        ),
        migrations.AddField(
            model_name='customer',
            name='ineterests',
            field=models.ManyToManyField(blank=True, related_name='customers_interests', to='home.Category'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='search',
        ),
        migrations.AddField(
            model_name='product',
            name='search',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 16, 10, 27, 20, 637803)),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_review', to='home.Review'),
        ),
    ]
