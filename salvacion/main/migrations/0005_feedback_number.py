# Generated by Django 4.2.5 on 2023-11-09 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_feedback_number_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='number',
            field=models.IntegerField(default=222),
            preserve_default=False,
        ),
    ]