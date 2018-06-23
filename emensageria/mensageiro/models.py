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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CODIGO_RESPOSTA = (
    (0, u'Cadastrado (Aguardando envio)'),
    (101, u'101 - Lote Aguardando Processamento'),
    (201, u'201 - Lote Processado com Sucesso'),
    (202, u'202 - Lote Processado com Advertências'),
    (301, u'301 - Erro Servidor eSocial'),
    (401, u'401 - Lote Incorreto - Erro preenchimento'),
    (402, u'402 - Lote Incorreto - schema Inválido'),
    (403, u'403 - Lote Incorreto - Versão do Schema não permitida'),
    (404, u'404 - Lote Incorreto - Erro Certificado'),
    (405, u'405 - Lote Incorreto - Lote nulo ou vazio'),
    (501, u'501 - Solicitação de Consulta Incorreta - Erro Preenchimento'),
    (502, u'502 - Solicitação de Consulta Incorreta - Schema Inválido.'),
    (503, u'503 - Solicitação de Consulta Incorreta - Versão do Schema Não Permitida.'),
    (504, u'504 - Solicitação de Consulta Incorreta - Erro Certificado.'),
    (505, u'505 - Solicitação de Consulta Incorreta - Consulta nula ou vazia.'),
)

TIPO_OCORRENCIA = (
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
)

EVENTOS_OCORRENCIAS_TIPO = (
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
)

EVENTOS_GRUPOS = (
    (1, u'1 - Eventos de Tabelas'),
    (2, u'2 - Eventos Não Periódicos'),
    (3, u'3 - Eventos Periódicos'),
)

CHOICES_S1000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class TransmissorLote(models.Model):
    empregador_tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC)
    empregador_nrinsc = models.CharField(max_length=15)
    transmissor_tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC)
    transmissor_nrinsc = models.CharField(max_length=15)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    resposta_codigo = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    resposta_descricao = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    recepcao_data_hora = models.DateTimeField(max_length=50, blank=True, null=True)
    recepcao_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    protocolo = models.CharField(max_length=50, blank=True, null=True)
    processamento_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    tempo_estimado_conclusao = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.empregador_tpinsc) + ' - ' + unicode(self.empregador_nrinsc) + ' - ' + unicode(self.transmissor_tpinsc) + ' - ' + unicode(self.transmissor_nrinsc) + ' - ' + unicode(self.resposta_codigo) + ' - ' + unicode(self.resposta_descricao)
    #transmissor_lote_custom#
    class Meta:
        db_table = r'transmissor_lote'
        managed = True


class TransmissorLoteOcorrencias(models.Model):
    transmissor_lote = models.ForeignKey('TransmissorLote',
        related_name='%(class)s_transmissor_lote')
    resposta_codigo = models.IntegerField(choices=TIPO_OCORRENCIA)
    descricao = models.TextField()
    tipo = models.IntegerField(choices=EVENTOS_OCORRENCIAS_TIPO)
    localizacao = models.CharField(max_length=50)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #transmissor_lote_ocorrencias_custom#
    class Meta:
        db_table = r'transmissor_lote_ocorrencias'
        managed = True


TPINSC_TRANSMISSOR_EVENTOS = (
    ('1', u'1 - CNPJ'),
    ('2', u'2 - CPF'),
    ('3', u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    ('4', u'4 - CNO (Cadastro Nacional de Obra)'),
)

class TransmissorEventos(models.Model):
    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #transmissor_lote_ocorrencias_custom#
    class Meta:
        db_table = r'transmissor_eventos'
        managed = False
