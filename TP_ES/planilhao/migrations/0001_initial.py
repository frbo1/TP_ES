# Generated by Django 3.2.5 on 2021-07-03 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=155)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('slug', models.SlugField(default=None, max_length=255, unique=True)),
            ],
            options={
                'db_table': 'professores',
            },
        ),
        migrations.CreateModel(
            name='Comentarios1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=500)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planilhao.professores')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comentarios',
            },
        ),
    ]
