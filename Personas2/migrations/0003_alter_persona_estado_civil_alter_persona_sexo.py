# Generated by Django 4.2.4 on 2023-08-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas2', '0002_persona_email_persona_vive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.CharField(choices=[('C', 'Casado'), ('S', 'Soltero'), ('V', 'Viudo'), ('O', 'Otro')], default='S', max_length=8),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'Otro')], default='F', max_length=10),
        ),
    ]
