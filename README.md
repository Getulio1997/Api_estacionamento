### Instalar o Django.

```bash
pip install django

# Criação de um projeto novo.

 django-admin startproject meu_projeto

# Criação de um novo app.

 python manage.py startapp meu_app

# Criar uma nova migrations.

  python manage.py makemigrations nome_do_app --empty --name create_initial_nome_da_tabela <br>
  python manage.py makemigrations nome_do_app --empty --name insert_initial_nome_da_tabela

# Aplicar as emigrations no banco.

 python manage.py migrate nome_do_app

# Reverter todas as migrações.

 python manage.py migrate nome_do_app zero