# Generated by Django 5.0.4 on 2024-04-14 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
