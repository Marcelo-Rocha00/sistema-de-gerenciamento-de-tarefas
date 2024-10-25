# Generated by Django 5.1.1 on 2024-10-23 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_de_tarefa', '0003_alter_task_atribuida_a_alter_task_data_limite_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='atribuida_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='data_limite',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]