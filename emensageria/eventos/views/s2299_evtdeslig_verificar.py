#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__license__ = "agpl v3"
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"
__status__ = "Development"

"""

    eMensageria - Sistema de Gerenciamento de Eventos do eSocial <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
from emensageria.s2299.models import *
from emensageria.s2299.forms import *


def txt_xml(texto):
    texto = str(texto)
    texto = texto.replace(">",'&gt;')
    texto = texto.replace("<",'&lt;')
    texto = texto.replace("&",'&amp;')
    texto = texto.replace('"','&quot;')
    texto = texto.replace("'",'&apos;')
    return texto



def verificar(request, hash, slug=0):
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageria'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.session['usuario_id']   
        dict_hash = get_hash_url( hash )
        s2299_evtdeslig_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_evtdeslig')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)
        s2299_evtdeslig_lista = s2299evtDeslig.objects.using( db_slug ).filter(id=s2299_evtdeslig_id, excluido = False).all()
        ocorrencias_lista = s2299evtDesligOcorrencias.objects.using( db_slug ).filter(evento_id=s2299_evtdeslig_id, excluido = False).all()

    
        s2299_observacoes_lista = s2299observacoes.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_sucessaovinc_lista = s2299sucessaoVinc.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_transftit_lista = s2299transfTit.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_verbasresc_lista = s2299verbasResc.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_dmdev_lista = s2299dmDev.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_lista = s2299infoPerApur.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_ideestablot_lista = s2299infoPerApurideEstabLot.objects.using(db_slug).filter(s2299_infoperapur_id__in = listar_ids(s2299_infoperapur_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detverbas_lista = s2299infoPerApurdetVerbas.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infosaudecolet_lista = s2299infoPerApurinfoSaudeColet.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detoper_lista = s2299infoPerApurdetOper.objects.using(db_slug).filter(s2299_infoperapur_infosaudecolet_id__in = listar_ids(s2299_infoperapur_infosaudecolet_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detplano_lista = s2299infoPerApurdetPlano.objects.using(db_slug).filter(s2299_infoperapur_detoper_id__in = listar_ids(s2299_infoperapur_detoper_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infoagnocivo_lista = s2299infoPerApurinfoAgNocivo.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infosimples_lista = s2299infoPerApurinfoSimples.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_lista = s2299infoPerAnt.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideadc_lista = s2299infoPerAntideADC.objects.using(db_slug).filter(s2299_infoperant_id__in = listar_ids(s2299_infoperant_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideperiodo_lista = s2299infoPerAntidePeriodo.objects.using(db_slug).filter(s2299_infoperant_ideadc_id__in = listar_ids(s2299_infoperant_ideadc_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideestablot_lista = s2299infoPerAntideEstabLot.objects.using(db_slug).filter(s2299_infoperant_ideperiodo_id__in = listar_ids(s2299_infoperant_ideperiodo_lista) ).filter(excluido=False).all()    
        s2299_infoperant_detverbas_lista = s2299infoPerAntdetVerbas.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_infoagnocivo_lista = s2299infoPerAntinfoAgNocivo.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_infosimples_lista = s2299infoPerAntinfoSimples.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_lista = s2299infoTrabInterm.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_procjudtrab_lista = s2299infoTrabIntermprocJudTrab.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_infomv_lista = s2299infoTrabInterminfoMV.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_remunoutrempr_lista = s2299infoTrabIntermremunOutrEmpr.objects.using(db_slug).filter(s2299_infotrabinterm_infomv_id__in = listar_ids(s2299_infotrabinterm_infomv_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_proccs_lista = s2299infoTrabIntermprocCS.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_quarentena_lista = s2299infoTrabIntermquarentena.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_consigfgts_lista = s2299infoTrabIntermconsigFGTS.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2299_evtdeslig'
        context = {
            's2299_evtdeslig_lista': s2299_evtdeslig_lista,
            's2299_evtdeslig_id': s2299_evtdeslig_id, 
            's2299_evtdeslig': s2299_evtdeslig, 
            'ocorrencias_lista': ocorrencias_lista, 
            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
    
            's2299_observacoes_lista': s2299_observacoes_lista,    
            's2299_sucessaovinc_lista': s2299_sucessaovinc_lista,    
            's2299_transftit_lista': s2299_transftit_lista,    
            's2299_verbasresc_lista': s2299_verbasresc_lista,    
            's2299_dmdev_lista': s2299_dmdev_lista,    
            's2299_infoperapur_lista': s2299_infoperapur_lista,    
            's2299_infoperapur_ideestablot_lista': s2299_infoperapur_ideestablot_lista,    
            's2299_infoperapur_detverbas_lista': s2299_infoperapur_detverbas_lista,    
            's2299_infoperapur_infosaudecolet_lista': s2299_infoperapur_infosaudecolet_lista,    
            's2299_infoperapur_detoper_lista': s2299_infoperapur_detoper_lista,    
            's2299_infoperapur_detplano_lista': s2299_infoperapur_detplano_lista,    
            's2299_infoperapur_infoagnocivo_lista': s2299_infoperapur_infoagnocivo_lista,    
            's2299_infoperapur_infosimples_lista': s2299_infoperapur_infosimples_lista,    
            's2299_infoperant_lista': s2299_infoperant_lista,    
            's2299_infoperant_ideadc_lista': s2299_infoperant_ideadc_lista,    
            's2299_infoperant_ideperiodo_lista': s2299_infoperant_ideperiodo_lista,    
            's2299_infoperant_ideestablot_lista': s2299_infoperant_ideestablot_lista,    
            's2299_infoperant_detverbas_lista': s2299_infoperant_detverbas_lista,    
            's2299_infoperant_infoagnocivo_lista': s2299_infoperant_infoagnocivo_lista,    
            's2299_infoperant_infosimples_lista': s2299_infoperant_infosimples_lista,    
            's2299_infotrabinterm_lista': s2299_infotrabinterm_lista,    
            's2299_infotrabinterm_procjudtrab_lista': s2299_infotrabinterm_procjudtrab_lista,    
            's2299_infotrabinterm_infomv_lista': s2299_infotrabinterm_infomv_lista,    
            's2299_infotrabinterm_remunoutrempr_lista': s2299_infotrabinterm_remunoutrempr_lista,    
            's2299_infotrabinterm_proccs_lista': s2299_infotrabinterm_proccs_lista,    
            's2299_infotrabinterm_quarentena_lista': s2299_infotrabinterm_quarentena_lista,    
            's2299_infotrabinterm_consigfgts_lista': s2299_infotrabinterm_consigfgts_lista,
        }
        return render(request, '%s/s2299_evtdeslig_verificar.html' % s2299_evtdeslig.versao, context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_s2299(s2299_evtdeslig_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s2299_evtdeslig_id:
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)
        s2299_evtdeslig_lista = s2299evtDeslig.objects.using( db_slug ).filter(id=s2299_evtdeslig_id, excluido = False).all()
    
        s2299_observacoes_lista = s2299observacoes.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_sucessaovinc_lista = s2299sucessaoVinc.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_transftit_lista = s2299transfTit.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_verbasresc_lista = s2299verbasResc.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_dmdev_lista = s2299dmDev.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_lista = s2299infoPerApur.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_ideestablot_lista = s2299infoPerApurideEstabLot.objects.using(db_slug).filter(s2299_infoperapur_id__in = listar_ids(s2299_infoperapur_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detverbas_lista = s2299infoPerApurdetVerbas.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infosaudecolet_lista = s2299infoPerApurinfoSaudeColet.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detoper_lista = s2299infoPerApurdetOper.objects.using(db_slug).filter(s2299_infoperapur_infosaudecolet_id__in = listar_ids(s2299_infoperapur_infosaudecolet_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_detplano_lista = s2299infoPerApurdetPlano.objects.using(db_slug).filter(s2299_infoperapur_detoper_id__in = listar_ids(s2299_infoperapur_detoper_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infoagnocivo_lista = s2299infoPerApurinfoAgNocivo.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperapur_infosimples_lista = s2299infoPerApurinfoSimples.objects.using(db_slug).filter(s2299_infoperapur_ideestablot_id__in = listar_ids(s2299_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_lista = s2299infoPerAnt.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideadc_lista = s2299infoPerAntideADC.objects.using(db_slug).filter(s2299_infoperant_id__in = listar_ids(s2299_infoperant_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideperiodo_lista = s2299infoPerAntidePeriodo.objects.using(db_slug).filter(s2299_infoperant_ideadc_id__in = listar_ids(s2299_infoperant_ideadc_lista) ).filter(excluido=False).all()    
        s2299_infoperant_ideestablot_lista = s2299infoPerAntideEstabLot.objects.using(db_slug).filter(s2299_infoperant_ideperiodo_id__in = listar_ids(s2299_infoperant_ideperiodo_lista) ).filter(excluido=False).all()    
        s2299_infoperant_detverbas_lista = s2299infoPerAntdetVerbas.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_infoagnocivo_lista = s2299infoPerAntinfoAgNocivo.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infoperant_infosimples_lista = s2299infoPerAntinfoSimples.objects.using(db_slug).filter(s2299_infoperant_ideestablot_id__in = listar_ids(s2299_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_lista = s2299infoTrabInterm.objects.using(db_slug).filter(s2299_dmdev_id__in = listar_ids(s2299_dmdev_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_procjudtrab_lista = s2299infoTrabIntermprocJudTrab.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_infomv_lista = s2299infoTrabInterminfoMV.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_remunoutrempr_lista = s2299infoTrabIntermremunOutrEmpr.objects.using(db_slug).filter(s2299_infotrabinterm_infomv_id__in = listar_ids(s2299_infotrabinterm_infomv_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_proccs_lista = s2299infoTrabIntermprocCS.objects.using(db_slug).filter(s2299_verbasresc_id__in = listar_ids(s2299_verbasresc_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_quarentena_lista = s2299infoTrabIntermquarentena.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()    
        s2299_infotrabinterm_consigfgts_lista = s2299infoTrabIntermconsigFGTS.objects.using(db_slug).filter(s2299_evtdeslig_id__in = listar_ids(s2299_evtdeslig_lista) ).filter(excluido=False).all()
        context = {
            'base': s2299_evtdeslig,
            's2299_evtdeslig_lista': s2299_evtdeslig_lista,
            's2299_evtdeslig_id': int(s2299_evtdeslig_id), 
            's2299_evtdeslig': s2299_evtdeslig,
    
            's2299_observacoes_lista': s2299_observacoes_lista,    
            's2299_sucessaovinc_lista': s2299_sucessaovinc_lista,    
            's2299_transftit_lista': s2299_transftit_lista,    
            's2299_verbasresc_lista': s2299_verbasresc_lista,    
            's2299_dmdev_lista': s2299_dmdev_lista,    
            's2299_infoperapur_lista': s2299_infoperapur_lista,    
            's2299_infoperapur_ideestablot_lista': s2299_infoperapur_ideestablot_lista,    
            's2299_infoperapur_detverbas_lista': s2299_infoperapur_detverbas_lista,    
            's2299_infoperapur_infosaudecolet_lista': s2299_infoperapur_infosaudecolet_lista,    
            's2299_infoperapur_detoper_lista': s2299_infoperapur_detoper_lista,    
            's2299_infoperapur_detplano_lista': s2299_infoperapur_detplano_lista,    
            's2299_infoperapur_infoagnocivo_lista': s2299_infoperapur_infoagnocivo_lista,    
            's2299_infoperapur_infosimples_lista': s2299_infoperapur_infosimples_lista,    
            's2299_infoperant_lista': s2299_infoperant_lista,    
            's2299_infoperant_ideadc_lista': s2299_infoperant_ideadc_lista,    
            's2299_infoperant_ideperiodo_lista': s2299_infoperant_ideperiodo_lista,    
            's2299_infoperant_ideestablot_lista': s2299_infoperant_ideestablot_lista,    
            's2299_infoperant_detverbas_lista': s2299_infoperant_detverbas_lista,    
            's2299_infoperant_infoagnocivo_lista': s2299_infoperant_infoagnocivo_lista,    
            's2299_infoperant_infosimples_lista': s2299_infoperant_infosimples_lista,    
            's2299_infotrabinterm_lista': s2299_infotrabinterm_lista,    
            's2299_infotrabinterm_procjudtrab_lista': s2299_infotrabinterm_procjudtrab_lista,    
            's2299_infotrabinterm_infomv_lista': s2299_infotrabinterm_infomv_lista,    
            's2299_infotrabinterm_remunoutrempr_lista': s2299_infotrabinterm_remunoutrempr_lista,    
            's2299_infotrabinterm_proccs_lista': s2299_infotrabinterm_proccs_lista,    
            's2299_infotrabinterm_quarentena_lista': s2299_infotrabinterm_quarentena_lista,    
            's2299_infotrabinterm_consigfgts_lista': s2299_infotrabinterm_consigfgts_lista,
        }
        #return render(request, 'xml/%s/s2299_evtdeslig.html' % s2299_evtdeslig.versao, context, content_type='text/xml')
        t = get_template('%s/s2299_evtdeslig_xml.html' % s2299_evtdeslig.versao)
        xml = t.render(context)
        xml_assinado = assinar(xml)
        return xml_assinado


def recibo(request, hash, slug=0):
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageria'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.session['usuario_id']   
        dict_hash = get_hash_url( hash )
        s2299_evtdeslig_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2299_evtdeslig')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2299_evtdeslig = get_object_or_404(s2299evtDeslig.objects.using( db_slug ), excluido = False, id = s2299_evtdeslig_id)
        ocorrencias_lista = s2299evtDesligOcorrencias.objects.using( db_slug ).filter(evento_id=s2299_evtdeslig_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's2299_evtdeslig_id': s2299_evtdeslig_id, 
            's2299_evtdeslig': s2299_evtdeslig, 
            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }
        return render(request, 's2299_evtdeslig_recibo.html', context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)


def gerar_xml(request, hash, slug=0):
    from django.http import HttpResponse
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageria'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    dict_hash = get_hash_url( hash )
    s2299_evtdeslig_id = int(dict_hash['id'])
    if s2299_evtdeslig_id:
        xml = gerar_xml_s2299(s2299_evtdeslig_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



