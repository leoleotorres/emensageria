#coding:utf-8
"""
Django settings for emensageria project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

"""

    eMensageria - Sistema de Gerenciamento de Eventos do eSocial <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

import psycopg2
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from emensageria.versao import versao

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2w0qr9j#u2e=q081@sk)^-t3g9p5+k0+k9-b=yx4*aw!j=dsm$'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emensageria.mensageiro',
    'emensageria.controle_de_acesso',
    'emensageria.eventos',
    'emensageria.s1000',
    'emensageria.s1005',
    'emensageria.s1010',
    'emensageria.s1020',
    'emensageria.s1030',
    'emensageria.s1035',
    'emensageria.s1040',
    'emensageria.s1050',
    'emensageria.s1060',
    'emensageria.s1070',
    'emensageria.s1080',
    'emensageria.s1200',
    'emensageria.s1202',
    'emensageria.s1207',
    'emensageria.s1210',
    'emensageria.s1250',
    'emensageria.s1260',
    'emensageria.s1270',
    'emensageria.s1280',
    'emensageria.s1295',
    'emensageria.s1298',
    'emensageria.s1299',
    'emensageria.s1300',
    'emensageria.s2190',
    'emensageria.s2200',
    'emensageria.s2205',
    'emensageria.s2206',
    'emensageria.s2210',
    'emensageria.s2220',
    'emensageria.s2230',
    'emensageria.s2240',
    'emensageria.s2241',
    'emensageria.s2250',
    'emensageria.s2260',
    'emensageria.s2298',
    'emensageria.s2299',
    'emensageria.s2300',
    'emensageria.s2306',
    'emensageria.s2399',
    'emensageria.s2400',
    'emensageria.s3000',
    'emensageria.s5001',
    'emensageria.s5002',
    'emensageria.s5011',
    'emensageria.s5012',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'emensageria.urls'

WSGI_APPLICATION = 'emensageria.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Internacionalização

LANGUAGE_CODE = 'pt-BR'

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = True

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#
# )

STATIC_URL = 'http://static.dominio.com.br/'
MEDIA_URL = 'http://media.dominio.com.br/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurações de Versão do Aplicativo - NÂO ALTERAR

VERSAO_EMENSAGERIA = versao['versao']
VERSAO_MODELO = versao['versao_esocial']



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts permitidos em Produção (obrigatório caso o DEBUG = False)

ALLOWED_HOSTS = [
    'www.dominio.com.br',
]

# Configuração do Banco de Dados

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nome-do-banco-de-dados',
        'USER': 'usuario-do-banco-de-dados',
        'PASSWORD': 'senha-do-banco-de-dados',
        'HOST': 'caminho-do-banco-de-dados',
        'PORT': '5432',
    },
}


# E-mail Config

EMAIL_HOST = 'smtp.dominio.com.br'
EMAIL_HOST_USER = 'contato@dominio.com.br'
EMAIL_HOST_PASSWORD = 'senha-do-email'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = 'contato@dominio.com.br'


# Configurações de Certificado

CERT_HOST = 'certificados/certificado.pfx'
CERT_PASS = 'senha-do-certificado'
CERT_PEM_FILE = 'certificados/cert.pem'
KEY_PEM_FILE = 'certificados/key.pem'
CA_CERT_PEM_FILE = 'certificados/acserproacfv5.crt'

# Configurações Específicas do eSocial

TP_AMB = 2 # 1-Produção; 2-Produção Restrita
FORCE_PRODUCAO_RESTRITA = True

# Chave para ter acesso a função de enviar e consultar eventos pela URL

PASS_SCRIPT = '123456'