# Generated by Django 5.0.1 on 2024-02-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_watch_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужские'), ('female', 'Женские'), ('unisex', 'Универсальные')], default='male', max_length=50),
        ),
        migrations.AlterField(
            model_name='watch',
            name='movement',
            field=models.CharField(choices=[('quartz', 'Кварц'), ('automatic', 'Автоматический'), ('solar', 'Солнечный'), ('mechanic', 'Механический'), ('elect', 'Электронные')], max_length=50),
        ),
    ]
