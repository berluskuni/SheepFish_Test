# Generated by Django 4.1.2 on 2022-10-21 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0005_alter_printer_api_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check',
            old_name='printer_id',
            new_name='printer',
        ),
    ]
