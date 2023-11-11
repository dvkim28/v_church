# Generated by Django 4.2.5 on 2023-11-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.EmailField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]