# Generated by Django 3.2.5 on 2021-07-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilhao', '0003_comentarios_professores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professores',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
