# Generated by Django 3.2.7 on 2021-09-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maqola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
