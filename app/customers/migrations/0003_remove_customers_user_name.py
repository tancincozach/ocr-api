# Generated by Django 4.2.15 on 2024-08-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user_name',
        ),
    ]
