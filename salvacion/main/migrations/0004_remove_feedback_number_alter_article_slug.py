# Generated by Django 4.2.5 on 2023-11-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='number',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
