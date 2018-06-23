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



CHOICES_S5001_CODCATEG = (
    (101, u'101 - Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT.'),
    (102, u'102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008'),
    (103, u'103 - Empregado - Aprendiz'),
    (104, u'104 - Empregado - Doméstico'),
    (105, u'105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98'),
    (106, u'106 - Trabalhador Temporário - contrato por prazo determinado nos termos da Lei 6019/74'),
    (111, u'111 - Empregado - contrato de trabalho intermitente'),
    (201, u'201 - Trabalhador Avulso Portuário'),
    (202, u'202 - Trabalhador Avulso Não Portuário'),
    (301, u'301 - Servidor Público Titular de Cargo Efetivo, Magistrado, Ministro de Tribunal de Contas, Conselheiro de Tribunal de Contas e Membro do Ministério Público'),
    (302, u'302 - Servidor Público Ocupante de Cargo exclusivo em comissão'),
    (303, u'303 - Agente Político'),
    (305, u'305 - Servidor Público indicado para conselho ou órgão deliberativo, na condição de representante do governo, órgão ou entidade da administração pública.'),
    (306, u'306 - Servidor Público Temporário, sujeito a regime administrativo especial definido em lei própria'),
    (307, u'307 - Militar efetivo'),
    (308, u'308 - Conscrito'),
    (309, u'309 - Agente Público - Outros'),
    (401, u'401 - Dirigente Sindical - informação prestada pelo Sindicato'),
    (410, u'410 - Trabalhador cedido - informação prestada pelo Cessionário'),
    (701, u'701 - Contribuinte individual - Autônomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual'),
    (711, u'711 - Contribuinte individual - Transportador autônomo de passageiros'),
    (712, u'712 - Contribuinte individual - Transportador autônomo de carga'),
    (721, u'721 - Contribuinte individual - Diretor não empregado, com FGTS'),
    (722, u'722 - Contribuinte individual - Diretor não empregado, sem FGTS'),
    (723, u'723 - Contribuinte individual - empresários, sócios e membro de conselho de administração ou fiscal'),
    (731, u'731 - Contribuinte individual - Cooperado que presta serviços por intermédio de Cooperativa de Trabalho'),
    (734, u'734 - Contribuinte individual - Transportador Cooperado que presta serviços por intermédio de cooperativa de trabalho'),
    (738, u'738 - Contribuinte individual - Cooperado filiado a Cooperativa de Produção'),
    (741, u'741 - Contribuinte individual - Microempreendedor Individual'),
    (751, u'751 - Contribuinte individual - magistrado classista temporário da Justiça do Trabalho ou da Justiça Eleitoral que seja aposentado de qualquer regime previdenciário'),
    (761, u'761 - Contribuinte individual - Associado eleito para direção de Cooperativa, associação ou entidade de classe de qualquer natureza ou finalidade, bem como o síndico ou administrador eleito para exercer atividade de direção condominial, desde que recebam remuneração'),
    (771, u'771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei nº 8.069, de 13 de julho de 1990'),
    (781, u'781 - Ministro de confissão religiosa ou membro de vida consagrada, de congregação ou de ordem religiosa'),
    (901, u'901 - Estagiário'),
    (902, u'902 - Médico Residente'),
    (903, u'903 - Bolsista, nos termos da lei 8958/1994'),
    (904, u'904 - Participante de curso de formação, como etapa de concurso público, sem vínculo de emprego/estatutário'),
    (905, u'905 - Atleta não profissional em formação que receba bolsa'),
)

CHOICES_S5001_IND13 = (
    (0, u'0 - Mensal'),
    (1, u'1 - 13° salário - {codIncCP} = [12, 14, 16, 22, 26, 32, 92, 94]'),
)

CHOICES_S5001_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S5001_TPCR = (
)

CHOICES_S5001_TPINSC = (
)

