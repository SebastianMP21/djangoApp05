# Generated by Django 4.0.4 on 2022-04-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default='error algo ocurrio', verbose_name='Fecha de nacimiento'),
        ),
    ]