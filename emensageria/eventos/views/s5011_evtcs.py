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
from emensageria.eventos.forms import *
from emensageria.eventos.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageria.s5011.models import s5011infoCPSeg
from emensageria.s5011.models import s5011infoPJ
from emensageria.s5011.models import s5011ideEstab
from emensageria.s5011.models import s5011infoCRContrib
from emensageria.s5011.forms import form_s5011_infocpseg
from emensageria.s5011.forms import form_s5011_infopj
from emensageria.s5011.forms import form_s5011_ideestab
from emensageria.s5011.forms import form_s5011_infocrcontrib

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s5011_evtcs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
    if request.method == 'POST':
        s5011evtCS.objects.using( db_slug ).filter(id = s5011_evtcs_id).delete()
        #s5011_evtcs_apagar_custom
        #s5011_evtcs_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's5011_evtcs_salvar':
            return redirect('s5011_evtcs', hash=request.session['retorno_hash'])
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
    return render(request, 's5011_evtcs_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s5011_evtcs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
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
            'show_classtrib': 1,
            'show_infocontrib': 0,
            'show_indexistinfo': 1,
            'show_nrrecarqbase': 0,
            'show_infocs': 0,
            'show_nrinsc': 1,
            'show_tpinsc': 1,
            'show_ideempregador': 0,
            'show_perapur': 1,
            'show_indapuracao': 1,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_evtcs': 0,
            'show_recibo_hash': 0,
            'show_recibo_numero': 0,
            'show_processamento_data_hora': 0,
            'show_processamento_versao_app_processamento': 0,
            'show_processamento_descricao_resposta': 0,
            'show_processamento_codigo_resposta': 1,
            'show_recepcao_protocolo_envio_lote': 0,
            'show_recepcao_versao_app': 0,
            'show_recepcao_data_hora': 0,
            'show_recepcao_tp_amb': 0,
            'show_versao': 0,
            'show_transmissor_lote': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'infocontrib': 'infocontrib',
                'indexistinfo': 'indexistinfo',
                'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                'infocs': 'infocs',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'perapur__icontains': 'perapur__icontains',
                'indapuracao': 'indapuracao',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtcs': 'evtcs',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote': 'transmissor_lote',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'infocontrib': 'infocontrib',
                'indexistinfo': 'indexistinfo',
                'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                'infocs': 'infocs',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'perapur__icontains': 'perapur__icontains',
                'indapuracao': 'indapuracao',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtcs': 'evtcs',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote': 'transmissor_lote',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s5011_evtcs_lista = s5011evtCS.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s5011_evtcs_lista) > 100:
            filtrar = True
            s5011_evtcs_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #s5011_evtcs_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5011_evtcs'
        context = {
            's5011_evtcs_lista': s5011_evtcs_lista,
            
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
       
            'transmissor_lote_lista': transmissor_lote_lista,
        }
        return render(request, 's5011_evtcs_listar.html', context)
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

#view_identidade_evento#
def identidade_evento(s5011_evtcs_id, db_slug):
    from emensageria.mensageiro.models import TransmissorEventos
    dados_evento = s5011evtCS.objects.using( db_slug ).get(id=s5011_evtcs_id)
    identidade = 'ID'
    identidade += str(dados_evento.tpinsc)
    nr_insc = dados_evento.nrinsc
    while len(nr_insc) != 14:
        nr_insc = nr_insc+'0'
    identidade += nr_insc
    identidade += str(dados_evento.criado_em.year)
    mes = str(dados_evento.criado_em.month)
    if len(mes) == 1: mes = '0'+mes
    identidade += mes
    dia = str(dados_evento.criado_em.day)
    if len(dia) == 1: dia = '0'+dia
    identidade += dia
    hora = str(dados_evento.criado_em.hour)
    if len(hora) == 1: hora = '0'+hora
    identidade += hora
    minuto = str(dados_evento.criado_em.minute)
    if len(minuto) == 1: minuto = '0'+minuto
    identidade += minuto
    segundo = str(dados_evento.criado_em.second)
    if len(segundo) == 1: segundo = '0'+segundo
    identidade += segundo
    existe = True
    n = 0
    while existe:
        n+=1
        sequencial = str(n)
        while len(sequencial) != 5:
            sequencial = '0'+sequencial
        identidade_temp = identidade + sequencial
        lista_eventos = TransmissorEventos.objects.using(db_slug).filter(criado_em=dados_evento.criado_em,
                                                                         excluido=False, identidade = identidade_temp).all()
        if not lista_eventos:
            s5011evtCS.objects.using(db_slug).filter(id=s5011_evtcs_id).update(identidade=identidade_temp)
            existe = False
    return identidade_temp
#view_identidade_evento#



def gerar_identidade(request, chave, evento_id):
    from emensageria.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        ident = identidade_evento(evento_id, db_slug)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


