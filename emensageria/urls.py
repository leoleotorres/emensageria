#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:

url(r'^recuperar-senha/$',
        'emensageria.controle_de_acesso.views.login_recuperar_senha.recuperar_senha',
        name='recuperar_senha'),

url(r'^alterar-senha/$',
        'emensageria.controle_de_acesso.views.login_alterar_senha.alterar_senha',
        name='alterar_senha'),

url(r'^transmissor-eventos/vincular/(?P<hash>.+)/$',
        'emensageria.mensageiro.views.transmissor.vincular_eventos',
        name='vincular_eventos'),
        
url(r'^transmissor-eventos/desvincular/(?P<hash>.+)/$',
        'emensageria.mensageiro.views.transmissor.desvincular_eventos',
        name='desvincular_eventos'),

url(r'^scripts/enviar-lote/(?P<chave>.*)/(?P<transmissor_lote_id>\d+)/$',
        'emensageria.mensageiro.views.transmissor_lote_comunicacao.scripts_enviar_lote',
        name='scripts_enviar_lote'),

url(r'^scripts/consultar-lote/(?P<chave>.*)/(?P<transmissor_lote_id>\d+)/$',
        'emensageria.mensageiro.views.transmissor_lote_comunicacao.scripts_consultar_lote',
        name='scripts_consultar_lote'),

url(r'^transmissor-lote/enviar/(?P<hash>.*)/$',
        'emensageria.mensageiro.views.transmissor_lote_comunicacao.enviar',
        name='transmissor_lote_enviar'),

url(r'^transmissor-lote/consultar/(?P<hash>.*)/$',
        'emensageria.mensageiro.views.transmissor_lote_comunicacao.consultar',
        name='transmissor_lote_consultar'),
        
        
url(r'^transmissor-lote/recibo/(?P<hash>.*)/$',
        'emensageria.mensageiro.views.transmissor_lote_comunicacao.recibo',
        name='transmissor_lote_recibo'),

url(r'^$',
        'emensageria.controle_de_acesso.views.login.login', 
        name='login'),









url(r'^config-modulos/listar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_modulos.listar', 
        name='config_modulos'),

url(r'^config-modulos/salvar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_modulos.salvar', 
        name='config_modulos_salvar'),

url(r'^config-modulos/apagar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_modulos.apagar', 
        name='config_modulos_apagar'),



url(r'^config-paginas/listar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_paginas.listar', 
        name='config_paginas'),

url(r'^config-paginas/salvar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_paginas.salvar', 
        name='config_paginas_salvar'),

url(r'^config-paginas/apagar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_paginas.apagar', 
        name='config_paginas_apagar'),



url(r'^config-perfis/listar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_perfis.listar', 
        name='config_perfis'),

url(r'^config-perfis/salvar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_perfis.salvar', 
        name='config_perfis_salvar'),

url(r'^config-perfis/apagar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_perfis.apagar', 
        name='config_perfis_apagar'),



url(r'^config-permissoes/listar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_permissoes.listar', 
        name='config_permissoes'),

url(r'^config-permissoes/salvar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_permissoes.salvar', 
        name='config_permissoes_salvar'),

url(r'^config-permissoes/apagar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.config_permissoes.apagar', 
        name='config_permissoes_apagar'),



url(r'^usuarios/listar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.usuarios.listar', 
        name='usuarios'),

url(r'^usuarios/salvar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.usuarios.salvar', 
        name='usuarios_salvar'),

url(r'^usuarios/apagar/(?P<hash>.*)/$', 
        'emensageria.controle_de_acesso.views.usuarios.apagar', 
        name='usuarios_apagar'),



url(r'^transmissor-lote/listar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote.listar', 
        name='transmissor_lote'),

url(r'^transmissor-lote/salvar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote.salvar', 
        name='transmissor_lote_salvar'),

url(r'^transmissor-lote/apagar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote.apagar', 
        name='transmissor_lote_apagar'),



url(r'^transmissor-lote-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote_ocorrencias.listar', 
        name='transmissor_lote_ocorrencias'),

url(r'^transmissor-lote-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote_ocorrencias.salvar', 
        name='transmissor_lote_ocorrencias_salvar'),

url(r'^transmissor-lote-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.mensageiro.views.transmissor_lote_ocorrencias.apagar', 
        name='transmissor_lote_ocorrencias_apagar'),

)


urlpatterns += patterns('',


url(r'^s1000-evtinfoempregador/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador.apagar', 
        name='s1000_evtinfoempregador_apagar'),

url(r'^s1000-evtinfoempregador/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador.listar', 
        name='s1000_evtinfoempregador'),
        
url(r'^s1000-evtinfoempregador/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_verificar.verificar', 
        name='s1000_evtinfoempregador_verificar'),
        
url(r'^s1000-evtinfoempregador/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_verificar.recibo', 
        name='s1000_evtinfoempregador_recibo'),
        
url(r'^s1000-evtinfoempregador/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_verificar.gerar_xml', 
        name='s1000_evtinfoempregador_xml'),

url(r'^s1000-evtinfoempregador/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador.salvar', 
        name='s1000_evtinfoempregador_salvar'),
        

url(r'^scripts/gerar-identidade/s1000-evtinfoempregador/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1000_evtinfoempregador.gerar_identidade', 
        name='s1000_evtinfoempregador_gerar_identidade'),



url(r'^s1005-evttabestab/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab.apagar', 
        name='s1005_evttabestab_apagar'),

url(r'^s1005-evttabestab/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab.listar', 
        name='s1005_evttabestab'),
        
url(r'^s1005-evttabestab/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_verificar.verificar', 
        name='s1005_evttabestab_verificar'),
        
url(r'^s1005-evttabestab/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_verificar.recibo', 
        name='s1005_evttabestab_recibo'),
        
url(r'^s1005-evttabestab/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_verificar.gerar_xml', 
        name='s1005_evttabestab_xml'),

url(r'^s1005-evttabestab/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab.salvar', 
        name='s1005_evttabestab_salvar'),
        

url(r'^scripts/gerar-identidade/s1005-evttabestab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1005_evttabestab.gerar_identidade', 
        name='s1005_evttabestab_gerar_identidade'),



url(r'^s1010-evttabrubrica/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica.apagar', 
        name='s1010_evttabrubrica_apagar'),

url(r'^s1010-evttabrubrica/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica.listar', 
        name='s1010_evttabrubrica'),
        
url(r'^s1010-evttabrubrica/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_verificar.verificar', 
        name='s1010_evttabrubrica_verificar'),
        
url(r'^s1010-evttabrubrica/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_verificar.recibo', 
        name='s1010_evttabrubrica_recibo'),
        
url(r'^s1010-evttabrubrica/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_verificar.gerar_xml', 
        name='s1010_evttabrubrica_xml'),

url(r'^s1010-evttabrubrica/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica.salvar', 
        name='s1010_evttabrubrica_salvar'),
        

url(r'^scripts/gerar-identidade/s1010-evttabrubrica/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1010_evttabrubrica.gerar_identidade', 
        name='s1010_evttabrubrica_gerar_identidade'),



url(r'^s1020-evttablotacao/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao.apagar', 
        name='s1020_evttablotacao_apagar'),

url(r'^s1020-evttablotacao/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao.listar', 
        name='s1020_evttablotacao'),
        
url(r'^s1020-evttablotacao/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_verificar.verificar', 
        name='s1020_evttablotacao_verificar'),
        
url(r'^s1020-evttablotacao/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_verificar.recibo', 
        name='s1020_evttablotacao_recibo'),
        
url(r'^s1020-evttablotacao/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_verificar.gerar_xml', 
        name='s1020_evttablotacao_xml'),

url(r'^s1020-evttablotacao/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao.salvar', 
        name='s1020_evttablotacao_salvar'),
        

url(r'^scripts/gerar-identidade/s1020-evttablotacao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1020_evttablotacao.gerar_identidade', 
        name='s1020_evttablotacao_gerar_identidade'),



url(r'^s1030-evttabcargo/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo.apagar', 
        name='s1030_evttabcargo_apagar'),

url(r'^s1030-evttabcargo/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo.listar', 
        name='s1030_evttabcargo'),
        
url(r'^s1030-evttabcargo/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_verificar.verificar', 
        name='s1030_evttabcargo_verificar'),
        
url(r'^s1030-evttabcargo/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_verificar.recibo', 
        name='s1030_evttabcargo_recibo'),
        
url(r'^s1030-evttabcargo/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_verificar.gerar_xml', 
        name='s1030_evttabcargo_xml'),

url(r'^s1030-evttabcargo/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo.salvar', 
        name='s1030_evttabcargo_salvar'),
        

url(r'^scripts/gerar-identidade/s1030-evttabcargo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1030_evttabcargo.gerar_identidade', 
        name='s1030_evttabcargo_gerar_identidade'),



url(r'^s1035-evttabcarreira/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira.apagar', 
        name='s1035_evttabcarreira_apagar'),

url(r'^s1035-evttabcarreira/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira.listar', 
        name='s1035_evttabcarreira'),
        
url(r'^s1035-evttabcarreira/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_verificar.verificar', 
        name='s1035_evttabcarreira_verificar'),
        
url(r'^s1035-evttabcarreira/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_verificar.recibo', 
        name='s1035_evttabcarreira_recibo'),
        
url(r'^s1035-evttabcarreira/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_verificar.gerar_xml', 
        name='s1035_evttabcarreira_xml'),

url(r'^s1035-evttabcarreira/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira.salvar', 
        name='s1035_evttabcarreira_salvar'),
        

url(r'^scripts/gerar-identidade/s1035-evttabcarreira/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1035_evttabcarreira.gerar_identidade', 
        name='s1035_evttabcarreira_gerar_identidade'),



url(r'^s1040-evttabfuncao/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao.apagar', 
        name='s1040_evttabfuncao_apagar'),

url(r'^s1040-evttabfuncao/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao.listar', 
        name='s1040_evttabfuncao'),
        
url(r'^s1040-evttabfuncao/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_verificar.verificar', 
        name='s1040_evttabfuncao_verificar'),
        
url(r'^s1040-evttabfuncao/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_verificar.recibo', 
        name='s1040_evttabfuncao_recibo'),
        
url(r'^s1040-evttabfuncao/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_verificar.gerar_xml', 
        name='s1040_evttabfuncao_xml'),

url(r'^s1040-evttabfuncao/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao.salvar', 
        name='s1040_evttabfuncao_salvar'),
        

url(r'^scripts/gerar-identidade/s1040-evttabfuncao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1040_evttabfuncao.gerar_identidade', 
        name='s1040_evttabfuncao_gerar_identidade'),



url(r'^s1050-evttabhortur/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur.apagar', 
        name='s1050_evttabhortur_apagar'),

url(r'^s1050-evttabhortur/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur.listar', 
        name='s1050_evttabhortur'),
        
url(r'^s1050-evttabhortur/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_verificar.verificar', 
        name='s1050_evttabhortur_verificar'),
        
url(r'^s1050-evttabhortur/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_verificar.recibo', 
        name='s1050_evttabhortur_recibo'),
        
url(r'^s1050-evttabhortur/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_verificar.gerar_xml', 
        name='s1050_evttabhortur_xml'),

url(r'^s1050-evttabhortur/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur.salvar', 
        name='s1050_evttabhortur_salvar'),
        

url(r'^scripts/gerar-identidade/s1050-evttabhortur/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1050_evttabhortur.gerar_identidade', 
        name='s1050_evttabhortur_gerar_identidade'),



url(r'^s1060-evttabambiente/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente.apagar', 
        name='s1060_evttabambiente_apagar'),

url(r'^s1060-evttabambiente/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente.listar', 
        name='s1060_evttabambiente'),
        
url(r'^s1060-evttabambiente/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_verificar.verificar', 
        name='s1060_evttabambiente_verificar'),
        
url(r'^s1060-evttabambiente/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_verificar.recibo', 
        name='s1060_evttabambiente_recibo'),
        
url(r'^s1060-evttabambiente/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_verificar.gerar_xml', 
        name='s1060_evttabambiente_xml'),

url(r'^s1060-evttabambiente/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente.salvar', 
        name='s1060_evttabambiente_salvar'),
        

url(r'^scripts/gerar-identidade/s1060-evttabambiente/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1060_evttabambiente.gerar_identidade', 
        name='s1060_evttabambiente_gerar_identidade'),



url(r'^s1070-evttabprocesso/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso.apagar', 
        name='s1070_evttabprocesso_apagar'),

url(r'^s1070-evttabprocesso/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso.listar', 
        name='s1070_evttabprocesso'),
        
url(r'^s1070-evttabprocesso/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_verificar.verificar', 
        name='s1070_evttabprocesso_verificar'),
        
url(r'^s1070-evttabprocesso/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_verificar.recibo', 
        name='s1070_evttabprocesso_recibo'),
        
url(r'^s1070-evttabprocesso/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_verificar.gerar_xml', 
        name='s1070_evttabprocesso_xml'),

url(r'^s1070-evttabprocesso/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso.salvar', 
        name='s1070_evttabprocesso_salvar'),
        

url(r'^scripts/gerar-identidade/s1070-evttabprocesso/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1070_evttabprocesso.gerar_identidade', 
        name='s1070_evttabprocesso_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s1080-evttaboperport/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport.apagar', 
        name='s1080_evttaboperport_apagar'),

url(r'^s1080-evttaboperport/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport.listar', 
        name='s1080_evttaboperport'),
        
url(r'^s1080-evttaboperport/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_verificar.verificar', 
        name='s1080_evttaboperport_verificar'),
        
url(r'^s1080-evttaboperport/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_verificar.recibo', 
        name='s1080_evttaboperport_recibo'),
        
url(r'^s1080-evttaboperport/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_verificar.gerar_xml', 
        name='s1080_evttaboperport_xml'),

url(r'^s1080-evttaboperport/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport.salvar', 
        name='s1080_evttaboperport_salvar'),
        

url(r'^scripts/gerar-identidade/s1080-evttaboperport/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1080_evttaboperport.gerar_identidade', 
        name='s1080_evttaboperport_gerar_identidade'),



url(r'^s1200-evtremun/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun.apagar', 
        name='s1200_evtremun_apagar'),

url(r'^s1200-evtremun/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun.listar', 
        name='s1200_evtremun'),
        
url(r'^s1200-evtremun/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_verificar.verificar', 
        name='s1200_evtremun_verificar'),
        
url(r'^s1200-evtremun/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_verificar.recibo', 
        name='s1200_evtremun_recibo'),
        
url(r'^s1200-evtremun/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_verificar.gerar_xml', 
        name='s1200_evtremun_xml'),

url(r'^s1200-evtremun/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun.salvar', 
        name='s1200_evtremun_salvar'),
        

url(r'^scripts/gerar-identidade/s1200-evtremun/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1200_evtremun.gerar_identidade', 
        name='s1200_evtremun_gerar_identidade'),



url(r'^s1202-evtrmnrpps/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps.apagar', 
        name='s1202_evtrmnrpps_apagar'),

url(r'^s1202-evtrmnrpps/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps.listar', 
        name='s1202_evtrmnrpps'),
        
url(r'^s1202-evtrmnrpps/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_verificar.verificar', 
        name='s1202_evtrmnrpps_verificar'),
        
url(r'^s1202-evtrmnrpps/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_verificar.recibo', 
        name='s1202_evtrmnrpps_recibo'),
        
url(r'^s1202-evtrmnrpps/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_verificar.gerar_xml', 
        name='s1202_evtrmnrpps_xml'),

url(r'^s1202-evtrmnrpps/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps.salvar', 
        name='s1202_evtrmnrpps_salvar'),
        

url(r'^scripts/gerar-identidade/s1202-evtrmnrpps/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1202_evtrmnrpps.gerar_identidade', 
        name='s1202_evtrmnrpps_gerar_identidade'),



url(r'^s1207-evtbenprrp/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp.apagar', 
        name='s1207_evtbenprrp_apagar'),

url(r'^s1207-evtbenprrp/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp.listar', 
        name='s1207_evtbenprrp'),
        
url(r'^s1207-evtbenprrp/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_verificar.verificar', 
        name='s1207_evtbenprrp_verificar'),
        
url(r'^s1207-evtbenprrp/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_verificar.recibo', 
        name='s1207_evtbenprrp_recibo'),
        
url(r'^s1207-evtbenprrp/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_verificar.gerar_xml', 
        name='s1207_evtbenprrp_xml'),

url(r'^s1207-evtbenprrp/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp.salvar', 
        name='s1207_evtbenprrp_salvar'),
        

url(r'^scripts/gerar-identidade/s1207-evtbenprrp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1207_evtbenprrp.gerar_identidade', 
        name='s1207_evtbenprrp_gerar_identidade'),



url(r'^s1210-evtpgtos/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos.apagar', 
        name='s1210_evtpgtos_apagar'),

url(r'^s1210-evtpgtos/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos.listar', 
        name='s1210_evtpgtos'),
        
url(r'^s1210-evtpgtos/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_verificar.verificar', 
        name='s1210_evtpgtos_verificar'),
        
url(r'^s1210-evtpgtos/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_verificar.recibo', 
        name='s1210_evtpgtos_recibo'),
        
url(r'^s1210-evtpgtos/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_verificar.gerar_xml', 
        name='s1210_evtpgtos_xml'),

url(r'^s1210-evtpgtos/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos.salvar', 
        name='s1210_evtpgtos_salvar'),
        

url(r'^scripts/gerar-identidade/s1210-evtpgtos/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1210_evtpgtos.gerar_identidade', 
        name='s1210_evtpgtos_gerar_identidade'),



url(r'^s1250-evtaqprod/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod.apagar', 
        name='s1250_evtaqprod_apagar'),

url(r'^s1250-evtaqprod/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod.listar', 
        name='s1250_evtaqprod'),
        
url(r'^s1250-evtaqprod/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_verificar.verificar', 
        name='s1250_evtaqprod_verificar'),
        
url(r'^s1250-evtaqprod/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_verificar.recibo', 
        name='s1250_evtaqprod_recibo'),
        
url(r'^s1250-evtaqprod/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_verificar.gerar_xml', 
        name='s1250_evtaqprod_xml'),

url(r'^s1250-evtaqprod/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod.salvar', 
        name='s1250_evtaqprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1250-evtaqprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1250_evtaqprod.gerar_identidade', 
        name='s1250_evtaqprod_gerar_identidade'),



url(r'^s1260-evtcomprod/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod.apagar', 
        name='s1260_evtcomprod_apagar'),

url(r'^s1260-evtcomprod/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod.listar', 
        name='s1260_evtcomprod'),
        
url(r'^s1260-evtcomprod/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_verificar.verificar', 
        name='s1260_evtcomprod_verificar'),
        
url(r'^s1260-evtcomprod/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_verificar.recibo', 
        name='s1260_evtcomprod_recibo'),
        
url(r'^s1260-evtcomprod/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_verificar.gerar_xml', 
        name='s1260_evtcomprod_xml'),

url(r'^s1260-evtcomprod/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod.salvar', 
        name='s1260_evtcomprod_salvar'),
        

url(r'^scripts/gerar-identidade/s1260-evtcomprod/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1260_evtcomprod.gerar_identidade', 
        name='s1260_evtcomprod_gerar_identidade'),



url(r'^s1270-evtcontratavnp/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp.apagar', 
        name='s1270_evtcontratavnp_apagar'),

url(r'^s1270-evtcontratavnp/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp.listar', 
        name='s1270_evtcontratavnp'),
        
url(r'^s1270-evtcontratavnp/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_verificar.verificar', 
        name='s1270_evtcontratavnp_verificar'),
        
url(r'^s1270-evtcontratavnp/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_verificar.recibo', 
        name='s1270_evtcontratavnp_recibo'),
        
url(r'^s1270-evtcontratavnp/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_verificar.gerar_xml', 
        name='s1270_evtcontratavnp_xml'),

url(r'^s1270-evtcontratavnp/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp.salvar', 
        name='s1270_evtcontratavnp_salvar'),
        

url(r'^scripts/gerar-identidade/s1270-evtcontratavnp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1270_evtcontratavnp.gerar_identidade', 
        name='s1270_evtcontratavnp_gerar_identidade'),



url(r'^s1280-evtinfocomplper/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper.apagar', 
        name='s1280_evtinfocomplper_apagar'),

url(r'^s1280-evtinfocomplper/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper.listar', 
        name='s1280_evtinfocomplper'),
        
url(r'^s1280-evtinfocomplper/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_verificar.verificar', 
        name='s1280_evtinfocomplper_verificar'),
        
url(r'^s1280-evtinfocomplper/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_verificar.recibo', 
        name='s1280_evtinfocomplper_recibo'),
        
url(r'^s1280-evtinfocomplper/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_verificar.gerar_xml', 
        name='s1280_evtinfocomplper_xml'),

url(r'^s1280-evtinfocomplper/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper.salvar', 
        name='s1280_evtinfocomplper_salvar'),
        

url(r'^scripts/gerar-identidade/s1280-evtinfocomplper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1280_evtinfocomplper.gerar_identidade', 
        name='s1280_evtinfocomplper_gerar_identidade'),



url(r'^s1295-evttotconting/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting.apagar', 
        name='s1295_evttotconting_apagar'),

url(r'^s1295-evttotconting/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting.listar', 
        name='s1295_evttotconting'),
        
url(r'^s1295-evttotconting/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_verificar.verificar', 
        name='s1295_evttotconting_verificar'),
        
url(r'^s1295-evttotconting/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_verificar.recibo', 
        name='s1295_evttotconting_recibo'),
        
url(r'^s1295-evttotconting/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_verificar.gerar_xml', 
        name='s1295_evttotconting_xml'),

url(r'^s1295-evttotconting/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting.salvar', 
        name='s1295_evttotconting_salvar'),
        

url(r'^scripts/gerar-identidade/s1295-evttotconting/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1295_evttotconting.gerar_identidade', 
        name='s1295_evttotconting_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s1298-evtreabreevper/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper.apagar', 
        name='s1298_evtreabreevper_apagar'),

url(r'^s1298-evtreabreevper/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper.listar', 
        name='s1298_evtreabreevper'),
        
url(r'^s1298-evtreabreevper/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_verificar.verificar', 
        name='s1298_evtreabreevper_verificar'),
        
url(r'^s1298-evtreabreevper/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_verificar.recibo', 
        name='s1298_evtreabreevper_recibo'),
        
url(r'^s1298-evtreabreevper/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_verificar.gerar_xml', 
        name='s1298_evtreabreevper_xml'),

url(r'^s1298-evtreabreevper/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper.salvar', 
        name='s1298_evtreabreevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1298-evtreabreevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1298_evtreabreevper.gerar_identidade', 
        name='s1298_evtreabreevper_gerar_identidade'),



url(r'^s1299-evtfechaevper/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper.apagar', 
        name='s1299_evtfechaevper_apagar'),

url(r'^s1299-evtfechaevper/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper.listar', 
        name='s1299_evtfechaevper'),
        
url(r'^s1299-evtfechaevper/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_verificar.verificar', 
        name='s1299_evtfechaevper_verificar'),
        
url(r'^s1299-evtfechaevper/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_verificar.recibo', 
        name='s1299_evtfechaevper_recibo'),
        
url(r'^s1299-evtfechaevper/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_verificar.gerar_xml', 
        name='s1299_evtfechaevper_xml'),

url(r'^s1299-evtfechaevper/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper.salvar', 
        name='s1299_evtfechaevper_salvar'),
        

url(r'^scripts/gerar-identidade/s1299-evtfechaevper/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1299_evtfechaevper.gerar_identidade', 
        name='s1299_evtfechaevper_gerar_identidade'),



url(r'^s1300-evtcontrsindpatr/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr.apagar', 
        name='s1300_evtcontrsindpatr_apagar'),

url(r'^s1300-evtcontrsindpatr/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr.listar', 
        name='s1300_evtcontrsindpatr'),
        
url(r'^s1300-evtcontrsindpatr/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_verificar.verificar', 
        name='s1300_evtcontrsindpatr_verificar'),
        
url(r'^s1300-evtcontrsindpatr/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_verificar.recibo', 
        name='s1300_evtcontrsindpatr_recibo'),
        
url(r'^s1300-evtcontrsindpatr/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_verificar.gerar_xml', 
        name='s1300_evtcontrsindpatr_xml'),

url(r'^s1300-evtcontrsindpatr/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr.salvar', 
        name='s1300_evtcontrsindpatr_salvar'),
        

url(r'^scripts/gerar-identidade/s1300-evtcontrsindpatr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s1300_evtcontrsindpatr.gerar_identidade', 
        name='s1300_evtcontrsindpatr_gerar_identidade'),



url(r'^s2190-evtadmprelim/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim.apagar', 
        name='s2190_evtadmprelim_apagar'),

url(r'^s2190-evtadmprelim/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim.listar', 
        name='s2190_evtadmprelim'),
        
url(r'^s2190-evtadmprelim/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_verificar.verificar', 
        name='s2190_evtadmprelim_verificar'),
        
url(r'^s2190-evtadmprelim/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_verificar.recibo', 
        name='s2190_evtadmprelim_recibo'),
        
url(r'^s2190-evtadmprelim/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_verificar.gerar_xml', 
        name='s2190_evtadmprelim_xml'),

url(r'^s2190-evtadmprelim/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim.salvar', 
        name='s2190_evtadmprelim_salvar'),
        

url(r'^scripts/gerar-identidade/s2190-evtadmprelim/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2190_evtadmprelim.gerar_identidade', 
        name='s2190_evtadmprelim_gerar_identidade'),



url(r'^s2200-evtadmissao/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao.apagar', 
        name='s2200_evtadmissao_apagar'),

url(r'^s2200-evtadmissao/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao.listar', 
        name='s2200_evtadmissao'),
        
url(r'^s2200-evtadmissao/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_verificar.verificar', 
        name='s2200_evtadmissao_verificar'),
        
url(r'^s2200-evtadmissao/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_verificar.recibo', 
        name='s2200_evtadmissao_recibo'),
        
url(r'^s2200-evtadmissao/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_verificar.gerar_xml', 
        name='s2200_evtadmissao_xml'),

url(r'^s2200-evtadmissao/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao.salvar', 
        name='s2200_evtadmissao_salvar'),
        

url(r'^scripts/gerar-identidade/s2200-evtadmissao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2200_evtadmissao.gerar_identidade', 
        name='s2200_evtadmissao_gerar_identidade'),



url(r'^s2205-evtaltcadastral/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral.apagar', 
        name='s2205_evtaltcadastral_apagar'),

url(r'^s2205-evtaltcadastral/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral.listar', 
        name='s2205_evtaltcadastral'),
        
url(r'^s2205-evtaltcadastral/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_verificar.verificar', 
        name='s2205_evtaltcadastral_verificar'),
        
url(r'^s2205-evtaltcadastral/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_verificar.recibo', 
        name='s2205_evtaltcadastral_recibo'),
        
url(r'^s2205-evtaltcadastral/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_verificar.gerar_xml', 
        name='s2205_evtaltcadastral_xml'),

url(r'^s2205-evtaltcadastral/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral.salvar', 
        name='s2205_evtaltcadastral_salvar'),
        

url(r'^scripts/gerar-identidade/s2205-evtaltcadastral/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2205_evtaltcadastral.gerar_identidade', 
        name='s2205_evtaltcadastral_gerar_identidade'),



url(r'^s2206-evtaltcontratual/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual.apagar', 
        name='s2206_evtaltcontratual_apagar'),

url(r'^s2206-evtaltcontratual/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual.listar', 
        name='s2206_evtaltcontratual'),
        
url(r'^s2206-evtaltcontratual/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_verificar.verificar', 
        name='s2206_evtaltcontratual_verificar'),
        
url(r'^s2206-evtaltcontratual/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_verificar.recibo', 
        name='s2206_evtaltcontratual_recibo'),
        
url(r'^s2206-evtaltcontratual/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_verificar.gerar_xml', 
        name='s2206_evtaltcontratual_xml'),

url(r'^s2206-evtaltcontratual/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual.salvar', 
        name='s2206_evtaltcontratual_salvar'),
        

url(r'^scripts/gerar-identidade/s2206-evtaltcontratual/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2206_evtaltcontratual.gerar_identidade', 
        name='s2206_evtaltcontratual_gerar_identidade'),



url(r'^s2210-evtcat/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat.apagar', 
        name='s2210_evtcat_apagar'),

url(r'^s2210-evtcat/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat.listar', 
        name='s2210_evtcat'),
        
url(r'^s2210-evtcat/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_verificar.verificar', 
        name='s2210_evtcat_verificar'),
        
url(r'^s2210-evtcat/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_verificar.recibo', 
        name='s2210_evtcat_recibo'),
        
url(r'^s2210-evtcat/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_verificar.gerar_xml', 
        name='s2210_evtcat_xml'),

url(r'^s2210-evtcat/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat.salvar', 
        name='s2210_evtcat_salvar'),
        

url(r'^scripts/gerar-identidade/s2210-evtcat/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2210_evtcat.gerar_identidade', 
        name='s2210_evtcat_gerar_identidade'),



url(r'^s2220-evtmonit/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit.apagar', 
        name='s2220_evtmonit_apagar'),

url(r'^s2220-evtmonit/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit.listar', 
        name='s2220_evtmonit'),
        
url(r'^s2220-evtmonit/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_verificar.verificar', 
        name='s2220_evtmonit_verificar'),
        
url(r'^s2220-evtmonit/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_verificar.recibo', 
        name='s2220_evtmonit_recibo'),
        
url(r'^s2220-evtmonit/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_verificar.gerar_xml', 
        name='s2220_evtmonit_xml'),

url(r'^s2220-evtmonit/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit.salvar', 
        name='s2220_evtmonit_salvar'),
        

url(r'^scripts/gerar-identidade/s2220-evtmonit/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2220_evtmonit.gerar_identidade', 
        name='s2220_evtmonit_gerar_identidade'),



url(r'^s2230-evtafasttemp/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp.apagar', 
        name='s2230_evtafasttemp_apagar'),

url(r'^s2230-evtafasttemp/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp.listar', 
        name='s2230_evtafasttemp'),
        
url(r'^s2230-evtafasttemp/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_verificar.verificar', 
        name='s2230_evtafasttemp_verificar'),
        
url(r'^s2230-evtafasttemp/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_verificar.recibo', 
        name='s2230_evtafasttemp_recibo'),
        
url(r'^s2230-evtafasttemp/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_verificar.gerar_xml', 
        name='s2230_evtafasttemp_xml'),

url(r'^s2230-evtafasttemp/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp.salvar', 
        name='s2230_evtafasttemp_salvar'),
        

url(r'^scripts/gerar-identidade/s2230-evtafasttemp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2230_evtafasttemp.gerar_identidade', 
        name='s2230_evtafasttemp_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s2240-evtexprisco/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco.apagar', 
        name='s2240_evtexprisco_apagar'),

url(r'^s2240-evtexprisco/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco.listar', 
        name='s2240_evtexprisco'),
        
url(r'^s2240-evtexprisco/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_verificar.verificar', 
        name='s2240_evtexprisco_verificar'),
        
url(r'^s2240-evtexprisco/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_verificar.recibo', 
        name='s2240_evtexprisco_recibo'),
        
url(r'^s2240-evtexprisco/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_verificar.gerar_xml', 
        name='s2240_evtexprisco_xml'),

url(r'^s2240-evtexprisco/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco.salvar', 
        name='s2240_evtexprisco_salvar'),
        

url(r'^scripts/gerar-identidade/s2240-evtexprisco/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2240_evtexprisco.gerar_identidade', 
        name='s2240_evtexprisco_gerar_identidade'),



url(r'^s2241-evtinsapo/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo.apagar', 
        name='s2241_evtinsapo_apagar'),

url(r'^s2241-evtinsapo/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo.listar', 
        name='s2241_evtinsapo'),
        
url(r'^s2241-evtinsapo/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_verificar.verificar', 
        name='s2241_evtinsapo_verificar'),
        
url(r'^s2241-evtinsapo/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_verificar.recibo', 
        name='s2241_evtinsapo_recibo'),
        
url(r'^s2241-evtinsapo/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_verificar.gerar_xml', 
        name='s2241_evtinsapo_xml'),

url(r'^s2241-evtinsapo/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo.salvar', 
        name='s2241_evtinsapo_salvar'),
        

url(r'^scripts/gerar-identidade/s2241-evtinsapo/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2241_evtinsapo.gerar_identidade', 
        name='s2241_evtinsapo_gerar_identidade'),



url(r'^s2250-evtavprevio/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio.apagar', 
        name='s2250_evtavprevio_apagar'),

url(r'^s2250-evtavprevio/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio.listar', 
        name='s2250_evtavprevio'),
        
url(r'^s2250-evtavprevio/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_verificar.verificar', 
        name='s2250_evtavprevio_verificar'),
        
url(r'^s2250-evtavprevio/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_verificar.recibo', 
        name='s2250_evtavprevio_recibo'),
        
url(r'^s2250-evtavprevio/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_verificar.gerar_xml', 
        name='s2250_evtavprevio_xml'),

url(r'^s2250-evtavprevio/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio.salvar', 
        name='s2250_evtavprevio_salvar'),
        

url(r'^scripts/gerar-identidade/s2250-evtavprevio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2250_evtavprevio.gerar_identidade', 
        name='s2250_evtavprevio_gerar_identidade'),



url(r'^s2260-evtconvinterm/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm.apagar', 
        name='s2260_evtconvinterm_apagar'),

url(r'^s2260-evtconvinterm/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm.listar', 
        name='s2260_evtconvinterm'),
        
url(r'^s2260-evtconvinterm/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_verificar.verificar', 
        name='s2260_evtconvinterm_verificar'),
        
url(r'^s2260-evtconvinterm/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_verificar.recibo', 
        name='s2260_evtconvinterm_recibo'),
        
url(r'^s2260-evtconvinterm/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_verificar.gerar_xml', 
        name='s2260_evtconvinterm_xml'),

url(r'^s2260-evtconvinterm/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm.salvar', 
        name='s2260_evtconvinterm_salvar'),
        

url(r'^scripts/gerar-identidade/s2260-evtconvinterm/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2260_evtconvinterm.gerar_identidade', 
        name='s2260_evtconvinterm_gerar_identidade'),



url(r'^s2298-evtreintegr/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr.apagar', 
        name='s2298_evtreintegr_apagar'),

url(r'^s2298-evtreintegr/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr.listar', 
        name='s2298_evtreintegr'),
        
url(r'^s2298-evtreintegr/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_verificar.verificar', 
        name='s2298_evtreintegr_verificar'),
        
url(r'^s2298-evtreintegr/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_verificar.recibo', 
        name='s2298_evtreintegr_recibo'),
        
url(r'^s2298-evtreintegr/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_verificar.gerar_xml', 
        name='s2298_evtreintegr_xml'),

url(r'^s2298-evtreintegr/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr.salvar', 
        name='s2298_evtreintegr_salvar'),
        

url(r'^scripts/gerar-identidade/s2298-evtreintegr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2298_evtreintegr.gerar_identidade', 
        name='s2298_evtreintegr_gerar_identidade'),



url(r'^s2299-evtdeslig/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig.apagar', 
        name='s2299_evtdeslig_apagar'),

url(r'^s2299-evtdeslig/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig.listar', 
        name='s2299_evtdeslig'),
        
url(r'^s2299-evtdeslig/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_verificar.verificar', 
        name='s2299_evtdeslig_verificar'),
        
url(r'^s2299-evtdeslig/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_verificar.recibo', 
        name='s2299_evtdeslig_recibo'),
        
url(r'^s2299-evtdeslig/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_verificar.gerar_xml', 
        name='s2299_evtdeslig_xml'),

url(r'^s2299-evtdeslig/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig.salvar', 
        name='s2299_evtdeslig_salvar'),
        

url(r'^scripts/gerar-identidade/s2299-evtdeslig/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2299_evtdeslig.gerar_identidade', 
        name='s2299_evtdeslig_gerar_identidade'),



url(r'^s2300-evttsvinicio/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio.apagar', 
        name='s2300_evttsvinicio_apagar'),

url(r'^s2300-evttsvinicio/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio.listar', 
        name='s2300_evttsvinicio'),
        
url(r'^s2300-evttsvinicio/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_verificar.verificar', 
        name='s2300_evttsvinicio_verificar'),
        
url(r'^s2300-evttsvinicio/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_verificar.recibo', 
        name='s2300_evttsvinicio_recibo'),
        
url(r'^s2300-evttsvinicio/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_verificar.gerar_xml', 
        name='s2300_evttsvinicio_xml'),

url(r'^s2300-evttsvinicio/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio.salvar', 
        name='s2300_evttsvinicio_salvar'),
        

url(r'^scripts/gerar-identidade/s2300-evttsvinicio/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2300_evttsvinicio.gerar_identidade', 
        name='s2300_evttsvinicio_gerar_identidade'),



url(r'^s2306-evttsvaltcontr/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr.apagar', 
        name='s2306_evttsvaltcontr_apagar'),

url(r'^s2306-evttsvaltcontr/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr.listar', 
        name='s2306_evttsvaltcontr'),
        
url(r'^s2306-evttsvaltcontr/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_verificar.verificar', 
        name='s2306_evttsvaltcontr_verificar'),
        
url(r'^s2306-evttsvaltcontr/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_verificar.recibo', 
        name='s2306_evttsvaltcontr_recibo'),
        
url(r'^s2306-evttsvaltcontr/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_verificar.gerar_xml', 
        name='s2306_evttsvaltcontr_xml'),

url(r'^s2306-evttsvaltcontr/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr.salvar', 
        name='s2306_evttsvaltcontr_salvar'),
        

url(r'^scripts/gerar-identidade/s2306-evttsvaltcontr/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2306_evttsvaltcontr.gerar_identidade', 
        name='s2306_evttsvaltcontr_gerar_identidade'),



url(r'^s2399-evttsvtermino/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino.apagar', 
        name='s2399_evttsvtermino_apagar'),

url(r'^s2399-evttsvtermino/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino.listar', 
        name='s2399_evttsvtermino'),
        
url(r'^s2399-evttsvtermino/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_verificar.verificar', 
        name='s2399_evttsvtermino_verificar'),
        
url(r'^s2399-evttsvtermino/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_verificar.recibo', 
        name='s2399_evttsvtermino_recibo'),
        
url(r'^s2399-evttsvtermino/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_verificar.gerar_xml', 
        name='s2399_evttsvtermino_xml'),

url(r'^s2399-evttsvtermino/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino.salvar', 
        name='s2399_evttsvtermino_salvar'),
        

url(r'^scripts/gerar-identidade/s2399-evttsvtermino/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2399_evttsvtermino.gerar_identidade', 
        name='s2399_evttsvtermino_gerar_identidade'),



url(r'^s2400-evtcdbenprrp/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp.apagar', 
        name='s2400_evtcdbenprrp_apagar'),

url(r'^s2400-evtcdbenprrp/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp.listar', 
        name='s2400_evtcdbenprrp'),
        
url(r'^s2400-evtcdbenprrp/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_verificar.verificar', 
        name='s2400_evtcdbenprrp_verificar'),
        
url(r'^s2400-evtcdbenprrp/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_verificar.recibo', 
        name='s2400_evtcdbenprrp_recibo'),
        
url(r'^s2400-evtcdbenprrp/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_verificar.gerar_xml', 
        name='s2400_evtcdbenprrp_xml'),

url(r'^s2400-evtcdbenprrp/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp.salvar', 
        name='s2400_evtcdbenprrp_salvar'),
        

url(r'^scripts/gerar-identidade/s2400-evtcdbenprrp/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s2400_evtcdbenprrp.gerar_identidade', 
        name='s2400_evtcdbenprrp_gerar_identidade'),

)


