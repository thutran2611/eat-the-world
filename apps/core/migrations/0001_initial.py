# Generated by Django 2.2.3 on 2019-07-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(max_length=160)),
            ],
        ),
    ]
