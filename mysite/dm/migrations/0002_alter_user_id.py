# Generated by Django 4.1 on 2023-03-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
