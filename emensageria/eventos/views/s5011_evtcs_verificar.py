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
from emensageria.s5011.models import *
from emensageria.s5011.forms import *


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
        s5011_evtcs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
        s5011_evtcs_lista = s5011evtCS.objects.using( db_slug ).filter(id=s5011_evtcs_id, excluido = False).all()
        ocorrencias_lista = s5011evtCSOcorrencias.objects.using( db_slug ).filter(evento_id=s5011_evtcs_id, excluido = False).all()

    
        s5011_infocpseg_lista = s5011infoCPSeg.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infopj_lista = s5011infoPJ.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infoatconc_lista = s5011infoAtConc.objects.using(db_slug).filter(s5011_infopj_id__in = listar_ids(s5011_infopj_lista) ).filter(excluido=False).all()    
        s5011_ideestab_lista = s5011ideEstab.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infoestab_lista = s5011infoEstab.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocomplobra_lista = s5011infoComplObra.objects.using(db_slug).filter(s5011_infoestab_id__in = listar_ids(s5011_infoestab_lista) ).filter(excluido=False).all()    
        s5011_idelotacao_lista = s5011ideLotacao.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infotercsusp_lista = s5011infoTercSusp.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_dadosopport_lista = s5011dadosOpPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesremun_lista = s5011basesRemun.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesavnport_lista = s5011basesAvNPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesaquis_lista = s5011basesAquis.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_basescomerc_lista = s5011basesComerc.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocrestab_lista = s5011infoCREstab.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocrcontrib_lista = s5011infoCRContrib.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5011_evtcs'
        context = {
            's5011_evtcs_lista': s5011_evtcs_lista,
            's5011_evtcs_id': s5011_evtcs_id, 
            's5011_evtcs': s5011_evtcs, 
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
    
            's5011_infocpseg_lista': s5011_infocpseg_lista,    
            's5011_infopj_lista': s5011_infopj_lista,    
            's5011_infoatconc_lista': s5011_infoatconc_lista,    
            's5011_ideestab_lista': s5011_ideestab_lista,    
            's5011_infoestab_lista': s5011_infoestab_lista,    
            's5011_infocomplobra_lista': s5011_infocomplobra_lista,    
            's5011_idelotacao_lista': s5011_idelotacao_lista,    
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,    
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,    
            's5011_dadosopport_lista': s5011_dadosopport_lista,    
            's5011_basesremun_lista': s5011_basesremun_lista,    
            's5011_basesavnport_lista': s5011_basesavnport_lista,    
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,    
            's5011_basesaquis_lista': s5011_basesaquis_lista,    
            's5011_basescomerc_lista': s5011_basescomerc_lista,    
            's5011_infocrestab_lista': s5011_infocrestab_lista,    
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
        }
        return render(request, '%s/s5011_evtcs_verificar.html' % s5011_evtcs.versao, context)
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



def gerar_xml_s5011(s5011_evtcs_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s5011_evtcs_id:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
        s5011_evtcs_lista = s5011evtCS.objects.using( db_slug ).filter(id=s5011_evtcs_id, excluido = False).all()
    
        s5011_infocpseg_lista = s5011infoCPSeg.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infopj_lista = s5011infoPJ.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infoatconc_lista = s5011infoAtConc.objects.using(db_slug).filter(s5011_infopj_id__in = listar_ids(s5011_infopj_lista) ).filter(excluido=False).all()    
        s5011_ideestab_lista = s5011ideEstab.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()    
        s5011_infoestab_lista = s5011infoEstab.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocomplobra_lista = s5011infoComplObra.objects.using(db_slug).filter(s5011_infoestab_id__in = listar_ids(s5011_infoestab_lista) ).filter(excluido=False).all()    
        s5011_idelotacao_lista = s5011ideLotacao.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infotercsusp_lista = s5011infoTercSusp.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_dadosopport_lista = s5011dadosOpPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesremun_lista = s5011basesRemun.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesavnport_lista = s5011basesAvNPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.using(db_slug).filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).filter(excluido=False).all()    
        s5011_basesaquis_lista = s5011basesAquis.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_basescomerc_lista = s5011basesComerc.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocrestab_lista = s5011infoCREstab.objects.using(db_slug).filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).filter(excluido=False).all()    
        s5011_infocrcontrib_lista = s5011infoCRContrib.objects.using(db_slug).filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).filter(excluido=False).all()
        context = {
            'base': s5011_evtcs,
            's5011_evtcs_lista': s5011_evtcs_lista,
            's5011_evtcs_id': int(s5011_evtcs_id), 
            's5011_evtcs': s5011_evtcs,
    
            's5011_infocpseg_lista': s5011_infocpseg_lista,    
            's5011_infopj_lista': s5011_infopj_lista,    
            's5011_infoatconc_lista': s5011_infoatconc_lista,    
            's5011_ideestab_lista': s5011_ideestab_lista,    
            's5011_infoestab_lista': s5011_infoestab_lista,    
            's5011_infocomplobra_lista': s5011_infocomplobra_lista,    
            's5011_idelotacao_lista': s5011_idelotacao_lista,    
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,    
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,    
            's5011_dadosopport_lista': s5011_dadosopport_lista,    
            's5011_basesremun_lista': s5011_basesremun_lista,    
            's5011_basesavnport_lista': s5011_basesavnport_lista,    
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,    
            's5011_basesaquis_lista': s5011_basesaquis_lista,    
            's5011_basescomerc_lista': s5011_basescomerc_lista,    
            's5011_infocrestab_lista': s5011_infocrestab_lista,    
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
        }
        #return render(request, 'xml/%s/s5011_evtcs.html' % s5011_evtcs.versao, context, content_type='text/xml')
        t = get_template('%s/s5011_evtcs_xml.html' % s5011_evtcs.versao)
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
        s5011_evtcs_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5011_evtcs')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5011_evtcs = get_object_or_404(s5011evtCS.objects.using( db_slug ), excluido = False, id = s5011_evtcs_id)
        ocorrencias_lista = s5011evtCSOcorrencias.objects.using( db_slug ).filter(evento_id=s5011_evtcs_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's5011_evtcs_id': s5011_evtcs_id, 
            's5011_evtcs': s5011_evtcs, 
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
        return render(request, 's5011_evtcs_recibo.html', context)
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
    s5011_evtcs_id = int(dict_hash['id'])
    if s5011_evtcs_id:
        xml = gerar_xml_s5011(s5011_evtcs_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



