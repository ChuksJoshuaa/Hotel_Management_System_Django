# Generated by Django 3.2.4 on 2021-12-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
