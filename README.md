# Instalar o Django.

# Criação de um projeto novo.

# Criação de um novo app.

# Criar uma nova migrations.

# Aplicar as emigrations no banco.

# Reverter todas as migrações.

```bash
 pip install django

 django-admin startproject meu_projeto

 python manage.py startapp meu_app

 python manage.py makemigrations nome_do_app --empty --name create_initial_nome_da_tabela <br>
 python manage.py makemigrations nome_do_app --empty --name insert_initial_nome_da_tabela

 python manage.py migrate nome_do_app

 python manage.py migrate nome_do_app zero