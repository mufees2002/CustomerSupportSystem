# Generated by Django 4.1.4 on 2022-12-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registration",
            old_name="LastName",
            new_name="Lastname",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="ConformPassword",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="Email",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="Phone_Number",
        ),
    ]
