# Generated by Django 2.1.2 on 2019-01-20 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clipId', models.CharField(max_length=20)),
                ('clipText', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime.utcnow, editable=False)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('link_duration', models.IntegerField(choices=[(0, 'On Access'), (1, '1 hr'), (24, '1 day'), (240, '10 days'), (480, '20 days'), (720, '30 days')], default=0)),
                ('isEncrypted', models.BooleanField(default=False)),
            ],
        ),
    ]
