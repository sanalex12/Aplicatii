# Generated by Django 5.0.2 on 2024-03-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_time_of_execution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_of_execution',
            field=models.IntegerField(default=0),
        ),
    ]