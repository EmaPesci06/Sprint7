# Generated by Django 4.2.7 on 2023-11-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta_number', models.TextField()),
                ('cvv', models.TextField()),
                ('issuance_date', models.TextField()),
                ('expiration_date', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
    ]
