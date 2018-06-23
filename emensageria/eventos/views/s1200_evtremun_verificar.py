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
from emensageria.s1200.models import *
from emensageria.s1200.forms import *


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
        s1200_evtremun_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1200_evtremun')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1200_evtremun = get_object_or_404(s1200evtRemun.objects.using( db_slug ), excluido = False, id = s1200_evtremun_id)
        s1200_evtremun_lista = s1200evtRemun.objects.using( db_slug ).filter(id=s1200_evtremun_id, excluido = False).all()
        ocorrencias_lista = s1200evtRemunOcorrencias.objects.using( db_slug ).filter(evento_id=s1200_evtremun_id, excluido = False).all()

    
        s1200_infomv_lista = s1200infoMV.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_remunoutrempr_lista = s1200remunOutrEmpr.objects.using(db_slug).filter(s1200_infomv_id__in = listar_ids(s1200_infomv_lista) ).filter(excluido=False).all()    
        s1200_infocomplem_lista = s1200infoComplem.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_sucessaovinc_lista = s1200sucessaoVinc.objects.using(db_slug).filter(s1200_infocomplem_id__in = listar_ids(s1200_infocomplem_lista) ).filter(excluido=False).all()    
        s1200_procjudtrab_lista = s1200procJudTrab.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_infointerm_lista = s1200infoInterm.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_dmdev_lista = s1200dmDev.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_lista = s1200infoPerApur.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_ideestablot_lista = s1200infoPerApurideEstabLot.objects.using(db_slug).filter(s1200_infoperapur_id__in = listar_ids(s1200_infoperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_remunperapur_lista = s1200infoPerApurremunPerApur.objects.using(db_slug).filter(s1200_infoperapur_ideestablot_id__in = listar_ids(s1200_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_itensremun_lista = s1200infoPerApuritensRemun.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infosaudecolet_lista = s1200infoPerApurinfoSaudeColet.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_detoper_lista = s1200infoPerApurdetOper.objects.using(db_slug).filter(s1200_infoperapur_infosaudecolet_id__in = listar_ids(s1200_infoperapur_infosaudecolet_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_detplano_lista = s1200infoPerApurdetPlano.objects.using(db_slug).filter(s1200_infoperapur_detoper_id__in = listar_ids(s1200_infoperapur_detoper_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infoagnocivo_lista = s1200infoPerApurinfoAgNocivo.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infotrabinterm_lista = s1200infoPerApurinfoTrabInterm.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperant_lista = s1200infoPerAnt.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideadc_lista = s1200infoPerAntideADC.objects.using(db_slug).filter(s1200_infoperant_id__in = listar_ids(s1200_infoperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideperiodo_lista = s1200infoPerAntidePeriodo.objects.using(db_slug).filter(s1200_infoperant_ideadc_id__in = listar_ids(s1200_infoperant_ideadc_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideestablot_lista = s1200infoPerAntideEstabLot.objects.using(db_slug).filter(s1200_infoperant_ideperiodo_id__in = listar_ids(s1200_infoperant_ideperiodo_lista) ).filter(excluido=False).all()    
        s1200_infoperant_remunperant_lista = s1200infoPerAntremunPerAnt.objects.using(db_slug).filter(s1200_infoperant_ideestablot_id__in = listar_ids(s1200_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s1200_infoperant_itensremun_lista = s1200infoPerAntitensRemun.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infoagnocivo_lista = s1200infoPerAntinfoAgNocivo.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infotrabinterm_lista = s1200infoPerAntinfoTrabInterm.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infocomplcont_lista = s1200infoPerAntinfoComplCont.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1200_evtremun'
        context = {
            's1200_evtremun_lista': s1200_evtremun_lista,
            's1200_evtremun_id': s1200_evtremun_id, 
            's1200_evtremun': s1200_evtremun, 
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
    
            's1200_infomv_lista': s1200_infomv_lista,    
            's1200_remunoutrempr_lista': s1200_remunoutrempr_lista,    
            's1200_infocomplem_lista': s1200_infocomplem_lista,    
            's1200_sucessaovinc_lista': s1200_sucessaovinc_lista,    
            's1200_procjudtrab_lista': s1200_procjudtrab_lista,    
            's1200_infointerm_lista': s1200_infointerm_lista,    
            's1200_dmdev_lista': s1200_dmdev_lista,    
            's1200_infoperapur_lista': s1200_infoperapur_lista,    
            's1200_infoperapur_ideestablot_lista': s1200_infoperapur_ideestablot_lista,    
            's1200_infoperapur_remunperapur_lista': s1200_infoperapur_remunperapur_lista,    
            's1200_infoperapur_itensremun_lista': s1200_infoperapur_itensremun_lista,    
            's1200_infoperapur_infosaudecolet_lista': s1200_infoperapur_infosaudecolet_lista,    
            's1200_infoperapur_detoper_lista': s1200_infoperapur_detoper_lista,    
            's1200_infoperapur_detplano_lista': s1200_infoperapur_detplano_lista,    
            's1200_infoperapur_infoagnocivo_lista': s1200_infoperapur_infoagnocivo_lista,    
            's1200_infoperapur_infotrabinterm_lista': s1200_infoperapur_infotrabinterm_lista,    
            's1200_infoperant_lista': s1200_infoperant_lista,    
            's1200_infoperant_ideadc_lista': s1200_infoperant_ideadc_lista,    
            's1200_infoperant_ideperiodo_lista': s1200_infoperant_ideperiodo_lista,    
            's1200_infoperant_ideestablot_lista': s1200_infoperant_ideestablot_lista,    
            's1200_infoperant_remunperant_lista': s1200_infoperant_remunperant_lista,    
            's1200_infoperant_itensremun_lista': s1200_infoperant_itensremun_lista,    
            's1200_infoperant_infoagnocivo_lista': s1200_infoperant_infoagnocivo_lista,    
            's1200_infoperant_infotrabinterm_lista': s1200_infoperant_infotrabinterm_lista,    
            's1200_infoperant_infocomplcont_lista': s1200_infoperant_infocomplcont_lista,
        }
        return render(request, '%s/s1200_evtremun_verificar.html' % s1200_evtremun.versao, context)
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



def gerar_xml_s1200(s1200_evtremun_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s1200_evtremun_id:
        s1200_evtremun = get_object_or_404(s1200evtRemun.objects.using( db_slug ), excluido = False, id = s1200_evtremun_id)
        s1200_evtremun_lista = s1200evtRemun.objects.using( db_slug ).filter(id=s1200_evtremun_id, excluido = False).all()
    
        s1200_infomv_lista = s1200infoMV.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_remunoutrempr_lista = s1200remunOutrEmpr.objects.using(db_slug).filter(s1200_infomv_id__in = listar_ids(s1200_infomv_lista) ).filter(excluido=False).all()    
        s1200_infocomplem_lista = s1200infoComplem.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_sucessaovinc_lista = s1200sucessaoVinc.objects.using(db_slug).filter(s1200_infocomplem_id__in = listar_ids(s1200_infocomplem_lista) ).filter(excluido=False).all()    
        s1200_procjudtrab_lista = s1200procJudTrab.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_infointerm_lista = s1200infoInterm.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_dmdev_lista = s1200dmDev.objects.using(db_slug).filter(s1200_evtremun_id__in = listar_ids(s1200_evtremun_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_lista = s1200infoPerApur.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_ideestablot_lista = s1200infoPerApurideEstabLot.objects.using(db_slug).filter(s1200_infoperapur_id__in = listar_ids(s1200_infoperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_remunperapur_lista = s1200infoPerApurremunPerApur.objects.using(db_slug).filter(s1200_infoperapur_ideestablot_id__in = listar_ids(s1200_infoperapur_ideestablot_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_itensremun_lista = s1200infoPerApuritensRemun.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infosaudecolet_lista = s1200infoPerApurinfoSaudeColet.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_detoper_lista = s1200infoPerApurdetOper.objects.using(db_slug).filter(s1200_infoperapur_infosaudecolet_id__in = listar_ids(s1200_infoperapur_infosaudecolet_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_detplano_lista = s1200infoPerApurdetPlano.objects.using(db_slug).filter(s1200_infoperapur_detoper_id__in = listar_ids(s1200_infoperapur_detoper_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infoagnocivo_lista = s1200infoPerApurinfoAgNocivo.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperapur_infotrabinterm_lista = s1200infoPerApurinfoTrabInterm.objects.using(db_slug).filter(s1200_infoperapur_remunperapur_id__in = listar_ids(s1200_infoperapur_remunperapur_lista) ).filter(excluido=False).all()    
        s1200_infoperant_lista = s1200infoPerAnt.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideadc_lista = s1200infoPerAntideADC.objects.using(db_slug).filter(s1200_infoperant_id__in = listar_ids(s1200_infoperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideperiodo_lista = s1200infoPerAntidePeriodo.objects.using(db_slug).filter(s1200_infoperant_ideadc_id__in = listar_ids(s1200_infoperant_ideadc_lista) ).filter(excluido=False).all()    
        s1200_infoperant_ideestablot_lista = s1200infoPerAntideEstabLot.objects.using(db_slug).filter(s1200_infoperant_ideperiodo_id__in = listar_ids(s1200_infoperant_ideperiodo_lista) ).filter(excluido=False).all()    
        s1200_infoperant_remunperant_lista = s1200infoPerAntremunPerAnt.objects.using(db_slug).filter(s1200_infoperant_ideestablot_id__in = listar_ids(s1200_infoperant_ideestablot_lista) ).filter(excluido=False).all()    
        s1200_infoperant_itensremun_lista = s1200infoPerAntitensRemun.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infoagnocivo_lista = s1200infoPerAntinfoAgNocivo.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infotrabinterm_lista = s1200infoPerAntinfoTrabInterm.objects.using(db_slug).filter(s1200_infoperant_remunperant_id__in = listar_ids(s1200_infoperant_remunperant_lista) ).filter(excluido=False).all()    
        s1200_infoperant_infocomplcont_lista = s1200infoPerAntinfoComplCont.objects.using(db_slug).filter(s1200_dmdev_id__in = listar_ids(s1200_dmdev_lista) ).filter(excluido=False).all()
        context = {
            'base': s1200_evtremun,
            's1200_evtremun_lista': s1200_evtremun_lista,
            's1200_evtremun_id': int(s1200_evtremun_id), 
            's1200_evtremun': s1200_evtremun,
    
            's1200_infomv_lista': s1200_infomv_lista,    
            's1200_remunoutrempr_lista': s1200_remunoutrempr_lista,    
            's1200_infocomplem_lista': s1200_infocomplem_lista,    
            's1200_sucessaovinc_lista': s1200_sucessaovinc_lista,    
            's1200_procjudtrab_lista': s1200_procjudtrab_lista,    
            's1200_infointerm_lista': s1200_infointerm_lista,    
            's1200_dmdev_lista': s1200_dmdev_lista,    
            's1200_infoperapur_lista': s1200_infoperapur_lista,    
            's1200_infoperapur_ideestablot_lista': s1200_infoperapur_ideestablot_lista,    
            's1200_infoperapur_remunperapur_lista': s1200_infoperapur_remunperapur_lista,    
            's1200_infoperapur_itensremun_lista': s1200_infoperapur_itensremun_lista,    
            's1200_infoperapur_infosaudecolet_lista': s1200_infoperapur_infosaudecolet_lista,    
            's1200_infoperapur_detoper_lista': s1200_infoperapur_detoper_lista,    
            's1200_infoperapur_detplano_lista': s1200_infoperapur_detplano_lista,    
            's1200_infoperapur_infoagnocivo_lista': s1200_infoperapur_infoagnocivo_lista,    
            's1200_infoperapur_infotrabinterm_lista': s1200_infoperapur_infotrabinterm_lista,    
            's1200_infoperant_lista': s1200_infoperant_lista,    
            's1200_infoperant_ideadc_lista': s1200_infoperant_ideadc_lista,    
            's1200_infoperant_ideperiodo_lista': s1200_infoperant_ideperiodo_lista,    
            's1200_infoperant_ideestablot_lista': s1200_infoperant_ideestablot_lista,    
            's1200_infoperant_remunperant_lista': s1200_infoperant_remunperant_lista,    
            's1200_infoperant_itensremun_lista': s1200_infoperant_itensremun_lista,    
            's1200_infoperant_infoagnocivo_lista': s1200_infoperant_infoagnocivo_lista,    
            's1200_infoperant_infotrabinterm_lista': s1200_infoperant_infotrabinterm_lista,    
            's1200_infoperant_infocomplcont_lista': s1200_infoperant_infocomplcont_lista,
        }
        #return render(request, 'xml/%s/s1200_evtremun.html' % s1200_evtremun.versao, context, content_type='text/xml')
        t = get_template('%s/s1200_evtremun_xml.html' % s1200_evtremun.versao)
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
        s1200_evtremun_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1200_evtremun')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1200_evtremun = get_object_or_404(s1200evtRemun.objects.using( db_slug ), excluido = False, id = s1200_evtremun_id)
        ocorrencias_lista = s1200evtRemunOcorrencias.objects.using( db_slug ).filter(evento_id=s1200_evtremun_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's1200_evtremun_id': s1200_evtremun_id, 
            's1200_evtremun': s1200_evtremun, 
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
        return render(request, 's1200_evtremun_recibo.html', context)
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
    s1200_evtremun_id = int(dict_hash['id'])
    if s1200_evtremun_id:
        xml = gerar_xml_s1200(s1200_evtremun_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



