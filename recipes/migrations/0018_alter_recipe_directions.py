# Generated by Django 3.2 on 2022-03-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_alter_recipe_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(),
        ),
    ]
