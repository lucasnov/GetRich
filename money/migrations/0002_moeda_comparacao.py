# Generated by Django 4.2.1 on 2023-05-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moeda',
            name='comparacao',
            field=models.BooleanField(default=False),
        ),
    ]
