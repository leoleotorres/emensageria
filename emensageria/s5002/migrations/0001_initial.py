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
            name='s5002basesIrrf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpvalor', models.IntegerField()),
                ('valor', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5002basesirrf_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5002basesirrf_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5002_infoirrf', 'tpvalor', 'valor'],
                'db_table': 's5002_basesirrf',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5002idePgtoExt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codpais', models.CharField(max_length=3, choices=[(b'008', '008 - Abu Dhabi'), (b'009', '009 - Dirce'), (b'013', '013 - Afeganistao'), (b'017', '017 - Albania, Republica Da'), (b'020', '020 - Alboran-Perejil,Ilhas'), (b'023', '023 - Alemanha'), (b'025', '025 - Alemanha, Republica Democratica'), (b'031', '031 - Burkina Faso'), (b'037', '037 - Andorra'), (b'040', '040 - Angola'), (b'041', '041 - Anguilla'), (b'043', '043 - Antigua E Barbuda'), (b'047', '047 - Antilhas Holandesas'), (b'053', '053 - Arabia Saudita'), (b'059', '059 - Argelia'), (b'063', '063 - Argentina'), (b'064', '064 - Armenia, Republica Da'), (b'065', '065 - Aruba'), (b'069', '069 - Australia'), (b'072', '072 - Austria'), (b'073', '073 - Azerbaijao, Republica Do'), (b'077', '077 - Bahamas, Ilhas'), (b'080', '080 - Bahrein, Ilhas'), (b'081', '081 - Bangladesh'), (b'083', '083 - Barbados'), (b'085', '085 - Belarus, Republica Da'), (b'087', '087 - Belgica'), (b'088', '088 - Belize'), (b'090', '090 - Bermudas'), (b'093', '093 - Mianmar (BIRMANIA)'), (b'097', '097 - Bolivia, Estado Plurinacional Da'), (b'098', '098 - Bosnia-Herzegovina (REPUBLICA Da)'), (b'100', '100 - Int.Z.F.Manaus'), (b'101', '101 - Botsuana'), (b'105', '105 - Brasil'), (b'106', '106 - Fretado P/Brasil'), (b'108', '108 - Brunei'), (b'111', '111 - Bulgaria, Republica Da'), (b'115', '115 - Burundi'), (b'119', '119 - Butao'), (b'127', '127 - Cabo Verde, Republica De'), (b'131', '131 - Cachemira'), (b'137', '137 - Cayman, Ilhas'), (b'141', '141 - Camboja'), (b'145', '145 - Camaroes'), (b'149', '149 - Canada'), (b'150', '150 - Jersey, Ilha Do Canal'), (b'151', '151 - Canarias, Ilhas'), (b'152', '152 - Canal,Ilhas'), (b'153', '153 - Cazaquistao, Republica Do'), (b'154', '154 - Catar'), (b'158', '158 - Chile'), (b'160', '160 - China, Republica Popular'), (b'161', '161 - Formosa (TAIWAN)'), (b'163', '163 - Chipre'), (b'165', '165 - Cocos(Keeling),Ilhas'), (b'169', '169 - Colombia'), (b'173', '173 - Comores, Ilhas'), (b'177', '177 - Congo'), (b'183', '183 - Cook, Ilhas'), (b'187', '187 - Coreia (DO Norte), Rep.Pop.Democratica'), (b'190', '190 - Coreia (DO Sul), Republica Da'), (b'193', '193 - Costa Do Marfim'), (b'195', '195 - Croacia (REPUBLICA Da)'), (b'196', '196 - Costa Rica'), (b'198', '198 - Coveite'), (b'199', '199 - Cuba'), (b'229', '229 - Benin'), (b'232', '232 - Dinamarca'), (b'235', '235 - Dominica,Ilha'), (b'237', '237 - Dubai'), (b'239', '239 - Equador'), (b'240', '240 - Egito'), (b'243', '243 - Eritreia'), (b'244', '244 - Emirados Arabes Unidos'), (b'245', '245 - Espanha'), (b'246', '246 - Eslovenia, Republica Da'), (b'247', '247 - Eslovaca, Republica'), (b'249', '249 - Estados Unidos'), (b'251', '251 - Estonia, Republica Da'), (b'253', '253 - Etiopia'), (b'255', '255 - Falkland (ILHAS Malvinas)'), (b'259', '259 - Feroe, Ilhas'), (b'263', '263 - Fezzan'), (b'267', '267 - Filipinas'), (b'271', '271 - Finlandia'), (b'275', '275 - Franca'), (b'281', '281 - Gabao'), (b'285', '285 - Gambia'), (b'289', '289 - Gana'), (b'291', '291 - Georgia, Republica Da'), (b'293', '293 - Gibraltar'), (b'297', '297 - Granada'), (b'301', '301 - Grecia'), (b'305', '305 - Groenlandia'), (b'309', '309 - Guadalupe'), (b'313', '313 - Guam'), (b'317', '317 - Guatemala'), (b'325', '325 - Guiana Francesa'), (b'329', '329 - Guine'), (b'331', '331 - Guine-Equatorial'), (b'334', '334 - Guine-Bissau'), (b'337', '337 - Guiana'), (b'341', '341 - Haiti'), (b'345', '345 - Honduras'), (b'351', '351 - Hong Kong'), (b'355', '355 - Hungria, Republica Da'), (b'357', '357 - Iemen'), (b'358', '358 - Iemem Do Sul'), (b'359', '359 - Man, Ilha De'), (b'361', '361 - India'), (b'365', '365 - Indonesia'), (b'367', '367 - Inglaterra'), (b'369', '369 - Iraque'), (b'372', '372 - Ira, Republica Islamica Do'), (b'375', '375 - Irlanda'), (b'379', '379 - Islandia'), (b'383', '383 - Israel'), (b'386', '386 - Italia'), (b'388', '388 - Servia E Montenegro'), (b'391', '391 - Jamaica'), (b'395', '395 - Jammu'), (b'396', '396 - Johnston, Ilhas'), (b'399', '399 - Japao'), (b'403', '403 - Jordania'), (b'411', '411 - Kiribati'), (b'420', '420 - Laos, Rep.Pop.Democr.Do'), (b'423', '423 - Lebuan,Ilhas'), (b'426', '426 - Lesoto'), (b'427', '427 - Letonia, Republica Da'), (b'431', '431 - Libano'), (b'434', '434 - Liberia'), (b'438', '438 - Libia'), (b'440', '440 - Liechtenstein'), (b'442', '442 - Lituania, Republica Da'), (b'445', '445 - Luxemburgo'), (b'447', '447 - Macau'), (b'449', '449 - Macedonia, Ant.Rep.Iugoslava'), (b'450', '450 - Madagascar'), (b'452', '452 - Ilha Da Madeira'), (b'455', '455 - Malasia'), (b'458', '458 - Malavi'), (b'461', '461 - Maldivas'), (b'464', '464 - Mali'), (b'467', '467 - Malta'), (b'472', '472 - Marianas Do Norte'), (b'474', '474 - Marrocos'), (b'476', '476 - Marshall,Ilhas'), (b'477', '477 - Martinica'), (b'485', '485 - Mauricio'), (b'488', '488 - Mauritania'), (b'490', '490 - Midway, Ilhas'), (b'493', '493 - Mexico'), (b'494', '494 - Moldavia, Republica Da'), (b'495', '495 - Monaco'), (b'497', '497 - Mongolia'), (b'499', '499 - Micronesia'), (b'501', '501 - Montserrat,Ilhas'), (b'505', '505 - Mocambique'), (b'507', '507 - Namibia'), (b'508', '508 - Nauru'), (b'511', '511 - Christmas,Ilha (NAVIDAD)'), (b'517', '517 - Nepal'), (b'521', '521 - Nicaragua'), (b'525', '525 - Niger'), (b'528', '528 - Nigeria'), (b'531', '531 - Niue,Ilha'), (b'535', '535 - Norfolk,Ilha'), (b'538', '538 - Noruega'), (b'542', '542 - Nova Caledonia'), (b'545', '545 - Papua Nova Guine'), (b'548', '548 - Nova Zelandia'), (b'551', '551 - Vanuatu'), (b'556', '556 - Oma'), (b'563', '563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'), (b'566', '566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'), (b'569', '569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'), (b'573', '573 - Paises Baixos (HOLANDA)'), (b'575', '575 - Palau'), (b'576', '576 - Paquistao'), (b'578', '578 - Palestina'), (b'580', '580 - Panama'), (b'583', '583 - Papua Nova Guin\xe9'), (b'586', '586 - Paraguai'), (b'589', '589 - Peru'), (b'593', '593 - Pitcairn,Ilha'), (b'599', '599 - Polinesia Francesa'), (b'603', '603 - Polonia, Republica Da'), (b'607', '607 - Portugal'), (b'611', '611 - Porto Rico'), (b'623', '623 - Quenia'), (b'625', '625 - Quirguiz, Republica'), (b'628', '628 - Reino Unido'), (b'640', '640 - Republica Centro-Africana'), (b'647', '647 - Republica Dominicana'), (b'660', '660 - Reuniao, Ilha'), (b'665', '665 - Zimbabue'), (b'670', '670 - Romenia'), (b'675', '675 - Ruanda'), (b'676', '676 - Russia, Federacao Da'), (b'677', '677 - Salomao, Ilhas'), (b'678', '678 - Saint Kitts E Nevis'), (b'685', '685 - Saara Ocidental'), (b'687', '687 - El Salvador'), (b'690', '690 - Samoa'), (b'691', '691 - Samoa Americana'), (b'695', '695 - Sao Cristovao E Neves,Ilhas'), (b'697', '697 - San Marino'), (b'700', '700 - Sao Pedro E Miquelon'), (b'705', '705 - Sao Vicente E Granadinas'), (b'710', '710 - Santa Helena'), (b'715', '715 - Santa Lucia'), (b'720', '720 - Sao Tome E Principe, Ilhas'), (b'728', '728 - Senegal'), (b'731', '731 - Seychelles'), (b'735', '735 - Serra Leoa'), (b'738', '738 - Sikkim'), (b'741', '741 - Cingapura'), (b'744', '744 - Siria, Republica Arabe Da'), (b'748', '748 - Somalia'), (b'750', '750 - Sri Lanka'), (b'754', '754 - Suazilandia'), (b'756', '756 - Africa Do Sul'), (b'759', '759 - Sudao'), (b'764', '764 - Suecia'), (b'767', '767 - Suica'), (b'770', '770 - Suriname'), (b'772', '772 - Tadjiquistao, Republica Do'), (b'776', '776 - Tailandia'), (b'780', '780 - Tanzania, Rep.Unida Da'), (b'782', '782 - Territorio Brit.Oc.Indico'), (b'783', '783 - Djibuti'), (b'785', '785 - Territorio da Alta Comissao do Pacifico Ocidental'), (b'788', '788 - Chade'), (b'790', '790 - Tchecoslovaquia'), (b'791', '791 - Tcheca, Republica'), (b'795', '795 - Timor Leste'), (b'800', '800 - Togo'), (b'805', '805 - Toquelau,Ilhas'), (b'810', '810 - Tonga'), (b'815', '815 - Trinidad E Tobago'), (b'820', '820 - Tunisia'), (b'823', '823 - Turcas E Caicos,Ilhas'), (b'824', '824 - Turcomenistao, Republica Do'), (b'827', '827 - Turquia'), (b'828', '828 - Tuvalu'), (b'831', '831 - Ucrania'), (b'833', '833 - Uganda'), (b'840', '840 - Uniao Das Republicas Socialistas Sovieticas'), (b'845', '845 - Uruguai'), (b'847', '847 - Uzbequistao, Republica Do'), (b'848', '848 - Vaticano, Est.Da Cidade Do'), (b'850', '850 - Venezuela'), (b'855', '855 - Vietname Norte'), (b'858', '858 - Vietna'), (b'863', '863 - Virgens,Ilhas (BRITANICAS)'), (b'866', '866 - Virgens,Ilhas (E.U.A.)'), (b'870', '870 - Fiji'), (b'873', '873 - Wake, Ilha'), (b'875', '875 - Wallis E Futuna, Ilhas'), (b'888', '888 - Congo, Republica Democratica Do'), (b'890', '890 - Zambia')])),
                ('indnif', models.IntegerField(choices=[(1, '1 - Benefici\xe1rio com NIF'), (2, '2 - Benefici\xe1rio dispensado do NIF'), (3, '3 - Pa\xeds n\xe3o exige NIF')])),
                ('nifbenef', models.CharField(max_length=20, null=True, blank=True)),
                ('dsclograd', models.CharField(max_length=80)),
                ('nrlograd', models.CharField(max_length=10, null=True, blank=True)),
                ('complem', models.CharField(max_length=30, null=True, blank=True)),
                ('bairro', models.CharField(max_length=60, null=True, blank=True)),
                ('nmcid', models.CharField(max_length=50)),
                ('codpostal', models.CharField(max_length=12, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5002idepgtoext_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5002idepgtoext_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5002_infoirrf', 'codpais', 'indnif', 'nifbenef', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'nmcid', 'codpostal'],
                'db_table': 's5002_idepgtoext',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5002infoDep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vrdeddep', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5002infodep_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5002infodep_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5002_evtirrfbenef', models.OneToOneField(related_name='s5002infodep_s5002_evtirrfbenef', to='eventos.s5002evtIrrfBenef')),
            ],
            options={
                'ordering': ['s5002_evtirrfbenef', 'vrdeddep'],
                'db_table': 's5002_infodep',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5002infoIrrf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcateg', models.IntegerField(blank=True, null=True, choices=[(101, '101 - Empregado - Geral, inclusive o empregado p\xfablico da administra\xe7\xe3o direta ou indireta contratado pela CLT.'), (102, '102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008'), (103, '103 - Empregado - Aprendiz'), (104, '104 - Empregado - Dom\xe9stico'), (105, '105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98'), (106, '106 - Trabalhador Tempor\xe1rio - contrato por prazo determinado nos termos da Lei 6019/74'), (111, '111 - Empregado - contrato de trabalho intermitente'), (201, '201 - Trabalhador Avulso Portu\xe1rio'), (202, '202 - Trabalhador Avulso N\xe3o Portu\xe1rio'), (301, '301 - Servidor P\xfablico Titular de Cargo Efetivo, Magistrado, Ministro de Tribunal de Contas, Conselheiro de Tribunal de Contas e Membro do Minist\xe9rio P\xfablico'), (302, '302 - Servidor P\xfablico Ocupante de Cargo exclusivo em comiss\xe3o'), (303, '303 - Agente Pol\xedtico'), (305, '305 - Servidor P\xfablico indicado para conselho ou \xf3rg\xe3o deliberativo, na condi\xe7\xe3o de representante do governo, \xf3rg\xe3o ou entidade da administra\xe7\xe3o p\xfablica.'), (306, '306 - Servidor P\xfablico Tempor\xe1rio, sujeito a regime administrativo especial definido em lei pr\xf3pria'), (307, '307 - Militar efetivo'), (308, '308 - Conscrito'), (309, '309 - Agente P\xfablico - Outros'), (401, '401 - Dirigente Sindical - informa\xe7\xe3o prestada pelo Sindicato'), (410, '410 - Trabalhador cedido - informa\xe7\xe3o prestada pelo Cession\xe1rio'), (701, '701 - Contribuinte individual - Aut\xf4nomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual'), (711, '711 - Contribuinte individual - Transportador aut\xf4nomo de passageiros'), (712, '712 - Contribuinte individual - Transportador aut\xf4nomo de carga'), (721, '721 - Contribuinte individual - Diretor n\xe3o empregado, com FGTS'), (722, '722 - Contribuinte individual - Diretor n\xe3o empregado, sem FGTS'), (723, '723 - Contribuinte individual - empres\xe1rios, s\xf3cios e membro de conselho de administra\xe7\xe3o ou fiscal'), (731, '731 - Contribuinte individual - Cooperado que presta servi\xe7os por interm\xe9dio de Cooperativa de Trabalho'), (734, '734 - Contribuinte individual - Transportador Cooperado que presta servi\xe7os por interm\xe9dio de cooperativa de trabalho'), (738, '738 - Contribuinte individual - Cooperado filiado a Cooperativa de Produ\xe7\xe3o'), (741, '741 - Contribuinte individual - Microempreendedor Individual'), (751, '751 - Contribuinte individual - magistrado classista tempor\xe1rio da Justi\xe7a do Trabalho ou da Justi\xe7a Eleitoral que seja aposentado de qualquer regime previdenci\xe1rio'), (761, '761 - Contribuinte individual - Associado eleito para dire\xe7\xe3o de Cooperativa, associa\xe7\xe3o ou entidade de classe de qualquer natureza ou finalidade, bem como o s\xedndico ou administrador eleito para exercer atividade de dire\xe7\xe3o condominial, desde que recebam remunera\xe7\xe3o'), (771, '771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei n\xba 8.069, de 13 de julho de 1990'), (781, '781 - Ministro de confiss\xe3o religiosa ou membro de vida consagrada, de congrega\xe7\xe3o ou de ordem religiosa'), (901, '901 - Estagi\xe1rio'), (902, '902 - M\xe9dico Residente'), (903, '903 - Bolsista, nos termos da lei 8958/1994'), (904, '904 - Participante de curso de forma\xe7\xe3o, como etapa de concurso p\xfablico, sem v\xednculo de emprego/estatut\xe1rio'), (905, '905 - Atleta n\xe3o profissional em forma\xe7\xe3o que receba bolsa')])),
                ('indresbr', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5002infoirrf_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5002infoirrf_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5002_evtirrfbenef', models.ForeignKey(related_name='s5002infoirrf_s5002_evtirrfbenef', to='eventos.s5002evtIrrfBenef')),
            ],
            options={
                'ordering': ['s5002_evtirrfbenef', 'codcateg', 'indresbr'],
                'db_table': 's5002_infoirrf',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5002irrf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpcr', models.IntegerField(choices=[(473, '0473-01 - Renda e Proventos de Qualquer Natureza'), (561, '0561-12 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio'), (561, '0561-11 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'), (561, '0561-10 - IRRF - Empregado dom\xe9stico - 13\xba sal\xe1rio'), (561, '0561-09 - IRRF - Empregado Dom\xe9stico - 13\xba Sal Rescis\xe3o'), (561, '0561-08 - IRRF - Empregado Dom\xe9stico'), (561, '0561-07 - IRRF - Rendimento do Trabalho Assalariado no Pa\xeds/Ausente no Exterior a Servi\xe7o do Pa\xeds'), (561, '0561-13 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio rescis\xf3rio'), (588, '0588-06 - IRRF - Rendimento do trabalho sem v\xednculo empregat\xedcio'), (610, '0610-01 - IRRF - Rendimentos relativos a presta\xe7\xe3o de servi\xe7os de transporte rodovi\xe1rio internacional de carga, pagos a transportador aut\xf4nomo PF residente no Paraguai'), (3280, '3280-06 - IRRF - Servi\xe7os Prestados por associados de cooperativas de trabalho'), (3533, '3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pens\xe3o Pagos por Previd\xeancia P\xfablica'), (3562, '3562-01 - IRRF - Participa\xe7\xe3o dos trabalhadores em Lucros ou Resultados (PLR)')])),
                ('vrirrfdesc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5002irrf_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5002irrf_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5002_infoirrf', models.ForeignKey(related_name='s5002irrf_s5002_infoirrf', to='s5002.s5002infoIrrf')),
            ],
            options={
                'ordering': ['s5002_infoirrf', 'tpcr', 'vrirrfdesc'],
                'db_table': 's5002_irrf',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s5002idepgtoext',
            name='s5002_infoirrf',
            field=models.OneToOneField(related_name='s5002idepgtoext_s5002_infoirrf', to='s5002.s5002infoIrrf'),
        ),
        migrations.AddField(
            model_name='s5002basesirrf',
            name='s5002_infoirrf',
            field=models.ForeignKey(related_name='s5002basesirrf_s5002_infoirrf', to='s5002.s5002infoIrrf'),
        ),
    ]