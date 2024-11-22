# Instalar o Django.

` ```bash` ``` `
 pip install django
` ```bash` ``` `

# Criação de um projeto novo.

` ```bash` ``` `
 django-admin startproject meu_projeto
` ```bash` ``` `

# Criação de um novo app.

` ```bash` ``` `
 python manage.py startapp meu_app
` ```bash` ``` `

# Criar uma nova migrations.

` ```bash` ``` `
  python manage.py makemigrations nome_do_app --empty --name create_initial_nome_da_tabela
  python manage.py makemigrations nome_do_app --empty --name insert_initial_nome_da_tabela
` ```bash` ``` `

# Aplicar as emigrations no banco.

` ```bash` ``` `
 python manage.py migrate nome_do_app
` ```bash` ``` `

# Reverter todas as migrações.

` ```bash` ``` `
 python manage.py migrate nome_do_app zero
` ```bash` ``` `