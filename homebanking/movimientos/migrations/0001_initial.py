# Generated by Django 4.2.7 on 2023-11-18 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cuenta', models.IntegerField(blank=True, null=True)),
                ('monto', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('tipo_operacion', models.CharField(blank=True, max_length=50, null=True)),
                ('hora', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
    ]
