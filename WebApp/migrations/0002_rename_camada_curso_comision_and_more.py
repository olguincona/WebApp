# Generated by Django 4.2.17 on 2024-12-09 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='camada',
            new_name='comision',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='curso',
        ),
    ]
