# Generated by Django 3.2.4 on 2021-12-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
    ]
