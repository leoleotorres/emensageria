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
from emensageria.s2206.models import *
from emensageria.s2206.forms import *


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
        s2206_evtaltcontratual_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2206_evtaltcontratual')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2206_evtaltcontratual = get_object_or_404(s2206evtAltContratual.objects.using( db_slug ), excluido = False, id = s2206_evtaltcontratual_id)
        s2206_evtaltcontratual_lista = s2206evtAltContratual.objects.using( db_slug ).filter(id=s2206_evtaltcontratual_id, excluido = False).all()
        ocorrencias_lista = s2206evtAltContratualOcorrencias.objects.using( db_slug ).filter(evento_id=s2206_evtaltcontratual_id, excluido = False).all()

    
        s2206_infoceletista_lista = s2206infoCeletista.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_trabtemp_lista = s2206trabTemp.objects.using(db_slug).filter(s2206_infoceletista_id__in = listar_ids(s2206_infoceletista_lista) ).filter(excluido=False).all()    
        s2206_aprend_lista = s2206aprend.objects.using(db_slug).filter(s2206_infoceletista_id__in = listar_ids(s2206_infoceletista_lista) ).filter(excluido=False).all()    
        s2206_infoestatutario_lista = s2206infoEstatutario.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_localtrabgeral_lista = s2206localTrabGeral.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_localtrabdom_lista = s2206localTrabDom.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_horcontratual_lista = s2206horContratual.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_horario_lista = s2206horario.objects.using(db_slug).filter(s2206_horcontratual_id__in = listar_ids(s2206_horcontratual_lista) ).filter(excluido=False).all()    
        s2206_filiacaosindical_lista = s2206filiacaoSindical.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_alvarajudicial_lista = s2206alvaraJudicial.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_observacoes_lista = s2206observacoes.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_servpubl_lista = s2206servPubl.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2206_evtaltcontratual'
        context = {
            's2206_evtaltcontratual_lista': s2206_evtaltcontratual_lista,
            's2206_evtaltcontratual_id': s2206_evtaltcontratual_id, 
            's2206_evtaltcontratual': s2206_evtaltcontratual, 
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
    
            's2206_infoceletista_lista': s2206_infoceletista_lista,    
            's2206_trabtemp_lista': s2206_trabtemp_lista,    
            's2206_aprend_lista': s2206_aprend_lista,    
            's2206_infoestatutario_lista': s2206_infoestatutario_lista,    
            's2206_localtrabgeral_lista': s2206_localtrabgeral_lista,    
            's2206_localtrabdom_lista': s2206_localtrabdom_lista,    
            's2206_horcontratual_lista': s2206_horcontratual_lista,    
            's2206_horario_lista': s2206_horario_lista,    
            's2206_filiacaosindical_lista': s2206_filiacaosindical_lista,    
            's2206_alvarajudicial_lista': s2206_alvarajudicial_lista,    
            's2206_observacoes_lista': s2206_observacoes_lista,    
            's2206_servpubl_lista': s2206_servpubl_lista,
        }
        return render(request, '%s/s2206_evtaltcontratual_verificar.html' % s2206_evtaltcontratual.versao, context)
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



def gerar_xml_s2206(s2206_evtaltcontratual_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s2206_evtaltcontratual_id:
        s2206_evtaltcontratual = get_object_or_404(s2206evtAltContratual.objects.using( db_slug ), excluido = False, id = s2206_evtaltcontratual_id)
        s2206_evtaltcontratual_lista = s2206evtAltContratual.objects.using( db_slug ).filter(id=s2206_evtaltcontratual_id, excluido = False).all()
    
        s2206_infoceletista_lista = s2206infoCeletista.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_trabtemp_lista = s2206trabTemp.objects.using(db_slug).filter(s2206_infoceletista_id__in = listar_ids(s2206_infoceletista_lista) ).filter(excluido=False).all()    
        s2206_aprend_lista = s2206aprend.objects.using(db_slug).filter(s2206_infoceletista_id__in = listar_ids(s2206_infoceletista_lista) ).filter(excluido=False).all()    
        s2206_infoestatutario_lista = s2206infoEstatutario.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_localtrabgeral_lista = s2206localTrabGeral.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_localtrabdom_lista = s2206localTrabDom.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_horcontratual_lista = s2206horContratual.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_horario_lista = s2206horario.objects.using(db_slug).filter(s2206_horcontratual_id__in = listar_ids(s2206_horcontratual_lista) ).filter(excluido=False).all()    
        s2206_filiacaosindical_lista = s2206filiacaoSindical.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_alvarajudicial_lista = s2206alvaraJudicial.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_observacoes_lista = s2206observacoes.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()    
        s2206_servpubl_lista = s2206servPubl.objects.using(db_slug).filter(s2206_evtaltcontratual_id__in = listar_ids(s2206_evtaltcontratual_lista) ).filter(excluido=False).all()
        context = {
            'base': s2206_evtaltcontratual,
            's2206_evtaltcontratual_lista': s2206_evtaltcontratual_lista,
            's2206_evtaltcontratual_id': int(s2206_evtaltcontratual_id), 
            's2206_evtaltcontratual': s2206_evtaltcontratual,
    
            's2206_infoceletista_lista': s2206_infoceletista_lista,    
            's2206_trabtemp_lista': s2206_trabtemp_lista,    
            's2206_aprend_lista': s2206_aprend_lista,    
            's2206_infoestatutario_lista': s2206_infoestatutario_lista,    
            's2206_localtrabgeral_lista': s2206_localtrabgeral_lista,    
            's2206_localtrabdom_lista': s2206_localtrabdom_lista,    
            's2206_horcontratual_lista': s2206_horcontratual_lista,    
            's2206_horario_lista': s2206_horario_lista,    
            's2206_filiacaosindical_lista': s2206_filiacaosindical_lista,    
            's2206_alvarajudicial_lista': s2206_alvarajudicial_lista,    
            's2206_observacoes_lista': s2206_observacoes_lista,    
            's2206_servpubl_lista': s2206_servpubl_lista,
        }
        #return render(request, 'xml/%s/s2206_evtaltcontratual.html' % s2206_evtaltcontratual.versao, context, content_type='text/xml')
        t = get_template('%s/s2206_evtaltcontratual_xml.html' % s2206_evtaltcontratual.versao)
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
        s2206_evtaltcontratual_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2206_evtaltcontratual')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s2206_evtaltcontratual = get_object_or_404(s2206evtAltContratual.objects.using( db_slug ), excluido = False, id = s2206_evtaltcontratual_id)
        ocorrencias_lista = s2206evtAltContratualOcorrencias.objects.using( db_slug ).filter(evento_id=s2206_evtaltcontratual_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's2206_evtaltcontratual_id': s2206_evtaltcontratual_id, 
            's2206_evtaltcontratual': s2206_evtaltcontratual, 
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
        return render(request, 's2206_evtaltcontratual_recibo.html', context)
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
    s2206_evtaltcontratual_id = int(dict_hash['id'])
    if s2206_evtaltcontratual_id:
        xml = gerar_xml_s2206(s2206_evtaltcontratual_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



