# Generated by Django 5.1.1 on 2024-10-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Questionary",
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
                ("questions", models.TextField(null=True)),
                ("option1", models.TextField(null=True)),
                ("option2", models.TextField(null=True)),
                ("option3", models.TextField(null=True)),
                ("option4", models.TextField(null=True)),
                ("correct_ans", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=30, null=True)),
                ("last_name", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=50, null=True)),
            ],
        ),
    ]
