#coding: utf-8

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageria.padrao import *
from emensageria.funcoes_esocial import *
from emensageria.mensageiro.forms import *
from emensageria.mensageiro.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas


#IMPORTACOES




def enviar(request, hash):
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
    a = send_xml(transmissor_lote_id, 'WsEnviarLoteEventos')
    if 'HTTP/1.1 200 OK' in a:
        messages.success(request, 'Lote enviado com sucesso!')
    else:
        messages.error(request, 'Erro no envio do Lote de Eventos! %s' % a)
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])


def consultar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        transmissor_lote_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='transmissor_lote')
    a = send_xml(transmissor_lote_id, 'WsConsultarLoteEventos')
    if 'HTTP/1.1 200 OK' in a:
        messages.success(request, 'Lote consultado com sucesso!')
    else:
        messages.error(request, 'Erro na consulta do Lote de Eventos! %s' % a)
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])


def recibo(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url(hash)
        transmissor_lote_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using(db_slug), excluido=False, id=usuario_id)
    pagina = ConfigPaginas.objects.using(db_slug).get(excluido=False, endereco='transmissor_lote')
    permissao = ConfigPermissoes.objects.using(db_slug).get(excluido=False, config_paginas=pagina,
                                                            config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote = get_object_or_404(TransmissorLote.objects.using(db_slug), excluido=False, id=transmissor_lote_id)
    ocorrencias_lista = TransmissorLoteOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_id=transmissor_lote.id).all()
    eventos_lista = TransmissorEventos.objects.using( db_slug ).filter(excluido = False, transmissor_lote_id=transmissor_lote.id).all()

    context = {
        'eventos_lista': eventos_lista,
        'ocorrencias_lista': ocorrencias_lista,
        'transmissor_lote': transmissor_lote,
        'transmissor_lote_id': int(transmissor_lote_id),
        'usuario': usuario,

        'hash': hash,
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'for_print': int(dict_hash['print']),
        #'transmissor_eventos_lista': transmissor_eventos_lista,
        #'transmissor_ocorrencias_lista': transmissor_ocorrencias_lista,
    }
    return render(request, 'transmissor_lote_recibo.html', context)



def scripts_enviar_lote(request, chave, transmissor_lote_id):
    from emensageria.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        transmissor_lote = get_object_or_404(TransmissorLote.objects.using(db_slug), excluido=False, id=transmissor_lote_id)
        a = send_xml(transmissor_lote_id, 'WsEnviarLoteEventos')
        if 'HTTP/1.1 200 OK' in a:
            mensagem = 'Lote enviado com sucesso!'
        else:
            mensagem = 'Erro no envio do Lote de Eventos! %s' % a
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


def scripts_consultar_lote(request, chave, transmissor_lote_id):
    from emensageria.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        transmissor_lote = get_object_or_404(TransmissorLote.objects.using(db_slug), excluido=False, id=transmissor_lote_id)
        a = send_xml(transmissor_lote_id, 'WsConsultarLoteEventos')
        if 'HTTP/1.1 200 OK' in a:
            mensagem = 'Lote consultado com sucesso!'
        else:
            mensagem = 'Erro na consulta do Lote de Eventos! %s' % a
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)