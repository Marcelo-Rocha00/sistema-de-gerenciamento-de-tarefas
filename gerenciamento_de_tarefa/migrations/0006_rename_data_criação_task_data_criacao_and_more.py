# Generated by Django 5.1.1 on 2024-10-28 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_de_tarefa', '0005_rename_atribuida_a_task_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='data_criação',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
