# Generated by Django 2.2 on 2019-04-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190416_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='rut',
            field=models.CharField(help_text='Tu RUT sin puntos ni guion', max_length=9),
        ),
    ]
