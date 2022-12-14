# Generated by Django 4.1.2 on 2022-10-19 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Name Printer')),
                ('api_key', models.CharField(blank=True, max_length=512, null=True, unique=True, verbose_name='Key access API')),
                ('check_type', models.CharField(blank=True, max_length=512, null=True, verbose_name='Type check')),
                ('point_id', models.IntegerField(verbose_name='Point bind printer')),
            ],
            options={
                'verbose_name': 'Printer',
                'verbose_name_plural': 'Printers',
            },
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=512, null=True, verbose_name='Type check')),
                ('order', models.JSONField(blank=True, null=True, verbose_name='Information order')),
                ('status', models.CharField(blank=True, max_length=512, null=True, verbose_name='Status check')),
                ('pdf_file', models.FileField(upload_to='', verbose_name='Check format PDF')),
                ('printer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printer', to='printer.printer')),
            ],
            options={
                'verbose_name': 'Check',
                'verbose_name_plural': 'Checks',
            },
        ),
    ]
