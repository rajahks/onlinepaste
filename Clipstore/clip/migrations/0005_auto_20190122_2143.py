# Generated by Django 2.1.2 on 2019-01-22 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0004_auto_20190122_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='clip',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
