# Generated by Django 4.0.6 on 2022-08-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trailers', '0005_alter_trailers_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailers',
            name='description',
            field=models.TextField(max_length=700),
        ),
    ]
