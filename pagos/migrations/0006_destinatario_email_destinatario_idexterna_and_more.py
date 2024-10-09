# Generated by Django 5.1.1 on 2024-10-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0005_remove_metodopago_usuario_transaccion_esreembolso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinatario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='destinatario',
            name='idExterna',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagador',
            name='idExterna',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
