# Generated by Django 4.0.4 on 2022-05-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chosen_one', models.BooleanField(default=False)),
                ('used', models.BooleanField(default=False)),
                ('bat_file', models.CharField(max_length=10000)),
            ],
        ),
    ]