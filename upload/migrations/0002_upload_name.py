# Generated by Django 4.0 on 2023-07-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]