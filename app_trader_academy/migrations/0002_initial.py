# Generated by Django 4.2.7 on 2024-01-03 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_trader_academy", "0001_initial"),
        ("app_clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="strategylesson",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="app_clients.client"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="app_clients.client"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app_trader_academy.unit",
            ),
        ),
    ]