urlpatterns += patterns('',


url(r'^s3000-evtexclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao.apagar', 
        name='s3000_evtexclusao_apagar'),

url(r'^s3000-evtexclusao/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao.listar', 
        name='s3000_evtexclusao'),
        
url(r'^s3000-evtexclusao/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_verificar.verificar', 
        name='s3000_evtexclusao_verificar'),
        
url(r'^s3000-evtexclusao/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_verificar.recibo', 
        name='s3000_evtexclusao_recibo'),
        
url(r'^s3000-evtexclusao/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_verificar.gerar_xml', 
        name='s3000_evtexclusao_xml'),

url(r'^s3000-evtexclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao.salvar', 
        name='s3000_evtexclusao_salvar'),
        

url(r'^scripts/gerar-identidade/s3000-evtexclusao/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s3000_evtexclusao.gerar_identidade', 
        name='s3000_evtexclusao_gerar_identidade'),



url(r'^s5001-evtbasestrab/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab.apagar', 
        name='s5001_evtbasestrab_apagar'),

url(r'^s5001-evtbasestrab/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab.listar', 
        name='s5001_evtbasestrab'),
        
url(r'^s5001-evtbasestrab/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_verificar.verificar', 
        name='s5001_evtbasestrab_verificar'),
        
url(r'^s5001-evtbasestrab/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_verificar.recibo', 
        name='s5001_evtbasestrab_recibo'),
        
url(r'^s5001-evtbasestrab/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_verificar.gerar_xml', 
        name='s5001_evtbasestrab_xml'),

url(r'^s5001-evtbasestrab/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab.salvar', 
        name='s5001_evtbasestrab_salvar'),
        

url(r'^scripts/gerar-identidade/s5001-evtbasestrab/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s5001_evtbasestrab.gerar_identidade', 
        name='s5001_evtbasestrab_gerar_identidade'),



url(r'^s5002-evtirrfbenef/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef.apagar', 
        name='s5002_evtirrfbenef_apagar'),

url(r'^s5002-evtirrfbenef/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef.listar', 
        name='s5002_evtirrfbenef'),
        
url(r'^s5002-evtirrfbenef/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_verificar.verificar', 
        name='s5002_evtirrfbenef_verificar'),
        
url(r'^s5002-evtirrfbenef/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_verificar.recibo', 
        name='s5002_evtirrfbenef_recibo'),
        
url(r'^s5002-evtirrfbenef/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_verificar.gerar_xml', 
        name='s5002_evtirrfbenef_xml'),

url(r'^s5002-evtirrfbenef/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef.salvar', 
        name='s5002_evtirrfbenef_salvar'),
        

url(r'^scripts/gerar-identidade/s5002-evtirrfbenef/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s5002_evtirrfbenef.gerar_identidade', 
        name='s5002_evtirrfbenef_gerar_identidade'),



url(r'^s5011-evtcs/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs.apagar', 
        name='s5011_evtcs_apagar'),

url(r'^s5011-evtcs/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs.listar', 
        name='s5011_evtcs'),
        
url(r'^s5011-evtcs/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_verificar.verificar', 
        name='s5011_evtcs_verificar'),
        
url(r'^s5011-evtcs/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_verificar.recibo', 
        name='s5011_evtcs_recibo'),
        
url(r'^s5011-evtcs/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_verificar.gerar_xml', 
        name='s5011_evtcs_xml'),

url(r'^s5011-evtcs/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs.salvar', 
        name='s5011_evtcs_salvar'),
        

url(r'^scripts/gerar-identidade/s5011-evtcs/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s5011_evtcs.gerar_identidade', 
        name='s5011_evtcs_gerar_identidade'),



url(r'^s5012-evtirrf/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf.apagar', 
        name='s5012_evtirrf_apagar'),

url(r'^s5012-evtirrf/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf.listar', 
        name='s5012_evtirrf'),
        
url(r'^s5012-evtirrf/verificar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_verificar.verificar', 
        name='s5012_evtirrf_verificar'),
        
url(r'^s5012-evtirrf/recibo/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_verificar.recibo', 
        name='s5012_evtirrf_recibo'),
        
url(r'^s5012-evtirrf/xml/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_verificar.gerar_xml', 
        name='s5012_evtirrf_xml'),

url(r'^s5012-evtirrf/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf.salvar', 
        name='s5012_evtirrf_salvar'),
        

url(r'^scripts/gerar-identidade/s5012-evtirrf/(?P<chave>.*)/(?P<evento_id>\d+)/$',
        'emensageria.eventos.views.s5012_evtirrf.gerar_identidade', 
        name='s5012_evtirrf_gerar_identidade'),



url(r'^s1000-evtinfoempregador-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_ocorrencias.apagar', 
        name='s1000_evtinfoempregador_ocorrencias_apagar'),

url(r'^s1000-evtinfoempregador-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_ocorrencias.listar', 
        name='s1000_evtinfoempregador_ocorrencias'),

url(r'^s1000-evtinfoempregador-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1000_evtinfoempregador_ocorrencias.salvar', 
        name='s1000_evtinfoempregador_ocorrencias_salvar'),



url(r'^s1005-evttabestab-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_ocorrencias.apagar', 
        name='s1005_evttabestab_ocorrencias_apagar'),

url(r'^s1005-evttabestab-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_ocorrencias.listar', 
        name='s1005_evttabestab_ocorrencias'),

url(r'^s1005-evttabestab-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1005_evttabestab_ocorrencias.salvar', 
        name='s1005_evttabestab_ocorrencias_salvar'),



url(r'^s1010-evttabrubrica-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_ocorrencias.apagar', 
        name='s1010_evttabrubrica_ocorrencias_apagar'),

url(r'^s1010-evttabrubrica-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_ocorrencias.listar', 
        name='s1010_evttabrubrica_ocorrencias'),

url(r'^s1010-evttabrubrica-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1010_evttabrubrica_ocorrencias.salvar', 
        name='s1010_evttabrubrica_ocorrencias_salvar'),



url(r'^s1020-evttablotacao-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_ocorrencias.apagar', 
        name='s1020_evttablotacao_ocorrencias_apagar'),

url(r'^s1020-evttablotacao-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_ocorrencias.listar', 
        name='s1020_evttablotacao_ocorrencias'),

url(r'^s1020-evttablotacao-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1020_evttablotacao_ocorrencias.salvar', 
        name='s1020_evttablotacao_ocorrencias_salvar'),



url(r'^s1030-evttabcargo-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_ocorrencias.apagar', 
        name='s1030_evttabcargo_ocorrencias_apagar'),

url(r'^s1030-evttabcargo-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_ocorrencias.listar', 
        name='s1030_evttabcargo_ocorrencias'),

url(r'^s1030-evttabcargo-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1030_evttabcargo_ocorrencias.salvar', 
        name='s1030_evttabcargo_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^s1035-evttabcarreira-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_ocorrencias.apagar', 
        name='s1035_evttabcarreira_ocorrencias_apagar'),

url(r'^s1035-evttabcarreira-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_ocorrencias.listar', 
        name='s1035_evttabcarreira_ocorrencias'),

url(r'^s1035-evttabcarreira-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1035_evttabcarreira_ocorrencias.salvar', 
        name='s1035_evttabcarreira_ocorrencias_salvar'),



url(r'^s1040-evttabfuncao-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_ocorrencias.apagar', 
        name='s1040_evttabfuncao_ocorrencias_apagar'),

url(r'^s1040-evttabfuncao-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_ocorrencias.listar', 
        name='s1040_evttabfuncao_ocorrencias'),

url(r'^s1040-evttabfuncao-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1040_evttabfuncao_ocorrencias.salvar', 
        name='s1040_evttabfuncao_ocorrencias_salvar'),



url(r'^s1050-evttabhortur-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_ocorrencias.apagar', 
        name='s1050_evttabhortur_ocorrencias_apagar'),

url(r'^s1050-evttabhortur-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_ocorrencias.listar', 
        name='s1050_evttabhortur_ocorrencias'),

url(r'^s1050-evttabhortur-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1050_evttabhortur_ocorrencias.salvar', 
        name='s1050_evttabhortur_ocorrencias_salvar'),



url(r'^s1060-evttabambiente-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_ocorrencias.apagar', 
        name='s1060_evttabambiente_ocorrencias_apagar'),

url(r'^s1060-evttabambiente-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_ocorrencias.listar', 
        name='s1060_evttabambiente_ocorrencias'),

url(r'^s1060-evttabambiente-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1060_evttabambiente_ocorrencias.salvar', 
        name='s1060_evttabambiente_ocorrencias_salvar'),



url(r'^s1070-evttabprocesso-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_ocorrencias.apagar', 
        name='s1070_evttabprocesso_ocorrencias_apagar'),

url(r'^s1070-evttabprocesso-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_ocorrencias.listar', 
        name='s1070_evttabprocesso_ocorrencias'),

url(r'^s1070-evttabprocesso-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1070_evttabprocesso_ocorrencias.salvar', 
        name='s1070_evttabprocesso_ocorrencias_salvar'),



url(r'^s1080-evttaboperport-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_ocorrencias.apagar', 
        name='s1080_evttaboperport_ocorrencias_apagar'),

url(r'^s1080-evttaboperport-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_ocorrencias.listar', 
        name='s1080_evttaboperport_ocorrencias'),

url(r'^s1080-evttaboperport-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1080_evttaboperport_ocorrencias.salvar', 
        name='s1080_evttaboperport_ocorrencias_salvar'),



url(r'^s1200-evtremun-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_ocorrencias.apagar', 
        name='s1200_evtremun_ocorrencias_apagar'),

url(r'^s1200-evtremun-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_ocorrencias.listar', 
        name='s1200_evtremun_ocorrencias'),

url(r'^s1200-evtremun-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1200_evtremun_ocorrencias.salvar', 
        name='s1200_evtremun_ocorrencias_salvar'),



url(r'^s1202-evtrmnrpps-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_ocorrencias.apagar', 
        name='s1202_evtrmnrpps_ocorrencias_apagar'),

url(r'^s1202-evtrmnrpps-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_ocorrencias.listar', 
        name='s1202_evtrmnrpps_ocorrencias'),

url(r'^s1202-evtrmnrpps-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1202_evtrmnrpps_ocorrencias.salvar', 
        name='s1202_evtrmnrpps_ocorrencias_salvar'),



url(r'^s1207-evtbenprrp-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_ocorrencias.apagar', 
        name='s1207_evtbenprrp_ocorrencias_apagar'),

url(r'^s1207-evtbenprrp-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_ocorrencias.listar', 
        name='s1207_evtbenprrp_ocorrencias'),

url(r'^s1207-evtbenprrp-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1207_evtbenprrp_ocorrencias.salvar', 
        name='s1207_evtbenprrp_ocorrencias_salvar'),



url(r'^s1210-evtpgtos-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_ocorrencias.apagar', 
        name='s1210_evtpgtos_ocorrencias_apagar'),

url(r'^s1210-evtpgtos-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_ocorrencias.listar', 
        name='s1210_evtpgtos_ocorrencias'),

url(r'^s1210-evtpgtos-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1210_evtpgtos_ocorrencias.salvar', 
        name='s1210_evtpgtos_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^s1250-evtaqprod-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_ocorrencias.apagar', 
        name='s1250_evtaqprod_ocorrencias_apagar'),

url(r'^s1250-evtaqprod-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_ocorrencias.listar', 
        name='s1250_evtaqprod_ocorrencias'),

url(r'^s1250-evtaqprod-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1250_evtaqprod_ocorrencias.salvar', 
        name='s1250_evtaqprod_ocorrencias_salvar'),



url(r'^s1260-evtcomprod-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_ocorrencias.apagar', 
        name='s1260_evtcomprod_ocorrencias_apagar'),

url(r'^s1260-evtcomprod-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_ocorrencias.listar', 
        name='s1260_evtcomprod_ocorrencias'),

url(r'^s1260-evtcomprod-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1260_evtcomprod_ocorrencias.salvar', 
        name='s1260_evtcomprod_ocorrencias_salvar'),



url(r'^s1270-evtcontratavnp-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_ocorrencias.apagar', 
        name='s1270_evtcontratavnp_ocorrencias_apagar'),

url(r'^s1270-evtcontratavnp-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_ocorrencias.listar', 
        name='s1270_evtcontratavnp_ocorrencias'),

url(r'^s1270-evtcontratavnp-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1270_evtcontratavnp_ocorrencias.salvar', 
        name='s1270_evtcontratavnp_ocorrencias_salvar'),



url(r'^s1280-evtinfocomplper-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_ocorrencias.apagar', 
        name='s1280_evtinfocomplper_ocorrencias_apagar'),

url(r'^s1280-evtinfocomplper-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_ocorrencias.listar', 
        name='s1280_evtinfocomplper_ocorrencias'),

url(r'^s1280-evtinfocomplper-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1280_evtinfocomplper_ocorrencias.salvar', 
        name='s1280_evtinfocomplper_ocorrencias_salvar'),



url(r'^s1295-evttotconting-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_ocorrencias.apagar', 
        name='s1295_evttotconting_ocorrencias_apagar'),

url(r'^s1295-evttotconting-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_ocorrencias.listar', 
        name='s1295_evttotconting_ocorrencias'),

url(r'^s1295-evttotconting-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1295_evttotconting_ocorrencias.salvar', 
        name='s1295_evttotconting_ocorrencias_salvar'),



url(r'^s1298-evtreabreevper-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_ocorrencias.apagar', 
        name='s1298_evtreabreevper_ocorrencias_apagar'),

url(r'^s1298-evtreabreevper-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_ocorrencias.listar', 
        name='s1298_evtreabreevper_ocorrencias'),

url(r'^s1298-evtreabreevper-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1298_evtreabreevper_ocorrencias.salvar', 
        name='s1298_evtreabreevper_ocorrencias_salvar'),



url(r'^s1299-evtfechaevper-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_ocorrencias.apagar', 
        name='s1299_evtfechaevper_ocorrencias_apagar'),

url(r'^s1299-evtfechaevper-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_ocorrencias.listar', 
        name='s1299_evtfechaevper_ocorrencias'),

url(r'^s1299-evtfechaevper-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1299_evtfechaevper_ocorrencias.salvar', 
        name='s1299_evtfechaevper_ocorrencias_salvar'),



url(r'^s1300-evtcontrsindpatr-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_ocorrencias.apagar', 
        name='s1300_evtcontrsindpatr_ocorrencias_apagar'),

url(r'^s1300-evtcontrsindpatr-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_ocorrencias.listar', 
        name='s1300_evtcontrsindpatr_ocorrencias'),

url(r'^s1300-evtcontrsindpatr-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s1300_evtcontrsindpatr_ocorrencias.salvar', 
        name='s1300_evtcontrsindpatr_ocorrencias_salvar'),



url(r'^s2190-evtadmprelim-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_ocorrencias.apagar', 
        name='s2190_evtadmprelim_ocorrencias_apagar'),

url(r'^s2190-evtadmprelim-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_ocorrencias.listar', 
        name='s2190_evtadmprelim_ocorrencias'),

url(r'^s2190-evtadmprelim-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2190_evtadmprelim_ocorrencias.salvar', 
        name='s2190_evtadmprelim_ocorrencias_salvar'),



url(r'^s2200-evtadmissao-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_ocorrencias.apagar', 
        name='s2200_evtadmissao_ocorrencias_apagar'),

url(r'^s2200-evtadmissao-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_ocorrencias.listar', 
        name='s2200_evtadmissao_ocorrencias'),

url(r'^s2200-evtadmissao-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2200_evtadmissao_ocorrencias.salvar', 
        name='s2200_evtadmissao_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^s2205-evtaltcadastral-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_ocorrencias.apagar', 
        name='s2205_evtaltcadastral_ocorrencias_apagar'),

url(r'^s2205-evtaltcadastral-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_ocorrencias.listar', 
        name='s2205_evtaltcadastral_ocorrencias'),

url(r'^s2205-evtaltcadastral-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2205_evtaltcadastral_ocorrencias.salvar', 
        name='s2205_evtaltcadastral_ocorrencias_salvar'),



url(r'^s2206-evtaltcontratual-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_ocorrencias.apagar', 
        name='s2206_evtaltcontratual_ocorrencias_apagar'),

url(r'^s2206-evtaltcontratual-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_ocorrencias.listar', 
        name='s2206_evtaltcontratual_ocorrencias'),

url(r'^s2206-evtaltcontratual-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2206_evtaltcontratual_ocorrencias.salvar', 
        name='s2206_evtaltcontratual_ocorrencias_salvar'),



url(r'^s2210-evtcat-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_ocorrencias.apagar', 
        name='s2210_evtcat_ocorrencias_apagar'),

url(r'^s2210-evtcat-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_ocorrencias.listar', 
        name='s2210_evtcat_ocorrencias'),

url(r'^s2210-evtcat-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2210_evtcat_ocorrencias.salvar', 
        name='s2210_evtcat_ocorrencias_salvar'),



url(r'^s2220-evtmonit-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_ocorrencias.apagar', 
        name='s2220_evtmonit_ocorrencias_apagar'),

url(r'^s2220-evtmonit-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_ocorrencias.listar', 
        name='s2220_evtmonit_ocorrencias'),

url(r'^s2220-evtmonit-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2220_evtmonit_ocorrencias.salvar', 
        name='s2220_evtmonit_ocorrencias_salvar'),



url(r'^s2230-evtafasttemp-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_ocorrencias.apagar', 
        name='s2230_evtafasttemp_ocorrencias_apagar'),

url(r'^s2230-evtafasttemp-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_ocorrencias.listar', 
        name='s2230_evtafasttemp_ocorrencias'),

url(r'^s2230-evtafasttemp-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2230_evtafasttemp_ocorrencias.salvar', 
        name='s2230_evtafasttemp_ocorrencias_salvar'),



url(r'^s2240-evtexprisco-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_ocorrencias.apagar', 
        name='s2240_evtexprisco_ocorrencias_apagar'),

url(r'^s2240-evtexprisco-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_ocorrencias.listar', 
        name='s2240_evtexprisco_ocorrencias'),

url(r'^s2240-evtexprisco-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2240_evtexprisco_ocorrencias.salvar', 
        name='s2240_evtexprisco_ocorrencias_salvar'),



url(r'^s2241-evtinsapo-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_ocorrencias.apagar', 
        name='s2241_evtinsapo_ocorrencias_apagar'),

url(r'^s2241-evtinsapo-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_ocorrencias.listar', 
        name='s2241_evtinsapo_ocorrencias'),

url(r'^s2241-evtinsapo-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2241_evtinsapo_ocorrencias.salvar', 
        name='s2241_evtinsapo_ocorrencias_salvar'),



url(r'^s2250-evtavprevio-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_ocorrencias.apagar', 
        name='s2250_evtavprevio_ocorrencias_apagar'),

url(r'^s2250-evtavprevio-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_ocorrencias.listar', 
        name='s2250_evtavprevio_ocorrencias'),

url(r'^s2250-evtavprevio-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2250_evtavprevio_ocorrencias.salvar', 
        name='s2250_evtavprevio_ocorrencias_salvar'),



url(r'^s2260-evtconvinterm-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_ocorrencias.apagar', 
        name='s2260_evtconvinterm_ocorrencias_apagar'),

url(r'^s2260-evtconvinterm-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_ocorrencias.listar', 
        name='s2260_evtconvinterm_ocorrencias'),

url(r'^s2260-evtconvinterm-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2260_evtconvinterm_ocorrencias.salvar', 
        name='s2260_evtconvinterm_ocorrencias_salvar'),



url(r'^s2298-evtreintegr-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_ocorrencias.apagar', 
        name='s2298_evtreintegr_ocorrencias_apagar'),

url(r'^s2298-evtreintegr-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_ocorrencias.listar', 
        name='s2298_evtreintegr_ocorrencias'),

url(r'^s2298-evtreintegr-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2298_evtreintegr_ocorrencias.salvar', 
        name='s2298_evtreintegr_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^s2299-evtdeslig-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_ocorrencias.apagar', 
        name='s2299_evtdeslig_ocorrencias_apagar'),

url(r'^s2299-evtdeslig-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_ocorrencias.listar', 
        name='s2299_evtdeslig_ocorrencias'),

url(r'^s2299-evtdeslig-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2299_evtdeslig_ocorrencias.salvar', 
        name='s2299_evtdeslig_ocorrencias_salvar'),



url(r'^s2300-evttsvinicio-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_ocorrencias.apagar', 
        name='s2300_evttsvinicio_ocorrencias_apagar'),

url(r'^s2300-evttsvinicio-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_ocorrencias.listar', 
        name='s2300_evttsvinicio_ocorrencias'),

url(r'^s2300-evttsvinicio-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2300_evttsvinicio_ocorrencias.salvar', 
        name='s2300_evttsvinicio_ocorrencias_salvar'),



url(r'^s2306-evttsvaltcontr-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_ocorrencias.apagar', 
        name='s2306_evttsvaltcontr_ocorrencias_apagar'),

url(r'^s2306-evttsvaltcontr-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_ocorrencias.listar', 
        name='s2306_evttsvaltcontr_ocorrencias'),

url(r'^s2306-evttsvaltcontr-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2306_evttsvaltcontr_ocorrencias.salvar', 
        name='s2306_evttsvaltcontr_ocorrencias_salvar'),



url(r'^s2399-evttsvtermino-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_ocorrencias.apagar', 
        name='s2399_evttsvtermino_ocorrencias_apagar'),

url(r'^s2399-evttsvtermino-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_ocorrencias.listar', 
        name='s2399_evttsvtermino_ocorrencias'),

url(r'^s2399-evttsvtermino-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2399_evttsvtermino_ocorrencias.salvar', 
        name='s2399_evttsvtermino_ocorrencias_salvar'),



url(r'^s2400-evtcdbenprrp-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_ocorrencias.apagar', 
        name='s2400_evtcdbenprrp_ocorrencias_apagar'),

url(r'^s2400-evtcdbenprrp-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_ocorrencias.listar', 
        name='s2400_evtcdbenprrp_ocorrencias'),

url(r'^s2400-evtcdbenprrp-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s2400_evtcdbenprrp_ocorrencias.salvar', 
        name='s2400_evtcdbenprrp_ocorrencias_salvar'),



url(r'^s3000-evtexclusao-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_ocorrencias.apagar', 
        name='s3000_evtexclusao_ocorrencias_apagar'),

url(r'^s3000-evtexclusao-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_ocorrencias.listar', 
        name='s3000_evtexclusao_ocorrencias'),

url(r'^s3000-evtexclusao-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s3000_evtexclusao_ocorrencias.salvar', 
        name='s3000_evtexclusao_ocorrencias_salvar'),



url(r'^s5001-evtbasestrab-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_ocorrencias.apagar', 
        name='s5001_evtbasestrab_ocorrencias_apagar'),

url(r'^s5001-evtbasestrab-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_ocorrencias.listar', 
        name='s5001_evtbasestrab_ocorrencias'),

url(r'^s5001-evtbasestrab-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5001_evtbasestrab_ocorrencias.salvar', 
        name='s5001_evtbasestrab_ocorrencias_salvar'),



url(r'^s5002-evtirrfbenef-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_ocorrencias.apagar', 
        name='s5002_evtirrfbenef_ocorrencias_apagar'),

url(r'^s5002-evtirrfbenef-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_ocorrencias.listar', 
        name='s5002_evtirrfbenef_ocorrencias'),

url(r'^s5002-evtirrfbenef-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5002_evtirrfbenef_ocorrencias.salvar', 
        name='s5002_evtirrfbenef_ocorrencias_salvar'),



url(r'^s5011-evtcs-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_ocorrencias.apagar', 
        name='s5011_evtcs_ocorrencias_apagar'),

url(r'^s5011-evtcs-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_ocorrencias.listar', 
        name='s5011_evtcs_ocorrencias'),

url(r'^s5011-evtcs-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5011_evtcs_ocorrencias.salvar', 
        name='s5011_evtcs_ocorrencias_salvar'),



url(r'^s5012-evtirrf-ocorrencias/apagar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_ocorrencias.apagar', 
        name='s5012_evtirrf_ocorrencias_apagar'),

url(r'^s5012-evtirrf-ocorrencias/listar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_ocorrencias.listar', 
        name='s5012_evtirrf_ocorrencias'),

url(r'^s5012-evtirrf-ocorrencias/salvar/(?P<hash>.*)/$', 
        'emensageria.eventos.views.s5012_evtirrf_ocorrencias.salvar', 
        name='s5012_evtirrf_ocorrencias_salvar'),

)


