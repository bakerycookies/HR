# Generated by Django 3.2.10 on 2022-07-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=100, null=True)),
            ],
        ),
    ]