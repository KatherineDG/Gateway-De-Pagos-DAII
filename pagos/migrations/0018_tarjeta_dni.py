# Generated by Django 5.1.1 on 2024-10-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0017_alter_transaccion_metodo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='dni',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
