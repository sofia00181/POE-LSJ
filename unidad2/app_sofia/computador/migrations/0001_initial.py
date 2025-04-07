# Generated by Django 5.1.7 on 2025-04-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teclado', models.CharField(max_length=100)),
                ('mouse', models.CharField(max_length=100)),
                ('pantalla', models.CharField(max_length=100)),
                ('software', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
