# Generated by Django 4.0 on 2022-07-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
