# Criar uma Nova Migração
python manage.py makemigrations nome_do_app --empty --name create_initial_nome_da_tabela <br>
python manage.py makemigrations nome_do_app --empty --name insert_initial_nome_da_tabela


# Rodar novamente as migrações do Django
python manage.py migrate nome_do_app

# Reverter todas as migrações
python manage.py migrate nome_do_app zero