# Generated by Django 4.0.6 on 2022-07-07 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_orderplace_sizeofproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplace',
            name='sizeofproduct',
        ),
    ]
