# Generated by Django 4.0.5 on 2022-06-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=5)),
                ('productdetail', models.TextField()),
                ('size_and_fit', models.CharField(max_length=100)),
                ('material_and_care', models.CharField(max_length=100)),
                ('product_img', models.ImageField(upload_to='product_img')),
            ],
        ),
    ]
