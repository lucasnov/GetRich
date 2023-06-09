# Generated by Django 4.2.1 on 2023-05-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('valor_cota', models.FloatField()),
                ('data_cota', models.DateField()),
                ('favoritada', models.BooleanField(default=False)),
            ],
        ),
    ]
