# Generated by Django 5.1.5 on 2025-01-16 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_session_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.film'),
        ),
    ]