CHOICES_S5001_TPVALOR = (
    (11, u'11 - Base de cálculo da Contribuição Previdenciária normal'),
    (12, u'12 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição'),
    (13, u'13 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição'),
    (14, u'14 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição'),
    (15, u'15 - Base de cálculo da contribuição previdenciária adicional normal - exclusiva do empregador'),
    (16, u'16 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição - exclusiva do empregador'),
    (17, u'17 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição - exclusiva do empregador'),
    (18, u'18 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição - exclusiva do empregador'),
    (19, u'19 - Base de cálculo da contribuição previdenciária exclusiva do empregado'),
    (21, u'21 - Valor total descontado do trabalhador para recolhimento à Previdência Social'),
    (22, u'22 - Valor descontado do trabalhador para recolhimento ao Sest'),
    (23, u'23 - Valor descontado do trabalhador para recolhimento ao Senat'),
    (31, u'31 - Valor pago ao trabalhador a título de salário-família'),
    (32, u'32 - Valor pago ao trabalhador a título de salário-maternidade'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial - Base de cálculo (BC) da Contribuição Previdenciária (CP) Normal'),
    (92, u'92 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 15 anos de trabalho'),
    (93, u'93 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 20 anos de trabalho'),
    (94, u'94 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 25 anos de trabalho'),
)

class s5001calcTerc(models.Model):
    s5001_infocategincid = models.ForeignKey('s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid')
    tpcr = models.IntegerField(choices=CHOICES_S5001_TPCR)
    vrcssegterc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescterc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_infocategincid) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcssegterc) + ' - ' + unicode(self.vrdescterc)
    #s5001_calcterc_custom#
    class Meta:
        db_table = r's5001_calcterc'
        managed = True
        ordering = ['s5001_infocategincid', 'tpcr', 'vrcssegterc', 'vrdescterc']


class s5001ideEstabLot(models.Model):
    s5001_evtbasestrab = models.ForeignKey('eventos.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    tpinsc = models.IntegerField(choices=CHOICES_S5001_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s5001_ideestablot_custom#
    class Meta:
        db_table = r's5001_ideestablot'
        managed = True
        ordering = ['s5001_evtbasestrab', 'tpinsc', 'nrinsc', 'codlotacao']


class s5001infoBaseCS(models.Model):
    s5001_infocategincid = models.ForeignKey('s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid')
    ind13 = models.IntegerField(choices=CHOICES_S5001_IND13)
    tpvalor = models.IntegerField(choices=CHOICES_S5001_TPVALOR)
    valor = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_infocategincid) + ' - ' + unicode(self.ind13) + ' - ' + unicode(self.tpvalor) + ' - ' + unicode(self.valor)
    #s5001_infobasecs_custom#
    class Meta:
        db_table = r's5001_infobasecs'
        managed = True
        ordering = ['s5001_infocategincid', 'ind13', 'tpvalor', 'valor']


class s5001infoCategIncid(models.Model):
    s5001_ideestablot = models.ForeignKey('s5001ideEstabLot',
        related_name='%(class)s_s5001_ideestablot')
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.IntegerField(choices=CHOICES_S5001_CODCATEG)
    indsimples = models.IntegerField(choices=CHOICES_S5001_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_ideestablot) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.indsimples)
    #s5001_infocategincid_custom#
    class Meta:
        db_table = r's5001_infocategincid'
        managed = True
        ordering = ['s5001_ideestablot', 'matricula', 'codcateg', 'indsimples']


class s5001infoCpCalc(models.Model):
    s5001_evtbasestrab = models.ForeignKey('eventos.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    tpcr = models.IntegerField(choices=CHOICES_S5001_TPCR)
    vrcpseg = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescseg = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcpseg) + ' - ' + unicode(self.vrdescseg)
    #s5001_infocpcalc_custom#
    class Meta:
        db_table = r's5001_infocpcalc'
        managed = True
        ordering = ['s5001_evtbasestrab', 'tpcr', 'vrcpseg', 'vrdescseg']


class s5001procJudTrab(models.Model):
    s5001_evtbasestrab = models.ForeignKey('eventos.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s5001_procjudtrab_custom#
    class Meta:
        db_table = r's5001_procjudtrab'
        managed = True
        ordering = ['s5001_evtbasestrab', 'nrprocjud', 'codsusp']


#VIEWS_MODELS
