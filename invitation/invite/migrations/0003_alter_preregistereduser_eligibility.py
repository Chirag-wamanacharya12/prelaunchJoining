# Generated by Django 5.2.1 on 2025-06-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0002_remove_preregistereduser_registered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preregistereduser',
            name='eligibility',
            field=models.CharField(default='eligible', max_length=10),
        ),
    ]
