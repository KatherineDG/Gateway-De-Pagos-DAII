# Generated by Django 5.1.1 on 2024-10-10 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0016_alter_transaccion_destinatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='metodo_pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagos.metodopago'),
        ),
    ]