urlpatterns += patterns('',


url(r'^s1000-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao.apagar', 
        name='s1000_inclusao_apagar'),

url(r'^s1000-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao.listar', 
        name='s1000_inclusao'),

url(r'^s1000-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao.salvar', 
        name='s1000_inclusao_salvar'),



url(r'^s1000-inclusao-dadosisencao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_dadosisencao.apagar', 
        name='s1000_inclusao_dadosisencao_apagar'),

url(r'^s1000-inclusao-dadosisencao/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_dadosisencao.listar', 
        name='s1000_inclusao_dadosisencao'),

url(r'^s1000-inclusao-dadosisencao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_dadosisencao.salvar', 
        name='s1000_inclusao_dadosisencao_salvar'),



url(r'^s1000-inclusao-infoop/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoop.apagar', 
        name='s1000_inclusao_infoop_apagar'),

url(r'^s1000-inclusao-infoop/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoop.listar', 
        name='s1000_inclusao_infoop'),

url(r'^s1000-inclusao-infoop/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoop.salvar', 
        name='s1000_inclusao_infoop_salvar'),



url(r'^s1000-inclusao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoefr.apagar', 
        name='s1000_inclusao_infoefr_apagar'),

url(r'^s1000-inclusao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoefr.listar', 
        name='s1000_inclusao_infoefr'),

url(r'^s1000-inclusao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoefr.salvar', 
        name='s1000_inclusao_infoefr_salvar'),



url(r'^s1000-inclusao-infoente/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoente.apagar', 
        name='s1000_inclusao_infoente_apagar'),

url(r'^s1000-inclusao-infoente/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoente.listar', 
        name='s1000_inclusao_infoente'),

url(r'^s1000-inclusao-infoente/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoente.salvar', 
        name='s1000_inclusao_infoente_salvar'),



url(r'^s1000-inclusao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoorginternacional.apagar', 
        name='s1000_inclusao_infoorginternacional_apagar'),

url(r'^s1000-inclusao-infoorginternacional/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoorginternacional.listar', 
        name='s1000_inclusao_infoorginternacional'),

url(r'^s1000-inclusao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_infoorginternacional.salvar', 
        name='s1000_inclusao_infoorginternacional_salvar'),



url(r'^s1000-inclusao-softwarehouse/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_softwarehouse.apagar', 
        name='s1000_inclusao_softwarehouse_apagar'),

url(r'^s1000-inclusao-softwarehouse/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_softwarehouse.listar', 
        name='s1000_inclusao_softwarehouse'),

url(r'^s1000-inclusao-softwarehouse/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_softwarehouse.salvar', 
        name='s1000_inclusao_softwarehouse_salvar'),



url(r'^s1000-inclusao-situacaopj/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopj.apagar', 
        name='s1000_inclusao_situacaopj_apagar'),

url(r'^s1000-inclusao-situacaopj/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopj.listar', 
        name='s1000_inclusao_situacaopj'),

url(r'^s1000-inclusao-situacaopj/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopj.salvar', 
        name='s1000_inclusao_situacaopj_salvar'),



url(r'^s1000-inclusao-situacaopf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopf.apagar', 
        name='s1000_inclusao_situacaopf_apagar'),

url(r'^s1000-inclusao-situacaopf/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopf.listar', 
        name='s1000_inclusao_situacaopf'),

url(r'^s1000-inclusao-situacaopf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_inclusao_situacaopf.salvar', 
        name='s1000_inclusao_situacaopf_salvar'),



url(r'^s1000-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao.apagar', 
        name='s1000_alteracao_apagar'),

url(r'^s1000-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao.listar', 
        name='s1000_alteracao'),

url(r'^s1000-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao.salvar', 
        name='s1000_alteracao_salvar'),

)


urlpatterns += patterns('',


url(r'^s1000-alteracao-dadosisencao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_dadosisencao.apagar', 
        name='s1000_alteracao_dadosisencao_apagar'),

url(r'^s1000-alteracao-dadosisencao/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_dadosisencao.listar', 
        name='s1000_alteracao_dadosisencao'),

url(r'^s1000-alteracao-dadosisencao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_dadosisencao.salvar', 
        name='s1000_alteracao_dadosisencao_salvar'),



url(r'^s1000-alteracao-infoop/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoop.apagar', 
        name='s1000_alteracao_infoop_apagar'),

url(r'^s1000-alteracao-infoop/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoop.listar', 
        name='s1000_alteracao_infoop'),

url(r'^s1000-alteracao-infoop/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoop.salvar', 
        name='s1000_alteracao_infoop_salvar'),



url(r'^s1000-alteracao-infoefr/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoefr.apagar', 
        name='s1000_alteracao_infoefr_apagar'),

url(r'^s1000-alteracao-infoefr/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoefr.listar', 
        name='s1000_alteracao_infoefr'),

url(r'^s1000-alteracao-infoefr/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoefr.salvar', 
        name='s1000_alteracao_infoefr_salvar'),



url(r'^s1000-alteracao-infoente/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoente.apagar', 
        name='s1000_alteracao_infoente_apagar'),

url(r'^s1000-alteracao-infoente/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoente.listar', 
        name='s1000_alteracao_infoente'),

url(r'^s1000-alteracao-infoente/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoente.salvar', 
        name='s1000_alteracao_infoente_salvar'),



url(r'^s1000-alteracao-infoorginternacional/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoorginternacional.apagar', 
        name='s1000_alteracao_infoorginternacional_apagar'),

url(r'^s1000-alteracao-infoorginternacional/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoorginternacional.listar', 
        name='s1000_alteracao_infoorginternacional'),

url(r'^s1000-alteracao-infoorginternacional/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_infoorginternacional.salvar', 
        name='s1000_alteracao_infoorginternacional_salvar'),



url(r'^s1000-alteracao-softwarehouse/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_softwarehouse.apagar', 
        name='s1000_alteracao_softwarehouse_apagar'),

url(r'^s1000-alteracao-softwarehouse/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_softwarehouse.listar', 
        name='s1000_alteracao_softwarehouse'),

url(r'^s1000-alteracao-softwarehouse/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_softwarehouse.salvar', 
        name='s1000_alteracao_softwarehouse_salvar'),



url(r'^s1000-alteracao-situacaopj/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopj.apagar', 
        name='s1000_alteracao_situacaopj_apagar'),

url(r'^s1000-alteracao-situacaopj/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopj.listar', 
        name='s1000_alteracao_situacaopj'),

url(r'^s1000-alteracao-situacaopj/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopj.salvar', 
        name='s1000_alteracao_situacaopj_salvar'),



url(r'^s1000-alteracao-situacaopf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopf.apagar', 
        name='s1000_alteracao_situacaopf_apagar'),

url(r'^s1000-alteracao-situacaopf/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopf.listar', 
        name='s1000_alteracao_situacaopf'),

url(r'^s1000-alteracao-situacaopf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_situacaopf.salvar', 
        name='s1000_alteracao_situacaopf_salvar'),



url(r'^s1000-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_novavalidade.apagar', 
        name='s1000_alteracao_novavalidade_apagar'),

url(r'^s1000-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_novavalidade.listar', 
        name='s1000_alteracao_novavalidade'),

url(r'^s1000-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_alteracao_novavalidade.salvar', 
        name='s1000_alteracao_novavalidade_salvar'),



url(r'^s1000-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_exclusao.apagar', 
        name='s1000_exclusao_apagar'),

url(r'^s1000-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_exclusao.listar', 
        name='s1000_exclusao'),

url(r'^s1000-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1000.views.s1000_exclusao.salvar', 
        name='s1000_exclusao_salvar'),

)


urlpatterns += patterns('',


url(r'^s1005-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao.apagar', 
        name='s1005_inclusao_apagar'),

url(r'^s1005-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao.listar', 
        name='s1005_inclusao'),

url(r'^s1005-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao.salvar', 
        name='s1005_inclusao_salvar'),



url(r'^s1005-inclusao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudrat.apagar', 
        name='s1005_inclusao_procadmjudrat_apagar'),

url(r'^s1005-inclusao-procadmjudrat/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudrat.listar', 
        name='s1005_inclusao_procadmjudrat'),

url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudrat.salvar', 
        name='s1005_inclusao_procadmjudrat_salvar'),



url(r'^s1005-inclusao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudfap.apagar', 
        name='s1005_inclusao_procadmjudfap_apagar'),

url(r'^s1005-inclusao-procadmjudfap/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudfap.listar', 
        name='s1005_inclusao_procadmjudfap'),

url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_procadmjudfap.salvar', 
        name='s1005_inclusao_procadmjudfap_salvar'),



url(r'^s1005-inclusao-infocaepf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infocaepf.apagar', 
        name='s1005_inclusao_infocaepf_apagar'),

url(r'^s1005-inclusao-infocaepf/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infocaepf.listar', 
        name='s1005_inclusao_infocaepf'),

url(r'^s1005-inclusao-infocaepf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infocaepf.salvar', 
        name='s1005_inclusao_infocaepf_salvar'),



url(r'^s1005-inclusao-infoobra/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoobra.apagar', 
        name='s1005_inclusao_infoobra_apagar'),

url(r'^s1005-inclusao-infoobra/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoobra.listar', 
        name='s1005_inclusao_infoobra'),

url(r'^s1005-inclusao-infoobra/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoobra.salvar', 
        name='s1005_inclusao_infoobra_salvar'),



url(r'^s1005-inclusao-infoenteduc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoenteduc.apagar', 
        name='s1005_inclusao_infoenteduc_apagar'),

url(r'^s1005-inclusao-infoenteduc/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoenteduc.listar', 
        name='s1005_inclusao_infoenteduc'),

url(r'^s1005-inclusao-infoenteduc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infoenteduc.salvar', 
        name='s1005_inclusao_infoenteduc_salvar'),



url(r'^s1005-inclusao-infopcd/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infopcd.apagar', 
        name='s1005_inclusao_infopcd_apagar'),

url(r'^s1005-inclusao-infopcd/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infopcd.listar', 
        name='s1005_inclusao_infopcd'),

url(r'^s1005-inclusao-infopcd/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_inclusao_infopcd.salvar', 
        name='s1005_inclusao_infopcd_salvar'),



url(r'^s1005-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao.apagar', 
        name='s1005_alteracao_apagar'),

url(r'^s1005-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao.listar', 
        name='s1005_alteracao'),

url(r'^s1005-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao.salvar', 
        name='s1005_alteracao_salvar'),



