# Generated by Django 5.0.3 on 2024-04-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0002_rentproperty_room_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentproperty",
            name="room_number",
            field=models.CharField(max_length=50),
        ),
    ]