# Generated by Django 3.2 on 2023-04-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]