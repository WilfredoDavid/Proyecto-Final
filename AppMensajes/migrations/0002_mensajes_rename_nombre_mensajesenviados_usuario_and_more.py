# Generated by Django 4.1 on 2022-09-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='mensajesenviados',
            old_name='nombre',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='mensajesrecibidos',
            old_name='nombre',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='mensajesenviados',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mensajesrecibidos',
            name='mensaje',
            field=models.TextField(),
        ),
    ]