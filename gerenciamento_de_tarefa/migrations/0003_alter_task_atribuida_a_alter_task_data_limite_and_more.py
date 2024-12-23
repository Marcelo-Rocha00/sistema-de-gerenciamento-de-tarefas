# Generated by Django 5.1.1 on 2024-10-23 21:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_de_tarefa', '0002_rename_data_limite_task_data_limite_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='atribuida_a',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='data_limite',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='descrição',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='titulo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
