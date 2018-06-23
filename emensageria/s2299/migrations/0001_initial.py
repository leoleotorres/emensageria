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
            name='s2299dmDev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idedmdev', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299dmdev_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299dmdev_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_verbasresc', 'idedmdev'],
                'db_table': 's2299_dmdev',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperant_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperant_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_dmdev', models.OneToOneField(related_name='s2299infoperant_s2299_dmdev', to='s2299.s2299dmDev')),
            ],
            options={
                'ordering': ['s2299_dmdev'],
                'db_table': 's2299_infoperant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntdetVerbas',
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
                ('criado_por', models.ForeignKey(related_name='s2299infoperantdetverbas_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantdetverbas_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_infoperant_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's2299_infoperant_detverbas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntideADC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtacconv', models.DateField()),
                ('tpacconv', models.CharField(max_length=1, choices=[(b'A', 'A - Acordo Coletivo de Trabalho'), (b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'C', 'C - Conven\xe7\xe3o Coletiva de Trabalho'), (b'D', 'D - Senten\xe7a Normativa - Diss\xeddio'), (b'E', 'E - Convers\xe3o de Licen\xe7a Sa\xfade em Acidente de Trabalho')])),
                ('compacconv', models.CharField(max_length=7, null=True, blank=True)),
                ('dtefacconv', models.DateField()),
                ('dsc', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperantideadc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantideadc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperant', models.ForeignKey(related_name='s2299infoperantideadc_s2299_infoperant', to='s2299.s2299infoPerAnt')),
            ],
            options={
                'ordering': ['s2299_infoperant', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc'],
                'db_table': 's2299_infoperant_ideadc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntideEstabLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codlotacao', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperantideestablot_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantideestablot_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao'],
                'db_table': 's2299_infoperant_ideestablot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntidePeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perref', models.CharField(max_length=7)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperantideperiodo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantideperiodo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperant_ideadc', models.ForeignKey(related_name='s2299infoperantideperiodo_s2299_infoperant_ideadc', to='s2299.s2299infoPerAntideADC')),
            ],
            options={
                'ordering': ['s2299_infoperant_ideadc', 'perref'],
                'db_table': 's2299_infoperant_ideperiodo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntinfoAgNocivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grauexp', models.IntegerField(choices=[(1, '1 - N\xe3o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribui\xe7\xe3o e al\xedquota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribui\xe7\xe3o e al\xedquota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribui\xe7\xe3o e al\xedquota de 6%)')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperantinfoagnocivo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantinfoagnocivo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperant_ideestablot', models.OneToOneField(related_name='s2299infoperantinfoagnocivo_s2299_infoperant_ideestablot', to='s2299.s2299infoPerAntideEstabLot')),
            ],
            options={
                'ordering': ['s2299_infoperant_ideestablot', 'grauexp'],
                'db_table': 's2299_infoperant_infoagnocivo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerAntinfoSimples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indsimples', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Substitu\xedda Integralmente'), (2, '2 - Contribui\xe7\xe3o n\xe3o substitu\xedda'), (3, '3 - Contribui\xe7\xe3o n\xe3o substitu\xedda concomitante com contribui\xe7\xe3o substitu\xedda')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperantinfosimples_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperantinfosimples_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperant_ideestablot', models.OneToOneField(related_name='s2299infoperantinfosimples_s2299_infoperant_ideestablot', to='s2299.s2299infoPerAntideEstabLot')),
            ],
            options={
                'ordering': ['s2299_infoperant_ideestablot', 'indsimples'],
                'db_table': 's2299_infoperant_infosimples',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_dmdev', models.OneToOneField(related_name='s2299infoperapur_s2299_dmdev', to='s2299.s2299dmDev')),
            ],
            options={
                'ordering': ['s2299_dmdev'],
                'db_table': 's2299_infoperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurdetOper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjoper', models.CharField(max_length=14)),
                ('regans', models.CharField(max_length=6)),
                ('vrpgtit', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurdetoper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurdetoper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'],
                'db_table': 's2299_infoperapur_detoper',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurdetPlano',
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
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurdetplano_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurdetplano_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperapur_detoper', models.ForeignKey(related_name='s2299infoperapurdetplano_s2299_infoperapur_detoper', to='s2299.s2299infoPerApurdetOper')),
            ],
            options={
                'ordering': ['s2299_infoperapur_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep'],
                'db_table': 's2299_infoperapur_detplano',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurdetVerbas',
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
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurdetverbas_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurdetverbas_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_infoperapur_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's2299_infoperapur_detverbas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurideEstabLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codlotacao', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurideestablot_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurideestablot_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperapur', models.ForeignKey(related_name='s2299infoperapurideestablot_s2299_infoperapur', to='s2299.s2299infoPerApur')),
            ],
            options={
                'ordering': ['s2299_infoperapur', 'tpinsc', 'nrinsc', 'codlotacao'],
                'db_table': 's2299_infoperapur_ideestablot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurinfoAgNocivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grauexp', models.IntegerField(choices=[(1, '1 - N\xe3o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribui\xe7\xe3o e al\xedquota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribui\xe7\xe3o e al\xedquota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribui\xe7\xe3o e al\xedquota de 6%)')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurinfoagnocivo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurinfoagnocivo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperapur_ideestablot', models.OneToOneField(related_name='s2299infoperapurinfoagnocivo_s2299_infoperapur_ideestablot', to='s2299.s2299infoPerApurideEstabLot')),
            ],
            options={
                'ordering': ['s2299_infoperapur_ideestablot', 'grauexp'],
                'db_table': 's2299_infoperapur_infoagnocivo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurinfoSaudeColet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurinfosaudecolet_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurinfosaudecolet_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperapur_ideestablot', models.OneToOneField(related_name='s2299infoperapurinfosaudecolet_s2299_infoperapur_ideestablot', to='s2299.s2299infoPerApurideEstabLot')),
            ],
            options={
                'ordering': ['s2299_infoperapur_ideestablot'],
                'db_table': 's2299_infoperapur_infosaudecolet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoPerApurinfoSimples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indsimples', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Substitu\xedda Integralmente'), (2, '2 - Contribui\xe7\xe3o n\xe3o substitu\xedda'), (3, '3 - Contribui\xe7\xe3o n\xe3o substitu\xedda concomitante com contribui\xe7\xe3o substitu\xedda')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infoperapurinfosimples_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infoperapurinfosimples_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infoperapur_ideestablot', models.OneToOneField(related_name='s2299infoperapurinfosimples_s2299_infoperapur_ideestablot', to='s2299.s2299infoPerApurideEstabLot')),
            ],
            options={
                'ordering': ['s2299_infoperapur_ideestablot', 'indsimples'],
                'db_table': 's2299_infoperapur_infosimples',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabInterm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codconv', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabinterm_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabinterm_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_dmdev', models.ForeignKey(related_name='s2299infotrabinterm_s2299_dmdev', to='s2299.s2299dmDev')),
            ],
            options={
                'ordering': ['s2299_dmdev', 'codconv'],
                'db_table': 's2299_infotrabinterm',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabIntermconsigFGTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('insconsig', models.CharField(max_length=5)),
                ('nrcontr', models.CharField(max_length=40)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabintermconsigfgts_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabintermconsigfgts_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.ForeignKey(related_name='s2299infotrabintermconsigfgts_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig', 'insconsig', 'nrcontr'],
                'db_table': 's2299_infotrabinterm_consigfgts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabInterminfoMV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indmv', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o descontada pelo primeiro empregador'), (2, '2 - Contribui\xe7\xe3o descontada por outra(s) empresa(s) sobre valor inferior ao limite m\xe1ximo do sal\xe1rio de contribui\xe7\xe3o'), (3, '3 - Contribui\xe7\xe3o sobre o limite m\xe1ximo de sal\xe1rio de contribui\xe7\xe3o j\xe1 descontada em outra(s) empresa(s)')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabinterminfomv_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabinterminfomv_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_verbasresc', 'indmv'],
                'db_table': 's2299_infotrabinterm_infomv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabIntermprocCS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrprocjud', models.CharField(max_length=20)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabintermproccs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabintermproccs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_verbasresc', 'nrprocjud'],
                'db_table': 's2299_infotrabinterm_proccs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabIntermprocJudTrab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tptrib', models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (3, '3 - IRRF'), (4, '4 - Contribui\xe7\xe3o sindical')])),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabintermprocjudtrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabintermprocjudtrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2299_verbasresc', 'tptrib', 'nrprocjud', 'codsusp'],
                'db_table': 's2299_infotrabinterm_procjudtrab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabIntermquarentena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtfimquar', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabintermquarentena_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabintermquarentena_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.OneToOneField(related_name='s2299infotrabintermquarentena_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig', 'dtfimquar'],
                'db_table': 's2299_infotrabinterm_quarentena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299infoTrabIntermremunOutrEmpr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codcateg', models.IntegerField()),
                ('vlrremunoe', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299infotrabintermremunoutrempr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299infotrabintermremunoutrempr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_infotrabinterm_infomv', models.ForeignKey(related_name='s2299infotrabintermremunoutrempr_s2299_infotrabinterm_infomv', to='s2299.s2299infoTrabInterminfoMV')),
            ],
            options={
                'ordering': ['s2299_infotrabinterm_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe'],
                'db_table': 's2299_infotrabinterm_remunoutrempr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299observacoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacao', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299observacoes_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299observacoes_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.ForeignKey(related_name='s2299observacoes_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig', 'observacao'],
                'db_table': 's2299_observacoes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299sucessaoVinc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjsucessora', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299sucessaovinc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299sucessaovinc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.OneToOneField(related_name='s2299sucessaovinc_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig', 'cnpjsucessora'],
                'db_table': 's2299_sucessaovinc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299transfTit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpfsubstituto', models.CharField(max_length=11)),
                ('dtnascto', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299transftit_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299transftit_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.OneToOneField(related_name='s2299transftit_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig', 'cpfsubstituto', 'dtnascto'],
                'db_table': 's2299_transftit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2299verbasResc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2299verbasresc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2299verbasresc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2299_evtdeslig', models.OneToOneField(related_name='s2299verbasresc_s2299_evtdeslig', to='eventos.s2299evtDeslig')),
            ],
            options={
                'ordering': ['s2299_evtdeslig'],
                'db_table': 's2299_verbasresc',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s2299infotrabintermprocjudtrab',
            name='s2299_verbasresc',
            field=models.ForeignKey(related_name='s2299infotrabintermprocjudtrab_s2299_verbasresc', to='s2299.s2299verbasResc'),
        ),
        migrations.AddField(
            model_name='s2299infotrabintermproccs',
            name='s2299_verbasresc',
            field=models.OneToOneField(related_name='s2299infotrabintermproccs_s2299_verbasresc', to='s2299.s2299verbasResc'),
        ),
        migrations.AddField(
            model_name='s2299infotrabinterminfomv',
            name='s2299_verbasresc',
            field=models.OneToOneField(related_name='s2299infotrabinterminfomv_s2299_verbasresc', to='s2299.s2299verbasResc'),
        ),
        migrations.AddField(
            model_name='s2299infoperapurdetverbas',
            name='s2299_infoperapur_ideestablot',
            field=models.ForeignKey(related_name='s2299infoperapurdetverbas_s2299_infoperapur_ideestablot', to='s2299.s2299infoPerApurideEstabLot'),
        ),
        migrations.AddField(
            model_name='s2299infoperapurdetoper',
            name='s2299_infoperapur_infosaudecolet',
            field=models.ForeignKey(related_name='s2299infoperapurdetoper_s2299_infoperapur_infosaudecolet', to='s2299.s2299infoPerApurinfoSaudeColet'),
        ),
        migrations.AddField(
            model_name='s2299infoperantideestablot',
            name='s2299_infoperant_ideperiodo',
            field=models.ForeignKey(related_name='s2299infoperantideestablot_s2299_infoperant_ideperiodo', to='s2299.s2299infoPerAntidePeriodo'),
        ),
        migrations.AddField(
            model_name='s2299infoperantdetverbas',
            name='s2299_infoperant_ideestablot',
            field=models.ForeignKey(related_name='s2299infoperantdetverbas_s2299_infoperant_ideestablot', to='s2299.s2299infoPerAntideEstabLot'),
        ),
        migrations.AddField(
            model_name='s2299dmdev',
            name='s2299_verbasresc',
            field=models.ForeignKey(related_name='s2299dmdev_s2299_verbasresc', to='s2299.s2299verbasResc'),
        ),
    ]
