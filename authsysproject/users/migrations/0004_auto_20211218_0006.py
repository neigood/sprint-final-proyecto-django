# Generated by Django 3.2.9 on 2021-12-18 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_caso_codigo_caso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caso',
            old_name='nombre_caso',
            new_name='tu_nombre',
        ),
        migrations.RenameField(
            model_name='caso',
            old_name='nombre_empresa',
            new_name='tu_opinion',
        ),
    ]