def salvar(request, hash):
    from emensageria.settings import VERSAO_EMENSAGERIA, VERSAO_MODELO, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s5011_evtcs_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s5011_evtcs_id:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s5011_evtcs_id:
            s5011_evtcs_form = form_s5011_evtcs(request.POST or None, instance = s5011_evtcs, slug = db_slug)
        else:
            s5011_evtcs_form = form_s5011_evtcs(request.POST or None, slug = db_slug, initial={'versao': VERSAO_MODELO, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s5011_evtcs_form.is_valid():
                dados = s5011_evtcs_form.cleaned_data
                if s5011_evtcs_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s5011_evtcs_campos_multiple_passo1
                    s5011evtCS.objects.using(db_slug).filter(id=s5011_evtcs_id).update(**dados)
                    obj = s5011evtCS.objects.using(db_slug).get(id=s5011_evtcs_id)
                    #s5011_evtcs_editar_custom
                    #s5011_evtcs_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['processamento_descricao_resposta'] = 'Cadastrado (Aguardando envio)'
                    dados['processamento_codigo_resposta'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s5011_evtcs_cadastrar_campos_multiple_passo1
                    obj = s5011evtCS(**dados)
                    obj.save(using = db_slug)
                    #s5011_evtcs_cadastrar_custom
                    #s5011_evtcs_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s5011_evtcs_apagar', 's5011_evtcs_salvar', 's5011_evtcs'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s5011_evtcs_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s5011_evtcs_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s5011_evtcs_form = disabled_form_fields(s5011_evtcs_form, permissao.permite_editar)
        #s5011_evtcs_campos_multiple_passo3

        for field in s5011_evtcs_form.fields.keys():
            s5011_evtcs_form.fields[field].widget.attrs['ng-model'] = 's5011_evtcs_'+field
        if int(dict_hash['print']):
            s5011_evtcs_form = disabled_form_for_print(s5011_evtcs_form)
   
        s5011_evtcs_ocorrencias_form = None
        s5011_evtcs_ocorrencias_lista = None
        s5011_infocpseg_form = None
        s5011_infocpseg_lista = None
        s5011_infopj_form = None
        s5011_infopj_lista = None
        s5011_ideestab_form = None
        s5011_ideestab_lista = None
        s5011_infocrcontrib_form = None
        s5011_infocrcontrib_lista = None
        if s5011_evtcs_id:
            s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
       
            s5011_evtcs_ocorrencias_form = form_s5011_evtcs_ocorrencias(initial={ 'evento': s5011_evtcs }, slug=db_slug)
            s5011_evtcs_ocorrencias_form.fields['evento'].widget.attrs['readonly'] = True
            s5011_evtcs_ocorrencias_lista = s5011evtCSOcorrencias.objects.using( db_slug ).filter(excluido = False, evento_id=s5011_evtcs.id).all()
            s5011_infocpseg_form = form_s5011_infocpseg(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infocpseg_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infocpseg_lista = s5011infoCPSeg.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_infopj_form = form_s5011_infopj(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infopj_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infopj_lista = s5011infoPJ.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_ideestab_form = form_s5011_ideestab(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_ideestab_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_ideestab_lista = s5011ideEstab.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
            s5011_infocrcontrib_form = form_s5011_infocrcontrib(initial={ 's5011_evtcs': s5011_evtcs }, slug=db_slug)
            s5011_infocrcontrib_form.fields['s5011_evtcs'].widget.attrs['readonly'] = True
            s5011_infocrcontrib_lista = s5011infoCRContrib.objects.using( db_slug ).filter(excluido = False, s5011_evtcs_id=s5011_evtcs.id).all()
        else:
            s5011_evtcs = None
        #s5011_evtcs_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        s5011_evtcs_form.fields['tpamb'].widget.attrs['disabled'] = True
        s5011_evtcs_form.fields['tpamb'].widget.attrs['readonly'] = True
        s5011_evtcs_form.fields['tpamb'].value = TP_AMB
        s5011_evtcs_form.fields['procemi'].widget.attrs['disabled'] = True
        s5011_evtcs_form.fields['procemi'].widget.attrs['readonly'] = True
        s5011_evtcs_form.fields['procemi'].value = 1
        s5011_evtcs_form.fields['verproc'].widget.attrs['readonly'] = True
        s5011_evtcs_form.fields['verproc'].value = VERSAO_EMENSAGERIA
    
        if dict_hash['tab'] or 's5011_evtcs' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's5011_evtcs_salvar'
        context = {
            's5011_evtcs': s5011_evtcs,
            's5011_evtcs_form': s5011_evtcs_form,
            'mensagem': mensagem,
            's5011_evtcs_id': int(s5011_evtcs_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's5011_evtcs_ocorrencias_form': s5011_evtcs_ocorrencias_form,
            's5011_evtcs_ocorrencias_lista': s5011_evtcs_ocorrencias_lista,
            's5011_infocpseg_form': s5011_infocpseg_form,
            's5011_infocpseg_lista': s5011_infocpseg_lista,
            's5011_infopj_form': s5011_infopj_form,
            's5011_infopj_lista': s5011_infopj_lista,
            's5011_ideestab_form': s5011_ideestab_form,
            's5011_ideestab_lista': s5011_ideestab_lista,
            's5011_infocrcontrib_form': s5011_infocrcontrib_form,
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s5011_evtcs_salvar_custom_variaveis_context#
        }
        return render(request, 's5011_evtcs_salvar.html', context)
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

