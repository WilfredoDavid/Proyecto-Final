# Generated by Django 4.1 on 2022-09-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MensajesEnviados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MensajesRecibidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=250)),
            ],
        ),
    ]
