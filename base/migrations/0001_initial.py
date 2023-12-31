# Generated by Django 4.1.9 on 2024-01-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact_us",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("mail_address", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("updated_time", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
