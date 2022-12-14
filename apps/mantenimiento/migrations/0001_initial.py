# Generated by Django 4.1.2 on 2022-10-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometraje', models.PositiveIntegerField(default=0, verbose_name='Kilometraje')),
                ('descripcion', models.CharField(max_length=250, verbose_name='decripcion')),
                ('costo', models.PositiveIntegerField(default=0, verbose_name='Costo')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('auto', models.ManyToManyField(to='auto.auto')),
            ],
            options={
                'verbose_name': 'Mantenimiento',
                'verbose_name_plural': 'Mantenimientos',
            },
        ),
    ]
