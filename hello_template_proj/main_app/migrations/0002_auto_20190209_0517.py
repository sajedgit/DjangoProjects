# Generated by Django 2.1.5 on 2019-02-08 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='quote_category',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.DeleteModel(
            name='QuoteCategory',
        ),
    ]
