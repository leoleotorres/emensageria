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
from emensageria.s1080.forms import *
from emensageria.s1080.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1080_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1080_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1080_alteracao = get_object_or_404(s1080alteracao.objects.using( db_slug ), excluido = False, id = s1080_alteracao_id)
    if request.method == 'POST':
        s1080alteracao.objects.using( db_slug ).filter(id = s1080_alteracao_id).delete()
        #s1080_alteracao_apagar_custom
        #s1080_alteracao_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's1080_alteracao_salvar':
            return redirect('s1080_alteracao', hash=request.session['retorno_hash'])
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
    return render(request, 's1080_alteracao_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1080_alteracao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1080_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1080_alteracao_id:
        s1080_alteracao = get_object_or_404(s1080alteracao.objects.using( db_slug ), excluido = False, id = s1080_alteracao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s1080_alteracao_id:
            s1080_alteracao_form = form_s1080_alteracao(request.POST or None, instance = s1080_alteracao, slug = db_slug)
        else:
            s1080_alteracao_form = form_s1080_alteracao(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s1080_alteracao_form.is_valid():
                dados = s1080_alteracao_form.cleaned_data
                if s1080_alteracao_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s1080_alteracao_campos_multiple_passo1
                    s1080alteracao.objects.using(db_slug).filter(id=s1080_alteracao_id).update(**dados)
                    obj = s1080alteracao.objects.using(db_slug).get(id=s1080_alteracao_id)
                    #s1080_alteracao_editar_custom
                    #s1080_alteracao_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1080_alteracao_cadastrar_campos_multiple_passo1
                    obj = s1080alteracao(**dados)
                    obj.save(using = db_slug)
                    #s1080_alteracao_cadastrar_custom
                    #s1080_alteracao_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s1080_alteracao_apagar', 's1080_alteracao_salvar', 's1080_alteracao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s1080_alteracao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1080_alteracao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s1080_alteracao_form = disabled_form_fields(s1080_alteracao_form, permissao.permite_editar)
        #s1080_alteracao_campos_multiple_passo3

        for field in s1080_alteracao_form.fields.keys():
            s1080_alteracao_form.fields[field].widget.attrs['ng-model'] = 's1080_alteracao_'+field
        if int(dict_hash['print']):
            s1080_alteracao_form = disabled_form_for_print(s1080_alteracao_form)
   
        s1080_alteracao_novavalidade_form = None
        s1080_alteracao_novavalidade_lista = None
        if s1080_alteracao_id:
            s1080_alteracao = get_object_or_404(s1080alteracao.objects.using( db_slug ), excluido = False, id = s1080_alteracao_id)
       
            s1080_alteracao_novavalidade_form = form_s1080_alteracao_novavalidade(initial={ 's1080_alteracao': s1080_alteracao }, slug=db_slug)
            s1080_alteracao_novavalidade_form.fields['s1080_alteracao'].widget.attrs['readonly'] = True
            s1080_alteracao_novavalidade_lista = s1080alteracaonovaValidade.objects.using( db_slug ).filter(excluido = False, s1080_alteracao_id=s1080_alteracao.id).all()
        else:
            s1080_alteracao = None
        #s1080_alteracao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1080_alteracao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1080_alteracao_salvar'
        context = {
            's1080_alteracao': s1080_alteracao,
            's1080_alteracao_form': s1080_alteracao_form,
            'mensagem': mensagem,
            's1080_alteracao_id': int(s1080_alteracao_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's1080_alteracao_novavalidade_form': s1080_alteracao_novavalidade_form,
            's1080_alteracao_novavalidade_lista': s1080_alteracao_novavalidade_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1080_alteracao_salvar_custom_variaveis_context#
        }
        return render(request, 's1080_alteracao_salvar.html', context)
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
        #s1080_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1080_alteracao')
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
            'show_aliqratajust': 1,
            'show_fap': 1,
            'show_aliqrat': 1,
            'show_dadosoperportuario': 0,
            'show_fimvalid': 0,
            'show_inivalid': 1,
            'show_cnpjopportuario': 1,
            'show_ideoperportuario': 0,
            'show_s1080_evttaboperport': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'aliqratajust': 'aliqratajust',
                'fap': 'fap',
                'aliqrat': 'aliqrat',
                'dadosoperportuario': 'dadosoperportuario',
                'fimvalid__icontains': 'fimvalid__icontains',
                'inivalid__icontains': 'inivalid__icontains',
                'cnpjopportuario__icontains': 'cnpjopportuario__icontains',
                'ideoperportuario': 'ideoperportuario',
                's1080_evttaboperport': 's1080_evttaboperport',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'aliqratajust': 'aliqratajust',
                'fap': 'fap',
                'aliqrat': 'aliqrat',
                'dadosoperportuario': 'dadosoperportuario',
                'fimvalid__icontains': 'fimvalid__icontains',
                'inivalid__icontains': 'inivalid__icontains',
                'cnpjopportuario__icontains': 'cnpjopportuario__icontains',
                'ideoperportuario': 'ideoperportuario',
                's1080_evttaboperport': 's1080_evttaboperport',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1080_alteracao_lista = s1080alteracao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1080_alteracao_lista) > 100:
            filtrar = True
            s1080_alteracao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #s1080_alteracao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1080_alteracao'
        context = {
            's1080_alteracao_lista': s1080_alteracao_lista,
            
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
        return render(request, 's1080_alteracao_listar.html', context)
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

