# Generated by Django 2.1.4 on 2019-01-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_auto_20190104_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state_bound',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
