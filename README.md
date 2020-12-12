# Projeto-Django
Projeto Web para desenvolvimento de uma pagina com Django em Python

Aplicação disponivel no [Heroku](https://jbspro.herokuapp.com/)

[![Build Status](https://travis-ci.org/JosemarBrito/Projeto-Django.svg?branch=main)](https://travis-ci.org/JosemarBrito/Projeto-Django)
[![codecov](https://codecov.io/gh/JosemarBrito/Projeto-Django/branch/main/graph/badge.svg)](https://codecov.io/gh/JosemarBrito/Projeto-Django)
[![Updates](https://pyup.io/repos/github/JosemarBrito/Projeto-Django/shield.svg)](https://pyup.io/repos/github/JosemarBrito/Projeto-Django/)
[![Python 3](https://pyup.io/repos/github/JosemarBrito/Projeto-Django/python-3-shield.svg)](https://pyup.io/repos/github/JosemarBrito/Projeto-Django/)

- pipenv install django
- pipenv sync -d
- pipenv install django
- django-admin
- startproject
- manage.py
- runserver
#
- ambiente virtual - alias mng='python $VIRTUAL_ENV/../manage.py (linux e mac)
- ambiente virtual - doskey mng=@python "VIRTUAL_ENV%/../manage.py "$* (windows)
#
- pubilcação no heroku
- pipenv install gunicorn (servidor de apps)
#
- Pytest-django - utilizado para nao permitir que erros cheguem no final da entrrega continua, ajudando o flake8, git-action, travis-CI.

- pipenv install -d 'pytest-django'
- criar variavel de ambiente indicado pelo site (pytest-django.read)
- criar pacote file 'pytest.ini, na raiz do projeto'
- pytest.ini (dentro da pasta)
- 1 - [pytest]
- 2 - DJANGO_SETTINGS_MODULE = jbs.settings
#
Na configuração do Pycharm
- Setings
- Integrate
- Defaut test runner (setar como pytest)

- Dentro da pasta base criar
- 1 pasta test
- 2 pacote test_home.py


Comando:
- def test_status_code(client: Client):
-   resp = clietn.get ('/)
-   assert resp.status_code == 200    

Cobertura de testes:
-pytest-cov
-pipenv install --dev 'pytest-cov' codecov

Gerar relatórios
- pipenv run pytest --cov jbs

Criar no ci travis ou ga
**configurando postgres
configuraço s3
configurado banco de dados com Sqlite
COnfigurado Backup do Postresql
corrigido
AKIARZD4SKDJZGOO7Q75

Utilizado 

[Twiter Bootstrap](https://getbootstrap.com/)

[Simulador](https://layoutit.com/pt)