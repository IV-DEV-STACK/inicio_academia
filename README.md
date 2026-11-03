# Academia

Projeto inicial de gerenciamento de academia com Django.

## Requisitos

- Python 3.12 ou superior
- Django 6.1

## Instalação no Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ para ver a página inicial ou
http://127.0.0.1:8000/admin/ para acessar a administração do Django.

Para criar um usuário administrador:

```powershell
python manage.py createsuperuser
```

## Configuração para produção

Por padrão, `DJANGO_DEBUG` fica ativado para desenvolvimento. Antes de publicar,
defina `DJANGO_DEBUG=False`, `DJANGO_SECRET_KEY` com uma chave secreta própria e
`DJANGO_ALLOWED_HOSTS` com os domínios permitidos, separados por vírgula.

O banco SQLite está configurado para o início do projeto; `db.sqlite3` não é
versionado.
