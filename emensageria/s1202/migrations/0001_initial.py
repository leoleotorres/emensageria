# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('eventos', '0002_auto_20180530_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1202dmDev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idedmdev', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202dmdev_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202dmdev_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_evtrmnrpps', models.ForeignKey(related_name='s1202dmdev_s1202_evtrmnrpps', to='eventos.s1202evtRmnRPPS')),
            ],
            options={
                'ordering': ['s1202_evtrmnrpps', 'idedmdev'],
                'db_table': 's1202_dmdev',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperant_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperant_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_dmdev', models.OneToOneField(related_name='s1202infoperant_s1202_dmdev', to='s1202.s1202dmDev')),
            ],
            options={
                'ordering': ['s1202_dmdev'],
                'db_table': 's1202_infoperant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAntideADC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtlei', models.DateField()),
                ('nrlei', models.CharField(max_length=12)),
                ('dtef', models.DateField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperantideadc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperantideadc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperant', models.ForeignKey(related_name='s1202infoperantideadc_s1202_infoperant', to='s1202.s1202infoPerAnt')),
            ],
            options={
                'ordering': ['s1202_infoperant', 'dtlei', 'nrlei', 'dtef'],
                'db_table': 's1202_infoperant_ideadc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAntideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperantideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperantideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1202_infoperant_ideperiodo', 'tpinsc', 'nrinsc'],
                'db_table': 's1202_infoperant_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAntidePeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perref', models.CharField(max_length=7)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperantideperiodo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperantideperiodo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperant_ideadc', models.ForeignKey(related_name='s1202infoperantideperiodo_s1202_infoperant_ideadc', to='s1202.s1202infoPerAntideADC')),
            ],
            options={
                'ordering': ['s1202_infoperant_ideadc', 'perref'],
                'db_table': 's1202_infoperant_ideperiodo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAntitensRemun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codrubr', models.CharField(max_length=30)),
                ('idetabrubr', models.CharField(max_length=8)),
                ('qtdrubr', models.DecimalField(max_length=6, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('fatorrubr', models.DecimalField(max_length=5, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrunit', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrrubr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperantitensremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperantitensremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1202_infoperant_remunperant', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's1202_infoperant_itensremun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerAntremunPerAnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.CharField(max_length=30, null=True, blank=True)),
                ('codcateg', models.IntegerField(choices=[(101, '101 - Empregado - Geral, inclusive o empregado p\xfablico da administra\xe7\xe3o direta ou indireta contratado pela CLT.'), (102, '102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008'), (103, '103 - Empregado - Aprendiz'), (104, '104 - Empregado - Dom\xe9stico'), (105, '105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98'), (106, '106 - Trabalhador Tempor\xe1rio - contrato por prazo determinado nos termos da Lei 6019/74'), (111, '111 - Empregado - contrato de trabalho intermitente'), (201, '201 - Trabalhador Avulso Portu\xe1rio'), (202, '202 - Trabalhador Avulso N\xe3o Portu\xe1rio'), (301, '301 - Servidor P\xfablico Titular de Cargo Efetivo, Magistrado, Ministro de Tribunal de Contas, Conselheiro de Tribunal de Contas e Membro do Minist\xe9rio P\xfablico'), (302, '302 - Servidor P\xfablico Ocupante de Cargo exclusivo em comiss\xe3o'), (303, '303 - Agente Pol\xedtico'), (305, '305 - Servidor P\xfablico indicado para conselho ou \xf3rg\xe3o deliberativo, na condi\xe7\xe3o de representante do governo, \xf3rg\xe3o ou entidade da administra\xe7\xe3o p\xfablica.'), (306, '306 - Servidor P\xfablico Tempor\xe1rio, sujeito a regime administrativo especial definido em lei pr\xf3pria'), (307, '307 - Militar efetivo'), (308, '308 - Conscrito'), (309, '309 - Agente P\xfablico - Outros'), (401, '401 - Dirigente Sindical - informa\xe7\xe3o prestada pelo Sindicato'), (410, '410 - Trabalhador cedido - informa\xe7\xe3o prestada pelo Cession\xe1rio'), (701, '701 - Contribuinte individual - Aut\xf4nomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual'), (711, '711 - Contribuinte individual - Transportador aut\xf4nomo de passageiros'), (712, '712 - Contribuinte individual - Transportador aut\xf4nomo de carga'), (721, '721 - Contribuinte individual - Diretor n\xe3o empregado, com FGTS'), (722, '722 - Contribuinte individual - Diretor n\xe3o empregado, sem FGTS'), (723, '723 - Contribuinte individual - empres\xe1rios, s\xf3cios e membro de conselho de administra\xe7\xe3o ou fiscal'), (731, '731 - Contribuinte individual - Cooperado que presta servi\xe7os por interm\xe9dio de Cooperativa de Trabalho'), (734, '734 - Contribuinte individual - Transportador Cooperado que presta servi\xe7os por interm\xe9dio de cooperativa de trabalho'), (738, '738 - Contribuinte individual - Cooperado filiado a Cooperativa de Produ\xe7\xe3o'), (741, '741 - Contribuinte individual - Microempreendedor Individual'), (751, '751 - Contribuinte individual - magistrado classista tempor\xe1rio da Justi\xe7a do Trabalho ou da Justi\xe7a Eleitoral que seja aposentado de qualquer regime previdenci\xe1rio'), (761, '761 - Contribuinte individual - Associado eleito para dire\xe7\xe3o de Cooperativa, associa\xe7\xe3o ou entidade de classe de qualquer natureza ou finalidade, bem como o s\xedndico ou administrador eleito para exercer atividade de dire\xe7\xe3o condominial, desde que recebam remunera\xe7\xe3o'), (771, '771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei n\xba 8.069, de 13 de julho de 1990'), (781, '781 - Ministro de confiss\xe3o religiosa ou membro de vida consagrada, de congrega\xe7\xe3o ou de ordem religiosa'), (901, '901 - Estagi\xe1rio'), (902, '902 - M\xe9dico Residente'), (903, '903 - Bolsista, nos termos da lei 8958/1994'), (904, '904 - Participante de curso de forma\xe7\xe3o, como etapa de concurso p\xfablico, sem v\xednculo de emprego/estatut\xe1rio'), (905, '905 - Atleta n\xe3o profissional em forma\xe7\xe3o que receba bolsa')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperantremunperant_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperantremunperant_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperant_ideestab', models.ForeignKey(related_name='s1202infoperantremunperant_s1202_infoperant_ideestab', to='s1202.s1202infoPerAntideEstab')),
            ],
            options={
                'ordering': ['s1202_infoperant_ideestab', 'matricula', 'codcateg'],
                'db_table': 's1202_infoperant_remunperant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_dmdev', models.OneToOneField(related_name='s1202infoperapur_s1202_dmdev', to='s1202.s1202dmDev')),
            ],
            options={
                'ordering': ['s1202_dmdev'],
                'db_table': 's1202_infoperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurdetOper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjoper', models.CharField(max_length=14)),
                ('regans', models.CharField(max_length=6)),
                ('vrpgtit', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapurdetoper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapurdetoper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1202_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'],
                'db_table': 's1202_infoperapur_detoper',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurdetPlano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpdep', models.CharField(max_length=2, choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')])),
                ('cpfdep', models.CharField(max_length=11, null=True, blank=True)),
                ('nmdep', models.CharField(max_length=70)),
                ('dtnascto', models.DateField()),
                ('vlrpgdep', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapurdetplano_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapurdetplano_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperapur_detoper', models.ForeignKey(related_name='s1202infoperapurdetplano_s1202_infoperapur_detoper', to='s1202.s1202infoPerApurdetOper')),
            ],
            options={
                'ordering': ['s1202_infoperapur_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep'],
                'db_table': 's1202_infoperapur_detplano',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapurideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapurideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperapur', models.ForeignKey(related_name='s1202infoperapurideestab_s1202_infoperapur', to='s1202.s1202infoPerApur')),
            ],
            options={
                'ordering': ['s1202_infoperapur', 'tpinsc', 'nrinsc'],
                'db_table': 's1202_infoperapur_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurinfoSaudeColet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapurinfosaudecolet_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapurinfosaudecolet_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1202_infoperapur_remunperapur'],
                'db_table': 's1202_infoperapur_infosaudecolet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApuritensRemun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codrubr', models.CharField(max_length=30)),
                ('idetabrubr', models.CharField(max_length=8)),
                ('qtdrubr', models.DecimalField(max_length=6, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('fatorrubr', models.DecimalField(max_length=5, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrunit', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrrubr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapuritensremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapuritensremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1202_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's1202_infoperapur_itensremun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurremunPerApur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.CharField(max_length=30, null=True, blank=True)),
                ('codcateg', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202infoperapurremunperapur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202infoperapurremunperapur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_infoperapur_ideestab', models.ForeignKey(related_name='s1202infoperapurremunperapur_s1202_infoperapur_ideestab', to='s1202.s1202infoPerApurideEstab')),
            ],
            options={
                'ordering': ['s1202_infoperapur_ideestab', 'matricula', 'codcateg'],
                'db_table': 's1202_infoperapur_remunperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1202procJudTrab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tptrib', models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (2, '2 - IRRF'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')])),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1202procjudtrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1202procjudtrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1202_evtrmnrpps', models.ForeignKey(related_name='s1202procjudtrab_s1202_evtrmnrpps', to='eventos.s1202evtRmnRPPS')),
            ],
            options={
                'ordering': ['s1202_evtrmnrpps', 'tptrib', 'nrprocjud', 'codsusp'],
                'db_table': 's1202_procjudtrab',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s1202infoperapuritensremun',
            name='s1202_infoperapur_remunperapur',
            field=models.ForeignKey(related_name='s1202infoperapuritensremun_s1202_infoperapur_remunperapur', to='s1202.s1202infoPerApurremunPerApur'),
        ),
        migrations.AddField(
            model_name='s1202infoperapurinfosaudecolet',
            name='s1202_infoperapur_remunperapur',
            field=models.OneToOneField(related_name='s1202infoperapurinfosaudecolet_s1202_infoperapur_remunperapur', to='s1202.s1202infoPerApurremunPerApur'),
        ),
        migrations.AddField(
            model_name='s1202infoperapurdetoper',
            name='s1202_infoperapur_infosaudecolet',
            field=models.ForeignKey(related_name='s1202infoperapurdetoper_s1202_infoperapur_infosaudecolet', to='s1202.s1202infoPerApurinfoSaudeColet'),
        ),
        migrations.AddField(
            model_name='s1202infoperantitensremun',
            name='s1202_infoperant_remunperant',
            field=models.ForeignKey(related_name='s1202infoperantitensremun_s1202_infoperant_remunperant', to='s1202.s1202infoPerAntremunPerAnt'),
        ),
        migrations.AddField(
            model_name='s1202infoperantideestab',
            name='s1202_infoperant_ideperiodo',
            field=models.ForeignKey(related_name='s1202infoperantideestab_s1202_infoperant_ideperiodo', to='s1202.s1202infoPerAntidePeriodo'),
        ),
    ]
