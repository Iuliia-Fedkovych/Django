# Generated by Django 2.2.4 on 2020-08-02 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Category name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Product name')),
                ('image', models.ImageField(blank=True, upload_to='products_image')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='short product description')),
                ('description', models.TextField(blank=True, verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Product price')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='storage quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
    ]
