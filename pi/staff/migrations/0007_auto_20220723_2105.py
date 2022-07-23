# Generated by Django 3.2.10 on 2022-07-23 13:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_employee_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='note',
            field=models.TextField(default=datetime.datetime(2022, 7, 23, 13, 5, 30, 230341, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
