# Generated by Django 4.2.5 on 2023-11-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_feedback_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
