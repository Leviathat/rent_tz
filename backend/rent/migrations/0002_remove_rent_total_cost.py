# Generated by Django 4.1.7 on 2024-03-03 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='total_cost',
        ),
    ]