url(r'^s1005-alteracao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudrat.apagar', 
        name='s1005_alteracao_procadmjudrat_apagar'),

url(r'^s1005-alteracao-procadmjudrat/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudrat.listar', 
        name='s1005_alteracao_procadmjudrat'),

url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudrat.salvar', 
        name='s1005_alteracao_procadmjudrat_salvar'),



url(r'^s1005-alteracao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudfap.apagar', 
        name='s1005_alteracao_procadmjudfap_apagar'),

url(r'^s1005-alteracao-procadmjudfap/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudfap.listar', 
        name='s1005_alteracao_procadmjudfap'),

url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_procadmjudfap.salvar', 
        name='s1005_alteracao_procadmjudfap_salvar'),

)


urlpatterns += patterns('',


url(r'^s1005-alteracao-infocaepf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infocaepf.apagar', 
        name='s1005_alteracao_infocaepf_apagar'),

url(r'^s1005-alteracao-infocaepf/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infocaepf.listar', 
        name='s1005_alteracao_infocaepf'),

url(r'^s1005-alteracao-infocaepf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infocaepf.salvar', 
        name='s1005_alteracao_infocaepf_salvar'),



url(r'^s1005-alteracao-infoobra/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoobra.apagar', 
        name='s1005_alteracao_infoobra_apagar'),

url(r'^s1005-alteracao-infoobra/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoobra.listar', 
        name='s1005_alteracao_infoobra'),

url(r'^s1005-alteracao-infoobra/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoobra.salvar', 
        name='s1005_alteracao_infoobra_salvar'),



url(r'^s1005-alteracao-infoenteduc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoenteduc.apagar', 
        name='s1005_alteracao_infoenteduc_apagar'),

url(r'^s1005-alteracao-infoenteduc/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoenteduc.listar', 
        name='s1005_alteracao_infoenteduc'),

url(r'^s1005-alteracao-infoenteduc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infoenteduc.salvar', 
        name='s1005_alteracao_infoenteduc_salvar'),



url(r'^s1005-alteracao-infopcd/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infopcd.apagar', 
        name='s1005_alteracao_infopcd_apagar'),

url(r'^s1005-alteracao-infopcd/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infopcd.listar', 
        name='s1005_alteracao_infopcd'),

url(r'^s1005-alteracao-infopcd/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_infopcd.salvar', 
        name='s1005_alteracao_infopcd_salvar'),



url(r'^s1005-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_novavalidade.apagar', 
        name='s1005_alteracao_novavalidade_apagar'),

url(r'^s1005-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_novavalidade.listar', 
        name='s1005_alteracao_novavalidade'),

url(r'^s1005-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_alteracao_novavalidade.salvar', 
        name='s1005_alteracao_novavalidade_salvar'),



url(r'^s1005-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_exclusao.apagar', 
        name='s1005_exclusao_apagar'),

url(r'^s1005-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_exclusao.listar', 
        name='s1005_exclusao'),

url(r'^s1005-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1005.views.s1005_exclusao.salvar', 
        name='s1005_exclusao_salvar'),



url(r'^s1010-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao.apagar', 
        name='s1010_inclusao_apagar'),

url(r'^s1010-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao.listar', 
        name='s1010_inclusao'),

url(r'^s1010-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao.salvar', 
        name='s1010_inclusao_salvar'),



url(r'^s1010-inclusao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessocp.apagar', 
        name='s1010_inclusao_ideprocessocp_apagar'),

url(r'^s1010-inclusao-ideprocessocp/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessocp.listar', 
        name='s1010_inclusao_ideprocessocp'),

url(r'^s1010-inclusao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessocp.salvar', 
        name='s1010_inclusao_ideprocessocp_salvar'),



url(r'^s1010-inclusao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessoirrf.apagar', 
        name='s1010_inclusao_ideprocessoirrf_apagar'),

url(r'^s1010-inclusao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessoirrf.listar', 
        name='s1010_inclusao_ideprocessoirrf'),

url(r'^s1010-inclusao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessoirrf.salvar', 
        name='s1010_inclusao_ideprocessoirrf_salvar'),



url(r'^s1010-inclusao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessofgts.apagar', 
        name='s1010_inclusao_ideprocessofgts_apagar'),

url(r'^s1010-inclusao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessofgts.listar', 
        name='s1010_inclusao_ideprocessofgts'),

url(r'^s1010-inclusao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessofgts.salvar', 
        name='s1010_inclusao_ideprocessofgts_salvar'),

)


urlpatterns += patterns('',


url(r'^s1010-inclusao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessosind.apagar', 
        name='s1010_inclusao_ideprocessosind_apagar'),

url(r'^s1010-inclusao-ideprocessosind/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessosind.listar', 
        name='s1010_inclusao_ideprocessosind'),

url(r'^s1010-inclusao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_inclusao_ideprocessosind.salvar', 
        name='s1010_inclusao_ideprocessosind_salvar'),



url(r'^s1010-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao.apagar', 
        name='s1010_alteracao_apagar'),

url(r'^s1010-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao.listar', 
        name='s1010_alteracao'),

url(r'^s1010-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao.salvar', 
        name='s1010_alteracao_salvar'),



url(r'^s1010-alteracao-ideprocessocp/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessocp.apagar', 
        name='s1010_alteracao_ideprocessocp_apagar'),

url(r'^s1010-alteracao-ideprocessocp/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessocp.listar', 
        name='s1010_alteracao_ideprocessocp'),

url(r'^s1010-alteracao-ideprocessocp/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessocp.salvar', 
        name='s1010_alteracao_ideprocessocp_salvar'),



url(r'^s1010-alteracao-ideprocessoirrf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessoirrf.apagar', 
        name='s1010_alteracao_ideprocessoirrf_apagar'),

url(r'^s1010-alteracao-ideprocessoirrf/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessoirrf.listar', 
        name='s1010_alteracao_ideprocessoirrf'),

url(r'^s1010-alteracao-ideprocessoirrf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessoirrf.salvar', 
        name='s1010_alteracao_ideprocessoirrf_salvar'),



url(r'^s1010-alteracao-ideprocessofgts/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessofgts.apagar', 
        name='s1010_alteracao_ideprocessofgts_apagar'),

url(r'^s1010-alteracao-ideprocessofgts/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessofgts.listar', 
        name='s1010_alteracao_ideprocessofgts'),

url(r'^s1010-alteracao-ideprocessofgts/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessofgts.salvar', 
        name='s1010_alteracao_ideprocessofgts_salvar'),



url(r'^s1010-alteracao-ideprocessosind/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessosind.apagar', 
        name='s1010_alteracao_ideprocessosind_apagar'),

url(r'^s1010-alteracao-ideprocessosind/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessosind.listar', 
        name='s1010_alteracao_ideprocessosind'),

url(r'^s1010-alteracao-ideprocessosind/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_ideprocessosind.salvar', 
        name='s1010_alteracao_ideprocessosind_salvar'),



url(r'^s1010-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_novavalidade.apagar', 
        name='s1010_alteracao_novavalidade_apagar'),

url(r'^s1010-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_novavalidade.listar', 
        name='s1010_alteracao_novavalidade'),

url(r'^s1010-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_alteracao_novavalidade.salvar', 
        name='s1010_alteracao_novavalidade_salvar'),



url(r'^s1010-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_exclusao.apagar', 
        name='s1010_exclusao_apagar'),

url(r'^s1010-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_exclusao.listar', 
        name='s1010_exclusao'),

url(r'^s1010-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1010.views.s1010_exclusao.salvar', 
        name='s1010_exclusao_salvar'),



url(r'^s1020-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao.apagar', 
        name='s1020_inclusao_apagar'),

url(r'^s1020-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao.listar', 
        name='s1020_inclusao'),

url(r'^s1020-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao.salvar', 
        name='s1020_inclusao_salvar'),



url(r'^s1020-inclusao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoprocjudterceiros.apagar', 
        name='s1020_inclusao_infoprocjudterceiros_apagar'),

url(r'^s1020-inclusao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoprocjudterceiros.listar', 
        name='s1020_inclusao_infoprocjudterceiros'),

url(r'^s1020-inclusao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoprocjudterceiros.salvar', 
        name='s1020_inclusao_infoprocjudterceiros_salvar'),

)


urlpatterns += patterns('',


url(r'^s1020-inclusao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_procjudterceiro.apagar', 
        name='s1020_inclusao_procjudterceiro_apagar'),

url(r'^s1020-inclusao-procjudterceiro/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_procjudterceiro.listar', 
        name='s1020_inclusao_procjudterceiro'),

url(r'^s1020-inclusao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_procjudterceiro.salvar', 
        name='s1020_inclusao_procjudterceiro_salvar'),



url(r'^s1020-inclusao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoemprparcial.apagar', 
        name='s1020_inclusao_infoemprparcial_apagar'),

url(r'^s1020-inclusao-infoemprparcial/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoemprparcial.listar', 
        name='s1020_inclusao_infoemprparcial'),

url(r'^s1020-inclusao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_inclusao_infoemprparcial.salvar', 
        name='s1020_inclusao_infoemprparcial_salvar'),



url(r'^s1020-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao.apagar', 
        name='s1020_alteracao_apagar'),

url(r'^s1020-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao.listar', 
        name='s1020_alteracao'),

url(r'^s1020-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao.salvar', 
        name='s1020_alteracao_salvar'),



url(r'^s1020-alteracao-infoprocjudterceiros/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoprocjudterceiros.apagar', 
        name='s1020_alteracao_infoprocjudterceiros_apagar'),

url(r'^s1020-alteracao-infoprocjudterceiros/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoprocjudterceiros.listar', 
        name='s1020_alteracao_infoprocjudterceiros'),

url(r'^s1020-alteracao-infoprocjudterceiros/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoprocjudterceiros.salvar', 
        name='s1020_alteracao_infoprocjudterceiros_salvar'),



url(r'^s1020-alteracao-procjudterceiro/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_procjudterceiro.apagar', 
        name='s1020_alteracao_procjudterceiro_apagar'),

url(r'^s1020-alteracao-procjudterceiro/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_procjudterceiro.listar', 
        name='s1020_alteracao_procjudterceiro'),

url(r'^s1020-alteracao-procjudterceiro/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_procjudterceiro.salvar', 
        name='s1020_alteracao_procjudterceiro_salvar'),



url(r'^s1020-alteracao-infoemprparcial/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoemprparcial.apagar', 
        name='s1020_alteracao_infoemprparcial_apagar'),

url(r'^s1020-alteracao-infoemprparcial/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoemprparcial.listar', 
        name='s1020_alteracao_infoemprparcial'),

url(r'^s1020-alteracao-infoemprparcial/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_infoemprparcial.salvar', 
        name='s1020_alteracao_infoemprparcial_salvar'),



url(r'^s1020-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_novavalidade.apagar', 
        name='s1020_alteracao_novavalidade_apagar'),

url(r'^s1020-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_novavalidade.listar', 
        name='s1020_alteracao_novavalidade'),

url(r'^s1020-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_alteracao_novavalidade.salvar', 
        name='s1020_alteracao_novavalidade_salvar'),



url(r'^s1020-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_exclusao.apagar', 
        name='s1020_exclusao_apagar'),

url(r'^s1020-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_exclusao.listar', 
        name='s1020_exclusao'),

url(r'^s1020-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1020.views.s1020_exclusao.salvar', 
        name='s1020_exclusao_salvar'),



url(r'^s1030-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao.apagar', 
        name='s1030_inclusao_apagar'),

url(r'^s1030-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao.listar', 
        name='s1030_inclusao'),

url(r'^s1030-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao.salvar', 
        name='s1030_inclusao_salvar'),



url(r'^s1030-inclusao-cargopublico/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao_cargopublico.apagar', 
        name='s1030_inclusao_cargopublico_apagar'),

url(r'^s1030-inclusao-cargopublico/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao_cargopublico.listar', 
        name='s1030_inclusao_cargopublico'),

url(r'^s1030-inclusao-cargopublico/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_inclusao_cargopublico.salvar', 
        name='s1030_inclusao_cargopublico_salvar'),

)


urlpatterns += patterns('',


url(r'^s1030-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao.apagar', 
        name='s1030_alteracao_apagar'),

url(r'^s1030-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao.listar', 
        name='s1030_alteracao'),

url(r'^s1030-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao.salvar', 
        name='s1030_alteracao_salvar'),



url(r'^s1030-alteracao-cargopublico/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_cargopublico.apagar', 
        name='s1030_alteracao_cargopublico_apagar'),

url(r'^s1030-alteracao-cargopublico/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_cargopublico.listar', 
        name='s1030_alteracao_cargopublico'),

url(r'^s1030-alteracao-cargopublico/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_cargopublico.salvar', 
        name='s1030_alteracao_cargopublico_salvar'),



url(r'^s1030-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_novavalidade.apagar', 
        name='s1030_alteracao_novavalidade_apagar'),

url(r'^s1030-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_novavalidade.listar', 
        name='s1030_alteracao_novavalidade'),

url(r'^s1030-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_alteracao_novavalidade.salvar', 
        name='s1030_alteracao_novavalidade_salvar'),



url(r'^s1030-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_exclusao.apagar', 
        name='s1030_exclusao_apagar'),

url(r'^s1030-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_exclusao.listar', 
        name='s1030_exclusao'),

url(r'^s1030-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1030.views.s1030_exclusao.salvar', 
        name='s1030_exclusao_salvar'),



url(r'^s1035-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_inclusao.apagar', 
        name='s1035_inclusao_apagar'),

url(r'^s1035-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_inclusao.listar', 
        name='s1035_inclusao'),

url(r'^s1035-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_inclusao.salvar', 
        name='s1035_inclusao_salvar'),



url(r'^s1035-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao.apagar', 
        name='s1035_alteracao_apagar'),

url(r'^s1035-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao.listar', 
        name='s1035_alteracao'),

url(r'^s1035-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao.salvar', 
        name='s1035_alteracao_salvar'),



url(r'^s1035-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao_novavalidade.apagar', 
        name='s1035_alteracao_novavalidade_apagar'),

url(r'^s1035-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao_novavalidade.listar', 
        name='s1035_alteracao_novavalidade'),

url(r'^s1035-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_alteracao_novavalidade.salvar', 
        name='s1035_alteracao_novavalidade_salvar'),



url(r'^s1035-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_exclusao.apagar', 
        name='s1035_exclusao_apagar'),

url(r'^s1035-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_exclusao.listar', 
        name='s1035_exclusao'),

url(r'^s1035-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1035.views.s1035_exclusao.salvar', 
        name='s1035_exclusao_salvar'),



url(r'^s1040-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_inclusao.apagar', 
        name='s1040_inclusao_apagar'),

url(r'^s1040-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_inclusao.listar', 
        name='s1040_inclusao'),

url(r'^s1040-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_inclusao.salvar', 
        name='s1040_inclusao_salvar'),



url(r'^s1040-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao.apagar', 
        name='s1040_alteracao_apagar'),

url(r'^s1040-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao.listar', 
        name='s1040_alteracao'),

url(r'^s1040-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao.salvar', 
        name='s1040_alteracao_salvar'),

)


urlpatterns += patterns('',


url(r'^s1040-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao_novavalidade.apagar', 
        name='s1040_alteracao_novavalidade_apagar'),

url(r'^s1040-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao_novavalidade.listar', 
        name='s1040_alteracao_novavalidade'),

url(r'^s1040-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_alteracao_novavalidade.salvar', 
        name='s1040_alteracao_novavalidade_salvar'),



url(r'^s1040-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_exclusao.apagar', 
        name='s1040_exclusao_apagar'),

url(r'^s1040-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_exclusao.listar', 
        name='s1040_exclusao'),

url(r'^s1040-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1040.views.s1040_exclusao.salvar', 
        name='s1040_exclusao_salvar'),



url(r'^s1050-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao.apagar', 
        name='s1050_inclusao_apagar'),

url(r'^s1050-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao.listar', 
        name='s1050_inclusao'),

url(r'^s1050-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao.salvar', 
        name='s1050_inclusao_salvar'),



url(r'^s1050-inclusao-horariointervalo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao_horariointervalo.apagar', 
        name='s1050_inclusao_horariointervalo_apagar'),

url(r'^s1050-inclusao-horariointervalo/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao_horariointervalo.listar', 
        name='s1050_inclusao_horariointervalo'),

url(r'^s1050-inclusao-horariointervalo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_inclusao_horariointervalo.salvar', 
        name='s1050_inclusao_horariointervalo_salvar'),



url(r'^s1050-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao.apagar', 
        name='s1050_alteracao_apagar'),

url(r'^s1050-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao.listar', 
        name='s1050_alteracao'),

url(r'^s1050-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao.salvar', 
        name='s1050_alteracao_salvar'),



url(r'^s1050-alteracao-horariointervalo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_horariointervalo.apagar', 
        name='s1050_alteracao_horariointervalo_apagar'),

url(r'^s1050-alteracao-horariointervalo/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_horariointervalo.listar', 
        name='s1050_alteracao_horariointervalo'),

url(r'^s1050-alteracao-horariointervalo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_horariointervalo.salvar', 
        name='s1050_alteracao_horariointervalo_salvar'),



url(r'^s1050-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_novavalidade.apagar', 
        name='s1050_alteracao_novavalidade_apagar'),

url(r'^s1050-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_novavalidade.listar', 
        name='s1050_alteracao_novavalidade'),

url(r'^s1050-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_alteracao_novavalidade.salvar', 
        name='s1050_alteracao_novavalidade_salvar'),



url(r'^s1050-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_exclusao.apagar', 
        name='s1050_exclusao_apagar'),

url(r'^s1050-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_exclusao.listar', 
        name='s1050_exclusao'),

url(r'^s1050-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1050.views.s1050_exclusao.salvar', 
        name='s1050_exclusao_salvar'),



url(r'^s1060-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao.apagar', 
        name='s1060_inclusao_apagar'),

url(r'^s1060-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao.listar', 
        name='s1060_inclusao'),

url(r'^s1060-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao.salvar', 
        name='s1060_inclusao_salvar'),



url(r'^s1060-inclusao-fatorrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao_fatorrisco.apagar', 
        name='s1060_inclusao_fatorrisco_apagar'),

url(r'^s1060-inclusao-fatorrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao_fatorrisco.listar', 
        name='s1060_inclusao_fatorrisco'),

url(r'^s1060-inclusao-fatorrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_inclusao_fatorrisco.salvar', 
        name='s1060_inclusao_fatorrisco_salvar'),

)


urlpatterns += patterns('',


url(r'^s1060-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao.apagar', 
        name='s1060_alteracao_apagar'),

url(r'^s1060-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao.listar', 
        name='s1060_alteracao'),

url(r'^s1060-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao.salvar', 
        name='s1060_alteracao_salvar'),



url(r'^s1060-alteracao-fatorrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_fatorrisco.apagar', 
        name='s1060_alteracao_fatorrisco_apagar'),

url(r'^s1060-alteracao-fatorrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_fatorrisco.listar', 
        name='s1060_alteracao_fatorrisco'),

url(r'^s1060-alteracao-fatorrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_fatorrisco.salvar', 
        name='s1060_alteracao_fatorrisco_salvar'),



url(r'^s1060-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_novavalidade.apagar', 
        name='s1060_alteracao_novavalidade_apagar'),

url(r'^s1060-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_novavalidade.listar', 
        name='s1060_alteracao_novavalidade'),

url(r'^s1060-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_alteracao_novavalidade.salvar', 
        name='s1060_alteracao_novavalidade_salvar'),



url(r'^s1060-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_exclusao.apagar', 
        name='s1060_exclusao_apagar'),

url(r'^s1060-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_exclusao.listar', 
        name='s1060_exclusao'),

url(r'^s1060-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1060.views.s1060_exclusao.salvar', 
        name='s1060_exclusao_salvar'),



url(r'^s1070-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao.apagar', 
        name='s1070_inclusao_apagar'),

url(r'^s1070-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao.listar', 
        name='s1070_inclusao'),

url(r'^s1070-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao.salvar', 
        name='s1070_inclusao_salvar'),



url(r'^s1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_dadosprocjud.apagar', 
        name='s1070_inclusao_dadosprocjud_apagar'),

url(r'^s1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_dadosprocjud.listar', 
        name='s1070_inclusao_dadosprocjud'),

url(r'^s1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_dadosprocjud.salvar', 
        name='s1070_inclusao_dadosprocjud_salvar'),



url(r'^s1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_infosusp.apagar', 
        name='s1070_inclusao_infosusp_apagar'),

url(r'^s1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_infosusp.listar', 
        name='s1070_inclusao_infosusp'),

url(r'^s1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_inclusao_infosusp.salvar', 
        name='s1070_inclusao_infosusp_salvar'),



url(r'^s1070-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao.apagar', 
        name='s1070_alteracao_apagar'),

url(r'^s1070-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao.listar', 
        name='s1070_alteracao'),

url(r'^s1070-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao.salvar', 
        name='s1070_alteracao_salvar'),



url(r'^s1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_dadosprocjud.apagar', 
        name='s1070_alteracao_dadosprocjud_apagar'),

url(r'^s1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_dadosprocjud.listar', 
        name='s1070_alteracao_dadosprocjud'),

url(r'^s1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_dadosprocjud.salvar', 
        name='s1070_alteracao_dadosprocjud_salvar'),



url(r'^s1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_infosusp.apagar', 
        name='s1070_alteracao_infosusp_apagar'),

url(r'^s1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_infosusp.listar', 
        name='s1070_alteracao_infosusp'),

url(r'^s1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_infosusp.salvar', 
        name='s1070_alteracao_infosusp_salvar'),

)


urlpatterns += patterns('',


url(r'^s1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_novavalidade.apagar', 
        name='s1070_alteracao_novavalidade_apagar'),

url(r'^s1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_novavalidade.listar', 
        name='s1070_alteracao_novavalidade'),

url(r'^s1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_alteracao_novavalidade.salvar', 
        name='s1070_alteracao_novavalidade_salvar'),



url(r'^s1070-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_exclusao.apagar', 
        name='s1070_exclusao_apagar'),

url(r'^s1070-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_exclusao.listar', 
        name='s1070_exclusao'),

url(r'^s1070-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1070.views.s1070_exclusao.salvar', 
        name='s1070_exclusao_salvar'),



url(r'^s1080-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_inclusao.apagar', 
        name='s1080_inclusao_apagar'),

url(r'^s1080-inclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_inclusao.listar', 
        name='s1080_inclusao'),

url(r'^s1080-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_inclusao.salvar', 
        name='s1080_inclusao_salvar'),



url(r'^s1080-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao.apagar', 
        name='s1080_alteracao_apagar'),

url(r'^s1080-alteracao/listar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao.listar', 
        name='s1080_alteracao'),

url(r'^s1080-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao.salvar', 
        name='s1080_alteracao_salvar'),



url(r'^s1080-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao_novavalidade.apagar', 
        name='s1080_alteracao_novavalidade_apagar'),

url(r'^s1080-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao_novavalidade.listar', 
        name='s1080_alteracao_novavalidade'),

url(r'^s1080-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_alteracao_novavalidade.salvar', 
        name='s1080_alteracao_novavalidade_salvar'),



url(r'^s1080-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_exclusao.apagar', 
        name='s1080_exclusao_apagar'),

url(r'^s1080-exclusao/listar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_exclusao.listar', 
        name='s1080_exclusao'),

url(r'^s1080-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageria.s1080.views.s1080_exclusao.salvar', 
        name='s1080_exclusao_salvar'),



url(r'^s1200-infomv/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infomv.apagar', 
        name='s1200_infomv_apagar'),

url(r'^s1200-infomv/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infomv.listar', 
        name='s1200_infomv'),

url(r'^s1200-infomv/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infomv.salvar', 
        name='s1200_infomv_salvar'),



url(r'^s1200-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_remunoutrempr.apagar', 
        name='s1200_remunoutrempr_apagar'),

url(r'^s1200-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_remunoutrempr.listar', 
        name='s1200_remunoutrempr'),

url(r'^s1200-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_remunoutrempr.salvar', 
        name='s1200_remunoutrempr_salvar'),



url(r'^s1200-infocomplem/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infocomplem.apagar', 
        name='s1200_infocomplem_apagar'),

url(r'^s1200-infocomplem/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infocomplem.listar', 
        name='s1200_infocomplem'),

url(r'^s1200-infocomplem/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infocomplem.salvar', 
        name='s1200_infocomplem_salvar'),



url(r'^s1200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_sucessaovinc.apagar', 
        name='s1200_sucessaovinc_apagar'),

url(r'^s1200-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_sucessaovinc.listar', 
        name='s1200_sucessaovinc'),

url(r'^s1200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_sucessaovinc.salvar', 
        name='s1200_sucessaovinc_salvar'),

)


