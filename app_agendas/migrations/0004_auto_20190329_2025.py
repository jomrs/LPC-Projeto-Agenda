# Generated by Django 2.1.7 on 2019-03-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agendas', '0003_auto_20190329_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Agenda Institucional')),
            ],
        ),
        migrations.AlterField(
            model_name='compromisso',
            name='descricao',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='institucional',
            name='compromisso',
            field=models.ManyToManyField(to='app_agendas.Compromisso'),
        ),
    ]