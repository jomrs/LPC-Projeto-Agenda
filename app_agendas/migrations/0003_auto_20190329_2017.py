# Generated by Django 2.1.7 on 2019-03-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agendas', '0002_auto_20190329_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Compromisso')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='compromissos',
            field=models.ManyToManyField(to='app_agendas.Compromisso'),
        ),
    ]