urlpatterns += patterns('',


url(r'^s1200-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_procjudtrab.apagar', 
        name='s1200_procjudtrab_apagar'),

url(r'^s1200-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_procjudtrab.listar', 
        name='s1200_procjudtrab'),

url(r'^s1200-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_procjudtrab.salvar', 
        name='s1200_procjudtrab_salvar'),



url(r'^s1200-infointerm/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infointerm.apagar', 
        name='s1200_infointerm_apagar'),

url(r'^s1200-infointerm/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infointerm.listar', 
        name='s1200_infointerm'),

url(r'^s1200-infointerm/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infointerm.salvar', 
        name='s1200_infointerm_salvar'),



url(r'^s1200-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_dmdev.apagar', 
        name='s1200_dmdev_apagar'),

url(r'^s1200-dmdev/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_dmdev.listar', 
        name='s1200_dmdev'),

url(r'^s1200-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_dmdev.salvar', 
        name='s1200_dmdev_salvar'),



url(r'^s1200-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur.apagar', 
        name='s1200_infoperapur_apagar'),

url(r'^s1200-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur.listar', 
        name='s1200_infoperapur'),

url(r'^s1200-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur.salvar', 
        name='s1200_infoperapur_salvar'),



url(r'^s1200-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_ideestablot.apagar', 
        name='s1200_infoperapur_ideestablot_apagar'),

url(r'^s1200-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_ideestablot.listar', 
        name='s1200_infoperapur_ideestablot'),

url(r'^s1200-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_ideestablot.salvar', 
        name='s1200_infoperapur_ideestablot_salvar'),



url(r'^s1200-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_remunperapur.apagar', 
        name='s1200_infoperapur_remunperapur_apagar'),

url(r'^s1200-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_remunperapur.listar', 
        name='s1200_infoperapur_remunperapur'),

url(r'^s1200-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_remunperapur.salvar', 
        name='s1200_infoperapur_remunperapur_salvar'),



url(r'^s1200-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_itensremun.apagar', 
        name='s1200_infoperapur_itensremun_apagar'),

url(r'^s1200-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_itensremun.listar', 
        name='s1200_infoperapur_itensremun'),

url(r'^s1200-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_itensremun.salvar', 
        name='s1200_infoperapur_itensremun_salvar'),



url(r'^s1200-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infosaudecolet.apagar', 
        name='s1200_infoperapur_infosaudecolet_apagar'),

url(r'^s1200-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infosaudecolet.listar', 
        name='s1200_infoperapur_infosaudecolet'),

url(r'^s1200-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infosaudecolet.salvar', 
        name='s1200_infoperapur_infosaudecolet_salvar'),



url(r'^s1200-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detoper.apagar', 
        name='s1200_infoperapur_detoper_apagar'),

url(r'^s1200-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detoper.listar', 
        name='s1200_infoperapur_detoper'),

url(r'^s1200-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detoper.salvar', 
        name='s1200_infoperapur_detoper_salvar'),



url(r'^s1200-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detplano.apagar', 
        name='s1200_infoperapur_detplano_apagar'),

url(r'^s1200-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detplano.listar', 
        name='s1200_infoperapur_detplano'),

url(r'^s1200-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_detplano.salvar', 
        name='s1200_infoperapur_detplano_salvar'),

)


urlpatterns += patterns('',


url(r'^s1200-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infoagnocivo.apagar', 
        name='s1200_infoperapur_infoagnocivo_apagar'),

url(r'^s1200-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infoagnocivo.listar', 
        name='s1200_infoperapur_infoagnocivo'),

url(r'^s1200-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infoagnocivo.salvar', 
        name='s1200_infoperapur_infoagnocivo_salvar'),



url(r'^s1200-infoperapur-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infotrabinterm.apagar', 
        name='s1200_infoperapur_infotrabinterm_apagar'),

url(r'^s1200-infoperapur-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infotrabinterm.listar', 
        name='s1200_infoperapur_infotrabinterm'),

url(r'^s1200-infoperapur-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperapur_infotrabinterm.salvar', 
        name='s1200_infoperapur_infotrabinterm_salvar'),



url(r'^s1200-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant.apagar', 
        name='s1200_infoperant_apagar'),

url(r'^s1200-infoperant/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant.listar', 
        name='s1200_infoperant'),

url(r'^s1200-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant.salvar', 
        name='s1200_infoperant_salvar'),



url(r'^s1200-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideadc.apagar', 
        name='s1200_infoperant_ideadc_apagar'),

url(r'^s1200-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideadc.listar', 
        name='s1200_infoperant_ideadc'),

url(r'^s1200-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideadc.salvar', 
        name='s1200_infoperant_ideadc_salvar'),



url(r'^s1200-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideperiodo.apagar', 
        name='s1200_infoperant_ideperiodo_apagar'),

url(r'^s1200-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideperiodo.listar', 
        name='s1200_infoperant_ideperiodo'),

url(r'^s1200-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideperiodo.salvar', 
        name='s1200_infoperant_ideperiodo_salvar'),



url(r'^s1200-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideestablot.apagar', 
        name='s1200_infoperant_ideestablot_apagar'),

url(r'^s1200-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideestablot.listar', 
        name='s1200_infoperant_ideestablot'),

url(r'^s1200-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_ideestablot.salvar', 
        name='s1200_infoperant_ideestablot_salvar'),



url(r'^s1200-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_remunperant.apagar', 
        name='s1200_infoperant_remunperant_apagar'),

url(r'^s1200-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_remunperant.listar', 
        name='s1200_infoperant_remunperant'),

url(r'^s1200-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_remunperant.salvar', 
        name='s1200_infoperant_remunperant_salvar'),



url(r'^s1200-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_itensremun.apagar', 
        name='s1200_infoperant_itensremun_apagar'),

url(r'^s1200-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_itensremun.listar', 
        name='s1200_infoperant_itensremun'),

url(r'^s1200-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_itensremun.salvar', 
        name='s1200_infoperant_itensremun_salvar'),



url(r'^s1200-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infoagnocivo.apagar', 
        name='s1200_infoperant_infoagnocivo_apagar'),

url(r'^s1200-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infoagnocivo.listar', 
        name='s1200_infoperant_infoagnocivo'),

url(r'^s1200-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infoagnocivo.salvar', 
        name='s1200_infoperant_infoagnocivo_salvar'),



url(r'^s1200-infoperant-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infotrabinterm.apagar', 
        name='s1200_infoperant_infotrabinterm_apagar'),

url(r'^s1200-infoperant-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infotrabinterm.listar', 
        name='s1200_infoperant_infotrabinterm'),

url(r'^s1200-infoperant-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infotrabinterm.salvar', 
        name='s1200_infoperant_infotrabinterm_salvar'),

)


urlpatterns += patterns('',


url(r'^s1200-infoperant-infocomplcont/apagar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infocomplcont.apagar', 
        name='s1200_infoperant_infocomplcont_apagar'),

url(r'^s1200-infoperant-infocomplcont/listar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infocomplcont.listar', 
        name='s1200_infoperant_infocomplcont'),

url(r'^s1200-infoperant-infocomplcont/salvar/(?P<hash>.*)/$', 
        'emensageria.s1200.views.s1200_infoperant_infocomplcont.salvar', 
        name='s1200_infoperant_infocomplcont_salvar'),



url(r'^s1202-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_procjudtrab.apagar', 
        name='s1202_procjudtrab_apagar'),

url(r'^s1202-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_procjudtrab.listar', 
        name='s1202_procjudtrab'),

url(r'^s1202-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_procjudtrab.salvar', 
        name='s1202_procjudtrab_salvar'),



url(r'^s1202-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_dmdev.apagar', 
        name='s1202_dmdev_apagar'),

url(r'^s1202-dmdev/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_dmdev.listar', 
        name='s1202_dmdev'),

url(r'^s1202-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_dmdev.salvar', 
        name='s1202_dmdev_salvar'),



url(r'^s1202-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur.apagar', 
        name='s1202_infoperapur_apagar'),

url(r'^s1202-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur.listar', 
        name='s1202_infoperapur'),

url(r'^s1202-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur.salvar', 
        name='s1202_infoperapur_salvar'),



url(r'^s1202-infoperapur-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_ideestab.apagar', 
        name='s1202_infoperapur_ideestab_apagar'),

url(r'^s1202-infoperapur-ideestab/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_ideestab.listar', 
        name='s1202_infoperapur_ideestab'),

url(r'^s1202-infoperapur-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_ideestab.salvar', 
        name='s1202_infoperapur_ideestab_salvar'),



url(r'^s1202-infoperapur-remunperapur/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_remunperapur.apagar', 
        name='s1202_infoperapur_remunperapur_apagar'),

url(r'^s1202-infoperapur-remunperapur/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_remunperapur.listar', 
        name='s1202_infoperapur_remunperapur'),

url(r'^s1202-infoperapur-remunperapur/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_remunperapur.salvar', 
        name='s1202_infoperapur_remunperapur_salvar'),



url(r'^s1202-infoperapur-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_itensremun.apagar', 
        name='s1202_infoperapur_itensremun_apagar'),

url(r'^s1202-infoperapur-itensremun/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_itensremun.listar', 
        name='s1202_infoperapur_itensremun'),

url(r'^s1202-infoperapur-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_itensremun.salvar', 
        name='s1202_infoperapur_itensremun_salvar'),



url(r'^s1202-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_infosaudecolet.apagar', 
        name='s1202_infoperapur_infosaudecolet_apagar'),

url(r'^s1202-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_infosaudecolet.listar', 
        name='s1202_infoperapur_infosaudecolet'),

url(r'^s1202-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_infosaudecolet.salvar', 
        name='s1202_infoperapur_infosaudecolet_salvar'),



url(r'^s1202-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detoper.apagar', 
        name='s1202_infoperapur_detoper_apagar'),

url(r'^s1202-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detoper.listar', 
        name='s1202_infoperapur_detoper'),

url(r'^s1202-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detoper.salvar', 
        name='s1202_infoperapur_detoper_salvar'),



url(r'^s1202-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detplano.apagar', 
        name='s1202_infoperapur_detplano_apagar'),

url(r'^s1202-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detplano.listar', 
        name='s1202_infoperapur_detplano'),

url(r'^s1202-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperapur_detplano.salvar', 
        name='s1202_infoperapur_detplano_salvar'),

)


urlpatterns += patterns('',


url(r'^s1202-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant.apagar', 
        name='s1202_infoperant_apagar'),

url(r'^s1202-infoperant/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant.listar', 
        name='s1202_infoperant'),

url(r'^s1202-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant.salvar', 
        name='s1202_infoperant_salvar'),



url(r'^s1202-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideadc.apagar', 
        name='s1202_infoperant_ideadc_apagar'),

url(r'^s1202-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideadc.listar', 
        name='s1202_infoperant_ideadc'),

url(r'^s1202-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideadc.salvar', 
        name='s1202_infoperant_ideadc_salvar'),



url(r'^s1202-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideperiodo.apagar', 
        name='s1202_infoperant_ideperiodo_apagar'),

url(r'^s1202-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideperiodo.listar', 
        name='s1202_infoperant_ideperiodo'),

url(r'^s1202-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideperiodo.salvar', 
        name='s1202_infoperant_ideperiodo_salvar'),



url(r'^s1202-infoperant-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideestab.apagar', 
        name='s1202_infoperant_ideestab_apagar'),

url(r'^s1202-infoperant-ideestab/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideestab.listar', 
        name='s1202_infoperant_ideestab'),

url(r'^s1202-infoperant-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_ideestab.salvar', 
        name='s1202_infoperant_ideestab_salvar'),



url(r'^s1202-infoperant-remunperant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_remunperant.apagar', 
        name='s1202_infoperant_remunperant_apagar'),

url(r'^s1202-infoperant-remunperant/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_remunperant.listar', 
        name='s1202_infoperant_remunperant'),

url(r'^s1202-infoperant-remunperant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_remunperant.salvar', 
        name='s1202_infoperant_remunperant_salvar'),



url(r'^s1202-infoperant-itensremun/apagar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_itensremun.apagar', 
        name='s1202_infoperant_itensremun_apagar'),

url(r'^s1202-infoperant-itensremun/listar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_itensremun.listar', 
        name='s1202_infoperant_itensremun'),

url(r'^s1202-infoperant-itensremun/salvar/(?P<hash>.*)/$', 
        'emensageria.s1202.views.s1202_infoperant_itensremun.salvar', 
        name='s1202_infoperant_itensremun_salvar'),



url(r'^s1207-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_dmdev.apagar', 
        name='s1207_dmdev_apagar'),

url(r'^s1207-dmdev/listar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_dmdev.listar', 
        name='s1207_dmdev'),

url(r'^s1207-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_dmdev.salvar', 
        name='s1207_dmdev_salvar'),



url(r'^s1207-itens/apagar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_itens.apagar', 
        name='s1207_itens_apagar'),

url(r'^s1207-itens/listar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_itens.listar', 
        name='s1207_itens'),

url(r'^s1207-itens/salvar/(?P<hash>.*)/$', 
        'emensageria.s1207.views.s1207_itens.salvar', 
        name='s1207_itens_salvar'),



url(r'^s1210-deps/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_deps.apagar', 
        name='s1210_deps_apagar'),

url(r'^s1210-deps/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_deps.listar', 
        name='s1210_deps'),

url(r'^s1210-deps/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_deps.salvar', 
        name='s1210_deps_salvar'),



url(r'^s1210-infopgto/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_infopgto.apagar', 
        name='s1210_infopgto_apagar'),

url(r'^s1210-infopgto/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_infopgto.listar', 
        name='s1210_infopgto'),

url(r'^s1210-infopgto/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_infopgto.salvar', 
        name='s1210_infopgto_salvar'),

)


urlpatterns += patterns('',


url(r'^s1210-detpgtofl/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl.apagar', 
        name='s1210_detpgtofl_apagar'),

url(r'^s1210-detpgtofl/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl.listar', 
        name='s1210_detpgtofl'),

url(r'^s1210-detpgtofl/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl.salvar', 
        name='s1210_detpgtofl_salvar'),



url(r'^s1210-detpgtofl-retpgtotot/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_retpgtotot.apagar', 
        name='s1210_detpgtofl_retpgtotot_apagar'),

url(r'^s1210-detpgtofl-retpgtotot/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_retpgtotot.listar', 
        name='s1210_detpgtofl_retpgtotot'),

url(r'^s1210-detpgtofl-retpgtotot/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_retpgtotot.salvar', 
        name='s1210_detpgtofl_retpgtotot_salvar'),



url(r'^s1210-detpgtofl-penalim/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_penalim.apagar', 
        name='s1210_detpgtofl_penalim_apagar'),

url(r'^s1210-detpgtofl-penalim/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_penalim.listar', 
        name='s1210_detpgtofl_penalim'),

url(r'^s1210-detpgtofl-penalim/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_penalim.salvar', 
        name='s1210_detpgtofl_penalim_salvar'),



url(r'^s1210-detpgtofl-infopgtoparc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_infopgtoparc.apagar', 
        name='s1210_detpgtofl_infopgtoparc_apagar'),

url(r'^s1210-detpgtofl-infopgtoparc/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_infopgtoparc.listar', 
        name='s1210_detpgtofl_infopgtoparc'),

url(r'^s1210-detpgtofl-infopgtoparc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofl_infopgtoparc.salvar', 
        name='s1210_detpgtofl_infopgtoparc_salvar'),



url(r'^s1210-detpgtobenpr/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr.apagar', 
        name='s1210_detpgtobenpr_apagar'),

url(r'^s1210-detpgtobenpr/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr.listar', 
        name='s1210_detpgtobenpr'),

url(r'^s1210-detpgtobenpr/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr.salvar', 
        name='s1210_detpgtobenpr_salvar'),



url(r'^s1210-detpgtobenpr-retpgtotot/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_retpgtotot.apagar', 
        name='s1210_detpgtobenpr_retpgtotot_apagar'),

url(r'^s1210-detpgtobenpr-retpgtotot/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_retpgtotot.listar', 
        name='s1210_detpgtobenpr_retpgtotot'),

url(r'^s1210-detpgtobenpr-retpgtotot/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_retpgtotot.salvar', 
        name='s1210_detpgtobenpr_retpgtotot_salvar'),



url(r'^s1210-detpgtobenpr-infopgtoparc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_infopgtoparc.apagar', 
        name='s1210_detpgtobenpr_infopgtoparc_apagar'),

url(r'^s1210-detpgtobenpr-infopgtoparc/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_infopgtoparc.listar', 
        name='s1210_detpgtobenpr_infopgtoparc'),

url(r'^s1210-detpgtobenpr-infopgtoparc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtobenpr_infopgtoparc.salvar', 
        name='s1210_detpgtobenpr_infopgtoparc_salvar'),



url(r'^s1210-detpgtofer/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer.apagar', 
        name='s1210_detpgtofer_apagar'),

url(r'^s1210-detpgtofer/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer.listar', 
        name='s1210_detpgtofer'),

url(r'^s1210-detpgtofer/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer.salvar', 
        name='s1210_detpgtofer_salvar'),



url(r'^s1210-detpgtofer-detrubrfer/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_detrubrfer.apagar', 
        name='s1210_detpgtofer_detrubrfer_apagar'),

url(r'^s1210-detpgtofer-detrubrfer/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_detrubrfer.listar', 
        name='s1210_detpgtofer_detrubrfer'),

url(r'^s1210-detpgtofer-detrubrfer/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_detrubrfer.salvar', 
        name='s1210_detpgtofer_detrubrfer_salvar'),



url(r'^s1210-detpgtofer-penalim/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_penalim.apagar', 
        name='s1210_detpgtofer_penalim_apagar'),

url(r'^s1210-detpgtofer-penalim/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_penalim.listar', 
        name='s1210_detpgtofer_penalim'),

url(r'^s1210-detpgtofer-penalim/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtofer_penalim.salvar', 
        name='s1210_detpgtofer_penalim_salvar'),

)


urlpatterns += patterns('',


url(r'^s1210-detpgtoant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant.apagar', 
        name='s1210_detpgtoant_apagar'),

url(r'^s1210-detpgtoant/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant.listar', 
        name='s1210_detpgtoant'),

url(r'^s1210-detpgtoant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant.salvar', 
        name='s1210_detpgtoant_salvar'),



url(r'^s1210-detpgtoant-infopgtoant/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant_infopgtoant.apagar', 
        name='s1210_detpgtoant_infopgtoant_apagar'),

url(r'^s1210-detpgtoant-infopgtoant/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant_infopgtoant.listar', 
        name='s1210_detpgtoant_infopgtoant'),

url(r'^s1210-detpgtoant-infopgtoant/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_detpgtoant_infopgtoant.salvar', 
        name='s1210_detpgtoant_infopgtoant_salvar'),



url(r'^s1210-idepgtoext/apagar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_idepgtoext.apagar', 
        name='s1210_idepgtoext_apagar'),

url(r'^s1210-idepgtoext/listar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_idepgtoext.listar', 
        name='s1210_idepgtoext'),

url(r'^s1210-idepgtoext/salvar/(?P<hash>.*)/$', 
        'emensageria.s1210.views.s1210_idepgtoext.salvar', 
        name='s1210_idepgtoext_salvar'),



url(r'^s1250-tpaquis/apagar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_tpaquis.apagar', 
        name='s1250_tpaquis_apagar'),

url(r'^s1250-tpaquis/listar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_tpaquis.listar', 
        name='s1250_tpaquis'),

url(r'^s1250-tpaquis/salvar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_tpaquis.salvar', 
        name='s1250_tpaquis_salvar'),



url(r'^s1250-ideprodutor/apagar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_ideprodutor.apagar', 
        name='s1250_ideprodutor_apagar'),

url(r'^s1250-ideprodutor/listar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_ideprodutor.listar', 
        name='s1250_ideprodutor'),

url(r'^s1250-ideprodutor/salvar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_ideprodutor.salvar', 
        name='s1250_ideprodutor_salvar'),



url(r'^s1250-nfs/apagar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_nfs.apagar', 
        name='s1250_nfs_apagar'),

url(r'^s1250-nfs/listar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_nfs.listar', 
        name='s1250_nfs'),

url(r'^s1250-nfs/salvar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_nfs.salvar', 
        name='s1250_nfs_salvar'),



url(r'^s1250-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_infoprocjud.apagar', 
        name='s1250_infoprocjud_apagar'),

url(r'^s1250-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_infoprocjud.listar', 
        name='s1250_infoprocjud'),

url(r'^s1250-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageria.s1250.views.s1250_infoprocjud.salvar', 
        name='s1250_infoprocjud_salvar'),



url(r'^s1260-tpcomerc/apagar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_tpcomerc.apagar', 
        name='s1260_tpcomerc_apagar'),

url(r'^s1260-tpcomerc/listar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_tpcomerc.listar', 
        name='s1260_tpcomerc'),

url(r'^s1260-tpcomerc/salvar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_tpcomerc.salvar', 
        name='s1260_tpcomerc_salvar'),



url(r'^s1260-ideadquir/apagar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_ideadquir.apagar', 
        name='s1260_ideadquir_apagar'),

url(r'^s1260-ideadquir/listar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_ideadquir.listar', 
        name='s1260_ideadquir'),

url(r'^s1260-ideadquir/salvar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_ideadquir.salvar', 
        name='s1260_ideadquir_salvar'),



url(r'^s1260-nfs/apagar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_nfs.apagar', 
        name='s1260_nfs_apagar'),

url(r'^s1260-nfs/listar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_nfs.listar', 
        name='s1260_nfs'),

url(r'^s1260-nfs/salvar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_nfs.salvar', 
        name='s1260_nfs_salvar'),

)


