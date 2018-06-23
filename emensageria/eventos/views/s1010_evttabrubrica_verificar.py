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
from emensageria.s1010.models import *
from emensageria.s1010.forms import *


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
        s1010_evttabrubrica_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1010_evttabrubrica')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1010_evttabrubrica = get_object_or_404(s1010evtTabRubrica.objects.using( db_slug ), excluido = False, id = s1010_evttabrubrica_id)
        s1010_evttabrubrica_lista = s1010evtTabRubrica.objects.using( db_slug ).filter(id=s1010_evttabrubrica_id, excluido = False).all()
        ocorrencias_lista = s1010evtTabRubricaOcorrencias.objects.using( db_slug ).filter(evento_id=s1010_evttabrubrica_id, excluido = False).all()

    
        s1010_inclusao_lista = s1010inclusao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessocp_lista = s1010inclusaoideProcessoCP.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessoirrf_lista = s1010inclusaoideProcessoIRRF.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessofgts_lista = s1010inclusaoideProcessoFGTS.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessosind_lista = s1010inclusaoideProcessoSIND.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_lista = s1010alteracao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessocp_lista = s1010alteracaoideProcessoCP.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessoirrf_lista = s1010alteracaoideProcessoIRRF.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessofgts_lista = s1010alteracaoideProcessoFGTS.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessosind_lista = s1010alteracaoideProcessoSIND.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_novavalidade_lista = s1010alteracaonovaValidade.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_exclusao_lista = s1010exclusao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1010_evttabrubrica'
        context = {
            's1010_evttabrubrica_lista': s1010_evttabrubrica_lista,
            's1010_evttabrubrica_id': s1010_evttabrubrica_id, 
            's1010_evttabrubrica': s1010_evttabrubrica, 
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
    
            's1010_inclusao_lista': s1010_inclusao_lista,    
            's1010_inclusao_ideprocessocp_lista': s1010_inclusao_ideprocessocp_lista,    
            's1010_inclusao_ideprocessoirrf_lista': s1010_inclusao_ideprocessoirrf_lista,    
            's1010_inclusao_ideprocessofgts_lista': s1010_inclusao_ideprocessofgts_lista,    
            's1010_inclusao_ideprocessosind_lista': s1010_inclusao_ideprocessosind_lista,    
            's1010_alteracao_lista': s1010_alteracao_lista,    
            's1010_alteracao_ideprocessocp_lista': s1010_alteracao_ideprocessocp_lista,    
            's1010_alteracao_ideprocessoirrf_lista': s1010_alteracao_ideprocessoirrf_lista,    
            's1010_alteracao_ideprocessofgts_lista': s1010_alteracao_ideprocessofgts_lista,    
            's1010_alteracao_ideprocessosind_lista': s1010_alteracao_ideprocessosind_lista,    
            's1010_alteracao_novavalidade_lista': s1010_alteracao_novavalidade_lista,    
            's1010_exclusao_lista': s1010_exclusao_lista,
        }
        return render(request, '%s/s1010_evttabrubrica_verificar.html' % s1010_evttabrubrica.versao, context)
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



def gerar_xml_s1010(s1010_evttabrubrica_id, db_slug):
    from emensageria.funcoes_esocial import assinar
    from django.template.loader import get_template
    if s1010_evttabrubrica_id:
        s1010_evttabrubrica = get_object_or_404(s1010evtTabRubrica.objects.using( db_slug ), excluido = False, id = s1010_evttabrubrica_id)
        s1010_evttabrubrica_lista = s1010evtTabRubrica.objects.using( db_slug ).filter(id=s1010_evttabrubrica_id, excluido = False).all()
    
        s1010_inclusao_lista = s1010inclusao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessocp_lista = s1010inclusaoideProcessoCP.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessoirrf_lista = s1010inclusaoideProcessoIRRF.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessofgts_lista = s1010inclusaoideProcessoFGTS.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_inclusao_ideprocessosind_lista = s1010inclusaoideProcessoSIND.objects.using(db_slug).filter(s1010_inclusao_id__in = listar_ids(s1010_inclusao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_lista = s1010alteracao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessocp_lista = s1010alteracaoideProcessoCP.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessoirrf_lista = s1010alteracaoideProcessoIRRF.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessofgts_lista = s1010alteracaoideProcessoFGTS.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_ideprocessosind_lista = s1010alteracaoideProcessoSIND.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_alteracao_novavalidade_lista = s1010alteracaonovaValidade.objects.using(db_slug).filter(s1010_alteracao_id__in = listar_ids(s1010_alteracao_lista) ).filter(excluido=False).all()    
        s1010_exclusao_lista = s1010exclusao.objects.using(db_slug).filter(s1010_evttabrubrica_id__in = listar_ids(s1010_evttabrubrica_lista) ).filter(excluido=False).all()
        context = {
            'base': s1010_evttabrubrica,
            's1010_evttabrubrica_lista': s1010_evttabrubrica_lista,
            's1010_evttabrubrica_id': int(s1010_evttabrubrica_id), 
            's1010_evttabrubrica': s1010_evttabrubrica,
    
            's1010_inclusao_lista': s1010_inclusao_lista,    
            's1010_inclusao_ideprocessocp_lista': s1010_inclusao_ideprocessocp_lista,    
            's1010_inclusao_ideprocessoirrf_lista': s1010_inclusao_ideprocessoirrf_lista,    
            's1010_inclusao_ideprocessofgts_lista': s1010_inclusao_ideprocessofgts_lista,    
            's1010_inclusao_ideprocessosind_lista': s1010_inclusao_ideprocessosind_lista,    
            's1010_alteracao_lista': s1010_alteracao_lista,    
            's1010_alteracao_ideprocessocp_lista': s1010_alteracao_ideprocessocp_lista,    
            's1010_alteracao_ideprocessoirrf_lista': s1010_alteracao_ideprocessoirrf_lista,    
            's1010_alteracao_ideprocessofgts_lista': s1010_alteracao_ideprocessofgts_lista,    
            's1010_alteracao_ideprocessosind_lista': s1010_alteracao_ideprocessosind_lista,    
            's1010_alteracao_novavalidade_lista': s1010_alteracao_novavalidade_lista,    
            's1010_exclusao_lista': s1010_exclusao_lista,
        }
        #return render(request, 'xml/%s/s1010_evttabrubrica.html' % s1010_evttabrubrica.versao, context, content_type='text/xml')
        t = get_template('%s/s1010_evttabrubrica_xml.html' % s1010_evttabrubrica.versao)
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
        s1010_evttabrubrica_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login', slug=slug)
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1010_evttabrubrica')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1010_evttabrubrica = get_object_or_404(s1010evtTabRubrica.objects.using( db_slug ), excluido = False, id = s1010_evttabrubrica_id)
        ocorrencias_lista = s1010evtTabRubricaOcorrencias.objects.using( db_slug ).filter(evento_id=s1010_evttabrubrica_id, excluido = False).all()

        context = {
            'ocorrencias_lista': ocorrencias_lista,
            's1010_evttabrubrica_id': s1010_evttabrubrica_id, 
            's1010_evttabrubrica': s1010_evttabrubrica, 
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
        return render(request, 's1010_evttabrubrica_recibo.html', context)
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
    s1010_evttabrubrica_id = int(dict_hash['id'])
    if s1010_evttabrubrica_id:
        xml = gerar_xml_s1010(s1010_evttabrubrica_id, db_slug)
        return HttpResponse(xml, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



