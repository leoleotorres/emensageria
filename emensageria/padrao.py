#coding: utf-8
import datetime

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

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

def range_ano_mes():
    from datetime import datetime
    anos = range(2010,datetime.now().year+1)
    meses = ['01','02','03','04','05','06','07','08','09','10','11','12',]
    meses_ext = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez',]
    lista = []
    for a in anos: 
        for (m, me) in zip(meses, meses_ext): 
            lista.append( (str(a)+'-'+m, me+'/'+str(a)) )
    print lista

def listar_ids(objeto):
    lista = []
    for a in objeto:
        lista.append(a.id)
    return lista



def get_permissoes(permissoes):
    dict = {}
    for a in permissoes:
        chave = a.config_paginas.endereco
        dict[chave+'_listar'] = a.permite_listar
        dict[chave+'_cadastrar'] = a.permite_cadastrar
        dict[chave+'_editar'] = a.permite_editar
        dict[chave+'_visualizar'] = a.permite_visualizar
        dict[chave+'_apagar'] = a.permite_apagar    
    return dict

def json_to_dict(texto):
    import json
    dicionario = json.loads(texto)
    return dicionario

def dict_to_json(dicionario):
    import json
    json_string = json.dumps(dicionario)
    return json_string

def correcao_data_range(data):
    a = data.split('/')
    return a[2]+'-'+a[1]+'-'+a[0]

def texto_to_int_list(texto):
    dados = []
    lista = texto.split(',')
    for a in lista:
        dados.append(int(a))
    return dados

def get_hash_url(hash):
    import base64
    texto = base64.b64decode( hash )
    return json_to_dict(texto)

def disabled_form_fields(form, permite_editar):
    if not permite_editar:
        for a in form.fields:
            form.fields[a].widget.attrs['readonly'] = True
            form.fields[a].widget.attrs['disabled'] = True
    return form


def disabled_form_for_print(form):
    for a in form.fields:
        form.fields[a].widget.attrs['readonly'] = True
        form.fields[a].widget.attrs['disabled'] = True
    return form

def clear_dict_fields(dict):
    dict_new = {}
    for a in dict:
        if dict[a]:
            dict_new[a] = dict[a]
    for a in dict_new:
        if 'data' in a:
            b = dict_new[a]
            c = b.split(' - ')
            n1 = correcao_data_range(c[0])
            n2 = correcao_data_range(c[1])
            dict_new[a] = [n1, n2]
    return dict_new

def salvar_arquivo(arquivo, texto):
    file = open(arquivo, "w")
    file.write( texto )
    file.close()
    print arquivo

def ler_arquivo(arquivo):
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto

