# Generated by Django 3.1.2 on 2022-11-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('envs', models.CharField(max_length=200)),
                ('command', models.CharField(max_length=200)),
            ],
        ),
    ]
