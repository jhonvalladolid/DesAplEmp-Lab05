# Generated by Django 5.0.4 on 2024-04-15 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calle', models.CharField(max_length=200)),
                ('manzana', models.CharField(max_length=50)),
                ('barrio', models.CharField(max_length=100)),
                ('numero_lote', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.direccion'),
        ),
    ]