urlpatterns += patterns('',


url(r'^s1260-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_infoprocjud.apagar', 
        name='s1260_infoprocjud_apagar'),

url(r'^s1260-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_infoprocjud.listar', 
        name='s1260_infoprocjud'),

url(r'^s1260-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageria.s1260.views.s1260_infoprocjud.salvar', 
        name='s1260_infoprocjud_salvar'),



url(r'^s1270-remunavnp/apagar/(?P<hash>.*)/$', 
        'emensageria.s1270.views.s1270_remunavnp.apagar', 
        name='s1270_remunavnp_apagar'),

url(r'^s1270-remunavnp/listar/(?P<hash>.*)/$', 
        'emensageria.s1270.views.s1270_remunavnp.listar', 
        name='s1270_remunavnp'),

url(r'^s1270-remunavnp/salvar/(?P<hash>.*)/$', 
        'emensageria.s1270.views.s1270_remunavnp.salvar', 
        name='s1270_remunavnp_salvar'),



url(r'^s1280-infosubstpatr/apagar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatr.apagar', 
        name='s1280_infosubstpatr_apagar'),

url(r'^s1280-infosubstpatr/listar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatr.listar', 
        name='s1280_infosubstpatr'),

url(r'^s1280-infosubstpatr/salvar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatr.salvar', 
        name='s1280_infosubstpatr_salvar'),



url(r'^s1280-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatropport.apagar', 
        name='s1280_infosubstpatropport_apagar'),

url(r'^s1280-infosubstpatropport/listar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatropport.listar', 
        name='s1280_infosubstpatropport'),

url(r'^s1280-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infosubstpatropport.salvar', 
        name='s1280_infosubstpatropport_salvar'),



url(r'^s1280-infoativconcom/apagar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infoativconcom.apagar', 
        name='s1280_infoativconcom_apagar'),

url(r'^s1280-infoativconcom/listar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infoativconcom.listar', 
        name='s1280_infoativconcom'),

url(r'^s1280-infoativconcom/salvar/(?P<hash>.*)/$', 
        'emensageria.s1280.views.s1280_infoativconcom.salvar', 
        name='s1280_infoativconcom_salvar'),



url(r'^s1295-iderespinf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1295.views.s1295_iderespinf.apagar', 
        name='s1295_iderespinf_apagar'),

url(r'^s1295-iderespinf/listar/(?P<hash>.*)/$', 
        'emensageria.s1295.views.s1295_iderespinf.listar', 
        name='s1295_iderespinf'),

url(r'^s1295-iderespinf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1295.views.s1295_iderespinf.salvar', 
        name='s1295_iderespinf_salvar'),



url(r'^s1299-iderespinf/apagar/(?P<hash>.*)/$', 
        'emensageria.s1299.views.s1299_iderespinf.apagar', 
        name='s1299_iderespinf_apagar'),

url(r'^s1299-iderespinf/listar/(?P<hash>.*)/$', 
        'emensageria.s1299.views.s1299_iderespinf.listar', 
        name='s1299_iderespinf'),

url(r'^s1299-iderespinf/salvar/(?P<hash>.*)/$', 
        'emensageria.s1299.views.s1299_iderespinf.salvar', 
        name='s1299_iderespinf_salvar'),



url(r'^s1300-contribsind/apagar/(?P<hash>.*)/$', 
        'emensageria.s1300.views.s1300_contribsind.apagar', 
        name='s1300_contribsind_apagar'),

url(r'^s1300-contribsind/listar/(?P<hash>.*)/$', 
        'emensageria.s1300.views.s1300_contribsind.listar', 
        name='s1300_contribsind'),

url(r'^s1300-contribsind/salvar/(?P<hash>.*)/$', 
        'emensageria.s1300.views.s1300_contribsind.salvar', 
        name='s1300_contribsind_salvar'),



url(r'^s2200-documentos/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_documentos.apagar', 
        name='s2200_documentos_apagar'),

url(r'^s2200-documentos/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_documentos.listar', 
        name='s2200_documentos'),

url(r'^s2200-documentos/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_documentos.salvar', 
        name='s2200_documentos_salvar'),



url(r'^s2200-ctps/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ctps.apagar', 
        name='s2200_ctps_apagar'),

url(r'^s2200-ctps/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ctps.listar', 
        name='s2200_ctps'),

url(r'^s2200-ctps/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ctps.salvar', 
        name='s2200_ctps_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-ric/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ric.apagar', 
        name='s2200_ric_apagar'),

url(r'^s2200-ric/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ric.listar', 
        name='s2200_ric'),

url(r'^s2200-ric/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ric.salvar', 
        name='s2200_ric_salvar'),



url(r'^s2200-rg/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rg.apagar', 
        name='s2200_rg_apagar'),

url(r'^s2200-rg/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rg.listar', 
        name='s2200_rg'),

url(r'^s2200-rg/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rg.salvar', 
        name='s2200_rg_salvar'),



url(r'^s2200-rne/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rne.apagar', 
        name='s2200_rne_apagar'),

url(r'^s2200-rne/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rne.listar', 
        name='s2200_rne'),

url(r'^s2200-rne/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_rne.salvar', 
        name='s2200_rne_salvar'),



url(r'^s2200-oc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_oc.apagar', 
        name='s2200_oc_apagar'),

url(r'^s2200-oc/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_oc.listar', 
        name='s2200_oc'),

url(r'^s2200-oc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_oc.salvar', 
        name='s2200_oc_salvar'),



url(r'^s2200-cnh/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_cnh.apagar', 
        name='s2200_cnh_apagar'),

url(r'^s2200-cnh/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_cnh.listar', 
        name='s2200_cnh'),

url(r'^s2200-cnh/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_cnh.salvar', 
        name='s2200_cnh_salvar'),



url(r'^s2200-brasil/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_brasil.apagar', 
        name='s2200_brasil_apagar'),

url(r'^s2200-brasil/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_brasil.listar', 
        name='s2200_brasil'),

url(r'^s2200-brasil/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_brasil.salvar', 
        name='s2200_brasil_salvar'),



url(r'^s2200-exterior/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_exterior.apagar', 
        name='s2200_exterior_apagar'),

url(r'^s2200-exterior/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_exterior.listar', 
        name='s2200_exterior'),

url(r'^s2200-exterior/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_exterior.salvar', 
        name='s2200_exterior_salvar'),



url(r'^s2200-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabestrangeiro.apagar', 
        name='s2200_trabestrangeiro_apagar'),

url(r'^s2200-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabestrangeiro.listar', 
        name='s2200_trabestrangeiro'),

url(r'^s2200-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabestrangeiro.salvar', 
        name='s2200_trabestrangeiro_salvar'),



url(r'^s2200-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodeficiencia.apagar', 
        name='s2200_infodeficiencia_apagar'),

url(r'^s2200-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodeficiencia.listar', 
        name='s2200_infodeficiencia'),

url(r'^s2200-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodeficiencia.salvar', 
        name='s2200_infodeficiencia_salvar'),



url(r'^s2200-dependente/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_dependente.apagar', 
        name='s2200_dependente_apagar'),

url(r'^s2200-dependente/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_dependente.listar', 
        name='s2200_dependente'),

url(r'^s2200-dependente/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_dependente.salvar', 
        name='s2200_dependente_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-aposentadoria/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aposentadoria.apagar', 
        name='s2200_aposentadoria_apagar'),

url(r'^s2200-aposentadoria/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aposentadoria.listar', 
        name='s2200_aposentadoria'),

url(r'^s2200-aposentadoria/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aposentadoria.salvar', 
        name='s2200_aposentadoria_salvar'),



url(r'^s2200-contato/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_contato.apagar', 
        name='s2200_contato_apagar'),

url(r'^s2200-contato/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_contato.listar', 
        name='s2200_contato'),

url(r'^s2200-contato/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_contato.salvar', 
        name='s2200_contato_salvar'),



url(r'^s2200-infoceletista/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoceletista.apagar', 
        name='s2200_infoceletista_apagar'),

url(r'^s2200-infoceletista/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoceletista.listar', 
        name='s2200_infoceletista'),

url(r'^s2200-infoceletista/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoceletista.salvar', 
        name='s2200_infoceletista_salvar'),



url(r'^s2200-trabtemporario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabtemporario.apagar', 
        name='s2200_trabtemporario_apagar'),

url(r'^s2200-trabtemporario/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabtemporario.listar', 
        name='s2200_trabtemporario'),

url(r'^s2200-trabtemporario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_trabtemporario.salvar', 
        name='s2200_trabtemporario_salvar'),



url(r'^s2200-ideestabvinc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ideestabvinc.apagar', 
        name='s2200_ideestabvinc_apagar'),

url(r'^s2200-ideestabvinc/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ideestabvinc.listar', 
        name='s2200_ideestabvinc'),

url(r'^s2200-ideestabvinc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_ideestabvinc.salvar', 
        name='s2200_ideestabvinc_salvar'),



url(r'^s2200-idetrabsubstituido/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_idetrabsubstituido.apagar', 
        name='s2200_idetrabsubstituido_apagar'),

url(r'^s2200-idetrabsubstituido/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_idetrabsubstituido.listar', 
        name='s2200_idetrabsubstituido'),

url(r'^s2200-idetrabsubstituido/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_idetrabsubstituido.salvar', 
        name='s2200_idetrabsubstituido_salvar'),



url(r'^s2200-aprend/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aprend.apagar', 
        name='s2200_aprend_apagar'),

url(r'^s2200-aprend/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aprend.listar', 
        name='s2200_aprend'),

url(r'^s2200-aprend/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_aprend.salvar', 
        name='s2200_aprend_salvar'),



url(r'^s2200-infoestatutario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoestatutario.apagar', 
        name='s2200_infoestatutario_apagar'),

url(r'^s2200-infoestatutario/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoestatutario.listar', 
        name='s2200_infoestatutario'),

url(r'^s2200-infoestatutario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infoestatutario.salvar', 
        name='s2200_infoestatutario_salvar'),



url(r'^s2200-infodecjud/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodecjud.apagar', 
        name='s2200_infodecjud_apagar'),

url(r'^s2200-infodecjud/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodecjud.listar', 
        name='s2200_infodecjud'),

url(r'^s2200-infodecjud/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_infodecjud.salvar', 
        name='s2200_infodecjud_salvar'),



url(r'^s2200-localtrabgeral/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabgeral.apagar', 
        name='s2200_localtrabgeral_apagar'),

url(r'^s2200-localtrabgeral/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabgeral.listar', 
        name='s2200_localtrabgeral'),

url(r'^s2200-localtrabgeral/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabgeral.salvar', 
        name='s2200_localtrabgeral_salvar'),

)


urlpatterns += patterns('',


url(r'^s2200-localtrabdom/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabdom.apagar', 
        name='s2200_localtrabdom_apagar'),

url(r'^s2200-localtrabdom/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabdom.listar', 
        name='s2200_localtrabdom'),

url(r'^s2200-localtrabdom/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_localtrabdom.salvar', 
        name='s2200_localtrabdom_salvar'),



url(r'^s2200-horcontratual/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horcontratual.apagar', 
        name='s2200_horcontratual_apagar'),

url(r'^s2200-horcontratual/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horcontratual.listar', 
        name='s2200_horcontratual'),

url(r'^s2200-horcontratual/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horcontratual.salvar', 
        name='s2200_horcontratual_salvar'),



url(r'^s2200-horario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horario.apagar', 
        name='s2200_horario_apagar'),

url(r'^s2200-horario/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horario.listar', 
        name='s2200_horario'),

url(r'^s2200-horario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_horario.salvar', 
        name='s2200_horario_salvar'),



url(r'^s2200-filiacaosindical/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_filiacaosindical.apagar', 
        name='s2200_filiacaosindical_apagar'),

url(r'^s2200-filiacaosindical/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_filiacaosindical.listar', 
        name='s2200_filiacaosindical'),

url(r'^s2200-filiacaosindical/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_filiacaosindical.salvar', 
        name='s2200_filiacaosindical_salvar'),



url(r'^s2200-alvarajudicial/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_alvarajudicial.apagar', 
        name='s2200_alvarajudicial_apagar'),

url(r'^s2200-alvarajudicial/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_alvarajudicial.listar', 
        name='s2200_alvarajudicial'),

url(r'^s2200-alvarajudicial/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_alvarajudicial.salvar', 
        name='s2200_alvarajudicial_salvar'),



url(r'^s2200-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_observacoes.apagar', 
        name='s2200_observacoes_apagar'),

url(r'^s2200-observacoes/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_observacoes.listar', 
        name='s2200_observacoes'),

url(r'^s2200-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_observacoes.salvar', 
        name='s2200_observacoes_salvar'),



url(r'^s2200-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_sucessaovinc.apagar', 
        name='s2200_sucessaovinc_apagar'),

url(r'^s2200-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_sucessaovinc.listar', 
        name='s2200_sucessaovinc'),

url(r'^s2200-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_sucessaovinc.salvar', 
        name='s2200_sucessaovinc_salvar'),



url(r'^s2200-transfdom/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_transfdom.apagar', 
        name='s2200_transfdom_apagar'),

url(r'^s2200-transfdom/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_transfdom.listar', 
        name='s2200_transfdom'),

url(r'^s2200-transfdom/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_transfdom.salvar', 
        name='s2200_transfdom_salvar'),



url(r'^s2200-afastamento/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_afastamento.apagar', 
        name='s2200_afastamento_apagar'),

url(r'^s2200-afastamento/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_afastamento.listar', 
        name='s2200_afastamento'),

url(r'^s2200-afastamento/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_afastamento.salvar', 
        name='s2200_afastamento_salvar'),



url(r'^s2200-desligamento/apagar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_desligamento.apagar', 
        name='s2200_desligamento_apagar'),

url(r'^s2200-desligamento/listar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_desligamento.listar', 
        name='s2200_desligamento'),

url(r'^s2200-desligamento/salvar/(?P<hash>.*)/$', 
        'emensageria.s2200.views.s2200_desligamento.salvar', 
        name='s2200_desligamento_salvar'),

)


urlpatterns += patterns('',


url(r'^s2205-documentos/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_documentos.apagar', 
        name='s2205_documentos_apagar'),

url(r'^s2205-documentos/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_documentos.listar', 
        name='s2205_documentos'),

url(r'^s2205-documentos/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_documentos.salvar', 
        name='s2205_documentos_salvar'),



url(r'^s2205-ctps/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ctps.apagar', 
        name='s2205_ctps_apagar'),

url(r'^s2205-ctps/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ctps.listar', 
        name='s2205_ctps'),

url(r'^s2205-ctps/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ctps.salvar', 
        name='s2205_ctps_salvar'),



url(r'^s2205-ric/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ric.apagar', 
        name='s2205_ric_apagar'),

url(r'^s2205-ric/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ric.listar', 
        name='s2205_ric'),

url(r'^s2205-ric/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_ric.salvar', 
        name='s2205_ric_salvar'),



url(r'^s2205-rg/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rg.apagar', 
        name='s2205_rg_apagar'),

url(r'^s2205-rg/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rg.listar', 
        name='s2205_rg'),

url(r'^s2205-rg/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rg.salvar', 
        name='s2205_rg_salvar'),



url(r'^s2205-rne/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rne.apagar', 
        name='s2205_rne_apagar'),

url(r'^s2205-rne/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rne.listar', 
        name='s2205_rne'),

url(r'^s2205-rne/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_rne.salvar', 
        name='s2205_rne_salvar'),



url(r'^s2205-oc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_oc.apagar', 
        name='s2205_oc_apagar'),

url(r'^s2205-oc/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_oc.listar', 
        name='s2205_oc'),

url(r'^s2205-oc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_oc.salvar', 
        name='s2205_oc_salvar'),



url(r'^s2205-cnh/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_cnh.apagar', 
        name='s2205_cnh_apagar'),

url(r'^s2205-cnh/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_cnh.listar', 
        name='s2205_cnh'),

url(r'^s2205-cnh/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_cnh.salvar', 
        name='s2205_cnh_salvar'),



url(r'^s2205-brasil/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_brasil.apagar', 
        name='s2205_brasil_apagar'),

url(r'^s2205-brasil/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_brasil.listar', 
        name='s2205_brasil'),

url(r'^s2205-brasil/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_brasil.salvar', 
        name='s2205_brasil_salvar'),



url(r'^s2205-exterior/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_exterior.apagar', 
        name='s2205_exterior_apagar'),

url(r'^s2205-exterior/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_exterior.listar', 
        name='s2205_exterior'),

url(r'^s2205-exterior/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_exterior.salvar', 
        name='s2205_exterior_salvar'),



url(r'^s2205-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_trabestrangeiro.apagar', 
        name='s2205_trabestrangeiro_apagar'),

url(r'^s2205-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_trabestrangeiro.listar', 
        name='s2205_trabestrangeiro'),

url(r'^s2205-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_trabestrangeiro.salvar', 
        name='s2205_trabestrangeiro_salvar'),

)


urlpatterns += patterns('',


url(r'^s2205-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_infodeficiencia.apagar', 
        name='s2205_infodeficiencia_apagar'),

url(r'^s2205-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_infodeficiencia.listar', 
        name='s2205_infodeficiencia'),

url(r'^s2205-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_infodeficiencia.salvar', 
        name='s2205_infodeficiencia_salvar'),



url(r'^s2205-dependente/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_dependente.apagar', 
        name='s2205_dependente_apagar'),

url(r'^s2205-dependente/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_dependente.listar', 
        name='s2205_dependente'),

url(r'^s2205-dependente/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_dependente.salvar', 
        name='s2205_dependente_salvar'),



url(r'^s2205-aposentadoria/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_aposentadoria.apagar', 
        name='s2205_aposentadoria_apagar'),

url(r'^s2205-aposentadoria/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_aposentadoria.listar', 
        name='s2205_aposentadoria'),

url(r'^s2205-aposentadoria/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_aposentadoria.salvar', 
        name='s2205_aposentadoria_salvar'),



url(r'^s2205-contato/apagar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_contato.apagar', 
        name='s2205_contato_apagar'),

url(r'^s2205-contato/listar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_contato.listar', 
        name='s2205_contato'),

url(r'^s2205-contato/salvar/(?P<hash>.*)/$', 
        'emensageria.s2205.views.s2205_contato.salvar', 
        name='s2205_contato_salvar'),



url(r'^s2206-infoceletista/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoceletista.apagar', 
        name='s2206_infoceletista_apagar'),

url(r'^s2206-infoceletista/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoceletista.listar', 
        name='s2206_infoceletista'),

url(r'^s2206-infoceletista/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoceletista.salvar', 
        name='s2206_infoceletista_salvar'),



url(r'^s2206-trabtemp/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_trabtemp.apagar', 
        name='s2206_trabtemp_apagar'),

url(r'^s2206-trabtemp/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_trabtemp.listar', 
        name='s2206_trabtemp'),

url(r'^s2206-trabtemp/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_trabtemp.salvar', 
        name='s2206_trabtemp_salvar'),



url(r'^s2206-aprend/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_aprend.apagar', 
        name='s2206_aprend_apagar'),

url(r'^s2206-aprend/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_aprend.listar', 
        name='s2206_aprend'),

url(r'^s2206-aprend/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_aprend.salvar', 
        name='s2206_aprend_salvar'),



url(r'^s2206-infoestatutario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoestatutario.apagar', 
        name='s2206_infoestatutario_apagar'),

url(r'^s2206-infoestatutario/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoestatutario.listar', 
        name='s2206_infoestatutario'),

url(r'^s2206-infoestatutario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_infoestatutario.salvar', 
        name='s2206_infoestatutario_salvar'),



url(r'^s2206-localtrabgeral/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabgeral.apagar', 
        name='s2206_localtrabgeral_apagar'),

url(r'^s2206-localtrabgeral/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabgeral.listar', 
        name='s2206_localtrabgeral'),

url(r'^s2206-localtrabgeral/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabgeral.salvar', 
        name='s2206_localtrabgeral_salvar'),



url(r'^s2206-localtrabdom/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabdom.apagar', 
        name='s2206_localtrabdom_apagar'),

url(r'^s2206-localtrabdom/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabdom.listar', 
        name='s2206_localtrabdom'),

url(r'^s2206-localtrabdom/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_localtrabdom.salvar', 
        name='s2206_localtrabdom_salvar'),

)


urlpatterns += patterns('',


url(r'^s2206-horcontratual/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horcontratual.apagar', 
        name='s2206_horcontratual_apagar'),

url(r'^s2206-horcontratual/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horcontratual.listar', 
        name='s2206_horcontratual'),

url(r'^s2206-horcontratual/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horcontratual.salvar', 
        name='s2206_horcontratual_salvar'),



url(r'^s2206-horario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horario.apagar', 
        name='s2206_horario_apagar'),

url(r'^s2206-horario/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horario.listar', 
        name='s2206_horario'),

url(r'^s2206-horario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_horario.salvar', 
        name='s2206_horario_salvar'),



url(r'^s2206-filiacaosindical/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_filiacaosindical.apagar', 
        name='s2206_filiacaosindical_apagar'),

url(r'^s2206-filiacaosindical/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_filiacaosindical.listar', 
        name='s2206_filiacaosindical'),

url(r'^s2206-filiacaosindical/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_filiacaosindical.salvar', 
        name='s2206_filiacaosindical_salvar'),



url(r'^s2206-alvarajudicial/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_alvarajudicial.apagar', 
        name='s2206_alvarajudicial_apagar'),

url(r'^s2206-alvarajudicial/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_alvarajudicial.listar', 
        name='s2206_alvarajudicial'),

url(r'^s2206-alvarajudicial/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_alvarajudicial.salvar', 
        name='s2206_alvarajudicial_salvar'),



url(r'^s2206-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_observacoes.apagar', 
        name='s2206_observacoes_apagar'),

url(r'^s2206-observacoes/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_observacoes.listar', 
        name='s2206_observacoes'),

url(r'^s2206-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_observacoes.salvar', 
        name='s2206_observacoes_salvar'),



url(r'^s2206-servpubl/apagar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_servpubl.apagar', 
        name='s2206_servpubl_apagar'),

url(r'^s2206-servpubl/listar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_servpubl.listar', 
        name='s2206_servpubl'),

url(r'^s2206-servpubl/salvar/(?P<hash>.*)/$', 
        'emensageria.s2206.views.s2206_servpubl.salvar', 
        name='s2206_servpubl_salvar'),



url(r'^s2210-parteatingida/apagar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_parteatingida.apagar', 
        name='s2210_parteatingida_apagar'),

url(r'^s2210-parteatingida/listar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_parteatingida.listar', 
        name='s2210_parteatingida'),

url(r'^s2210-parteatingida/salvar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_parteatingida.salvar', 
        name='s2210_parteatingida_salvar'),



url(r'^s2210-agentecausador/apagar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_agentecausador.apagar', 
        name='s2210_agentecausador_apagar'),

url(r'^s2210-agentecausador/listar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_agentecausador.listar', 
        name='s2210_agentecausador'),

url(r'^s2210-agentecausador/salvar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_agentecausador.salvar', 
        name='s2210_agentecausador_salvar'),



url(r'^s2210-atestado/apagar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_atestado.apagar', 
        name='s2210_atestado_apagar'),

url(r'^s2210-atestado/listar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_atestado.listar', 
        name='s2210_atestado'),

url(r'^s2210-atestado/salvar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_atestado.salvar', 
        name='s2210_atestado_salvar'),



url(r'^s2210-catorigem/apagar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_catorigem.apagar', 
        name='s2210_catorigem_apagar'),

url(r'^s2210-catorigem/listar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_catorigem.listar', 
        name='s2210_catorigem'),

url(r'^s2210-catorigem/salvar/(?P<hash>.*)/$', 
        'emensageria.s2210.views.s2210_catorigem.salvar', 
        name='s2210_catorigem_salvar'),

)


urlpatterns += patterns('',


url(r'^s2220-exame/apagar/(?P<hash>.*)/$', 
        'emensageria.s2220.views.s2220_exame.apagar', 
        name='s2220_exame_apagar'),

url(r'^s2220-exame/listar/(?P<hash>.*)/$', 
        'emensageria.s2220.views.s2220_exame.listar', 
        name='s2220_exame'),

url(r'^s2220-exame/salvar/(?P<hash>.*)/$', 
        'emensageria.s2220.views.s2220_exame.salvar', 
        name='s2220_exame_salvar'),



url(r'^s2230-iniafastamento/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_iniafastamento.apagar', 
        name='s2230_iniafastamento_apagar'),

url(r'^s2230-iniafastamento/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_iniafastamento.listar', 
        name='s2230_iniafastamento'),

url(r'^s2230-iniafastamento/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_iniafastamento.salvar', 
        name='s2230_iniafastamento_salvar'),



url(r'^s2230-infoatestado/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infoatestado.apagar', 
        name='s2230_infoatestado_apagar'),

url(r'^s2230-infoatestado/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infoatestado.listar', 
        name='s2230_infoatestado'),

url(r'^s2230-infoatestado/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infoatestado.salvar', 
        name='s2230_infoatestado_salvar'),



url(r'^s2230-emitente/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_emitente.apagar', 
        name='s2230_emitente_apagar'),

url(r'^s2230-emitente/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_emitente.listar', 
        name='s2230_emitente'),

url(r'^s2230-emitente/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_emitente.salvar', 
        name='s2230_emitente_salvar'),



url(r'^s2230-infocessao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infocessao.apagar', 
        name='s2230_infocessao_apagar'),

url(r'^s2230-infocessao/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infocessao.listar', 
        name='s2230_infocessao'),

url(r'^s2230-infocessao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infocessao.salvar', 
        name='s2230_infocessao_salvar'),



url(r'^s2230-infomandsind/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infomandsind.apagar', 
        name='s2230_infomandsind_apagar'),

url(r'^s2230-infomandsind/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infomandsind.listar', 
        name='s2230_infomandsind'),

url(r'^s2230-infomandsind/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_infomandsind.salvar', 
        name='s2230_infomandsind_salvar'),



url(r'^s2230-inforetif/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_inforetif.apagar', 
        name='s2230_inforetif_apagar'),

url(r'^s2230-inforetif/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_inforetif.listar', 
        name='s2230_inforetif'),

url(r'^s2230-inforetif/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_inforetif.salvar', 
        name='s2230_inforetif_salvar'),



url(r'^s2230-fimafastamento/apagar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_fimafastamento.apagar', 
        name='s2230_fimafastamento_apagar'),

url(r'^s2230-fimafastamento/listar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_fimafastamento.listar', 
        name='s2230_fimafastamento'),

url(r'^s2230-fimafastamento/salvar/(?P<hash>.*)/$', 
        'emensageria.s2230.views.s2230_fimafastamento.salvar', 
        name='s2230_fimafastamento_salvar'),



url(r'^s2240-iniexprisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco.apagar', 
        name='s2240_iniexprisco_apagar'),

url(r'^s2240-iniexprisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco.listar', 
        name='s2240_iniexprisco'),

url(r'^s2240-iniexprisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco.salvar', 
        name='s2240_iniexprisco_salvar'),



url(r'^s2240-iniexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_infoamb.apagar', 
        name='s2240_iniexprisco_infoamb_apagar'),

url(r'^s2240-iniexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_infoamb.listar', 
        name='s2240_iniexprisco_infoamb'),

url(r'^s2240-iniexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_infoamb.salvar', 
        name='s2240_iniexprisco_infoamb_salvar'),

)


