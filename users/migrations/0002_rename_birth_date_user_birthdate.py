# Generated by Django 4.1.7 on 2023-10-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="birth_date",
            new_name="birthdate",
        ),
    ]
