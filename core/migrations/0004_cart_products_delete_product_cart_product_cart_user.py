# Generated by Django 4.0.5 on 2022-06-28 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_rename_products_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('productdetail', models.TextField()),
                ('size_and_fit', models.CharField(max_length=100)),
                ('material_and_care', models.CharField(max_length=100)),
                ('product_img', models.ImageField(upload_to='product_img')),
                ('product_img1', models.ImageField(upload_to='product_img')),
                ('product_img2', models.ImageField(upload_to='product_img')),
                ('product_img3', models.ImageField(upload_to='product_img')),
                ('product_img4', models.ImageField(upload_to='product_img')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]