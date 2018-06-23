#coding: utf-8

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

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.
    
        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



SIM_NAO = (
    (0, u'Não'),
    (1, u'Sim'),
)

TIPOS_CONFIG_PAGINAS = (
    (0, u'Manual'),
    (1, u'Automático'),
)

class ConfigModulos(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    modulo_pai = models.ForeignKey('ConfigModulos',
        related_name='%(class)s_modulo_pai', blank=True, null=True)
    ordem = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_modulos_custom#
    class Meta:
        db_table = r'config_modulos'
        managed = True
        ordering = ['titulo']


class ConfigPaginas(models.Model):
    config_modulos = models.ForeignKey('ConfigModulos',
        related_name='%(class)s_config_modulos')
    titulo = models.CharField(max_length=2000)
    endereco = models.CharField(max_length=500)
    exibe_menu = models.IntegerField(choices=SIM_NAO)
    tipo = models.IntegerField(choices=TIPOS_CONFIG_PAGINAS)
    ordem = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_paginas_custom#
    class Meta:
        db_table = r'config_paginas'
        managed = True
        ordering = ['titulo']


class ConfigPerfis(models.Model):
    titulo = models.CharField(max_length=25)
    permissoes = models.TextField(blank=True, null=True)
    modulos_permitidos = models.TextField(blank=True, null=True)
    paginas_permitidas = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.titulo)
    #config_perfis_custom#
    class Meta:
        db_table = r'config_perfis'
        managed = True
        ordering = ['titulo']


class ConfigPermissoes(models.Model):
    config_perfis = models.ForeignKey('ConfigPerfis',
        related_name='%(class)s_config_perfis')
    config_paginas = models.ForeignKey('ConfigPaginas',
        related_name='%(class)s_config_paginas')
    permite_listar = models.IntegerField(choices=SIM_NAO)
    permite_cadastrar = models.IntegerField(choices=SIM_NAO)
    permite_editar = models.IntegerField(choices=SIM_NAO)
    permite_visualizar = models.IntegerField(choices=SIM_NAO)
    permite_apagar = models.IntegerField(choices=SIM_NAO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.config_perfis) + ' - ' + unicode(self.config_paginas)
    #config_permissoes_custom#
    class Meta:
        db_table = r'config_permissoes'
        managed = True
        ordering = ['config_perfis', 'config_paginas']


class Usuarios(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=300, blank=True, default='asdkl1231')
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    config_perfis = models.ForeignKey('ConfigPerfis',
        related_name='%(class)s_config_perfis')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.nome) + ' - ' + unicode(self.config_perfis)
    #usuarios_custom#
    class Meta:
        db_table = r'usuarios'
        managed = True
        ordering = ['nome', 'config_perfis']


#VIEWS_MODELS
