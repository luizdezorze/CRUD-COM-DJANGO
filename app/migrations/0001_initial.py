# Generated by Django 4.0.2 on 2022-02-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=150)),
                ('medicamento', models.CharField(max_length=150)),
                ('duracao', models.IntegerField()),
            ],
        ),
    ]
