# Generated by Django 3.1.7 on 2021-03-31 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antena', models.CharField(max_length=255)),
                ('metragem', models.CharField(max_length=255)),
                ('local', models.CharField(choices=[('Cacheira Paulista', 'Cacheira Paulista'), ('Cuiabá', 'Cuiabá')], max_length=255)),
            ],
            options={
                'ordering': ['local', 'antena'],
            },
        ),
        migrations.CreateModel(
            name='Satelite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satelite', models.CharField(max_length=255, verbose_name='Satélite')),
            ],
            options={
                'ordering': ['satelite'],
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servidor', models.CharField(max_length=255)),
                ('montagem', models.CharField(max_length=255, verbose_name='Montagem')),
                ('formato_diretorio', models.CharField(max_length=255, verbose_name='Formato do diretorio')),
            ],
            options={
                'verbose_name_plural': 'Servidores',
                'ordering': ['servidor'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(max_length=255)),
                ('satelite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensor_satelite', to='core.satelite')),
            ],
        ),
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
                ('qt_passagem', models.IntegerField(blank=True, null=True, verbose_name='Quant. Passagem')),
                ('qt_arquivos', models.IntegerField(blank=True, null=True, verbose_name='Quant. Arquivo')),
                ('antena', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.antena')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.sensor', verbose_name='Satélite/Sensor')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servidor')),
            ],
            options={
                'verbose_name_plural': 'Passagens',
                'ordering': ['-inicio'],
            },
        ),
    ]
