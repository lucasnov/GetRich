# Generated by Django 4.2.1 on 2023-05-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0004_moeda_compra_moeda_venda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moeda',
            name='data_atualizacao',
        ),
        migrations.AlterField(
            model_name='moeda',
            name='nome',
            field=models.CharField(max_length=20),
        ),
    ]
