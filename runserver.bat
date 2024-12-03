@echo off
REM Navega até o diretório do projeto
cd C:\Users\Aluno\OneDrive\Documentos\Erick\sistema-de-gerenciamento-de-tarefas

REM Ativa o ambiente virtual (se estiver usando)
REM Ativa o ambiente virtual (se estiver usando)
call venv\Scripts\activate

REM Abre o navegador no endereço padrão do Django
start http://127.0.0.1:8000

REM Executa o servidor Django
python manage.py runserver

REM Mantém o terminal aberto (opcional)
pause