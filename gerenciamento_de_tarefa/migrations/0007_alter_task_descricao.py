# Generated by Django 5.1.1 on 2024-10-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_de_tarefa', '0006_rename_data_criação_task_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
