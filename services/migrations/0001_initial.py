# Generated by Django 4.2.2 on 2023-07-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile1', models.TextField(max_length=264)),
                ('title2', models.TextField(max_length=264)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=600)),
            ],
        ),
    ]