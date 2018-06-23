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



CHOICES_S2399_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2399_INDMV = (
    (1, u'1 - Contribuição descontada pelo primeiro empregador'),
    (2, u'2 - Contribuição descontada por outra(s) empresa(s) sobre valor inferior ao limite máximo do salário de contribuição'),
    (3, u'3 - Contribuição sobre o limite máximo de salário de contribuição já descontada em outra(s) empresa(s)'),
)

CHOICES_S2399_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2399_TPDEP = (
    ('01', u'01 - Cônjuge'),
    ('02', u'02 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável'),
    ('03', u'03 - Filho(a) ou enteado(a)'),
    ('04', u'04 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau'),
    ('06', u'06 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'),
    ('07', u'07 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2° grau, do(a) qual detenha a guarda judicial'),
    ('09', u'09 - Pais, avós e bisavós'),
    ('10', u'10 - Menor pobre do qual detenha a guarda judicial'),
    ('11', u'11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'),
    ('12', u'12 - Ex-cônjuge'),
    ('99', u'99 - Agregado/Outros'),
)

CHOICES_S2399_TPINSC = (
)

CHOICES_S2399_TPTRIB = (
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (4, u'4 - Contribuição sindical'),
    (4, u'4 - IRRF'),
)

class s2399detOper(models.Model):
    s2399_infosaudecolet = models.ForeignKey('s2399infoSaudeColet',
        related_name='%(class)s_s2399_infosaudecolet')
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_infosaudecolet) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s2399_detoper_custom#
    class Meta:
        db_table = r's2399_detoper'
        managed = True
        ordering = ['s2399_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit']


class s2399detPlano(models.Model):
    s2399_detoper = models.ForeignKey('s2399detOper',
        related_name='%(class)s_s2399_detoper')
    tpdep = models.CharField(choices=CHOICES_S2399_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s2399_detplano_custom#
    class Meta:
        db_table = r's2399_detplano'
        managed = True
        ordering = ['s2399_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep']


class s2399detVerbas(models.Model):
    s2399_ideestablot = models.ForeignKey('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s2399_detverbas_custom#
    class Meta:
        db_table = r's2399_detverbas'
        managed = True
        ordering = ['s2399_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']


class s2399dmDev(models.Model):
    s2399_verbasresc = models.ForeignKey('s2399verbasResc',
        related_name='%(class)s_s2399_verbasresc')
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_verbasresc) + ' - ' + unicode(self.idedmdev)
    #s2399_dmdev_custom#
    class Meta:
        db_table = r's2399_dmdev'
        managed = True
        ordering = ['s2399_verbasresc', 'idedmdev']


class s2399ideEstabLot(models.Model):
    s2399_dmdev = models.ForeignKey('s2399dmDev',
        related_name='%(class)s_s2399_dmdev')
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
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
        return unicode(self.s2399_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2399_ideestablot_custom#
    class Meta:
        db_table = r's2399_ideestablot'
        managed = True
        ordering = ['s2399_dmdev', 'tpinsc', 'nrinsc', 'codlotacao']


class s2399infoAgNocivo(models.Model):
    s2399_ideestablot = models.OneToOneField('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    grauexp = models.IntegerField(choices=CHOICES_S2399_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2399_infoagnocivo_custom#
    class Meta:
        db_table = r's2399_infoagnocivo'
        managed = True
        ordering = ['s2399_ideestablot', 'grauexp']


class s2399infoMV(models.Model):
    s2399_verbasresc = models.OneToOneField('s2399verbasResc',
        related_name='%(class)s_s2399_verbasresc')
    indmv = models.IntegerField(choices=CHOICES_S2399_INDMV)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_verbasresc) + ' - ' + unicode(self.indmv)
    #s2399_infomv_custom#
    class Meta:
        db_table = r's2399_infomv'
        managed = True
        ordering = ['s2399_verbasresc', 'indmv']


class s2399infoSaudeColet(models.Model):
    s2399_ideestablot = models.OneToOneField('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot)
    #s2399_infosaudecolet_custom#
    class Meta:
        db_table = r's2399_infosaudecolet'
        managed = True
        ordering = ['s2399_ideestablot']


class s2399infoSimples(models.Model):
    s2399_ideestablot = models.OneToOneField('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    indsimples = models.IntegerField(choices=CHOICES_S2399_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2399_infosimples_custom#
    class Meta:
        db_table = r's2399_infosimples'
        managed = True
        ordering = ['s2399_ideestablot', 'indsimples']


class s2399procJudTrab(models.Model):
    s2399_verbasresc = models.ForeignKey('s2399verbasResc',
        related_name='%(class)s_s2399_verbasresc')
    tptrib = models.IntegerField(choices=CHOICES_S2399_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_verbasresc) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s2399_procjudtrab_custom#
    class Meta:
        db_table = r's2399_procjudtrab'
        managed = True
        ordering = ['s2399_verbasresc', 'tptrib', 'nrprocjud', 'codsusp']


class s2399quarentena(models.Model):
    s2399_evttsvtermino = models.OneToOneField('eventos.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    dtfimquar = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.dtfimquar)
    #s2399_quarentena_custom#
    class Meta:
        db_table = r's2399_quarentena'
        managed = True
        ordering = ['s2399_evttsvtermino', 'dtfimquar']


class s2399remunOutrEmpr(models.Model):
    s2399_infomv = models.ForeignKey('s2399infoMV',
        related_name='%(class)s_s2399_infomv')
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.IntegerField()
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s2399_remunoutrempr_custom#
    class Meta:
        db_table = r's2399_remunoutrempr'
        managed = True
        ordering = ['s2399_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']


class s2399verbasResc(models.Model):
    s2399_evttsvtermino = models.OneToOneField('eventos.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino)
    #s2399_verbasresc_custom#
    class Meta:
        db_table = r's2399_verbasresc'
        managed = True
        ordering = ['s2399_evttsvtermino']


#VIEWS_MODELS
