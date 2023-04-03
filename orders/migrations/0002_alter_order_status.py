# Generated by Django 3.2.13 on 2023-03-31 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'created'), (1, 'paid'), (2, 'on way'), (3, 'delivered')], default=0),
        ),
    ]