urlpatterns += patterns('',


url(r'^s2240-iniexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_fatrisco.apagar', 
        name='s2240_iniexprisco_fatrisco_apagar'),

url(r'^s2240-iniexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_fatrisco.listar', 
        name='s2240_iniexprisco_fatrisco'),

url(r'^s2240-iniexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_fatrisco.salvar', 
        name='s2240_iniexprisco_fatrisco_salvar'),



url(r'^s2240-iniexprisco-epc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epc.apagar', 
        name='s2240_iniexprisco_epc_apagar'),

url(r'^s2240-iniexprisco-epc/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epc.listar', 
        name='s2240_iniexprisco_epc'),

url(r'^s2240-iniexprisco-epc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epc.salvar', 
        name='s2240_iniexprisco_epc_salvar'),



url(r'^s2240-iniexprisco-epi/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epi.apagar', 
        name='s2240_iniexprisco_epi_apagar'),

url(r'^s2240-iniexprisco-epi/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epi.listar', 
        name='s2240_iniexprisco_epi'),

url(r'^s2240-iniexprisco-epi/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_iniexprisco_epi.salvar', 
        name='s2240_iniexprisco_epi_salvar'),



url(r'^s2240-altexprisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco.apagar', 
        name='s2240_altexprisco_apagar'),

url(r'^s2240-altexprisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco.listar', 
        name='s2240_altexprisco'),

url(r'^s2240-altexprisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco.salvar', 
        name='s2240_altexprisco_salvar'),



url(r'^s2240-altexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_infoamb.apagar', 
        name='s2240_altexprisco_infoamb_apagar'),

url(r'^s2240-altexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_infoamb.listar', 
        name='s2240_altexprisco_infoamb'),

url(r'^s2240-altexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_infoamb.salvar', 
        name='s2240_altexprisco_infoamb_salvar'),



url(r'^s2240-altexprisco-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_fatrisco.apagar', 
        name='s2240_altexprisco_fatrisco_apagar'),

url(r'^s2240-altexprisco-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_fatrisco.listar', 
        name='s2240_altexprisco_fatrisco'),

url(r'^s2240-altexprisco-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_fatrisco.salvar', 
        name='s2240_altexprisco_fatrisco_salvar'),



url(r'^s2240-altexprisco-epc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epc.apagar', 
        name='s2240_altexprisco_epc_apagar'),

url(r'^s2240-altexprisco-epc/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epc.listar', 
        name='s2240_altexprisco_epc'),

url(r'^s2240-altexprisco-epc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epc.salvar', 
        name='s2240_altexprisco_epc_salvar'),



url(r'^s2240-altexprisco-epi/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epi.apagar', 
        name='s2240_altexprisco_epi_apagar'),

url(r'^s2240-altexprisco-epi/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epi.listar', 
        name='s2240_altexprisco_epi'),

url(r'^s2240-altexprisco-epi/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_altexprisco_epi.salvar', 
        name='s2240_altexprisco_epi_salvar'),



url(r'^s2240-fimexprisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco.apagar', 
        name='s2240_fimexprisco_apagar'),

url(r'^s2240-fimexprisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco.listar', 
        name='s2240_fimexprisco'),

url(r'^s2240-fimexprisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco.salvar', 
        name='s2240_fimexprisco_salvar'),



url(r'^s2240-fimexprisco-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_infoamb.apagar', 
        name='s2240_fimexprisco_infoamb_apagar'),

url(r'^s2240-fimexprisco-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_infoamb.listar', 
        name='s2240_fimexprisco_infoamb'),

url(r'^s2240-fimexprisco-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_infoamb.salvar', 
        name='s2240_fimexprisco_infoamb_salvar'),

)


urlpatterns += patterns('',


url(r'^s2240-fimexprisco-respreg/apagar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_respreg.apagar', 
        name='s2240_fimexprisco_respreg_apagar'),

url(r'^s2240-fimexprisco-respreg/listar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_respreg.listar', 
        name='s2240_fimexprisco_respreg'),

url(r'^s2240-fimexprisco-respreg/salvar/(?P<hash>.*)/$', 
        'emensageria.s2240.views.s2240_fimexprisco_respreg.salvar', 
        name='s2240_fimexprisco_respreg_salvar'),



url(r'^s2241-insalperic/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_insalperic.apagar', 
        name='s2241_insalperic_apagar'),

url(r'^s2241-insalperic/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_insalperic.listar', 
        name='s2241_insalperic'),

url(r'^s2241-insalperic/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_insalperic.salvar', 
        name='s2241_insalperic_salvar'),



url(r'^s2241-iniinsalperic/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic.apagar', 
        name='s2241_iniinsalperic_apagar'),

url(r'^s2241-iniinsalperic/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic.listar', 
        name='s2241_iniinsalperic'),

url(r'^s2241-iniinsalperic/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic.salvar', 
        name='s2241_iniinsalperic_salvar'),



url(r'^s2241-iniinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_infoamb.apagar', 
        name='s2241_iniinsalperic_infoamb_apagar'),

url(r'^s2241-iniinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_infoamb.listar', 
        name='s2241_iniinsalperic_infoamb'),

url(r'^s2241-iniinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_infoamb.salvar', 
        name='s2241_iniinsalperic_infoamb_salvar'),



url(r'^s2241-iniinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_fatrisco.apagar', 
        name='s2241_iniinsalperic_fatrisco_apagar'),

url(r'^s2241-iniinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_fatrisco.listar', 
        name='s2241_iniinsalperic_fatrisco'),

url(r'^s2241-iniinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniinsalperic_fatrisco.salvar', 
        name='s2241_iniinsalperic_fatrisco_salvar'),



url(r'^s2241-altinsalperic/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic.apagar', 
        name='s2241_altinsalperic_apagar'),

url(r'^s2241-altinsalperic/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic.listar', 
        name='s2241_altinsalperic'),

url(r'^s2241-altinsalperic/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic.salvar', 
        name='s2241_altinsalperic_salvar'),



url(r'^s2241-altinsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_infoamb.apagar', 
        name='s2241_altinsalperic_infoamb_apagar'),

url(r'^s2241-altinsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_infoamb.listar', 
        name='s2241_altinsalperic_infoamb'),

url(r'^s2241-altinsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_infoamb.salvar', 
        name='s2241_altinsalperic_infoamb_salvar'),



url(r'^s2241-altinsalperic-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_fatrisco.apagar', 
        name='s2241_altinsalperic_fatrisco_apagar'),

url(r'^s2241-altinsalperic-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_fatrisco.listar', 
        name='s2241_altinsalperic_fatrisco'),

url(r'^s2241-altinsalperic-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altinsalperic_fatrisco.salvar', 
        name='s2241_altinsalperic_fatrisco_salvar'),



url(r'^s2241-fiminsalperic/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic.apagar', 
        name='s2241_fiminsalperic_apagar'),

url(r'^s2241-fiminsalperic/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic.listar', 
        name='s2241_fiminsalperic'),

url(r'^s2241-fiminsalperic/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic.salvar', 
        name='s2241_fiminsalperic_salvar'),



url(r'^s2241-fiminsalperic-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic_infoamb.apagar', 
        name='s2241_fiminsalperic_infoamb_apagar'),

url(r'^s2241-fiminsalperic-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic_infoamb.listar', 
        name='s2241_fiminsalperic_infoamb'),

url(r'^s2241-fiminsalperic-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fiminsalperic_infoamb.salvar', 
        name='s2241_fiminsalperic_infoamb_salvar'),

)


urlpatterns += patterns('',


url(r'^s2241-aposentesp/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_aposentesp.apagar', 
        name='s2241_aposentesp_apagar'),

url(r'^s2241-aposentesp/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_aposentesp.listar', 
        name='s2241_aposentesp'),

url(r'^s2241-aposentesp/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_aposentesp.salvar', 
        name='s2241_aposentesp_salvar'),



url(r'^s2241-iniaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp.apagar', 
        name='s2241_iniaposentesp_apagar'),

url(r'^s2241-iniaposentesp/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp.listar', 
        name='s2241_iniaposentesp'),

url(r'^s2241-iniaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp.salvar', 
        name='s2241_iniaposentesp_salvar'),



url(r'^s2241-iniaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_infoamb.apagar', 
        name='s2241_iniaposentesp_infoamb_apagar'),

url(r'^s2241-iniaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_infoamb.listar', 
        name='s2241_iniaposentesp_infoamb'),

url(r'^s2241-iniaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_infoamb.salvar', 
        name='s2241_iniaposentesp_infoamb_salvar'),



url(r'^s2241-iniaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_fatrisco.apagar', 
        name='s2241_iniaposentesp_fatrisco_apagar'),

url(r'^s2241-iniaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_fatrisco.listar', 
        name='s2241_iniaposentesp_fatrisco'),

url(r'^s2241-iniaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_iniaposentesp_fatrisco.salvar', 
        name='s2241_iniaposentesp_fatrisco_salvar'),



url(r'^s2241-altaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp.apagar', 
        name='s2241_altaposentesp_apagar'),

url(r'^s2241-altaposentesp/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp.listar', 
        name='s2241_altaposentesp'),

url(r'^s2241-altaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp.salvar', 
        name='s2241_altaposentesp_salvar'),



url(r'^s2241-altaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_infoamb.apagar', 
        name='s2241_altaposentesp_infoamb_apagar'),

url(r'^s2241-altaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_infoamb.listar', 
        name='s2241_altaposentesp_infoamb'),

url(r'^s2241-altaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_infoamb.salvar', 
        name='s2241_altaposentesp_infoamb_salvar'),



url(r'^s2241-altaposentesp-fatrisco/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_fatrisco.apagar', 
        name='s2241_altaposentesp_fatrisco_apagar'),

url(r'^s2241-altaposentesp-fatrisco/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_fatrisco.listar', 
        name='s2241_altaposentesp_fatrisco'),

url(r'^s2241-altaposentesp-fatrisco/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_altaposentesp_fatrisco.salvar', 
        name='s2241_altaposentesp_fatrisco_salvar'),



url(r'^s2241-fimaposentesp/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp.apagar', 
        name='s2241_fimaposentesp_apagar'),

url(r'^s2241-fimaposentesp/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp.listar', 
        name='s2241_fimaposentesp'),

url(r'^s2241-fimaposentesp/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp.salvar', 
        name='s2241_fimaposentesp_salvar'),



url(r'^s2241-fimaposentesp-infoamb/apagar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp_infoamb.apagar', 
        name='s2241_fimaposentesp_infoamb_apagar'),

url(r'^s2241-fimaposentesp-infoamb/listar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp_infoamb.listar', 
        name='s2241_fimaposentesp_infoamb'),

url(r'^s2241-fimaposentesp-infoamb/salvar/(?P<hash>.*)/$', 
        'emensageria.s2241.views.s2241_fimaposentesp_infoamb.salvar', 
        name='s2241_fimaposentesp_infoamb_salvar'),



url(r'^s2250-detavprevio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_detavprevio.apagar', 
        name='s2250_detavprevio_apagar'),

url(r'^s2250-detavprevio/listar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_detavprevio.listar', 
        name='s2250_detavprevio'),

url(r'^s2250-detavprevio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_detavprevio.salvar', 
        name='s2250_detavprevio_salvar'),

)


urlpatterns += patterns('',


url(r'^s2250-cancavprevio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_cancavprevio.apagar', 
        name='s2250_cancavprevio_apagar'),

url(r'^s2250-cancavprevio/listar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_cancavprevio.listar', 
        name='s2250_cancavprevio'),

url(r'^s2250-cancavprevio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2250.views.s2250_cancavprevio.salvar', 
        name='s2250_cancavprevio_salvar'),



url(r'^s2260-localtrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageria.s2260.views.s2260_localtrabinterm.apagar', 
        name='s2260_localtrabinterm_apagar'),

url(r'^s2260-localtrabinterm/listar/(?P<hash>.*)/$', 
        'emensageria.s2260.views.s2260_localtrabinterm.listar', 
        name='s2260_localtrabinterm'),

url(r'^s2260-localtrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageria.s2260.views.s2260_localtrabinterm.salvar', 
        name='s2260_localtrabinterm_salvar'),



url(r'^s2299-observacoes/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_observacoes.apagar', 
        name='s2299_observacoes_apagar'),

url(r'^s2299-observacoes/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_observacoes.listar', 
        name='s2299_observacoes'),

url(r'^s2299-observacoes/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_observacoes.salvar', 
        name='s2299_observacoes_salvar'),



url(r'^s2299-sucessaovinc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_sucessaovinc.apagar', 
        name='s2299_sucessaovinc_apagar'),

url(r'^s2299-sucessaovinc/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_sucessaovinc.listar', 
        name='s2299_sucessaovinc'),

url(r'^s2299-sucessaovinc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_sucessaovinc.salvar', 
        name='s2299_sucessaovinc_salvar'),



url(r'^s2299-transftit/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_transftit.apagar', 
        name='s2299_transftit_apagar'),

url(r'^s2299-transftit/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_transftit.listar', 
        name='s2299_transftit'),

url(r'^s2299-transftit/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_transftit.salvar', 
        name='s2299_transftit_salvar'),



url(r'^s2299-verbasresc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_verbasresc.apagar', 
        name='s2299_verbasresc_apagar'),

url(r'^s2299-verbasresc/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_verbasresc.listar', 
        name='s2299_verbasresc'),

url(r'^s2299-verbasresc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_verbasresc.salvar', 
        name='s2299_verbasresc_salvar'),



url(r'^s2299-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_dmdev.apagar', 
        name='s2299_dmdev_apagar'),

url(r'^s2299-dmdev/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_dmdev.listar', 
        name='s2299_dmdev'),

url(r'^s2299-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_dmdev.salvar', 
        name='s2299_dmdev_salvar'),



url(r'^s2299-infoperapur/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur.apagar', 
        name='s2299_infoperapur_apagar'),

url(r'^s2299-infoperapur/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur.listar', 
        name='s2299_infoperapur'),

url(r'^s2299-infoperapur/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur.salvar', 
        name='s2299_infoperapur_salvar'),



url(r'^s2299-infoperapur-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_ideestablot.apagar', 
        name='s2299_infoperapur_ideestablot_apagar'),

url(r'^s2299-infoperapur-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_ideestablot.listar', 
        name='s2299_infoperapur_ideestablot'),

url(r'^s2299-infoperapur-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_ideestablot.salvar', 
        name='s2299_infoperapur_ideestablot_salvar'),



url(r'^s2299-infoperapur-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detverbas.apagar', 
        name='s2299_infoperapur_detverbas_apagar'),

url(r'^s2299-infoperapur-detverbas/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detverbas.listar', 
        name='s2299_infoperapur_detverbas'),

url(r'^s2299-infoperapur-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detverbas.salvar', 
        name='s2299_infoperapur_detverbas_salvar'),

)


urlpatterns += patterns('',


url(r'^s2299-infoperapur-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosaudecolet.apagar', 
        name='s2299_infoperapur_infosaudecolet_apagar'),

url(r'^s2299-infoperapur-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosaudecolet.listar', 
        name='s2299_infoperapur_infosaudecolet'),

url(r'^s2299-infoperapur-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosaudecolet.salvar', 
        name='s2299_infoperapur_infosaudecolet_salvar'),



url(r'^s2299-infoperapur-detoper/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detoper.apagar', 
        name='s2299_infoperapur_detoper_apagar'),

url(r'^s2299-infoperapur-detoper/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detoper.listar', 
        name='s2299_infoperapur_detoper'),

url(r'^s2299-infoperapur-detoper/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detoper.salvar', 
        name='s2299_infoperapur_detoper_salvar'),



url(r'^s2299-infoperapur-detplano/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detplano.apagar', 
        name='s2299_infoperapur_detplano_apagar'),

url(r'^s2299-infoperapur-detplano/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detplano.listar', 
        name='s2299_infoperapur_detplano'),

url(r'^s2299-infoperapur-detplano/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_detplano.salvar', 
        name='s2299_infoperapur_detplano_salvar'),



url(r'^s2299-infoperapur-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infoagnocivo.apagar', 
        name='s2299_infoperapur_infoagnocivo_apagar'),

url(r'^s2299-infoperapur-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infoagnocivo.listar', 
        name='s2299_infoperapur_infoagnocivo'),

url(r'^s2299-infoperapur-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infoagnocivo.salvar', 
        name='s2299_infoperapur_infoagnocivo_salvar'),



url(r'^s2299-infoperapur-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosimples.apagar', 
        name='s2299_infoperapur_infosimples_apagar'),

url(r'^s2299-infoperapur-infosimples/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosimples.listar', 
        name='s2299_infoperapur_infosimples'),

url(r'^s2299-infoperapur-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperapur_infosimples.salvar', 
        name='s2299_infoperapur_infosimples_salvar'),



url(r'^s2299-infoperant/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant.apagar', 
        name='s2299_infoperant_apagar'),

url(r'^s2299-infoperant/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant.listar', 
        name='s2299_infoperant'),

url(r'^s2299-infoperant/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant.salvar', 
        name='s2299_infoperant_salvar'),



url(r'^s2299-infoperant-ideadc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideadc.apagar', 
        name='s2299_infoperant_ideadc_apagar'),

url(r'^s2299-infoperant-ideadc/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideadc.listar', 
        name='s2299_infoperant_ideadc'),

url(r'^s2299-infoperant-ideadc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideadc.salvar', 
        name='s2299_infoperant_ideadc_salvar'),



url(r'^s2299-infoperant-ideperiodo/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideperiodo.apagar', 
        name='s2299_infoperant_ideperiodo_apagar'),

url(r'^s2299-infoperant-ideperiodo/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideperiodo.listar', 
        name='s2299_infoperant_ideperiodo'),

url(r'^s2299-infoperant-ideperiodo/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideperiodo.salvar', 
        name='s2299_infoperant_ideperiodo_salvar'),



url(r'^s2299-infoperant-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideestablot.apagar', 
        name='s2299_infoperant_ideestablot_apagar'),

url(r'^s2299-infoperant-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideestablot.listar', 
        name='s2299_infoperant_ideestablot'),

url(r'^s2299-infoperant-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_ideestablot.salvar', 
        name='s2299_infoperant_ideestablot_salvar'),



url(r'^s2299-infoperant-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_detverbas.apagar', 
        name='s2299_infoperant_detverbas_apagar'),

url(r'^s2299-infoperant-detverbas/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_detverbas.listar', 
        name='s2299_infoperant_detverbas'),

url(r'^s2299-infoperant-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_detverbas.salvar', 
        name='s2299_infoperant_detverbas_salvar'),

)


urlpatterns += patterns('',


url(r'^s2299-infoperant-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infoagnocivo.apagar', 
        name='s2299_infoperant_infoagnocivo_apagar'),

url(r'^s2299-infoperant-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infoagnocivo.listar', 
        name='s2299_infoperant_infoagnocivo'),

url(r'^s2299-infoperant-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infoagnocivo.salvar', 
        name='s2299_infoperant_infoagnocivo_salvar'),



url(r'^s2299-infoperant-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infosimples.apagar', 
        name='s2299_infoperant_infosimples_apagar'),

url(r'^s2299-infoperant-infosimples/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infosimples.listar', 
        name='s2299_infoperant_infosimples'),

url(r'^s2299-infoperant-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infoperant_infosimples.salvar', 
        name='s2299_infoperant_infosimples_salvar'),



url(r'^s2299-infotrabinterm/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm.apagar', 
        name='s2299_infotrabinterm_apagar'),

url(r'^s2299-infotrabinterm/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm.listar', 
        name='s2299_infotrabinterm'),

url(r'^s2299-infotrabinterm/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm.salvar', 
        name='s2299_infotrabinterm_salvar'),



url(r'^s2299-infotrabinterm-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_procjudtrab.apagar', 
        name='s2299_infotrabinterm_procjudtrab_apagar'),

url(r'^s2299-infotrabinterm-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_procjudtrab.listar', 
        name='s2299_infotrabinterm_procjudtrab'),

url(r'^s2299-infotrabinterm-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_procjudtrab.salvar', 
        name='s2299_infotrabinterm_procjudtrab_salvar'),



url(r'^s2299-infotrabinterm-infomv/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_infomv.apagar', 
        name='s2299_infotrabinterm_infomv_apagar'),

url(r'^s2299-infotrabinterm-infomv/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_infomv.listar', 
        name='s2299_infotrabinterm_infomv'),

url(r'^s2299-infotrabinterm-infomv/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_infomv.salvar', 
        name='s2299_infotrabinterm_infomv_salvar'),



url(r'^s2299-infotrabinterm-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_remunoutrempr.apagar', 
        name='s2299_infotrabinterm_remunoutrempr_apagar'),

url(r'^s2299-infotrabinterm-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_remunoutrempr.listar', 
        name='s2299_infotrabinterm_remunoutrempr'),

url(r'^s2299-infotrabinterm-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_remunoutrempr.salvar', 
        name='s2299_infotrabinterm_remunoutrempr_salvar'),



url(r'^s2299-infotrabinterm-proccs/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_proccs.apagar', 
        name='s2299_infotrabinterm_proccs_apagar'),

url(r'^s2299-infotrabinterm-proccs/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_proccs.listar', 
        name='s2299_infotrabinterm_proccs'),

url(r'^s2299-infotrabinterm-proccs/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_proccs.salvar', 
        name='s2299_infotrabinterm_proccs_salvar'),



url(r'^s2299-infotrabinterm-quarentena/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_quarentena.apagar', 
        name='s2299_infotrabinterm_quarentena_apagar'),

url(r'^s2299-infotrabinterm-quarentena/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_quarentena.listar', 
        name='s2299_infotrabinterm_quarentena'),

url(r'^s2299-infotrabinterm-quarentena/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_quarentena.salvar', 
        name='s2299_infotrabinterm_quarentena_salvar'),



url(r'^s2299-infotrabinterm-consigfgts/apagar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_consigfgts.apagar', 
        name='s2299_infotrabinterm_consigfgts_apagar'),

url(r'^s2299-infotrabinterm-consigfgts/listar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_consigfgts.listar', 
        name='s2299_infotrabinterm_consigfgts'),

url(r'^s2299-infotrabinterm-consigfgts/salvar/(?P<hash>.*)/$', 
        'emensageria.s2299.views.s2299_infotrabinterm_consigfgts.salvar', 
        name='s2299_infotrabinterm_consigfgts_salvar'),



url(r'^s2300-documentos/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_documentos.apagar', 
        name='s2300_documentos_apagar'),

url(r'^s2300-documentos/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_documentos.listar', 
        name='s2300_documentos'),

url(r'^s2300-documentos/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_documentos.salvar', 
        name='s2300_documentos_salvar'),

)


urlpatterns += patterns('',


url(r'^s2300-ctps/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ctps.apagar', 
        name='s2300_ctps_apagar'),

url(r'^s2300-ctps/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ctps.listar', 
        name='s2300_ctps'),

url(r'^s2300-ctps/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ctps.salvar', 
        name='s2300_ctps_salvar'),



url(r'^s2300-ric/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ric.apagar', 
        name='s2300_ric_apagar'),

url(r'^s2300-ric/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ric.listar', 
        name='s2300_ric'),

url(r'^s2300-ric/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ric.salvar', 
        name='s2300_ric_salvar'),



url(r'^s2300-rg/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rg.apagar', 
        name='s2300_rg_apagar'),

url(r'^s2300-rg/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rg.listar', 
        name='s2300_rg'),

url(r'^s2300-rg/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rg.salvar', 
        name='s2300_rg_salvar'),



url(r'^s2300-rne/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rne.apagar', 
        name='s2300_rne_apagar'),

url(r'^s2300-rne/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rne.listar', 
        name='s2300_rne'),

url(r'^s2300-rne/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_rne.salvar', 
        name='s2300_rne_salvar'),



url(r'^s2300-oc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_oc.apagar', 
        name='s2300_oc_apagar'),

url(r'^s2300-oc/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_oc.listar', 
        name='s2300_oc'),

url(r'^s2300-oc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_oc.salvar', 
        name='s2300_oc_salvar'),



url(r'^s2300-cnh/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cnh.apagar', 
        name='s2300_cnh_apagar'),

url(r'^s2300-cnh/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cnh.listar', 
        name='s2300_cnh'),

url(r'^s2300-cnh/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cnh.salvar', 
        name='s2300_cnh_salvar'),



url(r'^s2300-brasil/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_brasil.apagar', 
        name='s2300_brasil_apagar'),

url(r'^s2300-brasil/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_brasil.listar', 
        name='s2300_brasil'),

url(r'^s2300-brasil/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_brasil.salvar', 
        name='s2300_brasil_salvar'),



url(r'^s2300-exterior/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_exterior.apagar', 
        name='s2300_exterior_apagar'),

url(r'^s2300-exterior/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_exterior.listar', 
        name='s2300_exterior'),

url(r'^s2300-exterior/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_exterior.salvar', 
        name='s2300_exterior_salvar'),



url(r'^s2300-trabestrangeiro/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_trabestrangeiro.apagar', 
        name='s2300_trabestrangeiro_apagar'),

url(r'^s2300-trabestrangeiro/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_trabestrangeiro.listar', 
        name='s2300_trabestrangeiro'),

url(r'^s2300-trabestrangeiro/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_trabestrangeiro.salvar', 
        name='s2300_trabestrangeiro_salvar'),



url(r'^s2300-infodeficiencia/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodeficiencia.apagar', 
        name='s2300_infodeficiencia_apagar'),

url(r'^s2300-infodeficiencia/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodeficiencia.listar', 
        name='s2300_infodeficiencia'),

url(r'^s2300-infodeficiencia/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodeficiencia.salvar', 
        name='s2300_infodeficiencia_salvar'),

)


