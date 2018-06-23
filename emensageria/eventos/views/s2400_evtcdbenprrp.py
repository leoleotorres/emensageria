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
from emensageria.s2400.models import s2400fimBeneficio
from emensageria.s2400.models import s2400brasil
from emensageria.s2400.models import s2400exterior
from emensageria.s2400.models import s2400iniBeneficio
from emensageria.s2400.models import s2400altBeneficio
from emensageria.s2400.forms import form_s2400_fimbeneficio
from emensageria.s2400.forms import form_s2400_brasil
from emensageria.s2400.forms import form_s2400_exterior
from emensageria.s2400.forms import form_s2400_inibeneficio
from emensageria.s2400.forms import form_s2400_altbeneficio

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2400_evtcdbenprrp_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_evtcdbenprrp')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2400_evtcdbenprrp = get_object_or_404(s2400evtCdBenPrRP.objects.using( db_slug ), excluido = False, id = s2400_evtcdbenprrp_id)
    if request.method == 'POST':
        s2400evtCdBenPrRP.objects.using( db_slug ).filter(id = s2400_evtcdbenprrp_id).delete()
        #s2400_evtcdbenprrp_apagar_custom
        #s2400_evtcdbenprrp_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's2400_evtcdbenprrp_salvar':
            return redirect('s2400_evtcdbenprrp', hash=request.session['retorno_hash'])
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
    return render(request, 's2400_evtcdbenprrp_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2400_evtcdbenprrp_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_evtcdbenprrp')
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
            'show_tpplanrp': 1,
            'show_infobeneficio': 0,
            'show_endereco': 0,
            'show_nmpai': 0,
            'show_nmmae': 0,
            'show_paisnac': 1,
            'show_paisnascto': 1,
            'show_uf': 0,
            'show_codmunic': 0,
            'show_dtnascto': 1,
            'show_dadosnasc': 0,
            'show_dadosbenef': 0,
            'show_nmbenefic': 1,
            'show_cpfbenef': 1,
            'show_idebenef': 0,
            'show_nrinsc': 1,
            'show_tpinsc': 1,
            'show_ideempregador': 0,
            'show_verproc': 0,
            'show_procemi': 0,
            'show_tpamb': 0,
            'show_nrrecibo': 0,
            'show_indretif': 1,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_evtcdbenprrp': 0,
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
            'show_operacao': 1,
            'show_versao': 0,
            'show_transmissor_lote': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tpplanrp': 'tpplanrp',
                'infobeneficio': 'infobeneficio',
                'endereco': 'endereco',
                'nmpai__icontains': 'nmpai__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'uf__icontains': 'uf__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'dtnascto__range': 'dtnascto__range',
                'dadosnasc': 'dadosnasc',
                'dadosbenef': 'dadosbenef',
                'nmbenefic__icontains': 'nmbenefic__icontains',
                'cpfbenef__icontains': 'cpfbenef__icontains',
                'idebenef': 'idebenef',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'indretif': 'indretif',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtcdbenprrp': 'evtcdbenprrp',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'operacao': 'operacao',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote': 'transmissor_lote',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tpplanrp': 'tpplanrp',
                'infobeneficio': 'infobeneficio',
                'endereco': 'endereco',
                'nmpai__icontains': 'nmpai__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'uf__icontains': 'uf__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'dtnascto__range': 'dtnascto__range',
                'dadosnasc': 'dadosnasc',
                'dadosbenef': 'dadosbenef',
                'nmbenefic__icontains': 'nmbenefic__icontains',
                'cpfbenef__icontains': 'cpfbenef__icontains',
                'idebenef': 'idebenef',
                'nrinsc__icontains': 'nrinsc__icontains',
                'tpinsc': 'tpinsc',
                'ideempregador': 'ideempregador',
                'verproc__icontains': 'verproc__icontains',
                'procemi': 'procemi',
                'tpamb': 'tpamb',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'indretif': 'indretif',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'evtcdbenprrp': 'evtcdbenprrp',
                'recibo_hash__icontains': 'recibo_hash__icontains',
                'recibo_numero__icontains': 'recibo_numero__icontains',
                'processamento_data_hora__range': 'processamento_data_hora__range',
                'processamento_versao_app_processamento__icontains': 'processamento_versao_app_processamento__icontains',
                'recepcao_protocolo_envio_lote__icontains': 'recepcao_protocolo_envio_lote__icontains',
                'operacao': 'operacao',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote': 'transmissor_lote',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2400_evtcdbenprrp_lista = s2400evtCdBenPrRP.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2400_evtcdbenprrp_lista) > 100:
            filtrar = True
            s2400_evtcdbenprrp_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #s2400_evtcdbenprrp_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2400_evtcdbenprrp'
        context = {
            's2400_evtcdbenprrp_lista': s2400_evtcdbenprrp_lista,
            
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
        return render(request, 's2400_evtcdbenprrp_listar.html', context)
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
def identidade_evento(s2400_evtcdbenprrp_id, db_slug):
    from emensageria.mensageiro.models import TransmissorEventos
    dados_evento = s2400evtCdBenPrRP.objects.using( db_slug ).get(id=s2400_evtcdbenprrp_id)
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
            s2400evtCdBenPrRP.objects.using(db_slug).filter(id=s2400_evtcdbenprrp_id).update(identidade=identidade_temp)
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
        s2400_evtcdbenprrp_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2400_evtcdbenprrp')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2400_evtcdbenprrp_id:
        s2400_evtcdbenprrp = get_object_or_404(s2400evtCdBenPrRP.objects.using( db_slug ), excluido = False, id = s2400_evtcdbenprrp_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s2400_evtcdbenprrp_id:
            s2400_evtcdbenprrp_form = form_s2400_evtcdbenprrp(request.POST or None, instance = s2400_evtcdbenprrp, slug = db_slug)
        else:
            s2400_evtcdbenprrp_form = form_s2400_evtcdbenprrp(request.POST or None, slug = db_slug, initial={'versao': VERSAO_MODELO, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2400_evtcdbenprrp_form.is_valid():
                dados = s2400_evtcdbenprrp_form.cleaned_data
                if s2400_evtcdbenprrp_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s2400_evtcdbenprrp_campos_multiple_passo1
                    s2400evtCdBenPrRP.objects.using(db_slug).filter(id=s2400_evtcdbenprrp_id).update(**dados)
                    obj = s2400evtCdBenPrRP.objects.using(db_slug).get(id=s2400_evtcdbenprrp_id)
                    #s2400_evtcdbenprrp_editar_custom
                    #s2400_evtcdbenprrp_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['processamento_descricao_resposta'] = 'Cadastrado (Aguardando envio)'
                    dados['processamento_codigo_resposta'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2400_evtcdbenprrp_cadastrar_campos_multiple_passo1
                    obj = s2400evtCdBenPrRP(**dados)
                    obj.save(using = db_slug)
                    #s2400_evtcdbenprrp_cadastrar_custom
                    #s2400_evtcdbenprrp_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s2400_evtcdbenprrp_apagar', 's2400_evtcdbenprrp_salvar', 's2400_evtcdbenprrp'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2400_evtcdbenprrp_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2400_evtcdbenprrp_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2400_evtcdbenprrp_form = disabled_form_fields(s2400_evtcdbenprrp_form, permissao.permite_editar)
        #s2400_evtcdbenprrp_campos_multiple_passo3

        for field in s2400_evtcdbenprrp_form.fields.keys():
            s2400_evtcdbenprrp_form.fields[field].widget.attrs['ng-model'] = 's2400_evtcdbenprrp_'+field
        if int(dict_hash['print']):
            s2400_evtcdbenprrp_form = disabled_form_for_print(s2400_evtcdbenprrp_form)
   
        s2400_evtcdbenprrp_ocorrencias_form = None
        s2400_evtcdbenprrp_ocorrencias_lista = None
        s2400_fimbeneficio_form = None
        s2400_fimbeneficio_lista = None
        s2400_brasil_form = None
        s2400_brasil_lista = None
        s2400_exterior_form = None
        s2400_exterior_lista = None
        s2400_inibeneficio_form = None
        s2400_inibeneficio_lista = None
        s2400_altbeneficio_form = None
        s2400_altbeneficio_lista = None
        if s2400_evtcdbenprrp_id:
            s2400_evtcdbenprrp = get_object_or_404(s2400evtCdBenPrRP.objects.using( db_slug ), excluido = False, id = s2400_evtcdbenprrp_id)
       
            s2400_evtcdbenprrp_ocorrencias_form = form_s2400_evtcdbenprrp_ocorrencias(initial={ 'evento': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_evtcdbenprrp_ocorrencias_form.fields['evento'].widget.attrs['readonly'] = True
            s2400_evtcdbenprrp_ocorrencias_lista = s2400evtCdBenPrRPOcorrencias.objects.using( db_slug ).filter(excluido = False, evento_id=s2400_evtcdbenprrp.id).all()
            s2400_fimbeneficio_form = form_s2400_fimbeneficio(initial={ 's2400_evtcdbenprrp': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_fimbeneficio_form.fields['s2400_evtcdbenprrp'].widget.attrs['readonly'] = True
            s2400_fimbeneficio_lista = s2400fimBeneficio.objects.using( db_slug ).filter(excluido = False, s2400_evtcdbenprrp_id=s2400_evtcdbenprrp.id).all()
            s2400_brasil_form = form_s2400_brasil(initial={ 's2400_evtcdbenprrp': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_brasil_form.fields['s2400_evtcdbenprrp'].widget.attrs['readonly'] = True
            s2400_brasil_lista = s2400brasil.objects.using( db_slug ).filter(excluido = False, s2400_evtcdbenprrp_id=s2400_evtcdbenprrp.id).all()
            s2400_exterior_form = form_s2400_exterior(initial={ 's2400_evtcdbenprrp': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_exterior_form.fields['s2400_evtcdbenprrp'].widget.attrs['readonly'] = True
            s2400_exterior_lista = s2400exterior.objects.using( db_slug ).filter(excluido = False, s2400_evtcdbenprrp_id=s2400_evtcdbenprrp.id).all()
            s2400_inibeneficio_form = form_s2400_inibeneficio(initial={ 's2400_evtcdbenprrp': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_inibeneficio_form.fields['s2400_evtcdbenprrp'].widget.attrs['readonly'] = True
            s2400_inibeneficio_lista = s2400iniBeneficio.objects.using( db_slug ).filter(excluido = False, s2400_evtcdbenprrp_id=s2400_evtcdbenprrp.id).all()
            s2400_altbeneficio_form = form_s2400_altbeneficio(initial={ 's2400_evtcdbenprrp': s2400_evtcdbenprrp }, slug=db_slug)
            s2400_altbeneficio_form.fields['s2400_evtcdbenprrp'].widget.attrs['readonly'] = True
            s2400_altbeneficio_lista = s2400altBeneficio.objects.using( db_slug ).filter(excluido = False, s2400_evtcdbenprrp_id=s2400_evtcdbenprrp.id).all()
        else:
            s2400_evtcdbenprrp = None
        #s2400_evtcdbenprrp_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        s2400_evtcdbenprrp_form.fields['tpamb'].widget.attrs['disabled'] = True
        s2400_evtcdbenprrp_form.fields['tpamb'].widget.attrs['readonly'] = True
        s2400_evtcdbenprrp_form.fields['tpamb'].value = TP_AMB
        s2400_evtcdbenprrp_form.fields['procemi'].widget.attrs['disabled'] = True
        s2400_evtcdbenprrp_form.fields['procemi'].widget.attrs['readonly'] = True
        s2400_evtcdbenprrp_form.fields['procemi'].value = 1
        s2400_evtcdbenprrp_form.fields['verproc'].widget.attrs['readonly'] = True
        s2400_evtcdbenprrp_form.fields['verproc'].value = VERSAO_EMENSAGERIA
    
        if dict_hash['tab'] or 's2400_evtcdbenprrp' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2400_evtcdbenprrp_salvar'
        context = {
            's2400_evtcdbenprrp': s2400_evtcdbenprrp,
            's2400_evtcdbenprrp_form': s2400_evtcdbenprrp_form,
            'mensagem': mensagem,
            's2400_evtcdbenprrp_id': int(s2400_evtcdbenprrp_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's2400_evtcdbenprrp_ocorrencias_form': s2400_evtcdbenprrp_ocorrencias_form,
            's2400_evtcdbenprrp_ocorrencias_lista': s2400_evtcdbenprrp_ocorrencias_lista,
            's2400_fimbeneficio_form': s2400_fimbeneficio_form,
            's2400_fimbeneficio_lista': s2400_fimbeneficio_lista,
            's2400_brasil_form': s2400_brasil_form,
            's2400_brasil_lista': s2400_brasil_lista,
            's2400_exterior_form': s2400_exterior_form,
            's2400_exterior_lista': s2400_exterior_lista,
            's2400_inibeneficio_form': s2400_inibeneficio_form,
            's2400_inibeneficio_lista': s2400_inibeneficio_lista,
            's2400_altbeneficio_form': s2400_altbeneficio_form,
            's2400_altbeneficio_lista': s2400_altbeneficio_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2400_evtcdbenprrp_salvar_custom_variaveis_context#
        }
        return render(request, 's2400_evtcdbenprrp_salvar.html', context)
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

