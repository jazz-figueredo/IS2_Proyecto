# Generated by Django 4.2 on 2023-04-26 23:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sprint', '0001_initial'),
        ('proyectousuario', '0002_rename_nombre_proyecto_proyectousuario_id_proyecto_and_more'),
        ('estadouserstory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id_userstory', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=8000, null=True)),
                ('story_point', models.IntegerField(blank=True, null=True)),
                ('definicion_hecho', models.CharField(blank=True, max_length=8000, null=True)),
                ('prioridad', models.IntegerField(blank=True, default=1, null=True)),
                ('fecha_inicio', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('id_estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estadouserstory.estadosuserstory')),
                ('id_proyectousuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectousuario.proyectousuario')),
                ('id_sprint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint.sprints')),
            ],
            options={
                'verbose_name': 'userstory',
                'verbose_name_plural': 'userstories',
                'db_table': 'user_stories',
            },
        ),
    ]