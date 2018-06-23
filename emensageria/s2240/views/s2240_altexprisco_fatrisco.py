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
from emensageria.s2240.forms import *
from emensageria.s2240.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2240_altexprisco_fatrisco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2240_altexprisco_fatrisco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2240_altexprisco_fatrisco = get_object_or_404(s2240altExpRiscofatRisco.objects.using( db_slug ), excluido = False, id = s2240_altexprisco_fatrisco_id)
    if request.method == 'POST':
        s2240altExpRiscofatRisco.objects.using( db_slug ).filter(id = s2240_altexprisco_fatrisco_id).delete()
        #s2240_altexprisco_fatrisco_apagar_custom
        #s2240_altexprisco_fatrisco_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's2240_altexprisco_fatrisco_salvar':
            return redirect('s2240_altexprisco_fatrisco', hash=request.session['retorno_hash'])
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
    return render(request, 's2240_altexprisco_fatrisco_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2240_altexprisco_fatrisco_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2240_altexprisco_fatrisco')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2240_altexprisco_fatrisco_id:
        s2240_altexprisco_fatrisco = get_object_or_404(s2240altExpRiscofatRisco.objects.using( db_slug ), excluido = False, id = s2240_altexprisco_fatrisco_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s2240_altexprisco_fatrisco_id:
            s2240_altexprisco_fatrisco_form = form_s2240_altexprisco_fatrisco(request.POST or None, instance = s2240_altexprisco_fatrisco, slug = db_slug)
        else:
            s2240_altexprisco_fatrisco_form = form_s2240_altexprisco_fatrisco(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s2240_altexprisco_fatrisco_form.is_valid():
                dados = s2240_altexprisco_fatrisco_form.cleaned_data
                if s2240_altexprisco_fatrisco_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s2240_altexprisco_fatrisco_campos_multiple_passo1
                    s2240altExpRiscofatRisco.objects.using(db_slug).filter(id=s2240_altexprisco_fatrisco_id).update(**dados)
                    obj = s2240altExpRiscofatRisco.objects.using(db_slug).get(id=s2240_altexprisco_fatrisco_id)
                    #s2240_altexprisco_fatrisco_editar_custom
                    #s2240_altexprisco_fatrisco_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2240_altexprisco_fatrisco_cadastrar_campos_multiple_passo1
                    obj = s2240altExpRiscofatRisco(**dados)
                    obj.save(using = db_slug)
                    #s2240_altexprisco_fatrisco_cadastrar_custom
                    #s2240_altexprisco_fatrisco_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s2240_altexprisco_fatrisco_apagar', 's2240_altexprisco_fatrisco_salvar', 's2240_altexprisco_fatrisco'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2240_altexprisco_fatrisco_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2240_altexprisco_fatrisco_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2240_altexprisco_fatrisco_form = disabled_form_fields(s2240_altexprisco_fatrisco_form, permissao.permite_editar)
        #s2240_altexprisco_fatrisco_campos_multiple_passo3

        for field in s2240_altexprisco_fatrisco_form.fields.keys():
            s2240_altexprisco_fatrisco_form.fields[field].widget.attrs['ng-model'] = 's2240_altexprisco_fatrisco_'+field
        if int(dict_hash['print']):
            s2240_altexprisco_fatrisco_form = disabled_form_for_print(s2240_altexprisco_fatrisco_form)
   
        s2240_altexprisco_epc_form = None
        s2240_altexprisco_epc_lista = None
        s2240_altexprisco_epi_form = None
        s2240_altexprisco_epi_lista = None
        if s2240_altexprisco_fatrisco_id:
            s2240_altexprisco_fatrisco = get_object_or_404(s2240altExpRiscofatRisco.objects.using( db_slug ), excluido = False, id = s2240_altexprisco_fatrisco_id)
       
            s2240_altexprisco_epc_form = form_s2240_altexprisco_epc(initial={ 's2240_altexprisco_fatrisco': s2240_altexprisco_fatrisco }, slug=db_slug)
            s2240_altexprisco_epc_form.fields['s2240_altexprisco_fatrisco'].widget.attrs['readonly'] = True
            s2240_altexprisco_epc_lista = s2240altExpRiscoepc.objects.using( db_slug ).filter(excluido = False, s2240_altexprisco_fatrisco_id=s2240_altexprisco_fatrisco.id).all()
            s2240_altexprisco_epi_form = form_s2240_altexprisco_epi(initial={ 's2240_altexprisco_fatrisco': s2240_altexprisco_fatrisco }, slug=db_slug)
            s2240_altexprisco_epi_form.fields['s2240_altexprisco_fatrisco'].widget.attrs['readonly'] = True
            s2240_altexprisco_epi_lista = s2240altExpRiscoepi.objects.using( db_slug ).filter(excluido = False, s2240_altexprisco_fatrisco_id=s2240_altexprisco_fatrisco.id).all()
        else:
            s2240_altexprisco_fatrisco = None
        #s2240_altexprisco_fatrisco_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2240_altexprisco_fatrisco' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2240_altexprisco_fatrisco_salvar'
        context = {
            's2240_altexprisco_fatrisco': s2240_altexprisco_fatrisco,
            's2240_altexprisco_fatrisco_form': s2240_altexprisco_fatrisco_form,
            'mensagem': mensagem,
            's2240_altexprisco_fatrisco_id': int(s2240_altexprisco_fatrisco_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's2240_altexprisco_epc_form': s2240_altexprisco_epc_form,
            's2240_altexprisco_epc_lista': s2240_altexprisco_epc_lista,
            's2240_altexprisco_epi_form': s2240_altexprisco_epi_form,
            's2240_altexprisco_epi_lista': s2240_altexprisco_epi_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2240_altexprisco_fatrisco_salvar_custom_variaveis_context#
        }
        return render(request, 's2240_altexprisco_fatrisco_salvar.html', context)
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
        #s2240_altexprisco_fatrisco_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2240_altexprisco_fatrisco')
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
            'show_utilizepi': 1,
            'show_utilizepc': 1,
            'show_epcepi': 0,
            'show_tecmedicao': 0,
            'show_intconc': 0,
            'show_codfatris': 1,
            'show_s2240_altexprisco_infoamb': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'utilizepi': 'utilizepi',
                'utilizepc': 'utilizepc',
                'epcepi': 'epcepi',
                'tecmedicao__icontains': 'tecmedicao__icontains',
                'intconc__icontains': 'intconc__icontains',
                'codfatris__icontains': 'codfatris__icontains',
                's2240_altexprisco_infoamb': 's2240_altexprisco_infoamb',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'utilizepi': 'utilizepi',
                'utilizepc': 'utilizepc',
                'epcepi': 'epcepi',
                'tecmedicao__icontains': 'tecmedicao__icontains',
                'intconc__icontains': 'intconc__icontains',
                'codfatris__icontains': 'codfatris__icontains',
                's2240_altexprisco_infoamb': 's2240_altexprisco_infoamb',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2240_altexprisco_fatrisco_lista = s2240altExpRiscofatRisco.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2240_altexprisco_fatrisco_lista) > 100:
            filtrar = True
            s2240_altexprisco_fatrisco_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        s2240_altexprisco_infoamb_lista = s2240altExpRiscoinfoAmb.objects.using( db_slug ).filter(excluido = False).all()
        #s2240_altexprisco_fatrisco_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2240_altexprisco_fatrisco'
        context = {
            's2240_altexprisco_fatrisco_lista': s2240_altexprisco_fatrisco_lista,
            
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
       
            's2240_altexprisco_infoamb_lista': s2240_altexprisco_infoamb_lista,
        }
        return render(request, 's2240_altexprisco_fatrisco_listar.html', context)
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

