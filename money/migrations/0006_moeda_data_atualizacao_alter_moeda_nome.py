# Generated by Django 4.2.1 on 2023-05-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0005_remove_moeda_data_atualizacao_alter_moeda_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='moeda',
            name='data_atualizacao',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moeda',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
