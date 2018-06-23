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
from emensageria.s2200.models import s2200documentos
from emensageria.s2200.models import s2200brasil
from emensageria.s2200.models import s2200exterior
from emensageria.s2200.models import s2200trabEstrangeiro
from emensageria.s2200.models import s2200infoDeficiencia
from emensageria.s2200.models import s2200dependente
from emensageria.s2200.models import s2200aposentadoria
from emensageria.s2200.models import s2200contato
from emensageria.s2200.models import s2200infoCeletista
from emensageria.s2200.models import s2200infoEstatutario
from emensageria.s2200.models import s2200localTrabGeral
from emensageria.s2200.models import s2200localTrabDom
from emensageria.s2200.models import s2200horContratual
from emensageria.s2200.models import s2200filiacaoSindical
from emensageria.s2200.models import s2200alvaraJudicial
from emensageria.s2200.models import s2200observacoes
from emensageria.s2200.models import s2200sucessaoVinc
from emensageria.s2200.models import s2200transfDom
from emensageria.s2200.models import s2200afastamento
from emensageria.s2200.models import s2200desligamento
from emensageria.s2200.forms import form_s2200_documentos
from emensageria.s2200.forms import form_s2200_brasil
from emensageria.s2200.forms import form_s2200_exterior
from emensageria.s2200.forms import form_s2200_trabestrangeiro
from emensageria.s2200.forms import form_s2200_infodeficiencia
from emensageria.s2200.forms import form_s2200_dependente
from emensageria.s2200.forms import form_s2200_aposentadoria
from emensageria.s2200.forms import form_s2200_contato
from emensageria.s2200.forms import form_s2200_infoceletista
from emensageria.s2200.forms import form_s2200_infoestatutario
from emensageria.s2200.forms import form_s2200_localtrabgeral
from emensageria.s2200.forms import form_s2200_localtrabdom
from emensageria.s2200.forms import form_s2200_horcontratual
from emensageria.s2200.forms import form_s2200_filiacaosindical
from emensageria.s2200.forms import form_s2200_alvarajudicial
from emensageria.s2200.forms import form_s2200_observacoes
from emensageria.s2200.forms import form_s2200_sucessaovinc
from emensageria.s2200.forms import form_s2200_transfdom
from emensageria.s2200.forms import form_s2200_afastamento
from emensageria.s2200.forms import form_s2200_desligamento

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
    if request.method == 'POST':
        s2200evtAdmissao.objects.using( db_slug ).filter(id = s2200_evtadmissao_id).delete()
        #s2200_evtadmissao_apagar_custom
        #s2200_evtadmissao_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 's2200_evtadmissao_salvar':
            return redirect('s2200_evtadmissao', hash=request.session['retorno_hash'])
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
    return render(request, 's2200_evtadmissao_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2200_evtadmissao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
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
            'show_localtrabalho': 0,
            'show_clauassec': 0,
            'show_dtterm': 0,
            'show_tpcontr': 1,
            'show_duracao': 0,
            'show_dscsalvar': 0,
            'show_undsalfixo': 1,
            'show_vrsalfx': 1,
            'show_remuneracao': 0,
            'show_dtingrcarr': 0,
            'show_codcarreira': 0,
            'show_codcateg': 1,
            'show_codfuncao': 0,
            'show_codcargo': 0,
            'show_infocontrato': 0,
            'show_inforegimetrab': 0,
            'show_cadini': 1,
            'show_nrrecinfprelim': 0,
            'show_tpregprev': 1,
            'show_tpregtrab': 1,
            'show_matricula': 1,
            'show_vinculo': 0,
            'show_endereco': 0,
            'show_nmpai': 0,
            'show_nmmae': 0,
            'show_paisnac': 1,
            'show_paisnascto': 1,
            'show_uf': 0,
            'show_codmunic': 0,
            'show_dtnascto': 1,
            'show_nascimento': 0,
            'show_nmsoc': 0,
            'show_indpriempr': 0,
            'show_grauinstr': 1,
            'show_estciv': 0,
            'show_racacor': 1,
            'show_sexo': 1,
            'show_nmtrab': 1,
            'show_nistrab': 1,
            'show_cpftrab': 1,
            'show_trabalhador': 0,
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
            'show_evtadmissao': 0,
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
                'localtrabalho': 'localtrabalho',
                'clauassec__icontains': 'clauassec__icontains',
                'dtterm__range': 'dtterm__range',
                'tpcontr': 'tpcontr',
                'duracao': 'duracao',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'undsalfixo': 'undsalfixo',
                'vrsalfx': 'vrsalfx',
                'remuneracao': 'remuneracao',
                'dtingrcarr__range': 'dtingrcarr__range',
                'codcarreira__icontains': 'codcarreira__icontains',
                'codcateg': 'codcateg',
                'codfuncao__icontains': 'codfuncao__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'infocontrato': 'infocontrato',
                'inforegimetrab': 'inforegimetrab',
                'cadini__icontains': 'cadini__icontains',
                'nrrecinfprelim__icontains': 'nrrecinfprelim__icontains',
                'tpregprev': 'tpregprev',
                'tpregtrab': 'tpregtrab',
                'matricula__icontains': 'matricula__icontains',
                'vinculo': 'vinculo',
                'endereco': 'endereco',
                'nmpai__icontains': 'nmpai__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'uf__icontains': 'uf__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'dtnascto__range': 'dtnascto__range',
                'nascimento': 'nascimento',
                'nmsoc__icontains': 'nmsoc__icontains',
                'indpriempr__icontains': 'indpriempr__icontains',
                'grauinstr__icontains': 'grauinstr__icontains',
                'estciv': 'estciv',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'trabalhador': 'trabalhador',
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
                'evtadmissao': 'evtadmissao',
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
                'localtrabalho': 'localtrabalho',
                'clauassec__icontains': 'clauassec__icontains',
                'dtterm__range': 'dtterm__range',
                'tpcontr': 'tpcontr',
                'duracao': 'duracao',
                'dscsalvar__icontains': 'dscsalvar__icontains',
                'undsalfixo': 'undsalfixo',
                'vrsalfx': 'vrsalfx',
                'remuneracao': 'remuneracao',
                'dtingrcarr__range': 'dtingrcarr__range',
                'codcarreira__icontains': 'codcarreira__icontains',
                'codcateg': 'codcateg',
                'codfuncao__icontains': 'codfuncao__icontains',
                'codcargo__icontains': 'codcargo__icontains',
                'infocontrato': 'infocontrato',
                'inforegimetrab': 'inforegimetrab',
                'cadini__icontains': 'cadini__icontains',
                'nrrecinfprelim__icontains': 'nrrecinfprelim__icontains',
                'tpregprev': 'tpregprev',
                'tpregtrab': 'tpregtrab',
                'matricula__icontains': 'matricula__icontains',
                'vinculo': 'vinculo',
                'endereco': 'endereco',
                'nmpai__icontains': 'nmpai__icontains',
                'nmmae__icontains': 'nmmae__icontains',
                'paisnac__icontains': 'paisnac__icontains',
                'paisnascto__icontains': 'paisnascto__icontains',
                'uf__icontains': 'uf__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'dtnascto__range': 'dtnascto__range',
                'nascimento': 'nascimento',
                'nmsoc__icontains': 'nmsoc__icontains',
                'indpriempr__icontains': 'indpriempr__icontains',
                'grauinstr__icontains': 'grauinstr__icontains',
                'estciv': 'estciv',
                'racacor': 'racacor',
                'sexo__icontains': 'sexo__icontains',
                'nmtrab__icontains': 'nmtrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'cpftrab__icontains': 'cpftrab__icontains',
                'trabalhador': 'trabalhador',
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
                'evtadmissao': 'evtadmissao',
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
        s2200_evtadmissao_lista = s2200evtAdmissao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2200_evtadmissao_lista) > 100:
            filtrar = True
            s2200_evtadmissao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        transmissor_lote_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #s2200_evtadmissao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2200_evtadmissao'
        context = {
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
            
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
        return render(request, 's2200_evtadmissao_listar.html', context)
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
def identidade_evento(s2200_evtadmissao_id, db_slug):
    from emensageria.mensageiro.models import TransmissorEventos
    dados_evento = s2200evtAdmissao.objects.using( db_slug ).get(id=s2200_evtadmissao_id)
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
            s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id).update(identidade=identidade_temp)
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
        s2200_evtadmissao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2200_evtadmissao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2200_evtadmissao_id:
        s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if s2200_evtadmissao_id:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, instance = s2200_evtadmissao, slug = db_slug)
        else:
            s2200_evtadmissao_form = form_s2200_evtadmissao(request.POST or None, slug = db_slug, initial={'versao': VERSAO_MODELO, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if s2200_evtadmissao_form.is_valid():
                dados = s2200_evtadmissao_form.cleaned_data
                if s2200_evtadmissao_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #s2200_evtadmissao_campos_multiple_passo1
                    s2200evtAdmissao.objects.using(db_slug).filter(id=s2200_evtadmissao_id).update(**dados)
                    obj = s2200evtAdmissao.objects.using(db_slug).get(id=s2200_evtadmissao_id)
                    #s2200_evtadmissao_editar_custom
                    #s2200_evtadmissao_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['processamento_descricao_resposta'] = 'Cadastrado (Aguardando envio)'
                    dados['processamento_codigo_resposta'] = 0

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s2200_evtadmissao_cadastrar_campos_multiple_passo1
                    obj = s2200evtAdmissao(**dados)
                    obj.save(using = db_slug)
                    #s2200_evtadmissao_cadastrar_custom
                    #s2200_evtadmissao_cadastrar_campos_multiple_passo2
                    identidade_evento(obj.id, db_slug)
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('s2200_evtadmissao_apagar', 's2200_evtadmissao_salvar', 's2200_evtadmissao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2200_evtadmissao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2200_evtadmissao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s2200_evtadmissao_form = disabled_form_fields(s2200_evtadmissao_form, permissao.permite_editar)
        #s2200_evtadmissao_campos_multiple_passo3

        for field in s2200_evtadmissao_form.fields.keys():
            s2200_evtadmissao_form.fields[field].widget.attrs['ng-model'] = 's2200_evtadmissao_'+field
        if int(dict_hash['print']):
            s2200_evtadmissao_form = disabled_form_for_print(s2200_evtadmissao_form)
   
        s2200_evtadmissao_ocorrencias_form = None
        s2200_evtadmissao_ocorrencias_lista = None
        s2200_documentos_form = None
        s2200_documentos_lista = None
        s2200_brasil_form = None
        s2200_brasil_lista = None
        s2200_exterior_form = None
        s2200_exterior_lista = None
        s2200_trabestrangeiro_form = None
        s2200_trabestrangeiro_lista = None
        s2200_infodeficiencia_form = None
        s2200_infodeficiencia_lista = None
        s2200_dependente_form = None
        s2200_dependente_lista = None
        s2200_aposentadoria_form = None
        s2200_aposentadoria_lista = None
        s2200_contato_form = None
        s2200_contato_lista = None
        s2200_infoceletista_form = None
        s2200_infoceletista_lista = None
        s2200_infoestatutario_form = None
        s2200_infoestatutario_lista = None
        s2200_localtrabgeral_form = None
        s2200_localtrabgeral_lista = None
        s2200_localtrabdom_form = None
        s2200_localtrabdom_lista = None
        s2200_horcontratual_form = None
        s2200_horcontratual_lista = None
        s2200_filiacaosindical_form = None
        s2200_filiacaosindical_lista = None
        s2200_alvarajudicial_form = None
        s2200_alvarajudicial_lista = None
        s2200_observacoes_form = None
        s2200_observacoes_lista = None
        s2200_sucessaovinc_form = None
        s2200_sucessaovinc_lista = None
        s2200_transfdom_form = None
        s2200_transfdom_lista = None
        s2200_afastamento_form = None
        s2200_afastamento_lista = None
        s2200_desligamento_form = None
        s2200_desligamento_lista = None
        if s2200_evtadmissao_id:
            s2200_evtadmissao = get_object_or_404(s2200evtAdmissao.objects.using( db_slug ), excluido = False, id = s2200_evtadmissao_id)
       
            s2200_evtadmissao_ocorrencias_form = form_s2200_evtadmissao_ocorrencias(initial={ 'evento': s2200_evtadmissao }, slug=db_slug)
            s2200_evtadmissao_ocorrencias_form.fields['evento'].widget.attrs['readonly'] = True
            s2200_evtadmissao_ocorrencias_lista = s2200evtAdmissaoOcorrencias.objects.using( db_slug ).filter(excluido = False, evento_id=s2200_evtadmissao.id).all()
            s2200_documentos_form = form_s2200_documentos(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_documentos_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_documentos_lista = s2200documentos.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_brasil_form = form_s2200_brasil(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_brasil_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_brasil_lista = s2200brasil.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_exterior_form = form_s2200_exterior(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_exterior_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_exterior_lista = s2200exterior.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_trabestrangeiro_form = form_s2200_trabestrangeiro(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_trabestrangeiro_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_trabestrangeiro_lista = s2200trabEstrangeiro.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infodeficiencia_form = form_s2200_infodeficiencia(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infodeficiencia_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infodeficiencia_lista = s2200infoDeficiencia.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_dependente_form = form_s2200_dependente(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_dependente_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_dependente_lista = s2200dependente.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_aposentadoria_form = form_s2200_aposentadoria(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_aposentadoria_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_aposentadoria_lista = s2200aposentadoria.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_contato_form = form_s2200_contato(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_contato_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_contato_lista = s2200contato.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoceletista_form = form_s2200_infoceletista(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infoceletista_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoceletista_lista = s2200infoCeletista.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_infoestatutario_form = form_s2200_infoestatutario(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_infoestatutario_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_infoestatutario_lista = s2200infoEstatutario.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabgeral_form = form_s2200_localtrabgeral(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_localtrabgeral_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabgeral_lista = s2200localTrabGeral.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_localtrabdom_form = form_s2200_localtrabdom(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_localtrabdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_localtrabdom_lista = s2200localTrabDom.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_horcontratual_form = form_s2200_horcontratual(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_horcontratual_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_horcontratual_lista = s2200horContratual.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_filiacaosindical_form = form_s2200_filiacaosindical(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_filiacaosindical_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_filiacaosindical_lista = s2200filiacaoSindical.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_alvarajudicial_form = form_s2200_alvarajudicial(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_alvarajudicial_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_alvarajudicial_lista = s2200alvaraJudicial.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_observacoes_form = form_s2200_observacoes(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_observacoes_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_observacoes_lista = s2200observacoes.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_sucessaovinc_form = form_s2200_sucessaovinc(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_sucessaovinc_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_sucessaovinc_lista = s2200sucessaoVinc.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_transfdom_form = form_s2200_transfdom(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_transfdom_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_transfdom_lista = s2200transfDom.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_afastamento_form = form_s2200_afastamento(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_afastamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_afastamento_lista = s2200afastamento.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
            s2200_desligamento_form = form_s2200_desligamento(initial={ 's2200_evtadmissao': s2200_evtadmissao }, slug=db_slug)
            s2200_desligamento_form.fields['s2200_evtadmissao'].widget.attrs['readonly'] = True
            s2200_desligamento_lista = s2200desligamento.objects.using( db_slug ).filter(excluido = False, s2200_evtadmissao_id=s2200_evtadmissao.id).all()
        else:
            s2200_evtadmissao = None
        #s2200_evtadmissao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        s2200_evtadmissao_form.fields['tpamb'].widget.attrs['disabled'] = True
        s2200_evtadmissao_form.fields['tpamb'].widget.attrs['readonly'] = True
        s2200_evtadmissao_form.fields['tpamb'].value = TP_AMB
        s2200_evtadmissao_form.fields['procemi'].widget.attrs['disabled'] = True
        s2200_evtadmissao_form.fields['procemi'].widget.attrs['readonly'] = True
        s2200_evtadmissao_form.fields['procemi'].value = 1
        s2200_evtadmissao_form.fields['verproc'].widget.attrs['readonly'] = True
        s2200_evtadmissao_form.fields['verproc'].value = VERSAO_EMENSAGERIA
    
        if dict_hash['tab'] or 's2200_evtadmissao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2200_evtadmissao_salvar'
        context = {
            's2200_evtadmissao': s2200_evtadmissao,
            's2200_evtadmissao_form': s2200_evtadmissao_form,
            'mensagem': mensagem,
            's2200_evtadmissao_id': int(s2200_evtadmissao_id),
            'usuario': usuario,
            
            'hash': hash,
       
            's2200_evtadmissao_ocorrencias_form': s2200_evtadmissao_ocorrencias_form,
            's2200_evtadmissao_ocorrencias_lista': s2200_evtadmissao_ocorrencias_lista,
            's2200_documentos_form': s2200_documentos_form,
            's2200_documentos_lista': s2200_documentos_lista,
            's2200_brasil_form': s2200_brasil_form,
            's2200_brasil_lista': s2200_brasil_lista,
            's2200_exterior_form': s2200_exterior_form,
            's2200_exterior_lista': s2200_exterior_lista,
            's2200_trabestrangeiro_form': s2200_trabestrangeiro_form,
            's2200_trabestrangeiro_lista': s2200_trabestrangeiro_lista,
            's2200_infodeficiencia_form': s2200_infodeficiencia_form,
            's2200_infodeficiencia_lista': s2200_infodeficiencia_lista,
            's2200_dependente_form': s2200_dependente_form,
            's2200_dependente_lista': s2200_dependente_lista,
            's2200_aposentadoria_form': s2200_aposentadoria_form,
            's2200_aposentadoria_lista': s2200_aposentadoria_lista,
            's2200_contato_form': s2200_contato_form,
            's2200_contato_lista': s2200_contato_lista,
            's2200_infoceletista_form': s2200_infoceletista_form,
            's2200_infoceletista_lista': s2200_infoceletista_lista,
            's2200_infoestatutario_form': s2200_infoestatutario_form,
            's2200_infoestatutario_lista': s2200_infoestatutario_lista,
            's2200_localtrabgeral_form': s2200_localtrabgeral_form,
            's2200_localtrabgeral_lista': s2200_localtrabgeral_lista,
            's2200_localtrabdom_form': s2200_localtrabdom_form,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            's2200_horcontratual_form': s2200_horcontratual_form,
            's2200_horcontratual_lista': s2200_horcontratual_lista,
            's2200_filiacaosindical_form': s2200_filiacaosindical_form,
            's2200_filiacaosindical_lista': s2200_filiacaosindical_lista,
            's2200_alvarajudicial_form': s2200_alvarajudicial_form,
            's2200_alvarajudicial_lista': s2200_alvarajudicial_lista,
            's2200_observacoes_form': s2200_observacoes_form,
            's2200_observacoes_lista': s2200_observacoes_lista,
            's2200_sucessaovinc_form': s2200_sucessaovinc_form,
            's2200_sucessaovinc_lista': s2200_sucessaovinc_lista,
            's2200_transfdom_form': s2200_transfdom_form,
            's2200_transfdom_lista': s2200_transfdom_lista,
            's2200_afastamento_form': s2200_afastamento_form,
            's2200_afastamento_lista': s2200_afastamento_lista,
            's2200_desligamento_form': s2200_desligamento_form,
            's2200_desligamento_lista': s2200_desligamento_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2200_evtadmissao_salvar_custom_variaveis_context#
        }
        return render(request, 's2200_evtadmissao_salvar.html', context)
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

