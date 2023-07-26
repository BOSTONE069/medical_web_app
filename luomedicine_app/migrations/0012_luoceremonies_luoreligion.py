# Generated by Django 4.2.2 on 2023-07-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luomedicine_app', '0011_alter_medicinalplant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuoCeremonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='luomedicine_app/static/luo_ceremonies/')),
            ],
        ),
        migrations.CreateModel(
            name='LuoReligion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='luomedicine_app/static/luo_religion/')),
            ],
        ),
    ]
