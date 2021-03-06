# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreInst', models.CharField(max_length=80)),
                ('DesCap', models.CharField(max_length=500)),
                ('FecIni', models.DateField()),
                ('FecFin', models.DateField()),
                ('NroHoras', models.IntegerField()),
                ('Vigente', models.IntegerField(choices=[(1, 'S'), (2, 'N')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='CentroEstudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescCentEst', models.CharField(max_length=100)),
                ('Vigente', models.IntegerField(choices=[(1, 'S'), (2, 'N')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LugarTrabajo', models.CharField(max_length=30)),
                ('DesTrabajo', models.CharField(max_length=800)),
                ('CodCargo', models.CharField(max_length=4)),
                ('FecIni', models.DateField()),
                ('FecFin', models.DateField()),
                ('NroConv', models.CharField(max_length=6)),
                ('Contrato', models.CharField(max_length=400)),
                ('MotivoRetiro', models.CharField(max_length=30)),
                ('Vigente', models.IntegerField(choices=[(1, 'S'), (2, 'N')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='PerProfesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroCIP', models.CharField(max_length=10)),
                ('FecCIPVig', models.DateField()),
                ('Vigente', models.IntegerField(choices=[(1, 'S'), (2, 'N')], default=2)),
                ('CodCentEst', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.CentroEstudio')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Profesiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grado', models.CharField(max_length=10)),
                ('DesProf', models.CharField(max_length=30)),
                ('Vigente', models.IntegerField(choices=[(1, 'S'), (2, 'N')], default=2)),
            ],
        ),
        migrations.AddField(
            model_name='perprofesion',
            name='CodPers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Persona'),
        ),
        migrations.AddField(
            model_name='perprofesion',
            name='CodProf',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Profesiones'),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='CodPers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Persona'),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='CodProf',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Profesiones'),
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='CodCentEst',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.CentroEstudio'),
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='CodPers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Persona'),
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='CodProf',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.Profesiones'),
        ),
    ]
