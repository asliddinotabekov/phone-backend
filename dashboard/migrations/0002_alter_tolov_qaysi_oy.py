# Generated by Django 4.1.7 on 2023-04-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tolov',
            name='qaysi_oy',
            field=models.DateField(blank=True, null=True),
        ),
    ]
