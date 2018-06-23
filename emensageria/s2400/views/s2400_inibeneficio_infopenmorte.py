#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

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

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageria.padrao import *
from emensageria.s2400.forms import *
from emensageria.s2400.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2400_inibeneficio_infopenmorte_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_inibeneficio_infopenmorte')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2400_inibeneficio_infopenmorte = get_object_or_404(s2400iniBeneficioinfoPenMorte.objects.using( db_slug ), excluido = False, id = s2400_inibeneficio_infopenmorte_id)
    if request.method == 'POST':
        s2400iniBeneficioinfoPenMorte.objects.using( db_slug ).filter(id = s2400_inibeneficio_infopenmorte_id).delete()
        #s2400_inibeneficio_infopenmorte_apagar_custom
        #s2400_inibeneficio_infopenmorte_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's2400_inibeneficio_infopenmorte_salvar':
            return redirect('s2400_inibeneficio_infopenmorte', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
        
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
        
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 's2400_inibeneficio_infopenmorte_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2400_inibeneficio_infopenmorte_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_inibeneficio_infopenmorte')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2400_inibeneficio_infopenmorte_id:
        s2400_inibeneficio_infopenmorte = get_object_or_404(s2400iniBeneficioinfoPenMorte.objects.using( db_slug ), excluido = False, id = s2400_inibeneficio_infopenmorte_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s2400_inibeneficio_infopenmorte_id:
            s2400_inibeneficio_infopenmorte_form = form_s2400_inibeneficio_infopenmorte(request.POST or None, instance = s2400_inibeneficio_infopenmorte, slug = db_slug)
        else:
            s2400_inibeneficio_infopenmorte_form = form_s2400_inibeneficio_infopenmorte(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s2400_inibeneficio_infopenmorte_form.is_valid():
                dados = s2400_inibeneficio_infopenmorte_form.cleaned_data
                if s2400_inibeneficio_infopenmorte_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s2400_inibeneficio_infopenmorte_campos_multiple_passo1
                    s2400iniBeneficioinfoPenMorte.objects.using(db_slug).filter(id=s2400_inibeneficio_infopenmorte_id).update(**dados)
                    obj = s2400iniBeneficioinfoPenMorte.objects.using(db_slug).get(id=s2400_inibeneficio_infopenmorte_id)
                    #s2400_inibeneficio_infopenmorte_editar_custom
                    #s2400_inibeneficio_infopenmorte_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2400_inibeneficio_infopenmorte_cadastrar_campos_multiple_passo1
                    obj = s2400iniBeneficioinfoPenMorte(**dados)
                    obj.save(using = db_slug)
                    #s2400_inibeneficio_infopenmorte_cadastrar_custom
                    #s2400_inibeneficio_infopenmorte_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s2400_inibeneficio_infopenmorte_apagar', 's2400_inibeneficio_infopenmorte_salvar', 's2400_inibeneficio_infopenmorte'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2400_inibeneficio_infopenmorte_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2400_inibeneficio_infopenmorte_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2400_inibeneficio_infopenmorte_form = disabled_form_fields(s2400_inibeneficio_infopenmorte_form, permissao.permite_editar)
        #s2400_inibeneficio_infopenmorte_campos_multiple_passo3

        for field in s2400_inibeneficio_infopenmorte_form.fields.keys():
            s2400_inibeneficio_infopenmorte_form.fields[field].widget.attrs['ng-model'] = 's2400_inibeneficio_infopenmorte_'+field
        if int(dict_hash['print']):
            s2400_inibeneficio_infopenmorte_form = disabled_form_for_print(s2400_inibeneficio_infopenmorte_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if s2400_inibeneficio_infopenmorte_id:
            s2400_inibeneficio_infopenmorte = get_object_or_404(s2400iniBeneficioinfoPenMorte.objects.using( db_slug ), excluido = False, id = s2400_inibeneficio_infopenmorte_id)
            pass
        else:
            s2400_inibeneficio_infopenmorte = None
        #s2400_inibeneficio_infopenmorte_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2400_inibeneficio_infopenmorte' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2400_inibeneficio_infopenmorte_salvar'
        context = {
            's2400_inibeneficio_infopenmorte': s2400_inibeneficio_infopenmorte,
            's2400_inibeneficio_infopenmorte_form': s2400_inibeneficio_infopenmorte_form,
            'mensagem': mensagem,
            's2400_inibeneficio_infopenmorte_id': int(s2400_inibeneficio_infopenmorte_id),
            'usuario': usuario,
            
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2400_inibeneficio_infopenmorte_salvar_custom_variaveis_context#
        }
        return render(request, 's2400_inibeneficio_infopenmorte_salvar.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2400_inibeneficio_infopenmorte_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_inibeneficio_infopenmorte')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_cpfinst': 1,
            'show_idquota': 1,
            'show_s2400_inibeneficio': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'cpfinst__icontains': 'cpfinst__icontains',
                'idquota__icontains': 'idquota__icontains',
                's2400_inibeneficio': 's2400_inibeneficio',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'cpfinst__icontains': 'cpfinst__icontains',
                'idquota__icontains': 'idquota__icontains',
                's2400_inibeneficio': 's2400_inibeneficio',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2400_inibeneficio_infopenmorte_lista = s2400iniBeneficioinfoPenMorte.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2400_inibeneficio_infopenmorte_lista) > 100:
            filtrar = True
            s2400_inibeneficio_infopenmorte_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #s2400_inibeneficio_infopenmorte_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2400_inibeneficio_infopenmorte'
        context = {
            's2400_inibeneficio_infopenmorte_lista': s2400_inibeneficio_infopenmorte_lista,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
        
        }
        return render(request, 's2400_inibeneficio_infopenmorte_listar.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

