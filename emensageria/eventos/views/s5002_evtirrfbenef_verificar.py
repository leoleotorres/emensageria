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
from emensageria.s5002.models import *
from emensageria.s5002.forms import *


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
        s5002_evtirrfbenef_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5002_evtirrfbenef')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef.objects.using( db_slug ), excluido = False, id = s5002_evtirrfbenef_id)
        s5002_evtirrfbenef_lista = s5002evtIrrfBenef.objects.using( db_slug ).filter(id=s5002_evtirrfbenef_id, excluido = False).all()
        ocorrencias_lista = s5002evtIrrfBenefOcorrencias.objects.using( db_slug ).filter(evento_id=s5002_evtirrfbenef_id, excluido = False).all()

    
        s5002_infodep_lista = s5002infoDep.objects.using(db_slug).filter(s5002_evtirrfbenef_id__in = listar_ids(s5002_evtirrfbenef_lista) ).filter(excluido=False).all()    
        s5002_infoirrf_lista = s5002infoIrrf.objects.using(db_slug).filter(s5002_evtirrfbenef_id__in = listar_ids(s5002_evtirrfbenef_lista) ).filter(excluido=False).all()    
        s5002_basesirrf_lista = s5002basesIrrf.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()    
        s5002_irrf_lista = s5002irrf.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()    
        s5002_idepgtoext_lista = s5002idePgtoExt.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's5002_evtirrfbenef'
        context = {
            's5002_evtirrfbenef_lista': s5002_evtirrfbenef_lista,
            's5002_evtirrfbenef_id': s5002_evtirrfbenef_id, 
            's5002_evtirrfbenef': s5002_evtirrfbenef, 
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
    
            's5002_infodep_lista': s5002_infodep_lista,    
            's5002_infoirrf_lista': s5002_infoirrf_lista,    
            's5002_basesirrf_lista': s5002_basesirrf_lista,    
            's5002_irrf_lista': s5002_irrf_lista,    
            's5002_idepgtoext_lista': s5002_idepgtoext_lista,
        }
        return render(request, '%s/s5002_evtirrfbenef_verificar.html' % s5002_evtirrfbenef.versao, context)
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



def gerar_xml_s5002(s5002_evtirrfbenef_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s5002_evtirrfbenef_id:
        s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef.objects.using( db_slug ), excluido = False, id = s5002_evtirrfbenef_id)
        s5002_evtirrfbenef_lista = s5002evtIrrfBenef.objects.using( db_slug ).filter(id=s5002_evtirrfbenef_id, excluido = False).all()
    
        s5002_infodep_lista = s5002infoDep.objects.using(db_slug).filter(s5002_evtirrfbenef_id__in = listar_ids(s5002_evtirrfbenef_lista) ).filter(excluido=False).all()    
        s5002_infoirrf_lista = s5002infoIrrf.objects.using(db_slug).filter(s5002_evtirrfbenef_id__in = listar_ids(s5002_evtirrfbenef_lista) ).filter(excluido=False).all()    
        s5002_basesirrf_lista = s5002basesIrrf.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()    
        s5002_irrf_lista = s5002irrf.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()    
        s5002_idepgtoext_lista = s5002idePgtoExt.objects.using(db_slug).filter(s5002_infoirrf_id__in = listar_ids(s5002_infoirrf_lista) ).filter(excluido=False).all()
        context = {
            'base': s5002_evtirrfbenef,
            's5002_evtirrfbenef_lista': s5002_evtirrfbenef_lista,
            's5002_evtirrfbenef_id': int(s5002_evtirrfbenef_id), 
            's5002_evtirrfbenef': s5002_evtirrfbenef,
    
            's5002_infodep_lista': s5002_infodep_lista,    
            's5002_infoirrf_lista': s5002_infoirrf_lista,    
            's5002_basesirrf_lista': s5002_basesirrf_lista,    
            's5002_irrf_lista': s5002_irrf_lista,    
            's5002_idepgtoext_lista': s5002_idepgtoext_lista,
        }
        #return render(request, 'xml/%s/s5002_evtirrfbenef.html' % s5002_evtirrfbenef.versao, context, content_type='text/xml')
        t = get_template('%s/s5002_evtirrfbenef_xml.html' % s5002_evtirrfbenef.versao)
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
        s5002_evtirrfbenef_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s5002_evtirrfbenef')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s5002_evtirrfbenef = get_object_or_404(s5002evtIrrfBenef.objects.using( db_slug ), excluido = False, id = s5002_evtirrfbenef_id)
        ocorrencias_lista = s5002evtIrrfBenefOcorrencias.objects.using( db_slug ).filter(evento_id=s5002_evtirrfbenef_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's5002_evtirrfbenef_id': s5002_evtirrfbenef_id, 
            's5002_evtirrfbenef': s5002_evtirrfbenef, 
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
        return render(request, 's5002_evtirrfbenef_recibo.html', context)
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
    s5002_evtirrfbenef_id = int(dict_hash['id'])
    if s5002_evtirrfbenef_id:
        xml = gerar_xml_s5002(s5002_evtirrfbenef_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



