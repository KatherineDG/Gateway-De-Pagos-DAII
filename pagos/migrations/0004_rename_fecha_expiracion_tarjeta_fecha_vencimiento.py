# Generated by Django 5.1.1 on 2024-10-08 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_remove_destinatario_email_alter_pagador_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarjeta',
            old_name='fecha_expiracion',
            new_name='fecha_vencimiento',
        ),
    ]
