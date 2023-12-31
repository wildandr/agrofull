# Generated by Django 4.2.6 on 2023-10-23 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("plants", "0002_plantdetection"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("disease_type", models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name="plant",
            name="plant_img",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="plantdetection",
            name="plant_img",
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name="Recomendation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("symptoms", models.CharField(max_length=255)),
                ("recomendation", models.CharField(max_length=255, null=True)),
                ("organic_control", models.CharField(max_length=255, null=True)),
                ("chemical_control_1", models.CharField(max_length=255, null=True)),
                ("chemical_control_2", models.CharField(max_length=255, null=True)),
                ("chemical_control_3", models.CharField(max_length=255, null=True)),
                ("chemical_control_4", models.CharField(max_length=255, null=True)),
                ("chemical_control_5", models.CharField(max_length=255, null=True)),
                (
                    "chemical_control_1_dosage",
                    models.CharField(max_length=255, null=True),
                ),
                (
                    "chemical_control_2_dosage",
                    models.CharField(max_length=255, null=True),
                ),
                (
                    "chemical_control_3_dosage",
                    models.CharField(max_length=255, null=True),
                ),
                (
                    "chemical_control_4_dosage",
                    models.CharField(max_length=255, null=True),
                ),
                (
                    "chemical_control_5_dosage",
                    models.CharField(max_length=255, null=True),
                ),
                ("additional_info", models.CharField(max_length=255, null=True)),
                (
                    "disease_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plants.disease"
                    ),
                ),
            ],
        ),
    ]
