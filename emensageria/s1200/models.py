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



CHOICES_S1200_CODCATEG = (
)

CHOICES_S1200_INDMV = (
    (1, u'1 - Contribuição descontada pelo primeiro empregador'),
    (2, u'2 - Contribuição descontada por outra(s) empresa(s) sobre valor inferior ao limite máximo do salário de contribuição'),
    (3, u'3 - Contribuição sobre o limite máximo de salário de contribuição já descontada em outra(s) empresa(s)'),
)

CHOICES_S1200_INFOPERANT_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S1200_INFOPERANT_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S1200_INFOPERANT_REMUNSUC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1200_INFOPERANT_TPACCONV = (
    ('A', u'A - Acordo Coletivo de Trabalho'),
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('C', u'C - Convenção Coletiva de Trabalho'),
    ('D', u'D - Sentença Normativa - Dissídio'),
    ('E', u'E - Conversão de Licença Saúde em Acidente de Trabalho'),
    ('F', u'F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento'),
)

CHOICES_S1200_INFOPERANT_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_INFOPERAPUR_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S1200_INFOPERAPUR_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S1200_INFOPERAPUR_TPDEP = (
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

CHOICES_S1200_INFOPERAPUR_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_TPINSC = (
)

CHOICES_S1200_TPTRIB = (
    (1, u'1 - IRRF'),
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (4, u'4 - Contribuição sindical'),
)

class s1200dmDev(models.Model):
    s1200_evtremun = models.ForeignKey('eventos.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    idedmdev = models.CharField(max_length=30)
    codcateg = models.IntegerField(choices=CHOICES_S1200_CODCATEG)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.codcateg)
    #s1200_dmdev_custom#
    class Meta:
        db_table = r's1200_dmdev'
        managed = True
        ordering = ['s1200_evtremun', 'idedmdev', 'codcateg']


class s1200infoComplem(models.Model):
    s1200_evtremun = models.OneToOneField('eventos.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    nmtrab = models.CharField(max_length=70)
    dtnascto = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.dtnascto)
    #s1200_infocomplem_custom#
    class Meta:
        db_table = r's1200_infocomplem'
        managed = True
        ordering = ['s1200_evtremun', 'nmtrab', 'dtnascto']


class s1200infoInterm(models.Model):
    s1200_evtremun = models.OneToOneField('eventos.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    qtddiasinterm = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.qtddiasinterm)
    #s1200_infointerm_custom#
    class Meta:
        db_table = r's1200_infointerm'
        managed = True
        ordering = ['s1200_evtremun', 'qtddiasinterm']


class s1200infoMV(models.Model):
    s1200_evtremun = models.OneToOneField('eventos.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    indmv = models.IntegerField(choices=CHOICES_S1200_INDMV)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.indmv)
    #s1200_infomv_custom#
    class Meta:
        db_table = r's1200_infomv'
        managed = True
        ordering = ['s1200_evtremun', 'indmv']


class s1200infoPerAnt(models.Model):
    s1200_dmdev = models.OneToOneField('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_dmdev)
    #s1200_infoperant_custom#
    class Meta:
        db_table = r's1200_infoperant'
        managed = True
        ordering = ['s1200_dmdev']


class s1200infoPerAntideADC(models.Model):
    s1200_infoperant = models.ForeignKey('s1200infoPerAnt',
        related_name='%(class)s_s1200_infoperant')
    dtacconv = models.DateField(blank=True, null=True)
    tpacconv = models.CharField(choices=CHOICES_S1200_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField(blank=True, null=True)
    dsc = models.CharField(max_length=255)
    remunsuc = models.CharField(choices=CHOICES_S1200_INFOPERANT_REMUNSUC, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperant) + ' - ' + unicode(self.dtacconv) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.compacconv) + ' - ' + unicode(self.dtefacconv) + ' - ' + unicode(self.dsc) + ' - ' + unicode(self.remunsuc)
    #s1200_infoperant_ideadc_custom#
    class Meta:
        db_table = r's1200_infoperant_ideadc'
        managed = True
        ordering = ['s1200_infoperant', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc', 'remunsuc']


class s1200infoPerAntideEstabLot(models.Model):
    s1200_infoperant_ideperiodo = models.ForeignKey('s1200infoPerAntidePeriodo',
        related_name='%(class)s_s1200_infoperant_ideperiodo')
    tpinsc = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_TPINSC)
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
        return unicode(self.s1200_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s1200_infoperant_ideestablot_custom#
    class Meta:
        db_table = r's1200_infoperant_ideestablot'
        managed = True
        ordering = ['s1200_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao']


class s1200infoPerAntidePeriodo(models.Model):
    s1200_infoperant_ideadc = models.ForeignKey('s1200infoPerAntideADC',
        related_name='%(class)s_s1200_infoperant_ideadc')
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s1200_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's1200_infoperant_ideperiodo'
        managed = True
        ordering = ['s1200_infoperant_ideadc', 'perref']


class s1200infoPerAntinfoAgNocivo(models.Model):
    s1200_infoperant_remunperant = models.OneToOneField('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
    grauexp = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.grauexp)
    #s1200_infoperant_infoagnocivo_custom#
    class Meta:
        db_table = r's1200_infoperant_infoagnocivo'
        managed = True
        ordering = ['s1200_infoperant_remunperant', 'grauexp']


class s1200infoPerAntinfoComplCont(models.Model):
    s1200_dmdev = models.OneToOneField('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    codcbo = models.CharField(max_length=6)
    natatividade = models.IntegerField(blank=True, null=True)
    qtddiastrab = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_dmdev) + ' - ' + unicode(self.codcbo) + ' - ' + unicode(self.natatividade) + ' - ' + unicode(self.qtddiastrab)
    #s1200_infoperant_infocomplcont_custom#
    class Meta:
        db_table = r's1200_infoperant_infocomplcont'
        managed = True
        ordering = ['s1200_dmdev', 'codcbo', 'natatividade', 'qtddiastrab']


class s1200infoPerAntinfoTrabInterm(models.Model):
    s1200_infoperant_remunperant = models.ForeignKey('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codconv)
    #s1200_infoperant_infotrabinterm_custom#
    class Meta:
        db_table = r's1200_infoperant_infotrabinterm'
        managed = True
        ordering = ['s1200_infoperant_remunperant', 'codconv']


class s1200infoPerAntitensRemun(models.Model):
    s1200_infoperant_remunperant = models.ForeignKey('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
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
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1200_infoperant_itensremun_custom#
    class Meta:
        db_table = r's1200_infoperant_itensremun'
        managed = True
        ordering = ['s1200_infoperant_remunperant', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']


class s1200infoPerAntremunPerAnt(models.Model):
    s1200_infoperant_ideestablot = models.ForeignKey('s1200infoPerAntideEstabLot',
        related_name='%(class)s_s1200_infoperant_ideestablot')
    matricula = models.CharField(max_length=30, blank=True, null=True)
    indsimples = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideestablot) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.indsimples)
    #s1200_infoperant_remunperant_custom#
    class Meta:
        db_table = r's1200_infoperant_remunperant'
        managed = True
        ordering = ['s1200_infoperant_ideestablot', 'matricula', 'indsimples']


class s1200infoPerApur(models.Model):
    s1200_dmdev = models.OneToOneField('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_dmdev)
    #s1200_infoperapur_custom#
    class Meta:
        db_table = r's1200_infoperapur'
        managed = True
        ordering = ['s1200_dmdev']


class s1200infoPerApurdetOper(models.Model):
    s1200_infoperapur_infosaudecolet = models.ForeignKey('s1200infoPerApurinfoSaudeColet',
        related_name='%(class)s_s1200_infoperapur_infosaudecolet')
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
        return unicode(self.s1200_infoperapur_infosaudecolet) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s1200_infoperapur_detoper_custom#
    class Meta:
        db_table = r's1200_infoperapur_detoper'
        managed = True
        ordering = ['s1200_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit']


class s1200infoPerApurdetPlano(models.Model):
    s1200_infoperapur_detoper = models.ForeignKey('s1200infoPerApurdetOper',
        related_name='%(class)s_s1200_infoperapur_detoper')
    tpdep = models.CharField(choices=CHOICES_S1200_INFOPERAPUR_TPDEP, max_length=2)
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
        return unicode(self.s1200_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s1200_infoperapur_detplano_custom#
    class Meta:
        db_table = r's1200_infoperapur_detplano'
        managed = True
        ordering = ['s1200_infoperapur_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep']


class s1200infoPerApurideEstabLot(models.Model):
    s1200_infoperapur = models.ForeignKey('s1200infoPerApur',
        related_name='%(class)s_s1200_infoperapur')
    tpinsc = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    qtddiasav = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.qtddiasav)
    #s1200_infoperapur_ideestablot_custom#
    class Meta:
        db_table = r's1200_infoperapur_ideestablot'
        managed = True
        ordering = ['s1200_infoperapur', 'tpinsc', 'nrinsc', 'codlotacao', 'qtddiasav']


class s1200infoPerApurinfoAgNocivo(models.Model):
    s1200_infoperapur_remunperapur = models.OneToOneField('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    grauexp = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.grauexp)
    #s1200_infoperapur_infoagnocivo_custom#
    class Meta:
        db_table = r's1200_infoperapur_infoagnocivo'
        managed = True
        ordering = ['s1200_infoperapur_remunperapur', 'grauexp']


class s1200infoPerApurinfoSaudeColet(models.Model):
    s1200_infoperapur_remunperapur = models.OneToOneField('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur)
    #s1200_infoperapur_infosaudecolet_custom#
    class Meta:
        db_table = r's1200_infoperapur_infosaudecolet'
        managed = True
        ordering = ['s1200_infoperapur_remunperapur']


class s1200infoPerApurinfoTrabInterm(models.Model):
    s1200_infoperapur_remunperapur = models.ForeignKey('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codconv)
    #s1200_infoperapur_infotrabinterm_custom#
    class Meta:
        db_table = r's1200_infoperapur_infotrabinterm'
        managed = True
        ordering = ['s1200_infoperapur_remunperapur', 'codconv']


class s1200infoPerApuritensRemun(models.Model):
    s1200_infoperapur_remunperapur = models.ForeignKey('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
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
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1200_infoperapur_itensremun_custom#
    class Meta:
        db_table = r's1200_infoperapur_itensremun'
        managed = True
        ordering = ['s1200_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']


class s1200infoPerApurremunPerApur(models.Model):
    s1200_infoperapur_ideestablot = models.ForeignKey('s1200infoPerApurideEstabLot',
        related_name='%(class)s_s1200_infoperapur_ideestablot')
    matricula = models.CharField(max_length=30, blank=True, null=True)
    indsimples = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_ideestablot) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.indsimples)
    #s1200_infoperapur_remunperapur_custom#
    class Meta:
        db_table = r's1200_infoperapur_remunperapur'
        managed = True
        ordering = ['s1200_infoperapur_ideestablot', 'matricula', 'indsimples']


class s1200procJudTrab(models.Model):
    s1200_evtremun = models.ForeignKey('eventos.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    tptrib = models.IntegerField(choices=CHOICES_S1200_TPTRIB)
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
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1200_procjudtrab_custom#
    class Meta:
        db_table = r's1200_procjudtrab'
        managed = True
        ordering = ['s1200_evtremun', 'tptrib', 'nrprocjud', 'codsusp']


class s1200remunOutrEmpr(models.Model):
    s1200_infomv = models.ForeignKey('s1200infoMV',
        related_name='%(class)s_s1200_infomv')
    tpinsc = models.IntegerField(choices=CHOICES_S1200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.IntegerField(choices=CHOICES_S1200_CODCATEG)
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s1200_remunoutrempr_custom#
    class Meta:
        db_table = r's1200_remunoutrempr'
        managed = True
        ordering = ['s1200_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']


class s1200sucessaoVinc(models.Model):
    s1200_infocomplem = models.OneToOneField('s1200infoComplem',
        related_name='%(class)s_s1200_infocomplem')
    cnpjempregant = models.CharField(max_length=14)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dtadm = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1200_infocomplem) + ' - ' + unicode(self.cnpjempregant) + ' - ' + unicode(self.matricant) + ' - ' + unicode(self.dtadm) + ' - ' + unicode(self.observacao)
    #s1200_sucessaovinc_custom#
    class Meta:
        db_table = r's1200_sucessaovinc'
        managed = True
        ordering = ['s1200_infocomplem', 'cnpjempregant', 'matricant', 'dtadm', 'observacao']


#VIEWS_MODELS