urlpatterns += patterns('',


url(r'^s2300-dependente/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_dependente.apagar', 
        name='s2300_dependente_apagar'),

url(r'^s2300-dependente/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_dependente.listar', 
        name='s2300_dependente'),

url(r'^s2300-dependente/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_dependente.salvar', 
        name='s2300_dependente_salvar'),



url(r'^s2300-contato/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_contato.apagar', 
        name='s2300_contato_apagar'),

url(r'^s2300-contato/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_contato.listar', 
        name='s2300_contato'),

url(r'^s2300-contato/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_contato.salvar', 
        name='s2300_contato_salvar'),



url(r'^s2300-infocomplementares/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infocomplementares.apagar', 
        name='s2300_infocomplementares_apagar'),

url(r'^s2300-infocomplementares/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infocomplementares.listar', 
        name='s2300_infocomplementares'),

url(r'^s2300-infocomplementares/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infocomplementares.salvar', 
        name='s2300_infocomplementares_salvar'),



url(r'^s2300-cargofuncao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cargofuncao.apagar', 
        name='s2300_cargofuncao_apagar'),

url(r'^s2300-cargofuncao/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cargofuncao.listar', 
        name='s2300_cargofuncao'),

url(r'^s2300-cargofuncao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_cargofuncao.salvar', 
        name='s2300_cargofuncao_salvar'),



url(r'^s2300-remuneracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_remuneracao.apagar', 
        name='s2300_remuneracao_apagar'),

url(r'^s2300-remuneracao/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_remuneracao.listar', 
        name='s2300_remuneracao'),

url(r'^s2300-remuneracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_remuneracao.salvar', 
        name='s2300_remuneracao_salvar'),



url(r'^s2300-fgts/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_fgts.apagar', 
        name='s2300_fgts_apagar'),

url(r'^s2300-fgts/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_fgts.listar', 
        name='s2300_fgts'),

url(r'^s2300-fgts/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_fgts.salvar', 
        name='s2300_fgts_salvar'),



url(r'^s2300-infodirigentesindical/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodirigentesindical.apagar', 
        name='s2300_infodirigentesindical_apagar'),

url(r'^s2300-infodirigentesindical/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodirigentesindical.listar', 
        name='s2300_infodirigentesindical'),

url(r'^s2300-infodirigentesindical/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infodirigentesindical.salvar', 
        name='s2300_infodirigentesindical_salvar'),



url(r'^s2300-infotrabcedido/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infotrabcedido.apagar', 
        name='s2300_infotrabcedido_apagar'),

url(r'^s2300-infotrabcedido/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infotrabcedido.listar', 
        name='s2300_infotrabcedido'),

url(r'^s2300-infotrabcedido/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infotrabcedido.salvar', 
        name='s2300_infotrabcedido_salvar'),



url(r'^s2300-infoestagiario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infoestagiario.apagar', 
        name='s2300_infoestagiario_apagar'),

url(r'^s2300-infoestagiario/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infoestagiario.listar', 
        name='s2300_infoestagiario'),

url(r'^s2300-infoestagiario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_infoestagiario.salvar', 
        name='s2300_infoestagiario_salvar'),



url(r'^s2300-ageintegracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ageintegracao.apagar', 
        name='s2300_ageintegracao_apagar'),

url(r'^s2300-ageintegracao/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ageintegracao.listar', 
        name='s2300_ageintegracao'),

url(r'^s2300-ageintegracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_ageintegracao.salvar', 
        name='s2300_ageintegracao_salvar'),

)


urlpatterns += patterns('',


url(r'^s2300-supervisorestagio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_supervisorestagio.apagar', 
        name='s2300_supervisorestagio_apagar'),

url(r'^s2300-supervisorestagio/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_supervisorestagio.listar', 
        name='s2300_supervisorestagio'),

url(r'^s2300-supervisorestagio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_supervisorestagio.salvar', 
        name='s2300_supervisorestagio_salvar'),



url(r'^s2300-afastamento/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_afastamento.apagar', 
        name='s2300_afastamento_apagar'),

url(r'^s2300-afastamento/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_afastamento.listar', 
        name='s2300_afastamento'),

url(r'^s2300-afastamento/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_afastamento.salvar', 
        name='s2300_afastamento_salvar'),



url(r'^s2300-termino/apagar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_termino.apagar', 
        name='s2300_termino_apagar'),

url(r'^s2300-termino/listar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_termino.listar', 
        name='s2300_termino'),

url(r'^s2300-termino/salvar/(?P<hash>.*)/$', 
        'emensageria.s2300.views.s2300_termino.salvar', 
        name='s2300_termino_salvar'),



url(r'^s2306-infocomplementares/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infocomplementares.apagar', 
        name='s2306_infocomplementares_apagar'),

url(r'^s2306-infocomplementares/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infocomplementares.listar', 
        name='s2306_infocomplementares'),

url(r'^s2306-infocomplementares/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infocomplementares.salvar', 
        name='s2306_infocomplementares_salvar'),



url(r'^s2306-cargofuncao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_cargofuncao.apagar', 
        name='s2306_cargofuncao_apagar'),

url(r'^s2306-cargofuncao/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_cargofuncao.listar', 
        name='s2306_cargofuncao'),

url(r'^s2306-cargofuncao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_cargofuncao.salvar', 
        name='s2306_cargofuncao_salvar'),



url(r'^s2306-remuneracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_remuneracao.apagar', 
        name='s2306_remuneracao_apagar'),

url(r'^s2306-remuneracao/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_remuneracao.listar', 
        name='s2306_remuneracao'),

url(r'^s2306-remuneracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_remuneracao.salvar', 
        name='s2306_remuneracao_salvar'),



url(r'^s2306-infoestagiario/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infoestagiario.apagar', 
        name='s2306_infoestagiario_apagar'),

url(r'^s2306-infoestagiario/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infoestagiario.listar', 
        name='s2306_infoestagiario'),

url(r'^s2306-infoestagiario/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_infoestagiario.salvar', 
        name='s2306_infoestagiario_salvar'),



url(r'^s2306-ageintegracao/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_ageintegracao.apagar', 
        name='s2306_ageintegracao_apagar'),

url(r'^s2306-ageintegracao/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_ageintegracao.listar', 
        name='s2306_ageintegracao'),

url(r'^s2306-ageintegracao/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_ageintegracao.salvar', 
        name='s2306_ageintegracao_salvar'),



url(r'^s2306-supervisorestagio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_supervisorestagio.apagar', 
        name='s2306_supervisorestagio_apagar'),

url(r'^s2306-supervisorestagio/listar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_supervisorestagio.listar', 
        name='s2306_supervisorestagio'),

url(r'^s2306-supervisorestagio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2306.views.s2306_supervisorestagio.salvar', 
        name='s2306_supervisorestagio_salvar'),



url(r'^s2399-verbasresc/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_verbasresc.apagar', 
        name='s2399_verbasresc_apagar'),

url(r'^s2399-verbasresc/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_verbasresc.listar', 
        name='s2399_verbasresc'),

url(r'^s2399-verbasresc/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_verbasresc.salvar', 
        name='s2399_verbasresc_salvar'),

)


urlpatterns += patterns('',


url(r'^s2399-dmdev/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_dmdev.apagar', 
        name='s2399_dmdev_apagar'),

url(r'^s2399-dmdev/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_dmdev.listar', 
        name='s2399_dmdev'),

url(r'^s2399-dmdev/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_dmdev.salvar', 
        name='s2399_dmdev_salvar'),



url(r'^s2399-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_ideestablot.apagar', 
        name='s2399_ideestablot_apagar'),

url(r'^s2399-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_ideestablot.listar', 
        name='s2399_ideestablot'),

url(r'^s2399-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_ideestablot.salvar', 
        name='s2399_ideestablot_salvar'),



url(r'^s2399-detverbas/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detverbas.apagar', 
        name='s2399_detverbas_apagar'),

url(r'^s2399-detverbas/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detverbas.listar', 
        name='s2399_detverbas'),

url(r'^s2399-detverbas/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detverbas.salvar', 
        name='s2399_detverbas_salvar'),



url(r'^s2399-infosaudecolet/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosaudecolet.apagar', 
        name='s2399_infosaudecolet_apagar'),

url(r'^s2399-infosaudecolet/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosaudecolet.listar', 
        name='s2399_infosaudecolet'),

url(r'^s2399-infosaudecolet/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosaudecolet.salvar', 
        name='s2399_infosaudecolet_salvar'),



url(r'^s2399-detoper/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detoper.apagar', 
        name='s2399_detoper_apagar'),

url(r'^s2399-detoper/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detoper.listar', 
        name='s2399_detoper'),

url(r'^s2399-detoper/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detoper.salvar', 
        name='s2399_detoper_salvar'),



url(r'^s2399-detplano/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detplano.apagar', 
        name='s2399_detplano_apagar'),

url(r'^s2399-detplano/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detplano.listar', 
        name='s2399_detplano'),

url(r'^s2399-detplano/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_detplano.salvar', 
        name='s2399_detplano_salvar'),



url(r'^s2399-infoagnocivo/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infoagnocivo.apagar', 
        name='s2399_infoagnocivo_apagar'),

url(r'^s2399-infoagnocivo/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infoagnocivo.listar', 
        name='s2399_infoagnocivo'),

url(r'^s2399-infoagnocivo/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infoagnocivo.salvar', 
        name='s2399_infoagnocivo_salvar'),



url(r'^s2399-infosimples/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosimples.apagar', 
        name='s2399_infosimples_apagar'),

url(r'^s2399-infosimples/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosimples.listar', 
        name='s2399_infosimples'),

url(r'^s2399-infosimples/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infosimples.salvar', 
        name='s2399_infosimples_salvar'),



url(r'^s2399-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_procjudtrab.apagar', 
        name='s2399_procjudtrab_apagar'),

url(r'^s2399-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_procjudtrab.listar', 
        name='s2399_procjudtrab'),

url(r'^s2399-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_procjudtrab.salvar', 
        name='s2399_procjudtrab_salvar'),



url(r'^s2399-infomv/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infomv.apagar', 
        name='s2399_infomv_apagar'),

url(r'^s2399-infomv/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infomv.listar', 
        name='s2399_infomv'),

url(r'^s2399-infomv/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_infomv.salvar', 
        name='s2399_infomv_salvar'),

)


urlpatterns += patterns('',


url(r'^s2399-remunoutrempr/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_remunoutrempr.apagar', 
        name='s2399_remunoutrempr_apagar'),

url(r'^s2399-remunoutrempr/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_remunoutrempr.listar', 
        name='s2399_remunoutrempr'),

url(r'^s2399-remunoutrempr/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_remunoutrempr.salvar', 
        name='s2399_remunoutrempr_salvar'),



url(r'^s2399-quarentena/apagar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_quarentena.apagar', 
        name='s2399_quarentena_apagar'),

url(r'^s2399-quarentena/listar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_quarentena.listar', 
        name='s2399_quarentena'),

url(r'^s2399-quarentena/salvar/(?P<hash>.*)/$', 
        'emensageria.s2399.views.s2399_quarentena.salvar', 
        name='s2399_quarentena_salvar'),



url(r'^s2400-brasil/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_brasil.apagar', 
        name='s2400_brasil_apagar'),

url(r'^s2400-brasil/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_brasil.listar', 
        name='s2400_brasil'),

url(r'^s2400-brasil/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_brasil.salvar', 
        name='s2400_brasil_salvar'),



url(r'^s2400-exterior/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_exterior.apagar', 
        name='s2400_exterior_apagar'),

url(r'^s2400-exterior/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_exterior.listar', 
        name='s2400_exterior'),

url(r'^s2400-exterior/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_exterior.salvar', 
        name='s2400_exterior_salvar'),



url(r'^s2400-inibeneficio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio.apagar', 
        name='s2400_inibeneficio_apagar'),

url(r'^s2400-inibeneficio/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio.listar', 
        name='s2400_inibeneficio'),

url(r'^s2400-inibeneficio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio.salvar', 
        name='s2400_inibeneficio_salvar'),



url(r'^s2400-inibeneficio-infopenmorte/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio_infopenmorte.apagar', 
        name='s2400_inibeneficio_infopenmorte_apagar'),

url(r'^s2400-inibeneficio-infopenmorte/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio_infopenmorte.listar', 
        name='s2400_inibeneficio_infopenmorte'),

url(r'^s2400-inibeneficio-infopenmorte/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_inibeneficio_infopenmorte.salvar', 
        name='s2400_inibeneficio_infopenmorte_salvar'),



url(r'^s2400-altbeneficio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio.apagar', 
        name='s2400_altbeneficio_apagar'),

url(r'^s2400-altbeneficio/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio.listar', 
        name='s2400_altbeneficio'),

url(r'^s2400-altbeneficio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio.salvar', 
        name='s2400_altbeneficio_salvar'),



url(r'^s2400-altbeneficio-infopenmorte/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio_infopenmorte.apagar', 
        name='s2400_altbeneficio_infopenmorte_apagar'),

url(r'^s2400-altbeneficio-infopenmorte/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio_infopenmorte.listar', 
        name='s2400_altbeneficio_infopenmorte'),

url(r'^s2400-altbeneficio-infopenmorte/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_altbeneficio_infopenmorte.salvar', 
        name='s2400_altbeneficio_infopenmorte_salvar'),



url(r'^s2400-fimbeneficio/apagar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_fimbeneficio.apagar', 
        name='s2400_fimbeneficio_apagar'),

url(r'^s2400-fimbeneficio/listar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_fimbeneficio.listar', 
        name='s2400_fimbeneficio'),

url(r'^s2400-fimbeneficio/salvar/(?P<hash>.*)/$', 
        'emensageria.s2400.views.s2400_fimbeneficio.salvar', 
        name='s2400_fimbeneficio_salvar'),



url(r'^s3000-idetrabalhador/apagar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idetrabalhador.apagar', 
        name='s3000_idetrabalhador_apagar'),

url(r'^s3000-idetrabalhador/listar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idetrabalhador.listar', 
        name='s3000_idetrabalhador'),

url(r'^s3000-idetrabalhador/salvar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idetrabalhador.salvar', 
        name='s3000_idetrabalhador_salvar'),

)


urlpatterns += patterns('',


url(r'^s3000-idefolhapagto/apagar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idefolhapagto.apagar', 
        name='s3000_idefolhapagto_apagar'),

url(r'^s3000-idefolhapagto/listar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idefolhapagto.listar', 
        name='s3000_idefolhapagto'),

url(r'^s3000-idefolhapagto/salvar/(?P<hash>.*)/$', 
        'emensageria.s3000.views.s3000_idefolhapagto.salvar', 
        name='s3000_idefolhapagto_salvar'),



url(r'^s5001-procjudtrab/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_procjudtrab.apagar', 
        name='s5001_procjudtrab_apagar'),

url(r'^s5001-procjudtrab/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_procjudtrab.listar', 
        name='s5001_procjudtrab'),

url(r'^s5001-procjudtrab/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_procjudtrab.salvar', 
        name='s5001_procjudtrab_salvar'),



url(r'^s5001-infocpcalc/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocpcalc.apagar', 
        name='s5001_infocpcalc_apagar'),

url(r'^s5001-infocpcalc/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocpcalc.listar', 
        name='s5001_infocpcalc'),

url(r'^s5001-infocpcalc/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocpcalc.salvar', 
        name='s5001_infocpcalc_salvar'),



url(r'^s5001-ideestablot/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_ideestablot.apagar', 
        name='s5001_ideestablot_apagar'),

url(r'^s5001-ideestablot/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_ideestablot.listar', 
        name='s5001_ideestablot'),

url(r'^s5001-ideestablot/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_ideestablot.salvar', 
        name='s5001_ideestablot_salvar'),



url(r'^s5001-infocategincid/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocategincid.apagar', 
        name='s5001_infocategincid_apagar'),

url(r'^s5001-infocategincid/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocategincid.listar', 
        name='s5001_infocategincid'),

url(r'^s5001-infocategincid/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infocategincid.salvar', 
        name='s5001_infocategincid_salvar'),



url(r'^s5001-infobasecs/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infobasecs.apagar', 
        name='s5001_infobasecs_apagar'),

url(r'^s5001-infobasecs/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infobasecs.listar', 
        name='s5001_infobasecs'),

url(r'^s5001-infobasecs/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_infobasecs.salvar', 
        name='s5001_infobasecs_salvar'),



url(r'^s5001-calcterc/apagar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_calcterc.apagar', 
        name='s5001_calcterc_apagar'),

url(r'^s5001-calcterc/listar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_calcterc.listar', 
        name='s5001_calcterc'),

url(r'^s5001-calcterc/salvar/(?P<hash>.*)/$', 
        'emensageria.s5001.views.s5001_calcterc.salvar', 
        name='s5001_calcterc_salvar'),



url(r'^s5002-infodep/apagar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infodep.apagar', 
        name='s5002_infodep_apagar'),

url(r'^s5002-infodep/listar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infodep.listar', 
        name='s5002_infodep'),

url(r'^s5002-infodep/salvar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infodep.salvar', 
        name='s5002_infodep_salvar'),



url(r'^s5002-infoirrf/apagar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infoirrf.apagar', 
        name='s5002_infoirrf_apagar'),

url(r'^s5002-infoirrf/listar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infoirrf.listar', 
        name='s5002_infoirrf'),

url(r'^s5002-infoirrf/salvar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_infoirrf.salvar', 
        name='s5002_infoirrf_salvar'),



url(r'^s5002-basesirrf/apagar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_basesirrf.apagar', 
        name='s5002_basesirrf_apagar'),

url(r'^s5002-basesirrf/listar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_basesirrf.listar', 
        name='s5002_basesirrf'),

url(r'^s5002-basesirrf/salvar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_basesirrf.salvar', 
        name='s5002_basesirrf_salvar'),

)


urlpatterns += patterns('',


url(r'^s5002-irrf/apagar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_irrf.apagar', 
        name='s5002_irrf_apagar'),

url(r'^s5002-irrf/listar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_irrf.listar', 
        name='s5002_irrf'),

url(r'^s5002-irrf/salvar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_irrf.salvar', 
        name='s5002_irrf_salvar'),



url(r'^s5002-idepgtoext/apagar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_idepgtoext.apagar', 
        name='s5002_idepgtoext_apagar'),

url(r'^s5002-idepgtoext/listar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_idepgtoext.listar', 
        name='s5002_idepgtoext'),

url(r'^s5002-idepgtoext/salvar/(?P<hash>.*)/$', 
        'emensageria.s5002.views.s5002_idepgtoext.salvar', 
        name='s5002_idepgtoext_salvar'),



url(r'^s5011-infocpseg/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocpseg.apagar', 
        name='s5011_infocpseg_apagar'),

url(r'^s5011-infocpseg/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocpseg.listar', 
        name='s5011_infocpseg'),

url(r'^s5011-infocpseg/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocpseg.salvar', 
        name='s5011_infocpseg_salvar'),



url(r'^s5011-infopj/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infopj.apagar', 
        name='s5011_infopj_apagar'),

url(r'^s5011-infopj/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infopj.listar', 
        name='s5011_infopj'),

url(r'^s5011-infopj/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infopj.salvar', 
        name='s5011_infopj_salvar'),



url(r'^s5011-infoatconc/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoatconc.apagar', 
        name='s5011_infoatconc_apagar'),

url(r'^s5011-infoatconc/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoatconc.listar', 
        name='s5011_infoatconc'),

url(r'^s5011-infoatconc/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoatconc.salvar', 
        name='s5011_infoatconc_salvar'),



url(r'^s5011-ideestab/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_ideestab.apagar', 
        name='s5011_ideestab_apagar'),

url(r'^s5011-ideestab/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_ideestab.listar', 
        name='s5011_ideestab'),

url(r'^s5011-ideestab/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_ideestab.salvar', 
        name='s5011_ideestab_salvar'),



url(r'^s5011-infoestab/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoestab.apagar', 
        name='s5011_infoestab_apagar'),

url(r'^s5011-infoestab/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoestab.listar', 
        name='s5011_infoestab'),

url(r'^s5011-infoestab/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoestab.salvar', 
        name='s5011_infoestab_salvar'),



url(r'^s5011-infocomplobra/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocomplobra.apagar', 
        name='s5011_infocomplobra_apagar'),

url(r'^s5011-infocomplobra/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocomplobra.listar', 
        name='s5011_infocomplobra'),

url(r'^s5011-infocomplobra/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocomplobra.salvar', 
        name='s5011_infocomplobra_salvar'),



url(r'^s5011-idelotacao/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_idelotacao.apagar', 
        name='s5011_idelotacao_apagar'),

url(r'^s5011-idelotacao/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_idelotacao.listar', 
        name='s5011_idelotacao'),

url(r'^s5011-idelotacao/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_idelotacao.salvar', 
        name='s5011_idelotacao_salvar'),



url(r'^s5011-infotercsusp/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infotercsusp.apagar', 
        name='s5011_infotercsusp_apagar'),

url(r'^s5011-infotercsusp/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infotercsusp.listar', 
        name='s5011_infotercsusp'),

url(r'^s5011-infotercsusp/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infotercsusp.salvar', 
        name='s5011_infotercsusp_salvar'),

)


urlpatterns += patterns('',


url(r'^s5011-infoemprparcial/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoemprparcial.apagar', 
        name='s5011_infoemprparcial_apagar'),

url(r'^s5011-infoemprparcial/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoemprparcial.listar', 
        name='s5011_infoemprparcial'),

url(r'^s5011-infoemprparcial/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infoemprparcial.salvar', 
        name='s5011_infoemprparcial_salvar'),



url(r'^s5011-dadosopport/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_dadosopport.apagar', 
        name='s5011_dadosopport_apagar'),

url(r'^s5011-dadosopport/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_dadosopport.listar', 
        name='s5011_dadosopport'),

url(r'^s5011-dadosopport/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_dadosopport.salvar', 
        name='s5011_dadosopport_salvar'),



url(r'^s5011-basesremun/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesremun.apagar', 
        name='s5011_basesremun_apagar'),

url(r'^s5011-basesremun/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesremun.listar', 
        name='s5011_basesremun'),

url(r'^s5011-basesremun/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesremun.salvar', 
        name='s5011_basesremun_salvar'),



url(r'^s5011-basesavnport/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesavnport.apagar', 
        name='s5011_basesavnport_apagar'),

url(r'^s5011-basesavnport/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesavnport.listar', 
        name='s5011_basesavnport'),

url(r'^s5011-basesavnport/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesavnport.salvar', 
        name='s5011_basesavnport_salvar'),



url(r'^s5011-infosubstpatropport/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infosubstpatropport.apagar', 
        name='s5011_infosubstpatropport_apagar'),

url(r'^s5011-infosubstpatropport/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infosubstpatropport.listar', 
        name='s5011_infosubstpatropport'),

url(r'^s5011-infosubstpatropport/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infosubstpatropport.salvar', 
        name='s5011_infosubstpatropport_salvar'),



url(r'^s5011-basesaquis/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesaquis.apagar', 
        name='s5011_basesaquis_apagar'),

url(r'^s5011-basesaquis/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesaquis.listar', 
        name='s5011_basesaquis'),

url(r'^s5011-basesaquis/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basesaquis.salvar', 
        name='s5011_basesaquis_salvar'),



url(r'^s5011-basescomerc/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basescomerc.apagar', 
        name='s5011_basescomerc_apagar'),

url(r'^s5011-basescomerc/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basescomerc.listar', 
        name='s5011_basescomerc'),

url(r'^s5011-basescomerc/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_basescomerc.salvar', 
        name='s5011_basescomerc_salvar'),



url(r'^s5011-infocrestab/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrestab.apagar', 
        name='s5011_infocrestab_apagar'),

url(r'^s5011-infocrestab/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrestab.listar', 
        name='s5011_infocrestab'),

url(r'^s5011-infocrestab/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrestab.salvar', 
        name='s5011_infocrestab_salvar'),



url(r'^s5011-infocrcontrib/apagar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrcontrib.apagar', 
        name='s5011_infocrcontrib_apagar'),

url(r'^s5011-infocrcontrib/listar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrcontrib.listar', 
        name='s5011_infocrcontrib'),

url(r'^s5011-infocrcontrib/salvar/(?P<hash>.*)/$', 
        'emensageria.s5011.views.s5011_infocrcontrib.salvar', 
        name='s5011_infocrcontrib_salvar'),



url(r'^s5012-infocrcontrib/apagar/(?P<hash>.*)/$', 
        'emensageria.s5012.views.s5012_infocrcontrib.apagar', 
        name='s5012_infocrcontrib_apagar'),

url(r'^s5012-infocrcontrib/listar/(?P<hash>.*)/$', 
        'emensageria.s5012.views.s5012_infocrcontrib.listar', 
        name='s5012_infocrcontrib'),

url(r'^s5012-infocrcontrib/salvar/(?P<hash>.*)/$', 
        'emensageria.s5012.views.s5012_infocrcontrib.salvar', 
        name='s5012_infocrcontrib_salvar'),

)


urlpatterns += patterns('',




) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
