# Generated by Django 3.1 on 2020-08-23 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_problemreported'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problemreported',
            options={'verbose_name': 'Problem Reported', 'verbose_name_plural': 'Problems Reported'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('created',)},
        ),
    ]