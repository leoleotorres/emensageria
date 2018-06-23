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
from emensageria.mensageiro.forms import *
from emensageria.mensageiro.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageria.eventos.models import s1000evtInfoEmpregador
from emensageria.eventos.models import s1005evtTabEstab
from emensageria.eventos.models import s1010evtTabRubrica
from emensageria.eventos.models import s1020evtTabLotacao
from emensageria.eventos.models import s1030evtTabCargo
from emensageria.eventos.models import s1035evtTabCarreira
from emensageria.eventos.models import s1040evtTabFuncao
from emensageria.eventos.models import s1050evtTabHorTur
from emensageria.eventos.models import s1060evtTabAmbiente
from emensageria.eventos.models import s1070evtTabProcesso
from emensageria.eventos.models import s1080evtTabOperPort
from emensageria.eventos.models import s1200evtRemun
from emensageria.eventos.models import s1202evtRmnRPPS
from emensageria.eventos.models import s1207evtBenPrRP
from emensageria.eventos.models import s1210evtPgtos
from emensageria.eventos.models import s1250evtAqProd
from emensageria.eventos.models import s1260evtComProd
from emensageria.eventos.models import s1270evtContratAvNP
from emensageria.eventos.models import s1280evtInfoComplPer
from emensageria.eventos.models import s1295evtTotConting
from emensageria.eventos.models import s1298evtReabreEvPer
from emensageria.eventos.models import s1299evtFechaEvPer
from emensageria.eventos.models import s1300evtContrSindPatr
from emensageria.eventos.models import s2190evtAdmPrelim
from emensageria.eventos.models import s2200evtAdmissao
from emensageria.eventos.models import s2205evtAltCadastral
from emensageria.eventos.models import s2206evtAltContratual
from emensageria.eventos.models import s2210evtCAT
from emensageria.eventos.models import s2220evtMonit
from emensageria.eventos.models import s2230evtAfastTemp
from emensageria.eventos.models import s2240evtExpRisco
from emensageria.eventos.models import s2241evtInsApo
from emensageria.eventos.models import s2250evtAvPrevio
from emensageria.eventos.models import s2260evtConvInterm
from emensageria.eventos.models import s2298evtReintegr
from emensageria.eventos.models import s2299evtDeslig
from emensageria.eventos.models import s2300evtTSVInicio
from emensageria.eventos.models import s2306evtTSVAltContr
from emensageria.eventos.models import s2399evtTSVTermino
from emensageria.eventos.models import s2400evtCdBenPrRP
from emensageria.eventos.models import s3000evtExclusao
from emensageria.eventos.models import s5001evtBasesTrab
from emensageria.eventos.models import s5002evtIrrfBenef
from emensageria.eventos.models import s5011evtCS
from emensageria.eventos.models import s5012evtIrrf
from emensageria.eventos.forms import form_s1000_evtinfoempregador
from emensageria.eventos.forms import form_s1005_evttabestab
from emensageria.eventos.forms import form_s1010_evttabrubrica
from emensageria.eventos.forms import form_s1020_evttablotacao
from emensageria.eventos.forms import form_s1030_evttabcargo
from emensageria.eventos.forms import form_s1035_evttabcarreira
from emensageria.eventos.forms import form_s1040_evttabfuncao
from emensageria.eventos.forms import form_s1050_evttabhortur
from emensageria.eventos.forms import form_s1060_evttabambiente
from emensageria.eventos.forms import form_s1070_evttabprocesso
from emensageria.eventos.forms import form_s1080_evttaboperport
from emensageria.eventos.forms import form_s1200_evtremun
from emensageria.eventos.forms import form_s1202_evtrmnrpps
from emensageria.eventos.forms import form_s1207_evtbenprrp
from emensageria.eventos.forms import form_s1210_evtpgtos
from emensageria.eventos.forms import form_s1250_evtaqprod
from emensageria.eventos.forms import form_s1260_evtcomprod
from emensageria.eventos.forms import form_s1270_evtcontratavnp
from emensageria.eventos.forms import form_s1280_evtinfocomplper
from emensageria.eventos.forms import form_s1295_evttotconting
from emensageria.eventos.forms import form_s1298_evtreabreevper
from emensageria.eventos.forms import form_s1299_evtfechaevper
from emensageria.eventos.forms import form_s1300_evtcontrsindpatr
from emensageria.eventos.forms import form_s2190_evtadmprelim
from emensageria.eventos.forms import form_s2200_evtadmissao
from emensageria.eventos.forms import form_s2205_evtaltcadastral
from emensageria.eventos.forms import form_s2206_evtaltcontratual
from emensageria.eventos.forms import form_s2210_evtcat
from emensageria.eventos.forms import form_s2220_evtmonit
from emensageria.eventos.forms import form_s2230_evtafasttemp
from emensageria.eventos.forms import form_s2240_evtexprisco
from emensageria.eventos.forms import form_s2241_evtinsapo
from emensageria.eventos.forms import form_s2250_evtavprevio
from emensageria.eventos.forms import form_s2260_evtconvinterm
from emensageria.eventos.forms import form_s2298_evtreintegr
from emensageria.eventos.forms import form_s2299_evtdeslig
from emensageria.eventos.forms import form_s2300_evttsvinicio
from emensageria.eventos.forms import form_s2306_evttsvaltcontr
from emensageria.eventos.forms import form_s2399_evttsvtermino
from emensageria.eventos.forms import form_s2400_evtcdbenprrp
from emensageria.eventos.forms import form_s3000_evtexclusao
from emensageria.eventos.forms import form_s5001_evtbasestrab
from emensageria.eventos.forms import form_s5002_evtirrfbenef
from emensageria.eventos.forms import form_s5011_evtcs
from emensageria.eventos.forms import form_s5012_evtirrf

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissor_lote_id)
    if request.method == 'POST':
        TransmissorLote.objects.using( db_slug ).filter(id = transmissor_lote_id).update(excluido = True)
        #transmissor_lote_apagar_custom
        #transmissor_lote_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissor_lote_salvar':
            return redirect('transmissor_lote', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissor_lote_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #transmissor_lote_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote')
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
            'show_tempo_estimado_conclusao': 0,
            'show_processamento_versao_aplicativo': 0,
            'show_protocolo': 0,
            'show_recepcao_versao_aplicativo': 0,
            'show_recepcao_data_hora': 0,
            'show_resposta_descricao': 0,
            'show_resposta_codigo': 1,
            'show_grupo': 1,
            'show_transmissor_nrinsc': 0,
            'show_transmissor_tpinsc': 0,
            'show_empregador_nrinsc': 1,
            'show_empregador_tpinsc': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'resposta_codigo': 'resposta_codigo',
                'grupo': 'grupo',
                'transmissor_nrinsc__icontains': 'transmissor_nrinsc__icontains',
                'transmissor_tpinsc': 'transmissor_tpinsc',
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'resposta_codigo': 'resposta_codigo',
                'grupo': 'grupo',
                'transmissor_nrinsc__icontains': 'transmissor_nrinsc__icontains',
                'transmissor_tpinsc': 'transmissor_tpinsc',
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissor_lote_lista = TransmissorLote.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissor_lote_lista) > 100:
            filtrar = True
            transmissor_lote_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
    
        #transmissor_lote_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote'
        context = {
            'transmissor_lote_lista': transmissor_lote_lista,
            
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
        return render(request, 'transmissor_lote_listar.html', context)
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

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissor_lote_id:
        transmissor_lote = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissor_lote_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissor_lote_id:
            transmissor_lote_form = form_transmissor_lote(request.POST or None, instance = transmissor_lote, slug = db_slug)
        else:
            transmissor_lote_form = form_transmissor_lote(request.POST or None, slug = db_slug, initial={'resposta_descricao': 'Cadastrado (Aguardando envio)', 'resposta_codigo': 0})
        if request.method == 'POST':
            if transmissor_lote_form.is_valid():
                dados = transmissor_lote_form.cleaned_data
                if transmissor_lote_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissor_lote_campos_multiple_passo1
                    TransmissorLote.objects.using(db_slug).filter(id=transmissor_lote_id).update(**dados)
                    obj = TransmissorLote.objects.using(db_slug).get(id=transmissor_lote_id)
                    #transmissor_lote_editar_custom
                    #transmissor_lote_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['resposta_descricao'] = 'Cadastrado (Aguardando envio)'

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissor_lote_cadastrar_campos_multiple_passo1
                    obj = TransmissorLote(**dados)
                    obj.save(using = db_slug)
                    #transmissor_lote_cadastrar_custom
                    #transmissor_lote_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissor_lote_apagar', 'transmissor_lote_salvar', 'transmissor_lote'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissor_lote_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissor_lote_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissor_lote_form = disabled_form_fields(transmissor_lote_form, permissao.permite_editar)
        #transmissor_lote_campos_multiple_passo3

        for field in transmissor_lote_form.fields.keys():
            transmissor_lote_form.fields[field].widget.attrs['ng-model'] = 'transmissor_lote_'+field
        if int(dict_hash['print']):
            transmissor_lote_form = disabled_form_for_print(transmissor_lote_form)
   
        transmissor_lote_ocorrencias_form = None
        transmissor_lote_ocorrencias_lista = None
        if transmissor_lote_id:
            transmissor_lote = get_object_or_404(TransmissorLote.objects.using( db_slug ), excluido = False, id = transmissor_lote_id)
       
            transmissor_lote_ocorrencias_form = form_transmissor_lote_ocorrencias(initial={ 'transmissor_lote': transmissor_lote }, slug=db_slug)
            transmissor_lote_ocorrencias_form.fields['transmissor_lote'].widget.attrs['readonly'] = True
            transmissor_lote_ocorrencias_lista = TransmissorLoteOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_id=transmissor_lote.id).all()
        else:
            transmissor_lote = None
        if transmissor_lote:
            transmissor_eventos_lista = TransmissorEventos.objects.using(db_slug).filter(excluido=False, transmissor_lote_id=transmissor_lote.id).all()
        else:
            transmissor_eventos_lista = None
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'transmissor_lote' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissor_lote_salvar'
        context = {
            'transmissor_lote': transmissor_lote,
            'transmissor_lote_form': transmissor_lote_form,
            'mensagem': mensagem,
            'transmissor_lote_id': int(transmissor_lote_id),
            'usuario': usuario,
            
            'hash': hash,
       
            'transmissor_lote_ocorrencias_form': transmissor_lote_ocorrencias_form,
            'transmissor_lote_ocorrencias_lista': transmissor_lote_ocorrencias_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            'transmissor_eventos_lista': transmissor_eventos_lista,
        }
        return render(request, 'transmissor_lote_salvar.html', context)
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

