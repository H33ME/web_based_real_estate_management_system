# Generated by Django 5.0.3 on 2024-04-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentproperty",
            name="room_number",
            field=models.CharField(default="NOT AVAILABLE", max_length=10),
            preserve_default=False,
        ),
    ]
