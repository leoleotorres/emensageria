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



CHOICES_S1040_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1202_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2299_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2205_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1250_TPINSCADQ = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5011_TPINSC = (
)

CHOICES_S1200_TPINSC = (
)

CHOICES_S1298_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S2298_INDPAGTOJUIZO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1005_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1280_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1270_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1299_EVTINFOCOMPLPER = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2220_TPASO = (
    (0, u'0 - Admissional'),
    (1, u'1 - Periódico, conforme planejamento do PCMSO'),
    (2, u'2 - De retorno ao trabalho'),
    (3, u'3 - De mudança de função'),
    (4, u'4 - De monitoração pontual, não enquadrado nos casos anteriores'),
    (8, u'8 - Demissional'),
)

CHOICES_S1035_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1298_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1298_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2210_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2240_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1210_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2205_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S2300_CADINI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2300_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S5011_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S1299_EVTREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2399_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1060_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1210_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2299_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2400_PAISNAC = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S1020_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1299_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2200_TPCONTR = (
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado'),
)

CHOICES_S1299_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1060_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1207_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1298_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1020_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1280_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2200_PAISNASCTO = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S2200_TPREGPREV = (
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior'),
)

CHOICES_S2210_TPREGISTRADOR = (
    (1, u'1 - Empregador'),
    (2, u'2 - Cooperativa'),
    (3, u'3 - Sindicato de trabalhadores avulsos não portuários'),
    (4, u'4 - Órgão Gestor de Mão de Obra'),
    (5, u'5 - Empregado'),
    (6, u'6 - Dependente do empregado'),
    (7, u'7 - Entidade Sindical competente'),
    (8, u'8 - Médico assistente'),
    (9, u'9 - Autoridade Pública'),
)

CHOICES_S2200_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1050_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1202_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1270_TPINSC = (
)

CHOICES_S2306_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2210_INDCATOBITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2260_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2298_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2306_CODCATEG = (
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

CHOICES_S1210_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1207_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1210_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1295_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2400_TPPLANRP = (
    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro'),
)

CHOICES_S2200_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S1300_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2190_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2300_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2190_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2240_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1005_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1260_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2300_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2250_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2210_INDCOMUNPOLICIA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1030_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1207_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S2205_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1260_TPINSC = (
)

CHOICES_S2200_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S1005_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1295_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2300_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2200_TPINSC = (
)

CHOICES_S2200_PAISNAC = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S2260_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2300_PAISNASCTO = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S2200_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1070_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2210_CODSITGERADORA = (
    (200004300, u'200004300 - Impacto de pessoa contra objeto parado'),
    (200004600, u'200004600 - Impacto de pessoa contra objeto em movimento'),
    (200008300, u'200008300 - Impacto sofrido por pessoa de objeto que cai'),
    (200008600, u'200008600 - Impacto sofrido por pessoa de objeto projetado'),
    (200008900, u'200008900 - Impacto sofrido por pessoa, NIC'),
    (200012200, u'200012200 - Queda de pessoa com diferença de nível de andaime, passagem, plataforma, etc.'),
    (200012300, u'200012300 - Queda de pessoa com diferença de nível de escada móvel ou fixada cujos degraus'),
    (200012400, u'200012400 - Queda de pessoa com diferença de nível de material empilhado'),
    (200012500, u'200012500 - Queda de pessoa com diferença de nível de veículo'),
    (200012600, u'200012600 - Queda de pessoa com diferença de nível em escada permanente'),
    (200012700, u'200012700 - Queda de pessoa com diferença de nível em poço, escavação, abertura no piso, etc.'),
    (200012900, u'200012900 - Queda de pessoa com diferença de nível, NIC'),
    (200016300, u'200016300 - Queda de pessoa em mesmo nível em passagem ou superfície de sustentação'),
    (200016600, u'200016600 - Queda de pessoa em mesmo nível sobre ou contra alguma coisa'),
    (200016900, u'200016900 - Queda de pessoa em mesmo nível, NIC'),
    (200020100, u'200020100 - Aprisionamento em, sobre ou entre objetos em movimento convergente'),
    (200020300, u'200020300 - Aprisionamento em, sobre ou entre objeto parado e outro em movimento'),
    (200020500, u'200020500 - Aprisionamento em, sobre ou entre dois ou mais objetos em movimento'),
    (200020700, u'200020700 - Aprisionamento em, sobre ou entre desabamento ou desmoronamento'),
    (200020900, u'200020900 - Aprisionamento em, sob ou entre, NIC'),
    (200024300, u'200024300 - Atrito ou abrasão por encostar, pisar, ajoelhar ou sentar em objeto'),
    (200024400, u'200024400 - Atrito ou abrasão por manusear objeto'),
    (200024500, u'200024500 - Atrito ou abrasão por objeto em vibração'),
    (200024600, u'200024600 - Atrito ou abrasão por corpo estranho no olho'),
    (200024700, u'200024700 - Atrito ou abrasão por compressão repetitiva'),
    (200024900, u'200024900 - Atrito ou abrasão, NIC'),
    (200028300, u'200028300 - Reação do corpo a movimento involuntário'),
    (200028600, u'200028600 - Reação do corpo a movimento voluntário'),
    (200032200, u'200032200 - Esforço excessivo ao erguer objeto'),
    (200032400, u'200032400 - Esforço excessivo ao empurrar ou puxar objeto'),
    (200032600, u'200032600 - Esforço excessivo ao manejar, sacudir ou arremessar objeto'),
    (200032900, u'200032900 - Esforço excessivo, NIC'),
    (200036000, u'200036000 - Elétrica, exposição a energia'),
    (200040300, u'200040300 - Temperatura muito alta, contato com objeto ou substância a'),
    (200040600, u'200040600 - Temperatura muito baixa, contato com objeto ou substância a'),
    (200044300, u'200044300 - Temperatura ambiente elevada, exposição a'),
    (200044600, u'200044600 - Temperatura ambiente baixa, exposição a'),
    (200048200, u'200048200 - Inalação de substância cáustica, tóxica ou nociva'),
    (200048400, u'200048400 - Ingestão de substância cáustica'),
    (200048600, u'200048600 - Absorção de substância cáustica'),
    (200048900, u'200048900 - Inalação, ingestão ou absorção, NIC'),
    (200052000, u'200052000 - Imersão'),
    (200056000, u'200056000 - Radiação não ionizante, exposição a'),
    (200060000, u'200060000 - Radiação ionizante, exposição a'),
    (200064000, u'200064000 - Ruído, exposição a'),
    (200068000, u'200068000 - Vibração, exposição a'),
    (200072000, u'200072000 - Pressão ambiente, exposição a'),
    (200072300, u'200072300 - Exposição à pressão ambiente elevada'),
    (200072600, u'200072600 - Exposição à pressão ambiente baixa'),
    (200076200, u'200076200 - Poluição da água, ação da (exposição à poluição da água)'),
    (200076400, u'200076400 - Poluição do ar, ação da (exposição à poluição do ar)'),
    (200076600, u'200076600 - Poluição do solo, ação da (exposição à poluição do solo)'),
    (200076900, u'200076900 - Poluição, NIC, exposição a (exposição à poluição, NIC)'),
    (200080200, u'200080200 - Ataque de ser vivo por mordedura, picada, chifrada, coice, etc.'),
    (200080400, u'200080400 - Ataque de ser vivo com peçonha'),
    (200080600, u'200080600 - Ataque de ser vivo com transmissão de doença'),
    (200080900, u'200080900 - Ataque de ser vivo, NIC'),
    (209000000, u'209000000 - Tipo, NIC'),
    (209500000, u'209500000 - Tipo inexistente'),
)

CHOICES_S1080_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2205_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2299_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2240_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1010_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2210_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2400_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

MUNICIPIOS = (
    ('00013', u'Acrelândia (AC)'),
    ('00015', u'Alta Floresta D`Oeste (RO)'),
    ('00023', u'Ariquemes (RO)'),
    ('00027', u'Amajari (RR)'),
    ('00029', u'Alvarães (AM)'),
    ('00031', u'Cabixi (RO)'),
    ('00034', u'Aceguá (RS)'),
    ('00049', u'Cacoal (RO)'),
    ('00050', u'Alto Alegre (RR)'),
    ('00050', u'Abadia de Goiás (GO)'),
    ('00051', u'Abdon Batista (SC)'),
    ('00053', u'Acauã (PI)'),
    ('00054', u'Abreu e Lima (PE)'),
    ('00054', u'Assis Brasil (AC)'),
    ('00055', u'Açailândia (MA)'),
    ('00055', u'Serra do Navio (AP)'),
    ('00056', u'Cerejeiras (RO)'),
    ('00059', u'Água Santa (RS)'),
    ('00060', u'Amaturá (AM)'),
    ('00064', u'Colorado do Oeste (RO)'),
    ('00072', u'Corumbiara (RO)'),
    ('00080', u'Costa Marques (RO)'),
    ('00086', u'Anamã (AM)'),
    ('00098', u'Espigão D`Oeste (RO)'),
    ('00100', u'Boa Vista (RR)'),
    ('00100', u'Amparo de São Francisco (SE)'),
    ('00100', u'Angra dos Reis (RJ)'),
    ('00100', u'Abadiânia (GO)'),
    ('00101', u'Abaiara (CE)'),
    ('00101', u'Abelardo Luz (SC)'),
    ('00102', u'Afonso Cláudio (ES)'),
    ('00102', u'Anori (AM)'),
    ('00102', u'Acorizal (MT)'),
    ('00102', u'Água Branca (AL)'),
    ('00103', u'Abatiá (PR)'),
    ('00103', u'Agricolândia (PI)'),
    ('00104', u'Afogados da Ingazeira (PE)'),
    ('00104', u'Brasiléia (AC)'),
    ('00104', u'Abadia dos Dourados (MG)'),
    ('00105', u'Amapá (AP)'),
    ('00105', u'Adamantina (SP)'),
    ('00105', u'Afonso Cunha (MA)'),
    ('00106', u'Guajará-Mirim (RO)'),
    ('00106', u'Água Branca (PB)'),
    ('00107', u'Abaetetuba (PA)'),
    ('00108', u'Brasília (DF)'),
    ('00108', u'Abaíra (BA)'),
    ('00109', u'Agudo (RS)'),
    ('00109', u'Acari (RN)'),
    ('00114', u'Jaru (RO)'),
    ('00122', u'Ji-Paraná (RO)'),
    ('00130', u'Machadinho D`Oeste (RO)'),
    ('00131', u'Abel Figueiredo (PA)'),
    ('00134', u'Acreúna (GO)'),
    ('00136', u'Águia Branca (ES)'),
    ('00138', u'Bujari (AC)'),
    ('00144', u'Apuí (AM)'),
    ('00148', u'Nova Brasilândia D`Oeste (RO)'),
    ('00150', u'Acarape (CE)'),
    ('00154', u'Água Doce do Maranhão (MA)'),
    ('00154', u'Pedra Branca do Amapari (AP)'),
    ('00155', u'Ouro Preto do Oeste (RO)'),
    ('00159', u'Bonfim (RR)'),
    ('00159', u'Adelândia (GO)'),
    ('00159', u'Aperibé (RJ)'),
    ('00169', u'Água Doce do Norte (ES)'),
    ('00175', u'Cantá (RR)'),
    ('00175', u'Água Fria de Goiás (GO)'),
    ('00179', u'Capixaba (AC)'),
    ('00189', u'Pimenta Bueno (RO)'),
    ('00200', u'Acaraú (CE)'),
    ('00200', u'Agrolândia (SC)'),
    ('00201', u'Atalaia do Norte (AM)'),
    ('00201', u'Anadia (AL)'),
    ('00201', u'Água Boa (MT)'),
    ('00201', u'Alegre (ES)'),
    ('00202', u'Água Branca (PI)'),
    ('00202', u'Adrianópolis (PR)'),
    ('00203', u'Afrânio (PE)'),
    ('00203', u'Água Clara (MS)'),
    ('00203', u'Abaeté (MG)'),
    ('00203', u'Cruzeiro do Sul (AC)'),
    ('00204', u'Calçoene (AP)'),
    ('00204', u'Alcântara (MA)'),
    ('00204', u'Adolfo (SP)'),
    ('00205', u'Aguiar (PB)'),
    ('00205', u'Porto Velho (RO)'),
    ('00206', u'Acará (PA)'),
    ('00207', u'Abaré (BA)'),
    ('00208', u'Ajuricaba (RS)'),
    ('00208', u'Açu (RN)'),
    ('00209', u'Caracaraí (RR)'),
    ('00209', u'Aquidabã (SE)'),
    ('00209', u'Água Limpa (GO)'),
    ('00209', u'Araruama (RJ)'),
    ('00212', u'Cutias (AP)'),
    ('00225', u'Areal (RJ)'),
    ('00233', u'Armação dos Búzios (RJ)'),
    ('00233', u'Caroebe (RR)'),
    ('00238', u'Ferreira Gomes (AP)'),
    ('00250', u'Alta Floresta (MT)'),
    ('00251', u'Alagoinha do Piauí (PI)'),
    ('00251', u'Abreulândia (TO)'),
    ('00252', u'Alcinópolis (MS)'),
    ('00252', u'Epitaciolândia (AC)'),
    ('00253', u'Itaubal (AP)'),
    ('00254', u'Presidente Médici (RO)'),
    ('00258', u'Águas Lindas de Goiás (GO)'),
    ('00258', u'Arraial do Cabo (RJ)'),
    ('00262', u'Rio Crespo (RO)'),
    ('00277', u'Alegrete do Piauí (PI)'),
    ('00279', u'Laranjal do Jari (AP)'),
    ('00282', u'Iracema (RR)'),
    ('00288', u'Rolim de Moura (RO)'),
    ('00296', u'Santa Luzia D`Oeste (RO)'),
    ('00300', u'Autazes (AM)'),
    ('00300', u'Alto Araguaia (MT)'),
    ('00300', u'Arapiraca (AL)'),
    ('00300', u'Alfredo Chaves (ES)'),
    ('00301', u'Alto Longá (PI)'),
    ('00301', u'Agudos do Sul (PR)'),
    ('00301', u'Aguiarnópolis (TO)'),
    ('00302', u'Feijó (AC)'),
    ('00302', u'Abre Campo (MG)'),
    ('00302', u'Agrestina (PE)'),
    ('00303', u'Macapá (AP)'),
    ('00303', u'Aguaí (SP)'),
    ('00303', u'Aldeias Altas (MA)'),
    ('00304', u'Vilhena (RO)'),
    ('00304', u'Alagoa Grande (PB)'),
    ('00305', u'Afuá (PA)'),
    ('00306', u'Acajutiba (BA)'),
    ('00307', u'Afonso Bezerra (RN)'),
    ('00307', u'Alecrim (RS)'),
    ('00308', u'Alexânia (GO)'),
    ('00308', u'Barra do Piraí (RJ)'),
    ('00308', u'Mucajaí (RR)'),
    ('00308', u'Aracaju (SE)'),
    ('00309', u'Acopiara (CE)'),
    ('00309', u'Agronômica (SC)'),
    ('00320', u'São Miguel do Guaporé (RO)'),
    ('00328', u'Jordão (AC)'),
    ('00336', u'Mâncio Lima (AC)'),
    ('00338', u'Nova Mamoré (RO)'),
    ('00344', u'Manoel Urbano (AC)'),
    ('00346', u'Alvorada D`Oeste (RO)'),
    ('00347', u'Água Azul do Norte (PA)'),
    ('00350', u'Aliança do Tocantins (TO)'),
    ('00351', u'Marechal Thaumaturgo (AC)'),
    ('00355', u'Adustina (BA)'),
    ('00359', u'Alto Rio Novo (ES)'),
    ('00359', u'Alto Boa Vista (MT)'),
    ('00379', u'Alto Alegre dos Parecis (RO)'),
    ('00385', u'Plácido de Castro (AC)'),
    ('00393', u'Porto Walter (AC)'),
    ('00400', u'Almirante Tamandaré (PR)'),
    ('00400', u'Almas (TO)'),
    ('00400', u'Altos (PI)'),
    ('00401', u'Água Preta (PE)'),
    ('00401', u'Acaiaca (MG)'),
    ('00401', u'Rio Branco (AC)'),
    ('00402', u'Mazagão (AP)'),
    ('00402', u'Altamira do Maranhão (MA)'),
    ('00402', u'Águas da Prata (SP)'),
    ('00403', u'Alto Paraíso (RO)'),
    ('00403', u'Alagoa Nova (PB)'),
    ('00404', u'Alenquer (PA)'),
    ('00405', u'Água Fria (BA)'),
    ('00406', u'Água Nova (RN)'),
    ('00406', u'Alegrete (RS)'),
    ('00407', u'Barra Mansa * (RJ)'),
    ('00407', u'Normandia (RR)'),
    ('00407', u'Arauá (SE)'),
    ('00408', u'Água Doce (SC)'),
    ('00408', u'Aiuaba (CE)'),
    ('00409', u'Atalaia (AL)'),
    ('00409', u'Anchieta (ES)'),
    ('00409', u'Barcelos (AM)'),
    ('00409', u'Alto Garças (MT)'),
    ('00427', u'Rodrigues Alves (AC)'),
    ('00435', u'Santa Rosa do Purus (AC)'),
    ('00436', u'Alto Alegre do Maranhão (MA)'),
    ('00450', u'Senador Guiomard (AC)'),
    ('00452', u'Buritis (RO)'),
    ('00455', u'Alegria (RS)'),
    ('00456', u'Belford Roxo * (RJ)'),
    ('00456', u'Pacaraima (RR)'),
    ('00459', u'Alvorada do Gurguéia (PI)'),
    ('00459', u'Altamira do Paraná (PR)'),
    ('00471', u'Almirante Tamandaré do Sul (RS)'),
    ('00472', u'Rorainópolis (RR)'),
    ('00477', u'Alto Alegre do Pindaré (MA)'),
    ('00500', u'Águas Belas (PE)'),
    ('00500', u'Sena Madureira (AC)'),
    ('00500', u'Açucena (MG)'),
    ('00501', u'Águas de Lindóia (SP)'),
    ('00501', u'Oiapoque (AP)'),
    ('00501', u'Alto Parnaíba (MA)'),
    ('00502', u'Novo Horizonte do Oeste (RO)'),
    ('00502', u'Alagoinha (PB)'),
    ('00503', u'Almeirim (PA)'),
    ('00504', u'Érico Cardoso (BA)'),
    ('00505', u'Alexandria (RN)'),
    ('00505', u'Alpestre (RS)'),
    ('00506', u'São João da Baliza (RR)'),
    ('00506', u'Areia Branca (SE)'),
    ('00506', u'Bom Jardim (RJ)'),
    ('00506', u'Aloândia (GO)'),
    ('00507', u'Águas de Chapecó (SC)'),
    ('00507', u'Alcântaras (CE)'),
    ('00508', u'Barra de Santo Antônio (AL)'),
    ('00508', u'Alto Paraguai (MT)'),
    ('00508', u'Apiacá (ES)'),
    ('00508', u'Barreirinha (AM)'),
    ('00509', u'Altônia (PR)'),
    ('00509', u'Amarante (PI)'),
    ('00535', u'Porto Grande (AP)'),
    ('00536', u'Alcantil (PB)'),
    ('00550', u'Águas de Santa Bárbara (SP)'),
    ('00550', u'Amapá do Maranhão (MA)'),
    ('00550', u'Pracuúba (AP)'),
    ('00554', u'Alto Alegre (RS)'),
    ('00555', u'Alto Horizonte (GO)'),
    ('00556', u'Águas Frias (SC)'),
    ('00570', u'Alto Feliz (RS)'),
    ('00577', u'Algodão de Jandaíra (PB)'),
    ('00600', u'Santana (AP)'),
    ('00600', u'Águas de São Pedro (SP)'),
    ('00600', u'Amarante do Maranhão (MA)'),
    ('00601', u'Alhandra (PB)'),
    ('00601', u'Cacaulândia (RO)'),
    ('00602', u'Altamira (PA)'),
    ('00603', u'Aiquara (BA)'),
    ('00604', u'Almino Afonso (RN)'),
    ('00604', u'Alvorada * (RS)'),
    ('00605', u'São Luiz (RR)'),
    ('00605', u'Barra dos Coqueiros (SE)'),
    ('00605', u'Alto Paraíso de Goiás (GO)'),
    ('00605', u'Bom Jesus do Itabapoana (RJ)'),
    ('00606', u'Águas Mornas (SC)'),
    ('00606', u'Altaneira (CE)'),
    ('00607', u'Barra de São Miguel (AL)'),
    ('00607', u'Alto Taquari (MT)'),
    ('00607', u'Aracruz (ES)'),
    ('00607', u'Benjamin Constant (AM)'),
    ('00608', u'Alto Paraná (PR)'),
    ('00608', u'Angical do Piauí (PI)'),
    ('00609', u'Água Boa (MG)'),
    ('00609', u'Alagoinha (PE)'),
    ('00609', u'Amambaí (MS)'),
    ('00609', u'Tarauacá (AC)'),
    ('00631', u'Beruri (AM)'),
    ('00638', u'Amaral Ferrador (RS)'),
    ('00646', u'Ametista do Sul (RS)'),
    ('00661', u'André da Rocha (RS)'),
    ('00670', u'Boquim (SE)'),
    ('00680', u'Boa Vista do Ramos (AM)'),
    ('00700', u'São João do Rio do Peixe (PB)'),
    ('00700', u'Campo Novo de Rondônia (RO)'),
    ('00701', u'Anajás (PA)'),
    ('00702', u'Alagoinhas (BA)'),
    ('00703', u'Alto do Rodrigues (RN)'),
    ('00703', u'Anta Gorda (RS)'),
    ('00704', u'Cabo Frio (RJ)'),
    ('00704', u'Uiramutã (RR)'),
    ('00704', u'Brejo Grande (SE)'),
    ('00705', u'Alfredo Wagner (SC)'),
    ('00705', u'Alto Santo (CE)'),
    ('00706', u'Atilio Vivacqua (ES)'),
    ('00706', u'Batalha (AL)'),
    ('00706', u'Boca do Acre (AM)'),
    ('00707', u'Alto Piquiri (PR)'),
    ('00707', u'Anísio de Abreu (PI)'),
    ('00707', u'Alvorada (TO)'),
    ('00708', u'Água Comprida (MG)'),
    ('00708', u'Xapuri (AC)'),
    ('00708', u'Anastácio (MS)'),
    ('00708', u'Aliança (PE)'),
    ('00709', u'Anajatuba (MA)'),
    ('00709', u'Tartarugalzinho (AP)'),
    ('00709', u'Agudos (SP)'),
    ('00734', u'Amparo (PB)'),
    ('00754', u'Amontada (CE)'),
    ('00754', u'Alto Bela Vista (SC)'),
    ('00758', u'Alambari (SP)'),
    ('00775', u'Aparecida (PB)'),
    ('00800', u'Ananindeua * (PA)'),
    ('00801', u'Alcobaça (BA)'),
    ('00802', u'Angicos (RN)'),
    ('00802', u'Antônio Prado (RS)'),
    ('00803', u'Alvorada do Norte (GO)'),
    ('00803', u'Cachoeiras de Macacu (RJ)'),
    ('00804', u'Anchieta (SC)'),
    ('00804', u'Antonina do Norte (CE)'),
    ('00805', u'Apiacás (MT)'),
    ('00805', u'Baixo Guandu (ES)'),
    ('00805', u'Borba (AM)'),
    ('00805', u'Belém (AL)'),
    ('00806', u'Antônio Almeida (PI)'),
    ('00806', u'Alvorada do Sul (PR)'),
    ('00807', u'Aguanil (MG)'),
    ('00807', u'Anaurilândia (MS)'),
    ('00807', u'Porto Acre (AC)'),
    ('00807', u'Altinho (PE)'),
    ('00808', u'Vitória do Jari (AP)'),
    ('00808', u'Alfredo Marcondes (SP)'),
    ('00808', u'Anapurus (MA)'),
    ('00809', u'Araçagi (PB)'),
    ('00809', u'Candeias do Jamari (RO)'),
    ('00829', u'Amaralina (GO)'),
    ('00832', u'Apicum-Açu (MA)'),
    ('00839', u'Caapiranga (AM)'),
    ('00851', u'Arambaré (RS)'),
    ('00852', u'Americano do Brasil (GO)'),
    ('00856', u'Angélica (MS)'),
    ('00859', u'Anapu (PA)'),
    ('00873', u'Araguanã (MA)'),
    ('00877', u'Araricá (RS)'),
    ('00900', u'Almadina (BA)'),
    ('00901', u'Antônio Martins (RN)'),
    ('00901', u'Aratiba (RS)'),
    ('00902', u'Cambuci (RJ)'),
    ('00902', u'Amorinópolis (GO)'),
    ('00903', u'Apuiarés (CE)'),
    ('00903', u'Angelina (SC)'),
    ('00904', u'Belo Monte (AL)'),
    ('00904', u'Canutama (AM)'),
    ('00904', u'Barra de São Francisco (ES)'),
    ('00905', u'Amaporã (PR)'),
    ('00905', u'Aroazes (PI)'),
    ('00906', u'Águas Formosas (MG)'),
    ('00906', u'Antônio João (MS)'),
    ('00906', u'Amaraji (PE)'),
    ('00907', u'Altair (SP)'),
    ('00907', u'Araioses (MA)'),
    ('00908', u'Castanheiras (RO)'),
    ('00908', u'Arara (PB)'),
    ('00909', u'Augusto Corrêa (PA)'),
    ('00924', u'Chupinguaia (RO)'),
    ('00936', u'Carapebus (RJ)'),
    ('00940', u'Cujubim (RO)'),
    ('00951', u'Comendador Levy Gasparian (RJ)'),
    ('00954', u'Aroeiras do Itaim (PI)'),
    ('00956', u'Arame (MA)'),
    ('00958', u'Aurora do Pará (PA)'),
    ('01000', u'Aquiraz (CE)'),
    ('01000', u'Anita Garibaldi (SC)'),
    ('01001', u'Boca da Mata (AL)'),
    ('01001', u'Boa Esperança (ES)'),
    ('01001', u'Carauari (AM)'),
    ('01001', u'Araguaiana (MT)'),
    ('01002', u'Arraial (PI)'),
    ('01002', u'Ampére (PR)'),
    ('01002', u'Ananás (TO)'),
    ('01003', u'Águas Vermelhas (MG)'),
    ('01003', u'Aparecida do Taboado (MS)'),
    ('01003', u'Angelim (PE)'),
    ('01004', u'Altinópolis (SP)'),
    ('01004', u'Arari (MA)'),
    ('01005', u'Governador Jorge Teixeira (RO)'),
    ('01005', u'Araruna (PB)'),
    ('01006', u'Aveiro (PA)'),
    ('01007', u'Amargosa (BA)'),
    ('01008', u'Apodi (RN)'),
    ('01008', u'Arroio do Meio (RS)'),
    ('01009', u'Campo do Brito (SE)'),
    ('01009', u'Campos dos Goytacazes * (RJ)'),
    ('01051', u'Angico (TO)'),
    ('01051', u'Assunção do Piauí (PI)'),
    ('01051', u'Anahy (PR)'),
    ('01052', u'Araçoiaba (PE)'),
    ('01057', u'Arroio do Sal (RS)'),
    ('01073', u'Arroio do Padre (RS)'),
    ('01100', u'Careiro (AM)'),
    ('01100', u'Branquinha (AL)'),
    ('01100', u'Bom Jesus do Norte (ES)'),
    ('01101', u'Avelino Lopes (PI)'),
    ('01101', u'Aparecida do Rio Negro (TO)'),
    ('01101', u'Andirá (PR)'),
    ('01102', u'Araripina (PE)'),
    ('01102', u'Aimorés (MG)'),
    ('01102', u'Aquidauana (MS)'),
    ('01103', u'Alto Alegre (SP)'),
    ('01103', u'Axixá (MA)'),
    ('01104', u'Itapuã do Oeste (RO)'),
    ('01104', u'Areia (PB)'),
    ('01105', u'Bagre (PA)'),
    ('01106', u'Amélia Rodrigues (BA)'),
    ('01107', u'Areia Branca (RN)'),
    ('01107', u'Arroio dos Ratos (RS)'),
    ('01108', u'Anápolis * (GO)'),
    ('01108', u'Canhoba (SE)'),
    ('01108', u'Cantagalo (RJ)'),
    ('01109', u'Anitápolis (SC)'),
    ('01109', u'Aracati (CE)'),
    ('01150', u'Ângulo (PR)'),
    ('01150', u'Baixa Grande do Ribeiro (PI)'),
    ('01152', u'Alumínio (SP)'),
    ('01153', u'Areia de Baraúnas (PB)'),
    ('01155', u'América Dourada (BA)'),
    ('01157', u'Cardoso Moreira (RJ)'),
    ('01159', u'Brejetuba (ES)'),
    ('01159', u'Careiro da Várzea (AM)'),
    ('01176', u'Barra D`Alcântara (PI)'),
    ('01200', u'Antonina (PR)'),
    ('01200', u'Barras (PI)'),
    ('01201', u'Arcoverde (PE)'),
    ('01201', u'Aiuruoca (MG)'),
    ('01202', u'Álvares Florence (SP)'),
    ('01202', u'Bacabal (MA)'),
    ('01203', u'Areial (PB)'),
    ('01203', u'Ministro Andreazza (RO)'),
    ('01204', u'Baião (PA)'),
    ('01205', u'Anagé (BA)'),
    ('01206', u'Arês (RN)'),
    ('01206', u'Arroio do Tigre (RS)'),
    ('01207', u'Carmo (RJ)'),
    ('01207', u'Canindé de São Francisco (SE)'),
    ('01207', u'Anhanguera (GO)'),
    ('01208', u'Antônio Carlos (SC)'),
    ('01208', u'Aracoiaba (CE)'),
    ('01209', u'Cachoeiro de Itapemirim * (ES)'),
    ('01209', u'Araguainha (MT)'),
    ('01209', u'Coari (AM)'),
    ('01209', u'Cacimbinhas (AL)'),
    ('01243', u'Aral Moreira (MS)'),
    ('01251', u'Bacabeira (MA)'),
    ('01253', u'Bannach (PA)'),
    ('01257', u'Apiúna (SC)'),
    ('01257', u'Ararendá (CE)'),
    ('01258', u'Araputanga (MT)'),
    ('01273', u'Arabutã (SC)'),
    ('01300', u'Alagoa (MG)'),
    ('01300', u'Barra de Guabiraba (PE)'),
    ('01301', u'Álvares Machado (SP)'),
    ('01301', u'Bacuri (MA)'),
    ('01302', u'Aroeiras (PB)'),
    ('01302', u'Mirante da Serra (RO)'),
    ('01303', u'Barcarena (PA)'),
    ('01304', u'Andaraí (BA)'),
    ('01305', u'Augusto Severo (RN)'),
    ('01305', u'Arroio Grande (RS)'),
    ('01306', u'Capela (SE)'),
    ('01306', u'Anicuns (GO)'),
    ('01306', u'Casimiro de Abreu (RJ)'),
    ('01307', u'Araquari (SC)'),
    ('01307', u'Araripe (CE)'),
    ('01308', u'Arenápolis (MT)'),
    ('01308', u'Cariacica * (ES)'),
    ('01308', u'Codajás (AM)'),
    ('01308', u'Cajueiro (AL)'),
    ('01309', u'Aragominas (TO)'),
    ('01309', u'Antônio Olinto (PR)'),
    ('01309', u'Barreiras do Piauí (PI)'),
    ('01350', u'Bacurituba (MA)'),
    ('01351', u'Assunção (PB)'),
    ('01353', u'Andorinha (BA)'),
    ('01357', u'Campestre (AL)'),
    ('01400', u'Álvaro de Carvalho (SP)'),
    ('01400', u'Balsas (MA)'),
    ('01401', u'Baía da Traição (PB)'),
    ('01401', u'Monte Negro (RO)'),
    ('01402', u'Belém * (PA)'),
    ('01403', u'Angical (BA)'),
    ('01404', u'Arvorezinha (RS)'),
    ('01404', u'Baía Formosa (RN)'),
    ('01405', u'Carira (SE)'),
    ('01405', u'Conceição de Macabu (RJ)'),
    ('01405', u'Aparecida de Goiânia * (GO)'),
    ('01406', u'Araranguá (SC)'),
    ('01406', u'Aratuba (CE)'),
    ('01407', u'Eirunepé (AM)'),
    ('01407', u'Castelo (ES)'),
    ('01407', u'Aripuanã (MT)'),
    ('01407', u'Campo Alegre (AL)'),
    ('01408', u'Apucarana (PR)'),
    ('01408', u'Barro Duro (PI)'),
    ('01409', u'Barreiros (PE)'),
    ('01409', u'Albertina (MG)'),
    ('01435', u'Nova União (RO)'),
    ('01450', u'Parecis (RO)'),
    ('01451', u'Belterra (PA)'),
    ('01453', u'Baraúna (RN)'),
    ('01454', u'Aparecida do Rio Doce (GO)'),
    ('01468', u'Pimenteiras do Oeste (RO)'),
    ('01476', u'Primavera de Rondônia (RO)'),
    ('01484', u'São Felipe D`Oeste (RO)'),
    ('01492', u'São Francisco do Guaporé (RO)'),
    ('01500', u'Bananeiras (PB)'),
    ('01500', u'Seringueiras (RO)'),
    ('01501', u'Benevides (PA)'),
    ('01502', u'Anguera (BA)'),
    ('01503', u'Barcelona (RN)'),
    ('01503', u'Augusto Pestana (RS)'),
    ('01504', u'Carmópolis (SE)'),
    ('01504', u'Cordeiro (RJ)'),
    ('01504', u'Aporé (GO)'),
    ('01505', u'Arneiroz (CE)'),
    ('01505', u'Armazém (SC)'),
    ('01506', u'Campo Grande (AL)'),
    ('01506', u'Colatina (ES)'),
    ('01506', u'Envira (AM)'),
    ('01507', u'Arapongas (PR)'),
    ('01507', u'Batalha (PI)'),
    ('01508', u'Bandeirantes (MS)'),
    ('01508', u'Belém de Maria (PE)'),
    ('01508', u'Além Paraíba (MG)'),
    ('01509', u'Barão de Grajaú (MA)'),
    ('01509', u'Alvinlândia (SP)'),
    ('01534', u'Baraúna (PB)'),
    ('01552', u'Áurea (RS)'),
    ('01556', u'Bela Vista do Piauí (PI)'),
    ('01559', u'Teixeirópolis (RO)'),
    ('01572', u'Belém do Piauí (PI)'),
    ('01575', u'Barra de Santana (PB)'),
    ('01576', u'Bom Jesus do Tocantins (PA)'),
    ('01600', u'Bonito (PA)'),
    ('01601', u'Antas (BA)'),
    ('01602', u'Bento Fernandes (RN)'),
    ('01602', u'Bagé (RS)'),
    ('01603', u'Duas Barras (RJ)'),
    ('01603', u'Araçu (GO)'),
    ('01603', u'Cedro de São João (SE)'),
    ('01604', u'Arroio Trinta (SC)'),
    ('01604', u'Assaré (CE)'),
    ('01605', u'Barão de Melgaço (MT)'),
    ('01605', u'Canapi (AL)'),
    ('01605', u'Fonte Boa (AM)'),
    ('01605', u'Conceição da Barra (ES)'),
    ('01606', u'Beneditinos (PI)'),
    ('01606', u'Arapoti (PR)'),
    ('01607', u'Alfenas (MG)'),
    ('01607', u'Belém de São Francisco (PE)'),
    ('01608', u'Americana * (SP)'),
    ('01608', u'Barra do Corda (MA)'),
    ('01609', u'Barra de Santa Rosa (PB)'),
    ('01609', u'Theobroma (RO)'),
    ('01631', u'Alfredo Vasconcelos (MG)'),
    ('01636', u'Balneário Pinhal (RS)'),
    ('01651', u'Bodó (RN)'),
    ('01651', u'Barão (RS)'),
    ('01653', u'Arvoredo (SC)'),
    ('01654', u'Guajará (AM)'),
    ('01655', u'Arapuã (PR)'),
    ('01700', u'Antônio Cardoso (BA)'),
    ('01701', u'Bom Jesus (RN)'),
    ('01701', u'Barão de Cotegipe (RS)'),
    ('01702', u'Duque de Caxias * (RJ)'),
    ('01702', u'Aragarças (GO)'),
    ('01702', u'Cristinápolis (SE)'),
    ('01703', u'Aurora (CE)'),
    ('01703', u'Ascurra (SC)'),
    ('01704', u'Conceição do Castelo (ES)'),
    ('01704', u'Capela (AL)'),
    ('01704', u'Barra do Bugres (MT)'),
    ('01704', u'Humaitá (AM)'),
    ('01705', u'Bertolínia (PI)'),
    ('01705', u'Araruna (PR)'),
    ('01706', u'Belo Jardim (PE)'),
    ('01706', u'Almenara (MG)'),
    ('01707', u'Barreirinhas (MA)'),
    ('01707', u'Américo Brasiliense (SP)'),
    ('01708', u'Urupá (RO)'),
    ('01708', u'Barra de São Miguel (PB)'),
    ('01709', u'Bragança (PA)'),
    ('01725', u'Brasil Novo (PA)'),
    ('01731', u'Belágua (MA)'),
    ('01739', u'Betânia do Piauí (PI)'),
    ('01750', u'Barão do Triunfo (RS)'),
    ('01757', u'Vale do Anari (RO)'),
    ('01758', u'Brejo Grande do Araguaia (PA)'),
    ('01770', u'Boa Hora (PI)'),
    ('01772', u'Bela Vista do Maranhão (MA)'),
    ('01782', u'Breu Branco (PA)'),
    ('01800', u'Brejinho (RN)'),
    ('01800', u'Barracão (RS)'),
    ('01801', u'Engenheiro Paulo de Frontin (RJ)'),
    ('01801', u'Aragoiânia (GO)'),
    ('01802', u'Atalanta (SC)'),
    ('01802', u'Baixio (CE)'),
    ('01803', u'Carneiros (AL)'),
    ('01803', u'Divino de São Lourenço (ES)'),
    ('01803', u'Barra do Garças (MT)'),
    ('01803', u'Ipixuna (AM)'),
    ('01804', u'Bocaina (PI)'),
    ('01804', u'Araucária (PR)'),
    ('01805', u'Alpercata (MG)'),
    ('01805', u'Betânia (PE)'),
    ('01806', u'Benedito Leite (MA)'),
    ('01806', u'Américo de Campos (SP)'),
    ('01807', u'Bayeux (PB)'),
    ('01807', u'Vale do Paraíso (RO)'),
    ('01808', u'Breves (PA)'),
    ('01809', u'Antônio Gonçalves (BA)'),
    ('01850', u'Guapimirim (RJ)'),
    ('01851', u'Banabuiú (CE)'),
    ('01852', u'Bom Jesus do Araguaia (MT)'),
    ('01852', u'Iranduba (AM)'),
    ('01853', u'Ariranha do Ivaí (PR)'),
    ('01859', u'Caiçara do Norte (RN)'),
    ('01859', u'Barra do Guarita (RS)'),
    ('01875', u'Barra do Quaraí (RS)'),
    ('01876', u'Iguaba Grande (RJ)'),
    ('01900', u'Itaboraí * (RJ)'),
    ('01900', u'Cumbe (SE)'),
    ('01901', u'Barbalha (CE)'),
    ('01901', u'Aurora (SC)'),
    ('01902', u'Domingos Martins (ES)'),
    ('01902', u'Itacoatiara (AM)'),
    ('01902', u'Chã Preta (AL)'),
    ('01902', u'Brasnorte (MT)'),
    ('01903', u'Bom Jesus (PI)'),
    ('01903', u'Araguacema (TO)'),
    ('01903', u'Assaí (PR)'),
    ('01904', u'Bataguassu (MS)'),
    ('01904', u'Alpinópolis (MG)'),
    ('01904', u'Bezerros (PE)'),
    ('01905', u'Bequimão (MA)'),
    ('01905', u'Amparo (SP)'),
    ('01906', u'Belém (PB)'),
    ('01907', u'Bujaru (PA)'),
    ('01908', u'Aporá (BA)'),
    ('01909', u'Barra do Ribeiro (RS)'),
    ('01909', u'Caiçara do Rio do Vento (RN)'),
    ('01919', u'Bom Princípio do Piauí (PI)'),
    ('01925', u'Barra do Rio Azul (RS)'),
    ('01929', u'Bonfim do Piauí (PI)'),
    ('01939', u'Bernardo do Mearim (MA)'),
    ('01945', u'Boqueirão do Piauí (PI)'),
    ('01950', u'Balneário Arroio do Silva (SC)'),
    ('01950', u'Barreira (CE)'),
    ('01951', u'Itamarati (AM)'),
    ('01956', u'Cachoeira do Piriá (PA)'),
    ('01957', u'Apuarema (BA)'),
    ('01958', u'Barra Funda (RS)'),
    ('01960', u'Brasileira (PI)'),
    ('01970', u'Boa Vista do Gurupi (MA)'),
    ('01988', u'Brejo do Piauí (PI)'),
    ('02000', u'Assis Chateaubriand (PR)'),
    ('02000', u'Araguaçu (TO)'),
    ('02000', u'Buriti dos Lopes (PI)'),
    ('02001', u'Alterosa (MG)'),
    ('02001', u'Bodocó (PE)'),
    ('02001', u'Batayporã (MS)'),
    ('02002', u'Bom Jardim (MA)'),
    ('02002', u'Analândia (SP)'),
    ('02003', u'Belém do Brejo do Cruz (PB)'),
    ('02004', u'Cachoeira do Arari (PA)'),
    ('02005', u'Aracatu (BA)'),
    ('02006', u'Caicó (RN)'),
    ('02006', u'Barros Cassal (RS)'),
    ('02007', u'Itaguaí (RJ)'),
    ('02007', u'Divina Pastora (SE)'),
    ('02008', u'Balneário Camboriú (SC)'),
    ('02008', u'Barro (CE)'),
    ('02009', u'Coité do Nóia (AL)'),
    ('02009', u'Dores do Rio Preto (ES)'),
    ('02009', u'Itapiranga (AM)'),
    ('02026', u'Buriti dos Montes (PI)'),
    ('02036', u'Bom Jesus das Selvas (MA)'),
    ('02050', u'Alto Caparaó (MG)'),
    ('02052', u'Bernardino Batista (PB)'),
    ('02054', u'Araças (BA)'),
    ('02055', u'Benjamin Constant do Sul (RS)'),
    ('02056', u'Italva (RJ)'),
    ('02057', u'Balneário Barra do Sul (SC)'),
    ('02057', u'Barroquinha (CE)'),
    ('02059', u'Cabeceiras do Piauí (PI)'),
    ('02073', u'Balneário Gaivota (SC)'),
    ('02075', u'Cajazeiras do Piauí (PI)'),
    ('02077', u'Bom Lugar (MA)'),
    ('02081', u'Bandeirante (SC)'),
    ('02083', u'Cajueiro da Praia (PI)'),
    ('02091', u'Caldeirão Grande do Piauí (PI)'),
    ('02099', u'Barra Bonita (SC)'),
    ('02100', u'Alto Rio Doce (MG)'),
    ('02100', u'Bela Vista (MS)'),
    ('02100', u'Bom Conselho (PE)'),
    ('02101', u'Andradina (SP)'),
    ('02101', u'Brejo (MA)'),
    ('02102', u'Boa Ventura (PB)'),
    ('02103', u'Cametá (PA)'),
    ('02104', u'Araci (BA)'),
    ('02105', u'Bento Gonçalves (RS)'),
    ('02105', u'Campo Redondo (RN)'),
    ('02106', u'Estância (SE)'),
    ('02106', u'Itaocara (RJ)'),
    ('02107', u'Baturité (CE)'),
    ('02107', u'Barra Velha (SC)'),
    ('02108', u'Ecoporanga (ES)'),
    ('02108', u'Japurá (AM)'),
    ('02108', u'Colônia Leopoldina (AL)'),
    ('02109', u'Campinas do Piauí (PI)'),
    ('02109', u'Araguaína (TO)'),
    ('02109', u'Astorga (PR)'),
    ('02117', u'Campo Alegre do Fidalgo (PI)'),
    ('02131', u'Bela Vista do Toldo (SC)'),
    ('02133', u'Campo Grande do Piauí (PI)'),
    ('02150', u'Brejo de Areia (MA)'),
    ('02151', u'Boa Vista (PB)'),
    ('02152', u'Canaã dos Carajás (PA)'),
    ('02154', u'Boa Vista das Missões (RS)'),
    ('02155', u'Araguapaz (GO)'),
    ('02156', u'Belmonte (SC)'),
    ('02158', u'Araguanã (TO)'),
    ('02159', u'Bodoquena (MS)'),
    ('02174', u'Campo Largo do Piauí (PI)'),
    ('02200', u'Angatuba (SP)'),
    ('02200', u'Buriti (MA)'),
    ('02201', u'Bom Jesus (PB)'),
    ('02202', u'Capanema (PA)'),
    ('02203', u'Aramari (BA)'),
    ('02204', u'Boa Vista do Buricá (RS)'),
    ('02204', u'Canguaretama (RN)'),
    ('02205', u'Feira Nova (SE)'),
    ('02205', u'Itaperuna (RJ)'),
    ('02206', u'Benedito Novo (SC)'),
    ('02206', u'Beberibe (CE)'),
    ('02207', u'Fundão (ES)'),
    ('02207', u'Coqueiro Seco (AL)'),
    ('02207', u'Juruá (AM)'),
    ('02208', u'Campo Maior (PI)'),
    ('02208', u'Atalaia (PR)'),
    ('02208', u'Araguatins (TO)'),
    ('02209', u'Bonito (MS)'),
    ('02209', u'Alvarenga (MG)'),
    ('02209', u'Bom Jardim (PE)'),
    ('02220', u'Boa Vista do Cadeado (RS)'),
    ('02238', u'Boa Vista do Incra (RS)'),
    ('02251', u'Canavieira (PI)'),
    ('02252', u'Arataca (BA)'),
    ('02253', u'Boa Vista do Sul (RS)'),
    ('02254', u'Itatiaia (RJ)'),
    ('02256', u'Governador Lindenberg (ES)'),
    ('02270', u'Japeri (RJ)'),
    ('02300', u'Bom Sucesso (PB)'),
    ('02301', u'Capitão Poço (PA)'),
    ('02302', u'Aratuípe (BA)'),
    ('02303', u'Bom Jesus (RS)'),
    ('02303', u'Caraúbas (RN)'),
    ('02304', u'Laje do Muriaé (RJ)'),
    ('02304', u'Frei Paulo (SE)'),
    ('02305', u'Biguaçu (SC)'),
    ('02305', u'Bela Cruz (CE)'),
    ('02306', u'Coruripe (AL)'),
    ('02306', u'Guaçuí (ES)'),
    ('02306', u'Jutaí (AM)'),
    ('02307', u'Balsa Nova (PR)'),
    ('02307', u'Canto do Buriti (PI)'),
    ('02307', u'Arapoema (TO)'),
    ('02308', u'Brasilândia (MS)'),
    ('02308', u'Bonito (PE)'),
    ('02308', u'Alvinópolis (MG)'),
    ('02309', u'Buriti Bravo (MA)'),
    ('02309', u'Anhembi (SP)'),
    ('02325', u'Buriticupu (MA)'),
    ('02352', u'Bom Princípio (RS)'),
    ('02353', u'Arenópolis (GO)'),
    ('02355', u'Craíbas (AL)'),
    ('02358', u'Buritirana (MA)'),
    ('02374', u'Cachoeira Grande (MA)'),
    ('02378', u'Bom Progresso (RS)'),
    ('02400', u'Castanhal (PA)'),
    ('02401', u'Aurelino Leal (BA)'),
    ('02402', u'Bom Retiro do Sul (RS)'),
    ('02402', u'Carnaúba dos Dantas (RN)'),
    ('02403', u'Gararu (SE)'),
    ('02403', u'Macaé (RJ)'),
    ('02404', u'Blumenau * (SC)'),
    ('02404', u'Boa Viagem (CE)'),
    ('02405', u'Lábrea (AM)'),
    ('02405', u'Delmiro Gouveia (AL)'),
    ('02405', u'Guarapari (ES)'),
    ('02406', u'Capitão de Campos (PI)'),
    ('02406', u'Bandeirantes (PR)'),
    ('02406', u'Arraias (TO)'),
    ('02407', u'Alvorada de Minas (MG)'),
    ('02407', u'Caarapó (MS)'),
    ('02407', u'Brejão (PE)'),
    ('02408', u'Cajapió (MA)'),
    ('02408', u'Anhumas (SP)'),
    ('02409', u'Bonito de Santa Fé (PB)'),
    ('02438', u'Bocaina do Sul (SC)'),
    ('02451', u'Boqueirão do Leão (RS)'),
    ('02452', u'Macuco (RJ)'),
    ('02453', u'Bombinhas (SC)'),
    ('02454', u'Ibatiba (ES)'),
    ('02455', u'Capitão Gervásio Oliveira (PI)'),
    ('02500', u'Baianópolis (BA)'),
    ('02501', u'Carnaubais (RN)'),
    ('02501', u'Bossoroca (RS)'),
    ('02502', u'Magé * (RJ)'),
    ('02502', u'Aruanã (GO)'),
    ('02502', u'General Maynard (SE)'),
    ('02503', u'Brejo Santo (CE)'),
    ('02503', u'Bom Jardim da Serra (SC)'),
    ('02504', u'Dois Riachos (AL)'),
    ('02504', u'Cáceres (MT)'),
    ('02504', u'Manacapuru (AM)'),
    ('02504', u'Ibiraçu (ES)'),
    ('02505', u'Caracol (PI)'),
    ('02505', u'Barbosa Ferraz (PR)'),
    ('02506', u'Brejinho (PE)'),
    ('02506', u'Amparo do Serra (MG)'),
    ('02507', u'Cajari (MA)'),
    ('02507', u'Aparecida (SP)'),
    ('02508', u'Boqueirão (PB)'),
    ('02509', u'Chaves (PA)'),
    ('02537', u'Bom Jesus (SC)'),
    ('02539', u'Caraúbas do Piauí (PI)'),
    ('02553', u'Ibitirama (ES)'),
    ('02553', u'Estrela de Alagoas (AL)'),
    ('02553', u'Manaquiri (AM)'),
    ('02554', u'Augustinópolis (TO)'),
    ('02554', u'Caridade do Piauí (PI)'),
    ('02556', u'Campestre do Maranhão (MA)'),
    ('02578', u'Bom Jesus do Oeste (SC)'),
    ('02584', u'Bozano (RS)'),
    ('02600', u'Braga (RS)'),
    ('02600', u'Ceará-Mirim (RN)'),
    ('02601', u'Gracho Cardoso (SE)'),
    ('02601', u'Aurilândia (GO)'),
    ('02601', u'Mangaratiba (RJ)'),
    ('02602', u'Camocim (CE)'),
    ('02602', u'Bom Retiro (SC)'),
    ('02603', u'Iconha (ES)'),
    ('02603', u'Campinápolis (MT)'),
    ('02603', u'Manaus (AM)'),
    ('02603', u'Feira Grande (AL)'),
    ('02604', u'Barracão (PR)'),
    ('02604', u'Castelo do Piauí (PI)'),
    ('02605', u'Camapuã (MS)'),
    ('02605', u'Brejo da Madre de Deus (PE)'),
    ('02605', u'Andradas (MG)'),
    ('02606', u'Aparecida d`Oeste (SP)'),
    ('02606', u'Cândido Mendes (MA)'),
    ('02607', u'Igaracy (PB)'),
    ('02608', u'Colares (PA)'),
    ('02609', u'Baixa Grande (BA)'),
    ('02637', u'Campo Novo do Parecis (MT)'),
    ('02652', u'Irupi (ES)'),
    ('02653', u'Caxingó (PI)'),
    ('02658', u'Banzaê (BA)'),
    ('02659', u'Brochier (RS)'),
    ('02678', u'Campo Verde (MT)'),
    ('02686', u'Campos de Júlio (MT)'),
    ('02694', u'Canabrava do Norte (MT)'),
    ('02700', u'Maricá (RJ)'),
    ('02700', u'Ilha das Flores (SE)'),
    ('02701', u'Botuverá (SC)'),
    ('02701', u'Campos Sales (CE)'),
    ('02702', u'Feliz Deserto (AL)'),
    ('02702', u'Canarana (MT)'),
    ('02702', u'Itaguaçu (ES)'),
    ('02702', u'Manicoré (AM)'),
    ('02703', u'Aurora do Tocantins (TO)'),
    ('02703', u'Cocal (PI)'),
    ('02703', u'Barra do Jacaré (PR)'),
    ('02704', u'Buenos Aires (PE)'),
    ('02704', u'Cachoeira de Pajeú (MG)'),
    ('02704', u'Campo Grande (MS)'),
    ('02705', u'Apiaí (SP)'),
    ('02705', u'Cantanhede (MA)'),
    ('02706', u'Borborema (PB)'),
    ('02707', u'Conceição do Araguaia (PA)'),
    ('02708', u'Barra (BA)'),
    ('02709', u'Butiá (RS)'),
    ('02709', u'Cerro Corá (RN)'),
    ('02711', u'Cocal de Telha (PI)'),
    ('02729', u'Cocal dos Alves (PI)'),
    ('02737', u'Coivaras (PI)'),
    ('02752', u'Colônia do Gurguéia (PI)'),
    ('02752', u'Bela Vista da Caroba (PR)'),
    ('02754', u'Capinzal do Norte (MA)'),
    ('02754', u'Araçariguama (SP)'),
    ('02756', u'Concórdia do Pará (PA)'),
    ('02764', u'Cumaru do Norte (PA)'),
    ('02772', u'Curionópolis (PA)'),
    ('02778', u'Colônia do Piauí (PI)'),
    ('02793', u'Carlinda (MT)'),
    ('02800', u'Braço do Norte (SC)'),
    ('02800', u'Canindé (CE)'),
    ('02801', u'Itapemirim (ES)'),
    ('02801', u'Flexeiras (AL)'),
    ('02801', u'Maraã (AM)'),
    ('02802', u'Bela Vista do Paraíso (PR)'),
    ('02802', u'Conceição do Canindé (PI)'),
    ('02803', u'Caracol (MS)'),
    ('02803', u'Buíque (PE)'),
    ('02803', u'Andrelândia (MG)'),
    ('02804', u'Carolina (MA)'),
    ('02804', u'Araçatuba * (SP)'),
    ('02805', u'Brejo do Cruz (PB)'),
    ('02806', u'Curralinho (PA)'),
    ('02807', u'Barra da Estiva (BA)'),
    ('02808', u'Caçapava do Sul (RS)'),
    ('02808', u'Coronel Ezequiel (RN)'),
    ('02809', u'Mendes (RJ)'),
    ('02809', u'Indiaroba (SE)'),
    ('02809', u'Avelinópolis (GO)'),
    ('02850', u'Castanheira (MT)'),
    ('02851', u'Coronel José Dias (PI)'),
    ('02852', u'Angelândia (MG)'),
    ('02855', u'Curuá (PA)'),
    ('02858', u'Mesquita * (RJ)'),
    ('02859', u'Braço do Trombudo (SC)'),
    ('02875', u'Brunópolis (SC)'),
    ('02900', u'Itarana (ES)'),
    ('02900', u'Maués (AM)'),
    ('02900', u'Girau do Ponciano (AL)'),
    ('02901', u'Corrente (PI)'),
    ('02901', u'Axixá do Tocantins (TO)'),
    ('02901', u'Bituruna (PR)'),
    ('02902', u'Antônio Carlos (MG)'),
    ('02902', u'Cassilândia (MS)'),
    ('02902', u'Cabo de Santo Agostinho (PE)'),
    ('02903', u'Araçoiaba da Serra (SP)'),
    ('02903', u'Carutapera (MA)'),
    ('02904', u'Brejo dos Santos (PB)'),
    ('02905', u'Curuçá (PA)'),
    ('02906', u'Barra do Choça (BA)'),
    ('02907', u'Cacequi (RS)'),
    ('02907', u'Coronel João Pessoa (RN)'),
    ('02908', u'Itabaiana (SE)'),
    ('02908', u'Miguel Pereira (RJ)'),
    ('02909', u'Capistrano (CE)'),
    ('02909', u'Brusque (SC)'),
    ('02939', u'Dom Eliseu (PA)'),
    ('02951', u'Chapadão do Sul (MS)'),
    ('02954', u'Eldorado dos Carajás (PA)'),
    ('03000', u'Aramina (SP)'),
    ('03000', u'Caxias (MA)'),
    ('03001', u'Caaporã (PB)'),
    ('03002', u'Faro (PA)'),
    ('03003', u'Barra do Mendes (BA)'),
    ('03004', u'Cruzeta (RN)'),
    ('03004', u'Cachoeira do Sul (RS)'),
    ('03005', u'Itabaianinha (SE)'),
    ('03005', u'Miracema (RJ)'),
    ('03006', u'Caçador (SC)'),
    ('03006', u'Caridade (CE)'),
    ('03007', u'Iúna (ES)'),
    ('03007', u'Ibateguara (AL)'),
    ('03007', u'Nhamundá (AM)'),
    ('03007', u'Chapada dos Guimarães (MT)'),
    ('03008', u'Boa Esperança (PR)'),
    ('03008', u'Cristalândia do Piauí (PI)'),
    ('03008', u'Babaçulândia (TO)'),
    ('03009', u'Cabrobó (PE)'),
    ('03009', u'Antônio Dias (MG)'),
    ('03024', u'Boa Esperança do Iguaçu (PR)'),
    ('03040', u'Boa Ventura de São Roque (PR)'),
    ('03044', u'Floresta do Araguaia (PA)'),
    ('03056', u'Jaguaré (ES)'),
    ('03056', u'Cláudia (MT)'),
    ('03057', u'Boa Vista da Aparecida (PR)'),
    ('03057', u'Bandeirantes do Tocantins (TO)'),
    ('03073', u'Barra do Ouro (TO)'),
    ('03077', u'Garrafão do Norte (PA)'),
    ('03093', u'Goianésia do Pará (PA)'),
    ('03100', u'Cabaceiras (PB)'),
    ('03101', u'Gurupá (PA)'),
    ('03102', u'Barra do Rocha (BA)'),
    ('03103', u'Cachoeirinha (RS)'),
    ('03103', u'Currais Novos (RN)'),
    ('03104', u'Itabi (SE)'),
    ('03104', u'Baliza (GO)'),
    ('03104', u'Natividade (RJ)'),
    ('03105', u'Cariré (CE)'),
    ('03105', u'Caibi (SC)'),
    ('03106', u'Igaci (AL)'),
    ('03106', u'Jerônimo Monteiro (ES)'),
    ('03106', u'Cocalinho (MT)'),
    ('03106', u'Nova Olinda do Norte (AM)'),
    ('03107', u'Barrolândia (TO)'),
    ('03107', u'Bocaiúva do Sul (PR)'),
    ('03107', u'Cristino Castro (PI)'),
    ('03108', u'Cachoeirinha (PE)'),
    ('03108', u'Corguinho (MS)'),
    ('03108', u'Antônio Prado de Minas (MG)'),
    ('03109', u'Cedral (MA)'),
    ('03109', u'Arandu (SP)'),
    ('03125', u'Central do Maranhão (MA)'),
    ('03130', u'João Neiva (ES)'),
    ('03154', u'Calmon (SC)'),
    ('03156', u'Bom Jesus do Sul (PR)'),
    ('03157', u'Coronel Sapucaia (MS)'),
    ('03158', u'Arapeí (SP)'),
    ('03158', u'Centro do Guilherme (MA)'),
    ('03163', u'Laranja da Terra (ES)'),
    ('03174', u'Centro Novo do Maranhão (MA)'),
    ('03200', u'Igarapé-Açu (PA)'),
    ('03201', u'Barreiras (BA)'),
    ('03202', u'Cacique Doble (RS)'),
    ('03202', u'Doutor Severiano (RN)'),
    ('03203', u'Barro Alto (GO)'),
    ('03203', u'Nilópolis (RJ)'),
    ('03203', u'Itaporanga d`Ajuda (SE)'),
    ('03204', u'Caririaçu (CE)'),
    ('03204', u'Camboriú (SC)'),
    ('03205', u'Novo Airão (AM)'),
    ('03205', u'Linhares (ES)'),
    ('03205', u'Igreja Nova (AL)'),
    ('03205', u'Colíder (MT)'),
    ('03206', u'Bom Sucesso (PR)'),
    ('03206', u'Curimatá (PI)'),
    ('03206', u'Bernardo Sayão (TO)'),
    ('03207', u'Corumbá (MS)'),
    ('03207', u'Caetés (PE)'),
    ('03207', u'Araçaí (MG)'),
    ('03208', u'Araraquara * (SP)'),
    ('03208', u'Chapadinha (MA)'),
    ('03209', u'Cabedelo (PB)'),
    ('03222', u'Bom Sucesso do Sul (PR)'),
    ('03230', u'Currais (PI)'),
    ('03235', u'Barro Alto (BA)'),
    ('03251', u'Parnamirim (RN)'),
    ('03253', u'Capão Alto (SC)'),
    ('03254', u'Colniza (MT)'),
    ('03255', u'Curralinhos (PI)'),
    ('03256', u'Costa Rica (MS)'),
    ('03257', u'Cidelândia (MA)'),
    ('03271', u'Curral Novo do Piauí (PI)'),
    ('03276', u'Barrocas (BA)'),
    ('03300', u'Barro Preto (BA)'),
    ('03301', u'Encanto (RN)'),
    ('03301', u'Caibaté (RS)'),
    ('03302', u'Japaratuba (SE)'),
    ('03302', u'Bela Vista de Goiás (GO)'),
    ('03302', u'Niterói * (RJ)'),
    ('03303', u'Campo Alegre (SC)'),
    ('03303', u'Cariús (CE)'),
    ('03304', u'Inhapi (AL)'),
    ('03304', u'Mantenópolis (ES)'),
    ('03304', u'Novo Aripuanã (AM)'),
    ('03304', u'Comodoro (MT)'),
    ('03305', u'Bom Jesus do Tocantins (TO)'),
    ('03305', u'Borrazópolis (PR)'),
    ('03305', u'Demerval Lobão (PI)'),
    ('03306', u'Calçado (PE)'),
    ('03306', u'Coxim (MS)'),
    ('03306', u'Aracitaba (MG)'),
    ('03307', u'Codó (MA)'),
    ('03307', u'Araras (SP)'),
    ('03308', u'Cachoeira dos Índios (PB)'),
    ('03309', u'Igarapé-Miri (PA)'),
    ('03320', u'Marataízes (ES)'),
    ('03346', u'Marechal Floriano (ES)'),
    ('03353', u'Confresa (MT)'),
    ('03353', u'Marilândia (ES)'),
    ('03354', u'Dirceu Arcoverde (PI)'),
    ('03354', u'Braganey (PR)'),
    ('03356', u'Arco-Íris (SP)'),
    ('03361', u'Conquista D`Oeste (MT)'),
    ('03370', u'Brasilândia do Sul (PR)'),
    ('03379', u'Cotriguaçu (MT)'),
    ('03400', u'Equador (RN)'),
    ('03400', u'Caiçara (RS)'),
    ('03401', u'Nova Friburgo * (RJ)'),
    ('03401', u'Japoatã (SE)'),
    ('03401', u'Bom Jardim de Goiás (GO)'),
    ('03402', u'Campo Belo do Sul (SC)'),
    ('03402', u'Carnaubal (CE)'),
    ('03403', u'Jacaré dos Homens (AL)'),
    ('03403', u'Mimoso do Sul (ES)'),
    ('03403', u'Parintins (AM)'),
    ('03403', u'Cuiabá (MT)'),
    ('03404', u'Cafeara (PR)'),
    ('03404', u'Dom Expedito Lopes (PI)'),
    ('03405', u'Calumbi (PE)'),
    ('03405', u'Araçuaí (MG)'),
    ('03406', u'Coelho Neto (MA)'),
    ('03406', u'Arealva (SP)'),
    ('03407', u'Cacimba de Areia (PB)'),
    ('03408', u'Inhangapi (PA)'),
    ('03409', u'Belmonte (BA)'),
    ('03420', u'Domingos Mourão (PI)'),
    ('03437', u'Curvelândia (MT)'),
    ('03452', u'Denise (MT)'),
    ('03453', u'Dom Inocêncio (PI)'),
    ('03453', u'Cafelândia (PR)'),
    ('03454', u'Deodápolis (MS)'),
    ('03454', u'Camaragibe (PE)'),
    ('03457', u'Ipixuna do Pará (PA)'),
    ('03479', u'Cafezal do Sul (PR)'),
    ('03488', u'Dois Irmãos do Buriti (MS)'),
    ('03500', u'Lagarto (SE)'),
    ('03500', u'Bom Jesus de Goiás (GO)'),
    ('03500', u'Nova Iguaçu * (RJ)'),
    ('03501', u'Campo Erê (SC)'),
    ('03501', u'Cascavel (CE)'),
    ('03502', u'Diamantino (MT)'),
    ('03502', u'Montanha (ES)'),
    ('03502', u'Jacuípe (AL)'),
    ('03502', u'Pauini (AM)'),
    ('03503', u'Elesbão Veloso (PI)'),
    ('03503', u'Califórnia (PR)'),
    ('03504', u'Araguari (MG)'),
    ('03504', u'Douradina (MS)'),
    ('03504', u'Camocim de São Félix (PE)'),
    ('03505', u'Colinas (MA)'),
    ('03505', u'Areias (SP)'),
    ('03506', u'Cacimba de Dentro (PB)'),
    ('03507', u'Irituia (PA)'),
    ('03508', u'Belo Campo (BA)'),
    ('03509', u'Espírito Santo (RN)'),
    ('03509', u'Camaquã (RS)'),
    ('03536', u'Presidente Figueiredo (AM)'),
    ('03554', u'Conceição do Lago-Açu (MA)'),
    ('03555', u'Cacimbas (PB)'),
    ('03558', u'Camargo (RS)'),
    ('03559', u'Bonfinópolis (GO)'),
    ('03569', u'Rio Preto da Eva (AM)'),
    ('03575', u'Bonópolis (GO)'),
    ('03600', u'Catarina (CE)'),
    ('03600', u'Campos Novos (SC)'),
    ('03601', u'Japaratinga (AL)'),
    ('03601', u'Dom Aquino (MT)'),
    ('03601', u'Mucurici (ES)'),
    ('03601', u'Santa Isabel do Rio Negro (AM)'),
    ('03602', u'Eliseu Martins (PI)'),
    ('03602', u'Brasilândia do Tocantins (TO)'),
    ('03602', u'Cambará (PR)'),
    ('03603', u'Arantina (MG)'),
    ('03603', u'Camutanga (PE)'),
    ('03604', u'Areiópolis (SP)'),
    ('03604', u'Coroatá (MA)'),
    ('03605', u'Caiçara (PB)'),
    ('03606', u'Itaituba (PA)'),
    ('03607', u'Biritinga (BA)'),
    ('03608', u'Extremoz (RN)'),
    ('03608', u'Cambará do Sul (RS)'),
    ('03609', u'Brazabrantes (GO)'),
    ('03609', u'Laranjeiras (SE)'),
    ('03609', u'Paracambi (RJ)'),
    ('03659', u'Catunda (CE)'),
    ('03673', u'Campestre da Serra (RS)'),
    ('03700', u'Muniz Freire (ES)'),
    ('03700', u'Santo Antônio do Içá (AM)'),
    ('03700', u'Jaramataia (AL)'),
    ('03700', u'Feliz Natal (MT)'),
    ('03701', u'Esperantina (PI)'),
    ('03701', u'Brejinho de Nazaré (TO)'),
    ('03701', u'Cambé (PR)'),
    ('03702', u'Canhotinho (PE)'),
    ('03702', u'Dourados (MS)'),
    ('03702', u'Araponga (MG)'),
    ('03703', u'Ariranha (SP)'),
    ('03703', u'Cururupu (MA)'),
    ('03704', u'Cajazeiras (PB)'),
    ('03705', u'Itupiranga (PA)'),
    ('03706', u'Boa Nova (BA)'),
    ('03707', u'Campina das Missões (RS)'),
    ('03707', u'Felipe Guerra (RN)'),
    ('03708', u'Macambira (SE)'),
    ('03708', u'Paraíba do Sul (RJ)'),
    ('03709', u'Caucaia * (CE)'),
    ('03709', u'Canelinha (SC)'),
    ('03750', u'Fartura do Piauí (PI)'),
    ('03751', u'Araporã (MG)'),
    ('03751', u'Eldorado (MS)'),
    ('03752', u'Davinópolis (MA)'),
    ('03753', u'Cajazeirinhas (PB)'),
    ('03754', u'Jacareacanga (PA)'),
    ('03756', u'Fernando Pedroza (RN)'),
    ('03759', u'Jequiá da Praia (AL)'),
    ('03800', u'Buriti do Tocantins (TO)'),
    ('03800', u'Flores do Piauí (PI)'),
    ('03800', u'Cambira (PR)'),
    ('03801', u'Capoeiras (PE)'),
    ('03801', u'Fátima do Sul (MS)'),
    ('03801', u'Arapuá (MG)'),
    ('03802', u'Dom Pedro (MA)'),
    ('03802', u'Artur Nogueira (SP)'),
    ('03803', u'Caldas Brandão (PB)'),
    ('03804', u'Jacundá (PA)'),
    ('03805', u'Boa Vista do Tupim (BA)'),
    ('03806', u'Campinas do Sul (RS)'),
    ('03806', u'Florânia (RN)'),
    ('03807', u'Britânia (GO)'),
    ('03807', u'Parati (RJ)'),
    ('03807', u'Malhada dos Bois (SE)'),
    ('03808', u'Canoinhas (SC)'),
    ('03808', u'Cedro (CE)'),
    ('03809', u'Muqui (ES)'),
    ('03809', u'Figueirópolis D`Oeste (MT)'),
    ('03809', u'Joaquim Gomes (AL)'),
    ('03809', u'São Gabriel da Cachoeira (AM)'),
    ('03826', u'Cachoeirinha (TO)'),
    ('03842', u'Campos Lindos (TO)'),
    ('03856', u'Paty do Alferes (RJ)'),
    ('03858', u'Gaúcha do Norte (MT)'),
    ('03859', u'Floresta do Piauí (PI)'),
    ('03867', u'Cariri do Tocantins (TO)'),
    ('03883', u'Carmolândia (TO)'),
    ('03891', u'Carrasco Bonito (TO)'),
    ('03900', u'Araújos (MG)'),
    ('03900', u'Figueirão (MS)'),
    ('03900', u'Carnaíba (PE)'),
    ('03901', u'Arujá (SP)'),
    ('03901', u'Duque Bacelar (MA)'),
    ('03902', u'Camalaú (PB)'),
    ('03903', u'Juruti (PA)'),
    ('03904', u'Bom Jesus da Lapa (BA)'),
    ('03905', u'Campo Bom (RS)'),
    ('03905', u'Francisco Dantas (RN)'),
    ('03906', u'Malhador (SE)'),
    ('03906', u'Buriti Alegre (GO)'),
    ('03906', u'Petrópolis * (RJ)'),
    ('03907', u'Capinzal (SC)'),
    ('03907', u'Chaval (CE)'),
    ('03908', u'Jundiá (AL)'),
    ('03908', u'São Paulo de Olivença (AM)'),
    ('03908', u'Nova Venécia (ES)'),
    ('03908', u'General Carneiro (MT)'),
    ('03909', u'Floriano (PI)'),
    ('03909', u'Campina da Lagoa (PR)'),
    ('03909', u'Caseara (TO)'),
    ('03926', u'Carnaubeira da Penha (PE)'),
    ('03931', u'Choró (CE)'),
    ('03939', u'Buriti de Goiás (GO)'),
    ('03950', u'Aspásia (SP)'),
    ('03953', u'Bom Jesus da Serra (BA)'),
    ('03955', u'Pinheiral (RJ)'),
    ('03956', u'Chorozinho (CE)'),
    ('03956', u'Capivari de Baixo (SC)'),
    ('03957', u'São Sebastião do Uatumã (AM)'),
    ('03957', u'Glória D`Oeste (MT)'),
    ('03958', u'Campina do Simão (PR)'),
    ('03962', u'Buritinópolis (GO)'),
    ('04000', u'Limoeiro do Ajuru (PA)'),
    ('04001', u'Boninal (BA)'),
    ('04002', u'Frutuoso Gomes (RN)'),
    ('04002', u'Campo Novo (RS)'),
    ('04003', u'Piraí (RJ)'),
    ('04003', u'Cabeceiras (GO)'),
    ('04003', u'Maruim (SE)'),
    ('04004', u'Coreaú (CE)'),
    ('04004', u'Catanduvas (SC)'),
    ('04005', u'Silves (AM)'),
    ('04005', u'Pancas (ES)'),
    ('04005', u'Junqueiro (AL)'),
    ('04006', u'Campina Grande do Sul (PR)'),
    ('04006', u'Francinópolis (PI)'),
    ('04007', u'Glória de Dourados (MS)'),
    ('04007', u'Carpina (PE)'),
    ('04007', u'Araxá (MG)'),
    ('04008', u'Esperantinópolis (MA)'),
    ('04008', u'Assis (SP)'),
    ('04009', u'Campina Grande (PB)'),
    ('04033', u'Capim (PB)'),
    ('04050', u'Bonito (BA)'),
    ('04054', u'Pedro Canário (ES)'),
    ('04055', u'Campo Bonito (PR)'),
    ('04057', u'Estreito (MA)'),
    ('04059', u'Mãe do Rio (PA)'),
    ('04062', u'Tabatinga (AM)'),
    ('04073', u'Feira Nova do Maranhão (MA)'),
    ('04074', u'Caraúbas (PB)'),
    ('04081', u'Fernando Falcão (MA)'),
    ('04099', u'Formosa da Serra Negra (MA)'),
    ('04100', u'Boquira (BA)'),
    ('04101', u'Galinhos (RN)'),
    ('04101', u'Campos Borges (RS)'),
    ('04102', u'Porciúncula (RJ)'),
    ('04102', u'Moita Bonita (SE)'),
    ('04102', u'Cachoeira Alta (GO)'),
    ('04103', u'Caxambu do Sul (SC)'),
    ('04103', u'Crateús (CE)'),
    ('04104', u'Pinheiros (ES)'),
    ('04104', u'Guarantã do Norte (MT)'),
    ('04104', u'Lagoa da Canoa (AL)'),
    ('04104', u'Tapauá (AM)'),
    ('04105', u'Francisco Ayres (PI)'),
    ('04105', u'Centenário (TO)'),
    ('04105', u'Campo do Tenente (PR)'),
    ('04106', u'Caruaru * (PE)'),
    ('04106', u'Guia Lopes da Laguna (MS)'),
    ('04106', u'Arceburgo (MG)'),
    ('04107', u'Fortaleza dos Nogueiras (MA)'),
    ('04107', u'Atibaia (SP)'),
    ('04108', u'Carrapateira (PB)'),
    ('04109', u'Magalhães Barata (PA)'),
    ('04110', u'Porto Real (RJ)'),
    ('04128', u'Quatis (RJ)'),
    ('04144', u'Queimados (RJ)'),
    ('04151', u'Quissamã (RJ)'),
    ('04152', u'Celso Ramos (SC)'),
    ('04154', u'Francisco Macedo (PI)'),
    ('04155', u'Casinhas (PE)'),
    ('04157', u'Casserengue (PB)'),
    ('04178', u'Cerro Negro (SC)'),
    ('04194', u'Chapadão do Lageado (SC)'),
    ('04200', u'Goianinha (RN)'),
    ('04200', u'Candelária (RS)'),
    ('04201', u'Monte Alegre de Sergipe (SE)'),
    ('04201', u'Cachoeira de Goiás (GO)'),
    ('04201', u'Resende (RJ)'),
    ('04202', u'Crato (CE)'),
    ('04202', u'Chapecó (SC)'),
    ('04203', u'Tefé (AM)'),
    ('04203', u'Piúma (ES)'),
    ('04203', u'Limoeiro de Anadia (AL)'),
    ('04203', u'Guiratinga (MT)'),
    ('04204', u'Francisco Santos (PI)'),
    ('04204', u'Campo Largo (PR)'),
    ('04205', u'Catende (PE)'),
    ('04205', u'Arcos (MG)'),
    ('04206', u'Auriflama (SP)'),
    ('04206', u'Fortuna (MA)'),
    ('04207', u'Catingueira (PB)'),
    ('04208', u'Marabá * (PA)'),
    ('04209', u'Botuporã (BA)'),
    ('04236', u'Croatá (CE)'),
    ('04237', u'Tonantins (AM)'),
    ('04250', u'Cachoeira Dourada (GO)'),
    ('04251', u'Cocal do Sul (SC)'),
    ('04251', u'Cruz (CE)'),
    ('04252', u'Ponto Belo (ES)'),
    ('04253', u'Campo Magro (PR)'),
    ('04260', u'Uarini (AM)'),
    ('04269', u'Deputado Irapuan Pinheiro (CE)'),
    ('04277', u'Ererê (CE)'),
    ('04285', u'Eusébio (CE)'),
    ('04300', u'Caçu (GO)'),
    ('04300', u'Muribeca (SE)'),
    ('04300', u'Rio Bonito (RJ)'),
    ('04301', u'Farias Brito (CE)'),
    ('04301', u'Concórdia (SC)'),
    ('04302', u'Presidente Kennedy (ES)'),
    ('04302', u'Urucará (AM)'),
    ('04302', u'Maceió (AL)'),
    ('04303', u'Fronteiras (PI)'),
    ('04303', u'Campo Mourão (PR)'),
    ('04304', u'Iguatemi (MS)'),
    ('04304', u'Areado (MG)'),
    ('04304', u'Cedro (PE)'),
    ('04305', u'Avaí (SP)'),
    ('04305', u'Godofredo Viana (MA)'),
    ('04306', u'Catolé do Rocha (PB)'),
    ('04307', u'Maracanã (PA)'),
    ('04308', u'Brejões (BA)'),
    ('04309', u'Governador Dix-Sept Rosado (RN)'),
    ('04309', u'Cândido Godói (RS)'),
    ('04350', u'Forquilha (CE)'),
    ('04350', u'Cordilheira Alta (SC)'),
    ('04351', u'Rio Bananal (ES)'),
    ('04352', u'Geminiano (PI)'),
    ('04355', u'Caturité (PB)'),
    ('04358', u'Candiota (RS)'),
    ('04400', u'Fortaleza * (CE)'),
    ('04400', u'Coronel Freitas (SC)'),
    ('04401', u'Major Isidoro (AL)'),
    ('04401', u'Urucurituba (AM)'),
    ('04401', u'Rio Novo do Sul (ES)'),
    ('04402', u'Cândido de Abreu (PR)'),
    ('04402', u'Gilbués (PI)'),
    ('04403', u'Chã de Alegria (PE)'),
    ('04403', u'Argirita (MG)'),
    ('04403', u'Inocência (MS)'),
    ('04404', u'Gonçalves Dias (MA)'),
    ('04404', u'Avanhandava (SP)'),
    ('04405', u'Conceição (PB)'),
    ('04406', u'Marapanim (PA)'),
    ('04407', u'Brejolândia (BA)'),
    ('04408', u'Canela (RS)'),
    ('04408', u'Grossos (RN)'),
    ('04409', u'Neópolis (SE)'),
    ('04409', u'Rio Claro (RJ)'),
    ('04409', u'Caiapônia (GO)'),
    ('04422', u'Marituba (PA)'),
    ('04428', u'Candói (PR)'),
    ('04451', u'Cantagalo (PR)'),
    ('04452', u'Aricanduva (MG)'),
    ('04455', u'Medicilândia (PA)'),
    ('04458', u'Nossa Senhora Aparecida (SE)'),
    ('04459', u'Coronel Martins (SC)'),
    ('04459', u'Fortim (CE)'),
    ('04500', u'Indiavaí (MT)'),
    ('04500', u'Maragogi (AL)'),
    ('04500', u'Santa Leopoldina (ES)'),
    ('04501', u'Guadalupe (PI)'),
    ('04501', u'Capanema (PR)'),
    ('04502', u'Itaporã (MS)'),
    ('04502', u'Arinos (MG)'),
    ('04502', u'Chã Grande (PE)'),
    ('04503', u'Governador Archer (MA)'),
    ('04503', u'Avaré (SP)'),
    ('04504', u'Condado (PB)'),
    ('04505', u'Melgaço (PA)'),
    ('04506', u'Brotas de Macaúbas (BA)'),
    ('04507', u'Guamaré (RN)'),
    ('04507', u'Canguçu (RS)'),
    ('04508', u'Rio das Flores (RJ)'),
    ('04508', u'Caldas Novas (GO)'),
    ('04508', u'Nossa Senhora da Glória (SE)'),
    ('04509', u'Frecheirinha (CE)'),
    ('04509', u'Corupá (SC)'),
    ('04524', u'Rio das Ostras (RJ)'),
    ('04526', u'Ipiranga do Norte (MT)'),
    ('04542', u'Itanhangá (MT)'),
    ('04550', u'Guaribas (PI)'),
    ('04552', u'Governador Edison Lobão (MA)'),
    ('04557', u'Rio de Janeiro * (RJ)'),
    ('04557', u'Caldazinha (GO)'),
    ('04558', u'Correia Pinto (SC)'),
    ('04559', u'Itaúba (MT)'),
    ('04559', u'Santa Maria de Jetibá (ES)'),
    ('04600', u'Hugo Napoleão (PI)'),
    ('04600', u'Chapada de Areia (TO)'),
    ('04600', u'Capitão Leônidas Marques (PR)'),
    ('04601', u'Itaquiraí (MS)'),
    ('04601', u'Condado (PE)'),
    ('04601', u'Astolfo Dutra (MG)'),
    ('04602', u'Governador Eugênio Barros (MA)'),
    ('04602', u'Bady Bassitt (SP)'),
    ('04603', u'Conde (PB)'),
    ('04604', u'Mocajuba (PA)'),
    ('04605', u'Brumado (BA)'),
    ('04606', u'Ielmo Marinho (RN)'),
    ('04606', u'Canoas * (RS)'),
    ('04607', u'Nossa Senhora das Dores (SE)'),
    ('04607', u'Campestre de Goiás (GO)'),
    ('04607', u'Santa Maria Madalena (RJ)'),
    ('04608', u'Criciúma * (SC)'),
    ('04608', u'General Sampaio (CE)'),
    ('04609', u'Itiquira (MT)'),
    ('04609', u'Maravilha (AL)'),
    ('04609', u'Santa Teresa (ES)'),
    ('04614', u'Canudos do Vale (RS)'),
    ('04622', u'Capão Bonito do Sul (RS)'),
    ('04628', u'Governador Luiz Rocha (MA)'),
    ('04630', u'Capão da Canoa (RS)'),
    ('04651', u'Governador Newton Bello (MA)'),
    ('04655', u'Capão do Cipó (RS)'),
    ('04656', u'Campinaçu (GO)'),
    ('04657', u'Graça (CE)'),
    ('04658', u'São Domingos do Norte (ES)'),
    ('04659', u'Carambeí (PR)'),
    ('04659', u'Ilha Grande (PI)'),
    ('04663', u'Capão do Leão (RS)'),
    ('04671', u'Capivari do Sul (RS)'),
    ('04677', u'Governador Nunes Freire (MA)'),
    ('04689', u'Capela de Santana (RS)'),
    ('04697', u'Capitão (RS)'),
    ('04700', u'Ataléia (MG)'),
    ('04700', u'Ivinhema (MS)'),
    ('04700', u'Correntes (PE)'),
    ('04701', u'Graça Aranha (MA)'),
    ('04701', u'Balbinos (SP)'),
    ('04702', u'Congo (PB)'),
    ('04703', u'Moju (PA)'),
    ('04704', u'Buerarema (BA)'),
    ('04705', u'Ipanguaçu (RN)'),
    ('04705', u'Carazinho (RS)'),
    ('04706', u'Campinorte (GO)'),
    ('04706', u'Santo Antônio de Pádua (RJ)'),
    ('04706', u'Nossa Senhora de Lourdes (SE)'),
    ('04707', u'Granja (CE)'),
    ('04707', u'Cunha Porã (SC)'),
    ('04708', u'São Gabriel da Palha (ES)'),
    ('04708', u'Marechal Deodoro (AL)'),
    ('04709', u'Carlópolis (PR)'),
    ('04709', u'Inhuma (PI)'),
    ('04713', u'Caraá (RS)'),
    ('04753', u'Buritirama (BA)'),
    ('04755', u'São Francisco de Itabapoana (RJ)'),
    ('04756', u'Cunhataí (SC)'),
    ('04800', u'Bálsamo (SP)'),
    ('04800', u'Grajaú (MA)'),
    ('04801', u'Coremas (PB)'),
    ('04802', u'Monte Alegre (PA)'),
    ('04803', u'Caatiba (BA)'),
    ('04804', u'Carlos Barbosa (RS)'),
    ('04804', u'Ipueira (RN)'),
    ('04805', u'Campo Alegre de Goiás (GO)'),
    ('04805', u'São Fidélis (RJ)'),
    ('04805', u'Nossa Senhora do Socorro (SE)'),
    ('04806', u'Curitibanos (SC)'),
    ('04806', u'Granjeiro (CE)'),
    ('04807', u'São José do Calçado (ES)'),
    ('04807', u'Jaciara (MT)'),
    ('04807', u'Maribondo (AL)'),
    ('04808', u'Cascavel * (PR)'),
    ('04808', u'Ipiranga do Piauí (PI)'),
    ('04809', u'Cortês (PE)'),
    ('04809', u'Japorã (MS)'),
    ('04809', u'Augusto de Lima (MG)'),
    ('04850', u'Coxixola (PB)'),
    ('04852', u'Cabaceiras do Paraguaçu (BA)'),
    ('04853', u'Itajá (RN)'),
    ('04853', u'Carlos Gomes (RS)'),
    ('04854', u'Campo Limpo de Goiás (GO)'),
    ('04900', u'Cruz do Espírito Santo (PB)'),
    ('04901', u'Muaná (PA)'),
    ('04902', u'Cachoeira (BA)'),
    ('04903', u'Casca (RS)'),
    ('04903', u'Itaú (RN)'),
    ('04904', u'São Gonçalo * (RJ)'),
    ('04904', u'Campos Belos (GO)'),
    ('04904', u'Pacatuba (SE)'),
    ('04905', u'Descanso (SC)'),
    ('04905', u'Groaíras (CE)'),
    ('04906', u'Mar Vermelho (AL)'),
    ('04906', u'São Mateus (ES)'),
    ('04906', u'Jangada (MT)'),
    ('04907', u'Isaías Coelho (PI)'),
    ('04907', u'Castro (PR)'),
    ('04908', u'Cumaru (PE)'),
    ('04908', u'Jaraguari (MS)'),
    ('04908', u'Baependi (MG)'),
    ('04909', u'Guimarães (MA)'),
    ('04909', u'Bananal (SP)'),
    ('04950', u'Nova Esperança do Piriá (PA)'),
    ('04952', u'Caseiros (RS)'),
    ('04953', u'Campos Verdes (GO)'),
    ('04954', u'Guaiúba (CE)'),
    ('04955', u'São Roque do Canaã (ES)'),
    ('04976', u'Nova Ipixuna (PA)'),
    ('05000', u'Pedra Mole (SE)'),
    ('05000', u'Carmo do Rio Verde (GO)'),
    ('05000', u'São João da Barra (RJ)'),
    ('05001', u'Dionísio Cerqueira (SC)'),
    ('05001', u'Guaraciaba do Norte (CE)'),
    ('05002', u'Serra * (ES)'),
    ('05002', u'Mata Grande (AL)'),
    ('05002', u'Jauru (MT)'),
    ('05003', u'Catanduvas (PR)'),
    ('05003', u'Itainópolis (PI)'),
    ('05004', u'Jardim (MS)'),
    ('05004', u'Cupira (PE)'),
    ('05004', u'Baldim (MG)'),
    ('05005', u'Barão de Antonina (SP)'),
    ('05005', u'Humberto de Campos (MA)'),
    ('05006', u'Cubati (PB)'),
    ('05007', u'Nova Timboteua (PA)'),
    ('05008', u'Caculé (BA)'),
    ('05009', u'Catuípe (RS)'),
    ('05009', u'Jaçanã (RN)'),
    ('05010', u'Sooretama (ES)'),
    ('05031', u'Novo Progresso (PA)'),
    ('05036', u'Vargem Alta (ES)'),
    ('05059', u'Castelândia (GO)'),
    ('05064', u'Novo Repartimento (PA)'),
    ('05069', u'Venda Nova do Imigrante (ES)'),
    ('05100', u'Dona Emma (SC)'),
    ('05100', u'Guaramiranga (CE)'),
    ('05101', u'Viana (ES)'),
    ('05101', u'Matriz de Camaragibe (AL)'),
    ('05101', u'Juara (MT)'),
    ('05102', u'Centenário do Sul (PR)'),
    ('05102', u'Itaueira (PI)'),
    ('05102', u'Chapada da Natividade (TO)'),
    ('05103', u'Jateí (MS)'),
    ('05103', u'Bambuí (MG)'),
    ('05103', u'Custódia (PE)'),
    ('05104', u'Barbosa (SP)'),
    ('05104', u'Icatu (MA)'),
    ('05105', u'Cuité (PB)'),
    ('05106', u'Óbidos (PA)'),
    ('05107', u'Caém (BA)'),
    ('05108', u'Jandaíra (RN)'),
    ('05108', u'Caxias do Sul * (RS)'),
    ('05109', u'São João de Meriti * (RJ)'),
    ('05109', u'Catalão (GO)'),
    ('05109', u'Pedrinhas (SE)'),
    ('05116', u'Centenário (RS)'),
    ('05124', u'Cerrito (RS)'),
    ('05132', u'Cerro Branco (RS)'),
    ('05133', u'São José de Ubá (RJ)'),
    ('05150', u'Juína (MT)'),
    ('05150', u'Vila Pavão (ES)'),
    ('05151', u'Jacobina do Piauí (PI)'),
    ('05152', u'Juti (MS)'),
    ('05152', u'Dormentes (PE)'),
    ('05153', u'Igarapé do Meio (MA)'),
    ('05156', u'Caetanos (BA)'),
    ('05157', u'Cerro Grande (RS)'),
    ('05158', u'São José do Vale do Rio Preto (RJ)'),
    ('05159', u'Doutor Pedrinho (SC)'),
    ('05173', u'Cerro Grande do Sul (RS)'),
    ('05175', u'Entre Rios (SC)'),
    ('05176', u'Vila Valério (ES)'),
    ('05176', u'Juruena (MT)'),
    ('05191', u'Ermo (SC)'),
    ('05200', u'Juscimeira (MT)'),
    ('05200', u'Vila Velha * (ES)'),
    ('05200', u'Messias (AL)'),
    ('05201', u'Cerro Azul (PR)'),
    ('05201', u'Jaicós (PI)'),
    ('05202', u'Ladário (MS)'),
    ('05202', u'Escada (PE)'),
    ('05202', u'Bandeira (MG)'),
    ('05203', u'Bariri (SP)'),
    ('05203', u'Igarapé Grande (MA)'),
    ('05204', u'Cuitegi (PB)'),
    ('05205', u'Oeiras do Pará (PA)'),
    ('05206', u'Caetité (BA)'),
    ('05207', u'Janduís (RN)'),
    ('05207', u'Cerro Largo (RS)'),
    ('05208', u'Caturaí (GO)'),
    ('05208', u'Pinhão (SE)'),
    ('05208', u'São Pedro da Aldeia (RJ)'),
    ('05209', u'Erval Velho (SC)'),
    ('05209', u'Hidrolândia (CE)'),
    ('05233', u'Horizonte (CE)'),
    ('05234', u'Lambari D`Oeste (MT)'),
    ('05238', u'Cuité de Mamanguape (PB)'),
    ('05250', u'Jardim do Mulato (PI)'),
    ('05251', u'Laguna Carapã (MS)'),
    ('05259', u'Lucas do Rio Verde (MT)'),
    ('05266', u'Ibaretama (CE)'),
    ('05276', u'Jatobá do Piauí (PI)'),
    ('05279', u'Curral de Cima (PB)'),
    ('05300', u'Céu Azul (PR)'),
    ('05300', u'Jerumenha (PI)'),
    ('05301', u'Bandeira do Sul (MG)'),
    ('05301', u'Exu (PE)'),
    ('05302', u'Imperatriz (MA)'),
    ('05302', u'Barra Bonita (SP)'),
    ('05303', u'Curral Velho (PB)'),
    ('05304', u'Oriximiná (PA)'),
    ('05305', u'Cafarnaum (BA)'),
    ('05306', u'Januário Cicco (RN)'),
    ('05306', u'Chapada (RS)'),
    ('05307', u'Pirambu (SE)'),
    ('05307', u'São Sebastião do Alto (RJ)'),
    ('05307', u'Cavalcante (GO)'),
    ('05308', u'Ibiapina (CE)'),
    ('05308', u'Faxinal dos Guedes (SC)'),
    ('05309', u'Minador do Negrão (AL)'),
    ('05309', u'Vitória * (ES)'),
    ('05309', u'Luciára (MT)'),
    ('05332', u'Ibicuitinga (CE)'),
    ('05351', u'Barra do Chapéu (SP)'),
    ('05351', u'Itaipava do Grajaú (MA)'),
    ('05352', u'Damião (PB)'),
    ('05355', u'Charqueadas (RS)'),
    ('05357', u'Icapuí (CE)'),
    ('05357', u'Flor do Sertão (SC)'),
    ('05359', u'João Costa (PI)'),
    ('05371', u'Charrua (RS)'),
    ('05400', u'Barão de Cocais (MG)'),
    ('05400', u'Feira Nova (PE)'),
    ('05400', u'Maracaju (MS)'),
    ('05401', u'Barra do Turvo (SP)'),
    ('05401', u'Itapecuru Mirim (MA)'),
    ('05402', u'Desterro (PB)'),
    ('05403', u'Ourém (PA)'),
    ('05404', u'Cairu (BA)'),
    ('05405', u'Chiapetta (RS)'),
    ('05405', u'Japi (RN)'),
    ('05406', u'Ceres (GO)'),
    ('05406', u'Sapucaia (RJ)'),
    ('05406', u'Poço Redondo (SE)'),
    ('05407', u'Florianópolis * (SC)'),
    ('05407', u'Icó (CE)'),
    ('05408', u'Monteirópolis (AL)'),
    ('05409', u'Chopinzinho (PR)'),
    ('05409', u'Joaquim Pires (PI)'),
    ('05427', u'Itinga do Maranhão (MA)'),
    ('05431', u'Formosa do Sul (SC)'),
    ('05437', u'Ourilândia do Norte (PA)'),
    ('05439', u'Chuí (RS)'),
    ('05447', u'Chuvisca (RS)'),
    ('05450', u'Jatobá (MA)'),
    ('05454', u'Cidreira (RS)'),
    ('05455', u'Cezarina (GO)'),
    ('05456', u'Forquilhinha (SC)'),
    ('05458', u'Joca Marques (PI)'),
    ('05459', u'Fernando de Noronha (PE)'),
    ('05471', u'Chapadão do Céu (GO)'),
    ('05476', u'Jenipapo dos Vieiras (MA)'),
    ('05486', u'Pacajá (PA)'),
    ('05494', u'Palestina do Pará (PA)'),
    ('05497', u'Cidade Ocidental (GO)'),
    ('05500', u'Barretos (SP)'),
    ('05500', u'João Lisboa (MA)'),
    ('05501', u'Vista Serrana (PB)'),
    ('05502', u'Paragominas (PA)'),
    ('05503', u'Caldeirão Grande (BA)'),
    ('05504', u'Jardim de Angicos (RN)'),
    ('05504', u'Ciríaco (RS)'),
    ('05505', u'Poço Verde (SE)'),
    ('05505', u'Saquarema (RJ)'),
    ('05506', u'Iguatu (CE)'),
    ('05506', u'Fraiburgo (SC)'),
    ('05507', u'Murici (AL)'),
    ('05507', u'Vila Bela da Santíssima Trindade (MT)'),
    ('05508', u'Colinas do Tocantins (TO)'),
    ('05508', u'José de Freitas (PI)'),
    ('05508', u'Cianorte (PR)'),
    ('05509', u'Barão de Monte Alto (MG)'),
    ('05509', u'Ferreiros (PE)'),
    ('05513', u'Cocalzinho de Goiás (GO)'),
    ('05516', u'Juazeiro do Piauí (PI)'),
    ('05521', u'Colinas do Sul (GO)'),
    ('05524', u'Júlio Borges (PI)'),
    ('05532', u'Jurema (PI)'),
    ('05536', u'Parauapebas (PA)'),
    ('05540', u'Lagoinha do Piauí (PI)'),
    ('05551', u'Pau D`Arco (PA)'),
    ('05554', u'Seropédica (RJ)'),
    ('05555', u'Frei Rogério (SC)'),
    ('05557', u'Lagoa Alegre (PI)'),
    ('05557', u'Combinado (TO)'),
    ('05565', u'Lagoa do Barro do Piauí (PI)'),
    ('05573', u'Lagoa de São Francisco (PI)'),
    ('05580', u'Marcelândia (MT)'),
    ('05581', u'Lagoa do Piauí (PI)'),
    ('05587', u'Colinas (RS)'),
    ('05599', u'Lagoa do Sítio (PI)'),
    ('05600', u'Diamante (PB)'),
    ('05601', u'Peixe-Boi (PA)'),
    ('05602', u'Camacan (BA)'),
    ('05603', u'Jardim de Piranhas (RN)'),
    ('05603', u'Colorado (RS)'),
    ('05604', u'Porto da Folha (SE)'),
    ('05604', u'Silva Jardim (RJ)'),
    ('05605', u'Independência (CE)'),
    ('05605', u'Galvão (SC)'),
    ('05606', u'Novo Lino (AL)'),
    ('05606', u'Matupá (MT)'),
    ('05607', u'Conceição do Tocantins (TO)'),
    ('05607', u'Cidade Gaúcha (PR)'),
    ('05607', u'Landri Sales (PI)'),
    ('05608', u'Barbacena (MG)'),
    ('05608', u'Miranda (MS)'),
    ('05608', u'Flores (PE)'),
    ('05609', u'Barrinha (SP)'),
    ('05609', u'Joselândia (MA)'),
    ('05622', u'Mirassol d`Oeste (MT)'),
    ('05635', u'Piçarra (PA)'),
    ('05650', u'Placas (PA)'),
    ('05654', u'Ipaporanga (CE)'),
    ('05658', u'Junco do Maranhão (MA)'),
    ('05681', u'Mundo Novo (MS)'),
    ('05700', u'Ponta de Pedras (PA)'),
    ('05701', u'Camaçari * (BA)'),
    ('05702', u'Jardim do Seridó (RN)'),
    ('05702', u'Condor (RS)'),
    ('05703', u'Córrego do Ouro (GO)'),
    ('05703', u'Sumidouro (RJ)'),
    ('05703', u'Propriá (SE)'),
    ('05704', u'Garopaba (SC)'),
    ('05704', u'Ipaumirim (CE)'),
    ('05705', u'Olho d`Água das Flores (AL)'),
    ('05706', u'Clevelândia (PR)'),
    ('05706', u'Luís Correia (PI)'),
    ('05707', u'Barra Longa (MG)'),
    ('05707', u'Naviraí (MS)'),
    ('05707', u'Floresta (PE)'),
    ('05708', u'Barueri * (SP)'),
    ('05708', u'Lago da Pedra (MA)'),
    ('05709', u'Dona Inês (PB)'),
    ('05752', u'Tanguá (RJ)'),
    ('05800', u'Camamu (BA)'),
    ('05801', u'João Câmara (RN)'),
    ('05801', u'Constantina (RS)'),
    ('05802', u'Teresópolis (RJ)'),
    ('05802', u'Corumbá de Goiás (GO)'),
    ('05802', u'Riachão do Dantas (SE)'),
    ('05803', u'Ipu (CE)'),
    ('05803', u'Garuva (SC)'),
    ('05804', u'Olho d`Água do Casado (AL)'),
    ('05805', u'Colombo * (PR)'),
    ('05805', u'Luzilândia (PI)'),
    ('05806', u'Nioaque (MS)'),
    ('05806', u'Frei Miguelinho (PE)'),
    ('05807', u'Lago do Junco (MA)'),
    ('05807', u'Bastos (SP)'),
    ('05808', u'Duas Estradas (PB)'),
    ('05809', u'Portel (PA)'),
    ('05835', u'Coqueiro Baixo (RS)'),
    ('05850', u'Coqueiros do Sul (RS)'),
    ('05854', u'Madeiro (PI)'),
    ('05871', u'Coronel Barros (RS)'),
    ('05900', u'João Dias (RN)'),
    ('05900', u'Coronel Bicaco (RS)'),
    ('05901', u'Trajano de Morais (RJ)'),
    ('05901', u'Riachuelo (SE)'),
    ('05901', u'Corumbaíba (GO)'),
    ('05902', u'Gaspar (SC)'),
    ('05902', u'Ipueiras (CE)'),
    ('05903', u'Olho d`Água Grande (AL)'),
    ('05903', u'Nobres (MT)'),
    ('05904', u'Colorado (PR)'),
    ('05904', u'Manoel Emídio (PI)'),
    ('05905', u'Gameleira (PE)'),
    ('05905', u'Barroso (MG)'),
    ('05906', u'Batatais (SP)'),
    ('05906', u'Lago Verde (MA)'),
    ('05907', u'Emas (PB)'),
    ('05908', u'Porto de Moz (PA)'),
    ('05909', u'Campo Alegre de Lourdes (BA)'),
    ('05922', u'Lagoa do Mato (MA)'),
    ('05934', u'Coronel Pilar (RS)'),
    ('05948', u'Lago dos Rodrigues (MA)'),
    ('05953', u'Marcolândia (PI)'),
    ('05959', u'Cotiporã (RS)'),
    ('05963', u'Lagoa Grande do Maranhão (MA)'),
    ('05975', u'Coxilha (RS)'),
    ('05989', u'Lajeado Novo (MA)'),
    ('06000', u'Olivença (AL)'),
    ('06000', u'Nortelândia (MT)'),
    ('06001', u'Couto de Magalhães (TO)'),
    ('06001', u'Congonhinhas (PR)'),
    ('06001', u'Marcos Parente (PI)'),
    ('06002', u'Nova Alvorada do Sul (MS)'),
    ('06002', u'Bela Vista de Minas (MG)'),
    ('06002', u'Garanhuns (PE)'),
    ('06003', u'Lima Campos (MA)'),
    ('06003', u'Bauru * (SP)'),
    ('06004', u'Esperança (PB)'),
    ('06005', u'Prainha (PA)'),
    ('06006', u'Campo Formoso (BA)'),
    ('06007', u'Crissiumal (RS)'),
    ('06007', u'José da Penha (RN)'),
    ('06008', u'Três Rios (RJ)'),
    ('06008', u'Ribeirópolis (SE)'),
    ('06009', u'Governador Celso Ramos (SC)'),
    ('06009', u'Iracema (CE)'),
    ('06050', u'Massapê do Piauí (PI)'),
    ('06056', u'Cristal (RS)'),
    ('06072', u'Cristal do Sul (RS)'),
    ('06100', u'Matias Olímpio (PI)'),
    ('06100', u'Conselheiro Mairinck (PR)'),
    ('06100', u'Cristalândia (TO)'),
    ('06101', u'Glória do Goitá (PE)'),
    ('06101', u'Belmiro Braga (MG)'),
    ('06102', u'Loreto (MA)'),
    ('06102', u'Bebedouro (SP)'),
    ('06103', u'Fagundes (PB)'),
    ('06104', u'Primavera (PA)'),
    ('06105', u'Canápolis (BA)'),
    ('06106', u'Jucurutu (RN)'),
    ('06106', u'Cruz Alta (RS)'),
    ('06107', u'Valença (RJ)'),
    ('06107', u'Rosário do Catete (SE)'),
    ('06108', u'Grão Pará (SC)'),
    ('06108', u'Irauçuba (CE)'),
    ('06109', u'Nossa Senhora do Livramento (MT)'),
    ('06109', u'Ouro Branco (AL)'),
    ('06112', u'Quatipuru (PA)'),
    ('06130', u'Cruzaltense (RS)'),
    ('06138', u'Redenção (PA)'),
    ('06155', u'Jundiá (RN)'),
    ('06156', u'Varre-Sai (RJ)'),
    ('06158', u'Nova Bandeirantes (MT)'),
    ('06161', u'Rio Maria (PA)'),
    ('06174', u'Nova Nazaré (MT)'),
    ('06182', u'Nova Lacerda (MT)'),
    ('06187', u'Rondon do Pará (PA)'),
    ('06190', u'Nova Santa Helena (MT)'),
    ('06195', u'Rurópolis (PA)'),
    ('06200', u'Nova Andradina (MS)'),
    ('06200', u'Goiana (PE)'),
    ('06200', u'Belo Horizonte * (MG)'),
    ('06201', u'Bento de Abreu (SP)'),
    ('06201', u'Luís Domingues (MA)'),
    ('06202', u'Frei Martinho (PB)'),
    ('06203', u'Salinópolis (PA)'),
    ('06204', u'Canarana (BA)'),
    ('06205', u'Lagoa d`Anta (RN)'),
    ('06205', u'Cruzeiro do Sul (RS)'),
    ('06206', u'Salgado (SE)'),
    ('06206', u'Vassouras (RJ)'),
    ('06206', u'Cristalina (GO)'),
    ('06207', u'Gravatal (SC)'),
    ('06207', u'Itaiçaba (CE)'),
    ('06208', u'Nova Brasilândia (MT)'),
    ('06208', u'Palestina (AL)'),
    ('06209', u'Contenda (PR)'),
    ('06209', u'Miguel Alves (PI)'),
    ('06216', u'Nova Canaã do Norte (MT)'),
    ('06224', u'Nova Mutum (MT)'),
    ('06232', u'Nova Olímpia (MT)'),
    ('06240', u'Nova Ubiratã (MT)'),
    ('06251', u'Gado Bravo (PB)'),
    ('06256', u'Itaitinga (CE)'),
    ('06257', u'Nova Xavantina (MT)'),
    ('06258', u'Crixás do Tocantins (TO)'),
    ('06259', u'Novo Horizonte do Sul (MS)'),
    ('06265', u'Novo Mundo (MT)'),
    ('06273', u'Novo Horizonte do Norte (MT)'),
    ('06281', u'Novo São Joaquim (MT)'),
    ('06299', u'Paranaíta (MT)'),
    ('06300', u'Bernardino de Campos (SP)'),
    ('06300', u'Magalhães de Almeida (MA)'),
    ('06301', u'Guarabira (PB)'),
    ('06302', u'Salvaterra (PA)'),
    ('06303', u'Canavieiras (BA)'),
    ('06304', u'David Canabarro (RS)'),
    ('06304', u'Lagoa de Pedras (RN)'),
    ('06305', u'Cristianópolis (GO)'),
    ('06305', u'Volta Redonda * (RJ)'),
    ('06305', u'Santa Luzia do Itanhy (SE)'),
    ('06306', u'Guabiruba (SC)'),
    ('06306', u'Itapagé (CE)'),
    ('06307', u'Palmeira dos Índios (AL)'),
    ('06307', u'Paranatinga (MT)'),
    ('06308', u'Corbélia (PR)'),
    ('06308', u'Miguel Leão (PI)'),
    ('06309', u'Belo Oriente (MG)'),
    ('06309', u'Paranaíba (MS)'),
    ('06309', u'Granito (PE)'),
    ('06315', u'Novo Santo Antônio (MT)'),
    ('06320', u'Derrubadas (RS)'),
    ('06326', u'Maracaçumé (MA)'),
    ('06351', u'Santa Bárbara do Pará (PA)'),
    ('06353', u'Dezesseis de Novembro (RS)'),
    ('06357', u'Milton Brandão (PI)'),
    ('06358', u'Paranhos (MS)'),
    ('06359', u'Bertioga (SP)'),
    ('06359', u'Marajá do Sena (MA)'),
    ('06372', u'Pedra Preta (MT)'),
    ('06375', u'Maranhãozinho (MA)'),
    ('06379', u'Dilermando de Aguiar (RS)'),
    ('06400', u'Gurinhém (PB)'),
    ('06401', u'Santa Cruz do Arari (PA)'),
    ('06402', u'Candeal (BA)'),
    ('06403', u'Lagoa de Velhos (RN)'),
    ('06403', u'Dois Irmãos (RS)'),
    ('06404', u'Santana do São Francisco (SE)'),
    ('06404', u'Crixás (GO)'),
    ('06405', u'Guaraciaba (SC)'),
    ('06405', u'Itapipoca (CE)'),
    ('06406', u'Pão de Açúcar (AL)'),
    ('06407', u'Cornélio Procópio (PR)'),
    ('06407', u'Monsenhor Gil (PI)'),
    ('06408', u'Belo Vale (MG)'),
    ('06408', u'Gravatá (PE)'),
    ('06408', u'Pedro Gomes (MS)'),
    ('06409', u'Mata Roma (MA)'),
    ('06409', u'Bilac (SP)'),
    ('06422', u'Pariconha (AL)'),
    ('06422', u'Peixoto de Azevedo (MT)'),
    ('06429', u'Dois Irmãos das Missões (RS)'),
    ('06448', u'Paripueira (AL)'),
    ('06452', u'Dois Lajeados (RS)'),
    ('06455', u'Planalto da Serra (MT)'),
    ('06456', u'Coronel Domingos Soares (PR)'),
    ('06500', u'Santa Isabel do Pará (PA)'),
    ('06501', u'Candeias (BA)'),
    ('06502', u'Dom Feliciano (RS)'),
    ('06502', u'Lagoa Nova (RN)'),
    ('06503', u'Santa Rosa de Lima (SE)'),
    ('06503', u'Cromínia (GO)'),
    ('06504', u'Guaramirim (SC)'),
    ('06504', u'Itapiúna (CE)'),
    ('06505', u'Poconé (MT)'),
    ('06505', u'Passo de Camaragibe (AL)'),
    ('06506', u'Coronel Vivida (PR)'),
    ('06506', u'Darcinópolis (TO)'),
    ('06506', u'Monsenhor Hipólito (PI)'),
    ('06507', u'Iati (PE)'),
    ('06507', u'Berilo (MG)'),
    ('06508', u'Birigui (SP)'),
    ('06508', u'Matinha (MA)'),
    ('06509', u'Gurjão (PB)'),
    ('06551', u'Dom Pedro de Alcântara (RS)'),
    ('06553', u'Itarema (CE)'),
    ('06555', u'Corumbataí do Sul (PR)'),
    ('06559', u'Santa Luzia do Pará (PA)'),
    ('06571', u'Cruzeiro do Iguaçu (PR)'),
    ('06583', u'Santa Maria das Barreiras (PA)'),
    ('06600', u'Candiba (BA)'),
    ('06601', u'Lagoa Salgada (RN)'),
    ('06601', u'Dom Pedrito (RS)'),
    ('06602', u'Cumari (GO)'),
    ('06602', u'Santo Amaro das Brotas (SE)'),
    ('06603', u'Guarujá do Sul (SC)'),
    ('06603', u'Itatira (CE)'),
    ('06604', u'Paulo Jacinto (AL)'),
    ('06605', u'Cruzeiro do Oeste (PR)'),
    ('06605', u'Monte Alegre do Piauí (PI)'),
    ('06606', u'Ponta Porã (MS)'),
    ('06606', u'Ibimirim (PE)'),
    ('06606', u'Bertópolis (MG)'),
    ('06607', u'Matões (MA)'),
    ('06607', u'Biritiba-Mirim (SP)'),
    ('06608', u'Ibiara (PB)'),
    ('06609', u'Santa Maria do Pará (PA)'),
    ('06631', u'Matões do Norte (MA)'),
    ('06652', u'Guatambú (SC)'),
    ('06653', u'Pontal do Araguaia (MT)'),
    ('06654', u'Morro Cabeça no Tempo (PI)'),
    ('06655', u'Berizal (MG)'),
    ('06670', u'Morro do Chapéu do Piauí (PI)'),
    ('06672', u'Milagres do Maranhão (MA)'),
    ('06696', u'Murici dos Portelas (PI)'),
    ('06700', u'Dona Francisca (RS)'),
    ('06700', u'Lajes (RN)'),
    ('06701', u'Damianópolis (GO)'),
    ('06701', u'São Cristóvão (SE)'),
    ('06702', u'Jaguaretama (CE)'),
    ('06702', u'Herval d`Oeste (SC)'),
    ('06703', u'Penedo (AL)'),
    ('06703', u'Ponte Branca (MT)'),
    ('06704', u'Cruzeiro do Sul (PR)'),
    ('06704', u'Nazaré do Piauí (PI)'),
    ('06705', u'Ibirajuba (PE)'),
    ('06705', u'Betim * (MG)'),
    ('06706', u'Mirador (MA)'),
    ('06706', u'Boa Esperança do Sul (SP)'),
    ('06707', u'Imaculada (PB)'),
    ('06708', u'Santana do Araguaia (PA)'),
    ('06709', u'Cândido Sales (BA)'),
    ('06734', u'Doutor Maurício Cardoso (RS)'),
    ('06751', u'Ibiam (SC)'),
    ('06752', u'Pontes e Lacerda (MT)'),
    ('06753', u'Nossa Senhora de Nazaré (PI)'),
    ('06755', u'Miranda do Norte (MA)'),
    ('06759', u'Doutor Ricardo (RS)'),
    ('06767', u'Eldorado do Sul (RS)'),
    ('06778', u'Porto Alegre do Norte (MT)'),
    ('06800', u'São Domingos (SE)'),
    ('06800', u'Damolândia (GO)'),
    ('06801', u'Jaguaribara (CE)'),
    ('06801', u'Ibicaré (SC)'),
    ('06802', u'Piaçabuçu (AL)'),
    ('06802', u'Porto dos Gaúchos (MT)'),
    ('06803', u'Cruz Machado (PR)'),
    ('06803', u'Nossa Senhora dos Remédios (PI)'),
    ('06804', u'Igarassu (PE)'),
    ('06804', u'Bias Fortes (MG)'),
    ('06805', u'Bocaina (SP)'),
    ('06805', u'Mirinzal (MA)'),
    ('06806', u'Ingá (PB)'),
    ('06807', u'Santarém * (PA)'),
    ('06808', u'Cansanção (BA)'),
    ('06809', u'Lajes Pintadas (RN)'),
    ('06809', u'Encantado (RS)'),
    ('06824', u'Canudos (BA)'),
    ('06828', u'Porto Esperidião (MT)'),
    ('06851', u'Porto Estrela (MT)'),
    ('06852', u'Cruzmaltina (PR)'),
    ('06857', u'Capela do Alto Alegre (BA)'),
    ('06873', u'Capim Grosso (BA)'),
    ('06899', u'Caraíbas (BA)'),
    ('06900', u'Jaguaribe (CE)'),
    ('06900', u'Ibirama (SC)'),
    ('06901', u'Pilar (AL)'),
    ('06902', u'Novo Oriente do Piauí (PI)'),
    ('06902', u'Curitiba * (PR)'),
    ('06903', u'Bicas (MG)'),
    ('06903', u'Porto Murtinho (MS)'),
    ('06903', u'Iguaraci (PE)'),
    ('06904', u'Monção (MA)'),
    ('06904', u'Bofete (SP)'),
    ('06905', u'Itabaiana (PB)'),
    ('06906', u'Santarém Novo (PA)'),
    ('06907', u'Caravelas (BA)'),
    ('06908', u'Encruzilhada do Sul (RS)'),
    ('06908', u'Lucrécia (RN)'),
    ('06909', u'São Francisco (SE)'),
    ('06909', u'Davinópolis (GO)'),
    ('06924', u'Engenho Velho (RS)'),
    ('06932', u'Entre-Ijuís (RS)'),
    ('06951', u'Novo Santo Antônio (PI)'),
    ('06957', u'Entre Rios do Sul (RS)'),
    ('06973', u'Erebango (RS)'),
    ('07000', u'Biquinhas (MG)'),
    ('07000', u'Inajá (PE)'),
    ('07001', u'Boituva (SP)'),
    ('07001', u'Montes Altos (MA)'),
    ('07002', u'Itaporanga (PB)'),
    ('07003', u'Santo Antônio do Tauá (PA)'),
    ('07004', u'Cardeal da Silva (BA)'),
    ('07005', u'Erechim (RS)'),
    ('07005', u'Luís Gomes (RN)'),
    ('07006', u'São Miguel do Aleixo (SE)'),
    ('07007', u'Jaguaruana (CE)'),
    ('07007', u'Içara (SC)'),
    ('07008', u'Poxoréo (MT)'),
    ('07008', u'Pindoba (AL)'),
    ('07009', u'Dianópolis (TO)'),
    ('07009', u'Curiúva (PR)'),
    ('07009', u'Oeiras (PI)'),
    ('07040', u'Primavera do Leste (MT)'),
    ('07054', u'Ernestina (RS)'),
    ('07065', u'Querência (MT)'),
    ('07100', u'Bom Jesus dos Perdões (SP)'),
    ('07100', u'Morros (MA)'),
    ('07101', u'Itapororoca (PB)'),
    ('07102', u'São Caetano de Odivelas (PA)'),
    ('07103', u'Carinhanha (BA)'),
    ('07104', u'Macaíba (RN)'),
    ('07104', u'Herval (RS)'),
    ('07105', u'Diorama (GO)'),
    ('07105', u'Simão Dias (SE)'),
    ('07106', u'Jardim (CE)'),
    ('07106', u'Ilhota (SC)'),
    ('07107', u'São José dos Quatro Marcos (MT)'),
    ('07107', u'Piranhas (AL)'),
    ('07108', u'Divinópolis do Tocantins (TO)'),
    ('07108', u'Olho D`Água do Piauí (PI)'),
    ('07108', u'Diamante do Norte (PR)'),
    ('07109', u'Ingazeira (PE)'),
    ('07109', u'Boa Esperança (MG)'),
    ('07109', u'Ribas do Rio Pardo (MS)'),
    ('07124', u'Diamante do Sul (PR)'),
    ('07151', u'São Domingos do Araguaia (PA)'),
    ('07156', u'Reserva do Cabaçal (MT)'),
    ('07157', u'Diamante D`Oeste (PR)'),
    ('07159', u'Bom Sucesso de Itararé (SP)'),
    ('07180', u'Ribeirão Cascalheira (MT)'),
    ('07198', u'Ribeirãozinho (MT)'),
    ('07200', u'Itatuba (PB)'),
    ('07201', u'São Domingos do Capim (PA)'),
    ('07202', u'Casa Nova (BA)'),
    ('07203', u'Macau (RN)'),
    ('07203', u'Erval Grande (RS)'),
    ('07204', u'Siriri (SE)'),
    ('07205', u'Jati (CE)'),
    ('07205', u'Imaruí (SC)'),
    ('07206', u'Rio Branco (MT)'),
    ('07206', u'Poço das Trincheiras (AL)'),
    ('07207', u'Dois Vizinhos (PR)'),
    ('07207', u'Dois Irmãos do Tocantins (TO)'),
    ('07207', u'Padre Marcos (PI)'),
    ('07208', u'Rio Brilhante (MS)'),
    ('07208', u'Bocaina de Minas (MG)'),
    ('07208', u'Ipojuca (PE)'),
    ('07209', u'Nina Rodrigues (MA)'),
    ('07209', u'Borá (SP)'),
    ('07248', u'Santa Carmem (MT)'),
    ('07252', u'Major Sales (RN)'),
    ('07253', u'Doverlândia (GO)'),
    ('07254', u'Jijoca de Jericoacoara (CE)'),
    ('07256', u'Douradina (PR)'),
    ('07258', u'Nova Colinas (MA)'),
    ('07263', u'Santo Afonso (MT)'),
    ('07297', u'São José do Povo (MT)'),
    ('07300', u'São Félix do Xingu (PA)'),
    ('07301', u'Castro Alves (BA)'),
    ('07302', u'Marcelino Vieira (RN)'),
    ('07302', u'Erval Seco (RS)'),
    ('07303', u'Telha (SE)'),
    ('07304', u'Juazeiro do Norte * (CE)'),
    ('07304', u'Imbituba (SC)'),
    ('07305', u'Porto Calvo (AL)'),
    ('07305', u'São José do Rio Claro (MT)'),
    ('07306', u'Dueré (TO)'),
    ('07306', u'Paes Landim (PI)'),
    ('07306', u'Doutor Camargo (PR)'),
    ('07307', u'Ipubi (PE)'),
    ('07307', u'Rio Negro (MS)'),
    ('07307', u'Bocaiúva (MG)'),
    ('07308', u'Nova Iorque (MA)'),
    ('07308', u'Boracéia (SP)'),
    ('07309', u'Jacaraú (PB)'),
    ('07352', u'Edealina (GO)'),
    ('07354', u'São José do Xingu (MT)'),
    ('07355', u'Pajeú do Piauí (PI)'),
    ('07357', u'Nova Olinda do Maranhão (MA)'),
    ('07400', u'Catolândia (BA)'),
    ('07401', u'Martins (RN)'),
    ('07401', u'Esmeralda (RS)'),
    ('07402', u'Tobias Barreto (SE)'),
    ('07402', u'Edéia (GO)'),
    ('07403', u'Imbuia (SC)'),
    ('07403', u'Jucás (CE)'),
    ('07404', u'São Pedro da Cipa (MT)'),
    ('07404', u'Porto de Pedras (AL)'),
    ('07405', u'Enéas Marques (PR)'),
    ('07405', u'Esperantina (TO)'),
    ('07405', u'Palmeira do Piauí (PI)'),
    ('07406', u'Rio Verde de Mato Grosso (MS)'),
    ('07406', u'Itacuruba (PE)'),
    ('07406', u'Bom Despacho (MG)'),
    ('07407', u'Olho d`Água das Cunhãs (MA)'),
    ('07407', u'Borborema (SP)'),
    ('07408', u'Jericó (PB)'),
    ('07409', u'São Francisco do Pará (PA)'),
    ('07450', u'Esperança do Sul (RS)'),
    ('07456', u'Olinda Nova do Maranhão (MA)'),
    ('07456', u'Borebi (SP)'),
    ('07458', u'São Geraldo do Araguaia (PA)'),
    ('07466', u'São João da Ponta (PA)'),
    ('07474', u'São João de Pirabas (PA)'),
    ('07500', u'Espumoso (RS)'),
    ('07500', u'Maxaranguape (RN)'),
    ('07501', u'Estrela do Norte (GO)'),
    ('07501', u'Tomar do Geru (SE)'),
    ('07502', u'Indaial (SC)'),
    ('07502', u'Lavras da Mangabeira (CE)'),
    ('07503', u'Porto Real do Colégio (AL)'),
    ('07504', u'Palmeirais (PI)'),
    ('07504', u'Engenheiro Beltrão (PR)'),
    ('07505', u'Rochedo (MS)'),
    ('07505', u'Itaíba (PE)'),
    ('07505', u'Bom Jardim de Minas (MG)'),
    ('07506', u'Paço do Lumiar (MA)'),
    ('07506', u'Botucatu (SP)'),
    ('07507', u'João Pessoa (PB)'),
    ('07508', u'São João do Araguaia (PA)'),
    ('07509', u'Catu (BA)'),
    ('07520', u'Esperança Nova (PR)'),
    ('07535', u'Faina (GO)'),
    ('07538', u'Entre Rios do Oeste (PR)'),
    ('07546', u'Espigão Alto do Iguaçu (PR)'),
    ('07553', u'Fátima (TO)'),
    ('07553', u'Farol (PR)'),
    ('07553', u'Paquetá (PI)'),
    ('07554', u'Santa Rita do Pardo (MS)'),
    ('07558', u'Caturama (BA)'),
    ('07559', u'Estação (RS)'),
    ('07577', u'Iomerê (SC)'),
    ('07578', u'Rondolândia (MT)'),
    ('07600', u'Fazenda Nova (GO)'),
    ('07600', u'Umbaúba (SE)'),
    ('07601', u'Ipira (SC)'),
    ('07601', u'Limoeiro do Norte (CE)'),
    ('07602', u'Rondonópolis (MT)'),
    ('07602', u'Quebrangulo (AL)'),
    ('07603', u'Faxinal (PR)'),
    ('07603', u'Parnaguá (PI)'),
    ('07604', u'Ilha de Itamaracá (PE)'),
    ('07604', u'Bom Jesus da Penha (MG)'),
    ('07605', u'Palmeirândia (MA)'),
    ('07605', u'Bragança Paulista (SP)'),
    ('07606', u'Juarez Távora (PB)'),
    ('07607', u'São Miguel do Guamá (PA)'),
    ('07608', u'Central (BA)'),
    ('07609', u'Estância Velha (RS)'),
    ('07609', u'Messias Targino (RN)'),
    ('07635', u'Madalena (CE)'),
    ('07650', u'Iporã do Oeste (SC)'),
    ('07650', u'Maracanaú * (CE)'),
    ('07652', u'Figueirópolis (TO)'),
    ('07652', u'Fazenda Rio Grande (PR)'),
    ('07653', u'Itambé (PE)'),
    ('07684', u'Ipuaçu (SC)'),
    ('07695', u'São Gabriel do Oeste (MS)'),
    ('07700', u'Ipumirim (SC)'),
    ('07700', u'Maranguape (CE)'),
    ('07701', u'Rio Largo (AL)'),
    ('07701', u'Rosário Oeste (MT)'),
    ('07702', u'Fênix (PR)'),
    ('07702', u'Filadélfia (TO)'),
    ('07702', u'Parnaíba (PI)'),
    ('07703', u'Itapetim (PE)'),
    ('07703', u'Sete Quedas (MS)'),
    ('07703', u'Bom Jesus do Amparo (MG)'),
    ('07704', u'Braúna (SP)'),
    ('07704', u'Paraibano (MA)'),
    ('07705', u'Juazeirinho (PB)'),
    ('07706', u'São Sebastião da Boa Vista (PA)'),
    ('07707', u'Chorrochó (BA)'),
    ('07708', u'Montanhas (RN)'),
    ('07708', u'Esteio (RS)'),
    ('07736', u'Fernandes Pinheiro (PR)'),
    ('07743', u'Santa Cruz do Xingu (MT)'),
    ('07750', u'Salto do Céu (MT)'),
    ('07751', u'Passagem Franca do Piauí (PI)'),
    ('07751', u'Figueira (PR)'),
    ('07752', u'Itapissuma (PE)'),
    ('07753', u'Brejo Alegre (SP)'),
    ('07755', u'Sapucaia (PA)'),
    ('07759', u'Iraceminha (SC)'),
    ('07768', u'Santa Rita do Trivelato (MT)'),
    ('07776', u'Santa Terezinha (MT)'),
    ('07777', u'Patos do Piauí (PI)'),
    ('07792', u'Santo Antônio do Leste (MT)'),
    ('07793', u'Pau D`Arco do Piauí (PI)'),
    ('07800', u'Santo Antônio do Leverger (MT)'),
    ('07800', u'Roteiro (AL)'),
    ('07801', u'Floraí (PR)'),
    ('07801', u'Paulistana (PI)'),
    ('07802', u'Selvíria (MS)'),
    ('07802', u'Itaquitinga (PE)'),
    ('07802', u'Bom Jesus do Galho (MG)'),
    ('07803', u'Parnarama (MA)'),
    ('07803', u'Brodowski (SP)'),
    ('07804', u'Junco do Seridó (PB)'),
    ('07805', u'Senador José Porfírio (PA)'),
    ('07806', u'Cícero Dantas (BA)'),
    ('07807', u'Estrela (RS)'),
    ('07807', u'Monte Alegre (RN)'),
    ('07808', u'Firminópolis (GO)'),
    ('07809', u'Marco (CE)'),
    ('07809', u'Irani (SC)'),
    ('07815', u'Estrela Velha (RS)'),
    ('07831', u'Eugênio de Castro (RS)'),
    ('07850', u'Flor da Serra do Sul (PR)'),
    ('07850', u'Pavussu (PI)'),
    ('07858', u'Irati (SC)'),
    ('07859', u'São Félix do Araguaia (MT)'),
    ('07864', u'Fagundes Varela (RS)'),
    ('07875', u'Sapezal (MT)'),
    ('07883', u'Serra Nova Dourada (MT)'),
    ('07900', u'Pedro II (PI)'),
    ('07900', u'Floresta (PR)'),
    ('07901', u'Jaboatão dos Guararapes * (PE)'),
    ('07901', u'Bom Repouso (MG)'),
    ('07901', u'Sidrolândia (MS)'),
    ('07902', u'Brotas (SP)'),
    ('07902', u'Passagem Franca (MA)'),
    ('07903', u'Juripiranga (PB)'),
    ('07904', u'Soure (PA)'),
    ('07905', u'Cipó (BA)'),
    ('07906', u'Monte das Gameleiras (RN)'),
    ('07906', u'Farroupilha (RS)'),
    ('07907', u'Flores de Goiás (GO)'),
    ('07908', u'Irineópolis (SC)'),
    ('07908', u'Martinópole (CE)'),
    ('07909', u'Santa Luzia do Norte (AL)'),
    ('07909', u'Sinop (MT)'),
    ('07925', u'Sorriso (MT)'),
    ('07934', u'Pedro Laurentino (PI)'),
    ('07935', u'Sonora (MS)'),
    ('07941', u'Tabaporã (MT)'),
    ('07950', u'Tacuru (MS)'),
    ('07950', u'Jaqueira (PE)'),
    ('07953', u'Tailândia (PA)'),
    ('07958', u'Tangará da Serra (MT)'),
    ('07959', u'Nova Santa Rita (PI)'),
    ('07961', u'Terra Alta (PA)'),
    ('07976', u'Taquarussu (MS)'),
    ('07979', u'Terra Santa (PA)'),
    ('08000', u'Juru (PB)'),
    ('08001', u'Tomé-Açu (PA)'),
    ('08002', u'Coaraci (BA)'),
    ('08003', u'Faxinal do Soturno (RS)'),
    ('08003', u'Mossoró (RN)'),
    ('08004', u'Formosa (GO)'),
    ('08005', u'Itá (SC)'),
    ('08005', u'Massapê (CE)'),
    ('08006', u'Santana do Ipanema (AL)'),
    ('08006', u'Tapurah (MT)'),
    ('08007', u'Florestópolis (PR)'),
    ('08007', u'Picos (PI)'),
    ('08008', u'Terenos (MS)'),
    ('08008', u'Bom Sucesso (MG)'),
    ('08008', u'Jataúba (PE)'),
    ('08009', u'Buri (SP)'),
    ('08009', u'Pastos Bons (MA)'),
    ('08035', u'Tracuateua (PA)'),
    ('08050', u'Trairão (PA)'),
    ('08052', u'Faxinalzinho (RS)'),
    ('08055', u'Terra Nova do Norte (MT)'),
    ('08057', u'Jatobá (PE)'),
    ('08058', u'Paulino Neves (MA)'),
    ('08078', u'Fazenda Vilanova (RS)'),
    ('08084', u'Tucumã (PA)'),
    ('08100', u'Tucuruí (PA)'),
    ('08101', u'Cocos (BA)'),
    ('08102', u'Natal (RN)'),
    ('08102', u'Feliz (RS)'),
    ('08103', u'Formoso (GO)'),
    ('08104', u'Mauriti (CE)'),
    ('08104', u'Itaiópolis (SC)'),
    ('08105', u'Santana do Mundaú (AL)'),
    ('08105', u'Tesouro (MT)'),
    ('08106', u'Pimenteiras (PI)'),
    ('08106', u'Flórida (PR)'),
    ('08107', u'Bonfim (MG)'),
    ('08107', u'João Alfredo (PE)'),
    ('08108', u'Paulo Ramos (MA)'),
    ('08108', u'Buritama (SP)'),
    ('08109', u'Lagoa (PB)'),
    ('08126', u'Ulianópolis (PA)'),
    ('08152', u'Gameleira de Goiás (GO)'),
    ('08159', u'Uruará (por decisão judicial)** (PA)'),
    ('08200', u'Conceição da Feira (BA)'),
    ('08201', u'Nísia Floresta (RN)'),
    ('08201', u'Flores da Cunha (RS)'),
    ('08203', u'Itajaí (SC)'),
    ('08203', u'Meruoca (CE)'),
    ('08204', u'Torixoréu (MT)'),
    ('08204', u'São Brás (AL)'),
    ('08205', u'Formoso do Araguaia (TO)'),
    ('08205', u'Pio IX (PI)'),
    ('08205', u'Formosa do Oeste (PR)'),
    ('08206', u'Bonfinópolis de Minas (MG)'),
    ('08206', u'Joaquim Nabuco (PE)'),
    ('08207', u'Buritizal (SP)'),
    ('08207', u'Pedreiras (MA)'),
    ('08208', u'Lagoa de Dentro (PB)'),
    ('08209', u'Vigia (PA)'),
    ('08250', u'Floriano Peixoto (RS)'),
    ('08254', u'Fortaleza do Tabocão (TO)'),
    ('08255', u'Bonito de Minas (MG)'),
    ('08255', u'Jucati (PE)'),
    ('08256', u'Pedro do Rosário (MA)'),
    ('08300', u'Nova Cruz (RN)'),
    ('08300', u'Fontoura Xavier (RS)'),
    ('08301', u'Divinópolis de Goiás (GO)'),
    ('08302', u'Milagres (CE)'),
    ('08302', u'Itapema (SC)'),
    ('08303', u'São José da Laje (AL)'),
    ('08303', u'União do Sul (MT)'),
    ('08304', u'Piracuruca (PI)'),
    ('08304', u'Foz do Iguaçu * (PR)'),
    ('08304', u'Goianorte (TO)'),
    ('08305', u'Borda da Mata (MG)'),
    ('08305', u'Jupi (PE)'),
    ('08305', u'Três Lagoas (MS)'),
    ('08306', u'Penalva (MA)'),
    ('08306', u'Cabrália Paulista (SP)'),
    ('08307', u'Lagoa Seca (PB)'),
    ('08308', u'Viseu (PA)'),
    ('08309', u'Conceição do Almeida (BA)'),
    ('08320', u'Francisco Alves (PR)'),
    ('08351', u'Milhã (CE)'),
    ('08352', u'Vale de São Domingos (MT)'),
    ('08357', u'Vitória do Xingu (PA)'),
    ('08377', u'Miraíma (CE)'),
    ('08400', u'Goianápolis (GO)'),
    ('08401', u'Missão Velha (CE)'),
    ('08401', u'Itapiranga (SC)'),
    ('08402', u'São José da Tapera (AL)'),
    ('08402', u'Várzea Grande (MT)'),
    ('08403', u'Piripiri (PI)'),
    ('08403', u'Francisco Beltrão (PR)'),
    ('08404', u'Jurema (PE)'),
    ('08404', u'Vicentina (MS)'),
    ('08404', u'Botelhos (MG)'),
    ('08405', u'Cabreúva (SP)'),
    ('08405', u'Peri Mirim (MA)'),
    ('08406', u'Lastro (PB)'),
    ('08407', u'Xinguara (PA)'),
    ('08408', u'Conceição do Coité (BA)'),
    ('08409', u'Olho-d`Água do Borges (RN)'),
    ('08409', u'Formigueiro (RS)'),
    ('08433', u'Forquetinha (RS)'),
    ('08450', u'Itapoá (SC)'),
    ('08452', u'Foz do Jordão (PR)'),
    ('08453', u'Lagoa do Carro (PE)'),
    ('08454', u'Peritoró (MA)'),
    ('08458', u'Fortaleza dos Valos (RS)'),
    ('08500', u'Ituporanga (SC)'),
    ('08500', u'Mombaça (CE)'),
    ('08501', u'São Luís do Quitunde (AL)'),
    ('08501', u'Vera (MT)'),
    ('08502', u'Porto (PI)'),
    ('08502', u'General Carneiro (PR)'),
    ('08503', u'Botumirim (MG)'),
    ('08503', u'Lagoa do Itaenga (PE)'),
    ('08504', u'Pindaré-Mirim (MA)'),
    ('08504', u'Caçapava (SP)'),
    ('08505', u'Livramento (PB)'),
    ('08507', u'Conceição do Jacuípe (BA)'),
    ('08508', u'Frederico Westphalen (RS)'),
    ('08508', u'Ouro Branco (RN)'),
    ('08509', u'Goiandira (GO)'),
    ('08551', u'Godoy Moreira (PR)'),
    ('08551', u'Porto Alegre do Piauí (PI)'),
    ('08552', u'Brasilândia de Minas (MG)'),
    ('08554', u'Logradouro (PB)'),
    ('08600', u'Vila Rica (MT)'),
    ('08600', u'São Miguel dos Campos (AL)'),
    ('08601', u'Goioerê (PR)'),
    ('08601', u'Prata do Piauí (PI)'),
    ('08602', u'Lagoa do Ouro (PE)'),
    ('08602', u'Brasília de Minas (MG)'),
    ('08603', u'Cachoeira Paulista (SP)'),
    ('08603', u'Pinheiro (MA)'),
    ('08604', u'Lucena (PB)'),
    ('08606', u'Conde (BA)'),
    ('08607', u'Garibaldi (RS)'),
    ('08607', u'Paraná (RN)'),
    ('08608', u'Goianésia (GO)'),
    ('08609', u'Jaborá (SC)'),
    ('08609', u'Monsenhor Tabosa (CE)'),
    ('08650', u'Goioxim (PR)'),
    ('08650', u'Queimada Nova (PI)'),
    ('08656', u'Garruchos (RS)'),
    ('08700', u'Redenção do Gurguéia (PI)'),
    ('08700', u'Grandes Rios (PR)'),
    ('08701', u'Lagoa dos Gatos (PE)'),
    ('08701', u'Brás Pires (MG)'),
    ('08702', u'Pio XII (MA)'),
    ('08702', u'Caconde (SP)'),
    ('08703', u'Mãe d`Água (PB)'),
    ('08705', u'Condeúba (BA)'),
    ('08706', u'Paraú (RN)'),
    ('08706', u'Gaurama (RS)'),
    ('08707', u'Goiânia * (GO)'),
    ('08708', u'Jacinto Machado (SC)'),
    ('08708', u'Morada Nova (CE)'),
    ('08709', u'São Miguel dos Milagres (AL)'),
    ('08750', u'Lagoa Grande (PE)'),
    ('08800', u'Braúnas (MG)'),
    ('08800', u'Lajedo (PE)'),
    ('08801', u'Cafelândia (SP)'),
    ('08801', u'Pirapemas (MA)'),
    ('08802', u'Malta (PB)'),
    ('08804', u'Contendas do Sincorá (BA)'),
    ('08805', u'Parazinho (RN)'),
    ('08805', u'General Câmara (RS)'),
    ('08806', u'Goianira (GO)'),
    ('08807', u'Jaguaruna (SC)'),
    ('08807', u'Moraújo (CE)'),
    ('08808', u'São Sebastião (AL)'),
    ('08808', u'Nova Guarita (MT)'),
    ('08809', u'Guaíra (PR)'),
    ('08809', u'Regeneração (PI)'),
    ('08854', u'Gentil (RS)'),
    ('08857', u'Nova Marilândia (MT)'),
    ('08858', u'Riacho Frio (PI)'),
    ('08874', u'Ribeira do Piauí (PI)'),
    ('08900', u'Caiabu (SP)'),
    ('08900', u'Poção de Pedras (MA)'),
    ('08901', u'Mamanguape (PB)'),
    ('08903', u'Coração de Maria (BA)'),
    ('08904', u'Parelhas (RN)'),
    ('08904', u'Getúlio Vargas (RS)'),
    ('08905', u'Goiás (GO)'),
    ('08906', u'Morrinhos (CE)'),
    ('08906', u'Jaraguá do Sul (SC)'),
    ('08907', u'Nova Maringá (MT)'),
    ('08907', u'Satuba (AL)'),
    ('08908', u'Guairaçá (PR)'),
    ('08908', u'Ribeiro Gonçalves (PI)'),
    ('08909', u'Brasópolis (MG)'),
    ('08909', u'Limoeiro (PE)'),
    ('08953', u'Rio do Fogo (RN)'),
    ('08955', u'Jardinópolis (SC)'),
    ('08956', u'Nova Monte Verde (MT)'),
    ('08956', u'Senador Rui Palmeira (AL)'),
    ('08957', u'Guamiranga (PR)'),
    ('09000', u'Cordeiros (BA)'),
    ('09001', u'Giruá (RS)'),
    ('09003', u'Mucambo (CE)'),
    ('09003', u'Joaçaba (SC)'),
    ('09004', u'Tanque d`Arca (AL)'),
    ('09005', u'Goiatins (TO)'),
    ('09005', u'Guapirama (PR)'),
    ('09005', u'Rio Grande do Piauí (PI)'),
    ('09006', u'Brumadinho (MG)'),
    ('09006', u'Macaparana (PE)'),
    ('09007', u'Porto Franco (MA)'),
    ('09007', u'Caieiras (SP)'),
    ('09008', u'Manaíra (PB)'),
    ('09050', u'Glorinha (RS)'),
    ('09056', u'Porto Rico do Maranhão (MA)'),
    ('09057', u'Marcação (PB)'),
    ('09100', u'Gramado (RS)'),
    ('09100', u'Passa e Fica (RN)'),
    ('09101', u'Goiatuba (GO)'),
    ('09102', u'Mulungu (CE)'),
    ('09102', u'Joinville * (SC)'),
    ('09103', u'Taquarana (AL)'),
    ('09104', u'Guaporema (PR)'),
    ('09104', u'Santa Cruz do Piauí (PI)'),
    ('09105', u'Bueno Brandão (MG)'),
    ('09105', u'Machados (PE)'),
    ('09106', u'Presidente Dutra (MA)'),
    ('09106', u'Caiuá (SP)'),
    ('09107', u'Mari (PB)'),
    ('09109', u'Coribe (BA)'),
    ('09126', u'Gramado dos Loureiros (RS)'),
    ('09150', u'Gouvelândia (GO)'),
    ('09151', u'José Boiteux (SC)'),
    ('09152', u'Teotônio Vilela (AL)'),
    ('09153', u'Santa Cruz dos Milagres (PI)'),
    ('09154', u'Manari (PE)'),
    ('09156', u'Marizópolis (PB)'),
    ('09159', u'Gramado Xavier (RS)'),
    ('09177', u'Jupiá (SC)'),
    ('09200', u'Guapó (GO)'),
    ('09201', u'Lacerdópolis (SC)'),
    ('09201', u'Nova Olinda (CE)'),
    ('09202', u'Traipu (AL)'),
    ('09203', u'Guaraci (PR)'),
    ('09203', u'Santa Filomena (PI)'),
    ('09204', u'Maraial (PE)'),
    ('09204', u'Buenópolis (MG)'),
    ('09205', u'Cajamar (SP)'),
    ('09205', u'Presidente Juscelino (MA)'),
    ('09206', u'Massaranduba (PB)'),
    ('09208', u'Coronel João Sá (BA)'),
    ('09209', u'Gravataí * (RS)'),
    ('09209', u'Passagem (RN)'),
    ('09239', u'Presidente Médici (MA)'),
    ('09253', u'Bugre (MG)'),
    ('09254', u'Cajati (SP)'),
    ('09258', u'Guabiju (RS)'),
    ('09270', u'Presidente Sarney (MA)'),
    ('09291', u'Guaraíta (GO)'),
    ('09300', u'Lages (SC)'),
    ('09300', u'Nova Russas (CE)'),
    ('09301', u'União dos Palmares (AL)'),
    ('09302', u'Guaraniaçu (PR)'),
    ('09302', u'Guaraí (TO)'),
    ('09302', u'Santa Luz (PI)'),
    ('09303', u'Mirandiba (PE)'),
    ('09303', u'Buritis (MG)'),
    ('09304', u'Presidente Vargas (MA)'),
    ('09304', u'Cajobi (SP)'),
    ('09305', u'Mataraca (PB)'),
    ('09307', u'Correntina (BA)'),
    ('09308', u'Guaíba (RS)'),
    ('09308', u'Patu (RN)'),
    ('09332', u'Santa Maria (RN)'),
    ('09339', u'Matinhas (PB)'),
    ('09351', u'Santana do Piauí (PI)'),
    ('09370', u'Mato Grosso (PB)'),
    ('09377', u'Santa Rosa do Piauí (PI)'),
    ('09396', u'Maturéia (PB)'),
    ('09400', u'Viçosa (AL)'),
    ('09401', u'Guarapuava (PR)'),
    ('09401', u'Santo Antônio de Lisboa (PI)'),
    ('09402', u'Moreno (PE)'),
    ('09402', u'Buritizeiro (MG)'),
    ('09403', u'Cajuru (SP)'),
    ('09403', u'Primeira Cruz (MA)'),
    ('09404', u'Mogeiro (PB)'),
    ('09406', u'Cotegipe (BA)'),
    ('09407', u'Pau dos Ferros (RN)'),
    ('09407', u'Guaporé (RS)'),
    ('09408', u'Guarani de Goiás (GO)'),
    ('09409', u'Laguna (SC)'),
    ('09409', u'Novo Oriente (CE)'),
    ('09450', u'Santo Antônio dos Milagres (PI)'),
    ('09451', u'Cabeceira Grande (MG)'),
    ('09452', u'Raposa (MA)'),
    ('09452', u'Campina do Monte Alegre (SP)'),
    ('09457', u'Guarinos (GO)'),
    ('09458', u'Ocara (CE)'),
    ('09458', u'Lajeado Grande (SC)'),
    ('09500', u'Guaraqueçaba (PR)'),
    ('09500', u'Gurupi (TO)'),
    ('09500', u'Santo Inácio do Piauí (PI)'),
    ('09501', u'Cabo Verde (MG)'),
    ('09501', u'Nazaré da Mata (PE)'),
    ('09502', u'Campinas * (SP)'),
    ('09502', u'Riachão (MA)'),
    ('09503', u'Montadas (PB)'),
    ('09505', u'Cravolândia (BA)'),
    ('09506', u'Pedra Grande (RN)'),
    ('09506', u'Guarani das Missões (RS)'),
    ('09508', u'Laurentino (SC)'),
    ('09508', u'Orós (CE)'),
    ('09551', u'Ribamar Fiquene (MA)'),
    ('09555', u'Harmonia (RS)'),
    ('09559', u'São Braz do Piauí (PI)'),
    ('09571', u'Herveiras (RS)'),
    ('09600', u'Olinda * (PE)'),
    ('09600', u'Cachoeira da Prata (MG)'),
    ('09601', u'Campo Limpo Paulista (SP)'),
    ('09601', u'Rosário (MA)'),
    ('09602', u'Monte Horebe (PB)'),
    ('09604', u'Crisópolis (BA)'),
    ('09605', u'Pedra Preta (RN)'),
    ('09605', u'Horizontina (RS)'),
    ('09606', u'Heitoraí (GO)'),
    ('09607', u'Pacajus (CE)'),
    ('09607', u'Lauro Muller (SC)'),
    ('09609', u'São Félix do Piauí (PI)'),
    ('09609', u'Guaratuba (PR)'),
    ('09654', u'Hulha Negra (RS)'),
    ('09658', u'São Francisco de Assis do Piauí (PI)'),
    ('09658', u'Honório Serpa (PR)'),
    ('09700', u'Sambaíba (MA)'),
    ('09700', u'Campos do Jordão (SP)'),
    ('09701', u'Monteiro (PB)'),
    ('09703', u'Cristópolis (BA)'),
    ('09704', u'Pedro Avelino (RN)'),
    ('09704', u'Humaitá (RS)'),
    ('09705', u'Hidrolândia (GO)'),
    ('09706', u'Pacatuba (CE)'),
    ('09706', u'Lebon Régis (SC)'),
    ('09708', u'São Francisco do Piauí (PI)'),
    ('09708', u'Ibaiti (PR)'),
    ('09709', u'Cachoeira de Minas (MG)'),
    ('09709', u'Orobó (PE)'),
    ('09753', u'Ibarama (RS)'),
    ('09757', u'São Gonçalo do Gurguéia (PI)'),
    ('09757', u'Ibema (PR)'),
    ('09759', u'Santa Filomena do Maranhão (MA)'),
    ('09800', u'Mulungu (PB)'),
    ('09802', u'Cruz das Almas (BA)'),
    ('09803', u'Ibiaçá (RS)'),
    ('09803', u'Pedro Velho (RN)'),
    ('09804', u'Hidrolina (GO)'),
    ('09805', u'Leoberto Leal (SC)'),
    ('09805', u'Pacoti (CE)'),
    ('09807', u'Ipueiras (TO)'),
    ('09807', u'Ibiporã (PR)'),
    ('09807', u'São Gonçalo do Piauí (PI)'),
    ('09808', u'Cachoeira Dourada (MG)'),
    ('09808', u'Orocó (PE)'),
    ('09809', u'Santa Helena (MA)'),
    ('09809', u'Campos Novos Paulista (SP)'),
    ('09854', u'Lindóia do Sul (SC)'),
    ('09856', u'São João da Canabrava (PI)'),
    ('09872', u'São João da Fronteira (PI)'),
    ('09901', u'Curaçá (BA)'),
    ('09902', u'Ibiraiaras (RS)'),
    ('09902', u'Pendências (RN)'),
    ('09903', u'Iaciara (GO)'),
    ('09904', u'Pacujá (CE)'),
    ('09904', u'Lontras (SC)'),
    ('09906', u'Icaraíma (PR)'),
    ('09906', u'São João da Serra (PI)'),
    ('09907', u'Caetanópolis (MG)'),
    ('09907', u'Ouricuri (PE)'),
    ('09908', u'Santa Inês (MA)'),
    ('09908', u'Cananéia (SP)'),
    ('09909', u'Natuba (PB)'),
    ('09937', u'Inaciolândia (GO)'),
    ('09951', u'Ibirapuitã (RS)'),
    ('09952', u'Indiara (GO)'),
    ('09955', u'São João da Varjota (PI)'),
    ('09957', u'Canas (SP)'),
    ('09971', u'São João do Arraial (PI)'),
    ('10000', u'Inhumas (GO)'),
    ('10001', u'Luiz Alves (SC)'),
    ('10001', u'Palhano (CE)'),
    ('10003', u'São João do Piauí (PI)'),
    ('10003', u'Iguaraçu (PR)'),
    ('10004', u'Caeté (MG)'),
    ('10004', u'Palmares (PE)'),
    ('10005', u'Cândido Mota (SP)'),
    ('10005', u'Santa Luzia (MA)'),
    ('10006', u'Nazarezinho (PB)'),
    ('10008', u'Dário Meira (BA)'),
    ('10009', u'Pilões (RN)'),
    ('10009', u'Ibirubá (RS)'),
    ('10035', u'Luzerna (SC)'),
    ('10039', u'Santa Luzia do Paruá (MA)'),
    ('10050', u'Macieira (SC)'),
    ('10052', u'Iguatu (PR)'),
    ('10052', u'São José do Divino (PI)'),
    ('10057', u'Dias d`Ávila (BA)'),
    ('10078', u'Imbaú (PR)'),
    ('10100', u'Palmácia (CE)'),
    ('10100', u'Mafra (SC)'),
    ('10102', u'São José do Peixe (PI)'),
    ('10102', u'Imbituva (PR)'),
    ('10103', u'Caiana (MG)'),
    ('10103', u'Palmeirina (PE)'),
    ('10104', u'Cândido Rodrigues (SP)'),
    ('10104', u'Santa Quitéria do Maranhão (MA)'),
    ('10105', u'Nova Floresta (PB)'),
    ('10107', u'Dom Basílio (BA)'),
    ('10108', u'Igrejinha (RS)'),
    ('10108', u'Poço Branco (RN)'),
    ('10109', u'Ipameri (GO)'),
    ('10153', u'Canitar (SP)'),
    ('10158', u'Ipiranga de Goiás (GO)'),
    ('10201', u'Inácio Martins (PR)'),
    ('10201', u'São José do Piauí (PI)'),
    ('10202', u'Panelas (PE)'),
    ('10202', u'Cajuri (MG)'),
    ('10203', u'Capão Bonito (SP)'),
    ('10203', u'Santa Rita (MA)'),
    ('10204', u'Nova Olinda (PB)'),
    ('10206', u'Dom Macedo Costa (BA)'),
    ('10207', u'Ijuí (RS)'),
    ('10207', u'Portalegre (RN)'),
    ('10208', u'Iporá (GO)'),
    ('10209', u'Major Gercino (SC)'),
    ('10209', u'Paracuru (CE)'),
    ('10237', u'Santana do Maranhão (MA)'),
    ('10256', u'Porto do Mangue (RN)'),
    ('10258', u'Paraipaba (CE)'),
    ('10278', u'Santo Amaro do Maranhão (MA)'),
    ('10300', u'São Julião (PI)'),
    ('10300', u'Inajá (PR)'),
    ('10301', u'Paranatama (PE)'),
    ('10301', u'Caldas (MG)'),
    ('10302', u'Santo Antônio dos Lopes (MA)'),
    ('10302', u'Capela do Alto (SP)'),
    ('10303', u'Nova Palmeira (PB)'),
    ('10305', u'Elísio Medrado (BA)'),
    ('10306', u'Ilópolis (RS)'),
    ('10306', u'Presidente Juscelino (RN)'),
    ('10307', u'Israelândia (GO)'),
    ('10308', u'Parambu (CE)'),
    ('10308', u'Major Vieira (SC)'),
    ('10330', u'Imbé (RS)'),
    ('10359', u'São Lourenço do Piauí (PI)'),
    ('10363', u'Imigrante (RS)'),
    ('10375', u'São Luis do Piauí (PI)'),
    ('10383', u'São Miguel da Baixa Grande (PI)'),
    ('10391', u'São Miguel do Fidalgo (PI)'),
    ('10400', u'Parnamirim (PE)'),
    ('10400', u'Camacho (MG)'),
    ('10401', u'Capivari (SP)'),
    ('10401', u'São Benedito do Rio Preto (MA)'),
    ('10402', u'Olho d`Água (PB)'),
    ('10404', u'Encruzilhada (BA)'),
    ('10405', u'Independência (RS)'),
    ('10405', u'Pureza (RN)'),
    ('10406', u'Itaberaí (GO)'),
    ('10407', u'Maracajá (SC)'),
    ('10407', u'Paramoti (CE)'),
    ('10409', u'São Miguel do Tapuio (PI)'),
    ('10409', u'Indianópolis (PR)'),
    ('10413', u'Inhacorá (RS)'),
    ('10439', u'Ipê (RS)'),
    ('10462', u'Ipiranga do Sul (RS)'),
    ('10500', u'Caraguatatuba (SP)'),
    ('10500', u'São Bento (MA)'),
    ('10501', u'Olivedos (PB)'),
    ('10503', u'Entre Rios (BA)'),
    ('10504', u'Rafael Fernandes (RN)'),
    ('10504', u'Iraí (RS)'),
    ('10506', u'Pedra Branca (CE)'),
    ('10506', u'Maravilha (SC)'),
    ('10508', u'Itacajá (TO)'),
    ('10508', u'Ipiranga (PR)'),
    ('10508', u'São Pedro do Piauí (PI)'),
    ('10509', u'Camanducaia (MG)'),
    ('10509', u'Passira (PE)'),
    ('10538', u'Itaara (RS)'),
    ('10553', u'Itacurubi (RS)'),
    ('10555', u'Marema (SC)'),
    ('10562', u'Itaguari (GO)'),
    ('10579', u'Itapuca (RS)'),
    ('10600', u'Ouro Velho (PB)'),
    ('10602', u'Esplanada (BA)'),
    ('10603', u'Itaqui (RS)'),
    ('10603', u'Rafael Godeiro (RN)'),
    ('10604', u'Itaguaru (GO)'),
    ('10605', u'Massaranduba (SC)'),
    ('10605', u'Penaforte (CE)'),
    ('10607', u'Iporã (PR)'),
    ('10607', u'São Raimundo Nonato (PI)'),
    ('10608', u'Paudalho (PE)'),
    ('10608', u'Cambuí (MG)'),
    ('10609', u'Carapicuíba * (SP)'),
    ('10609', u'São Bernardo (MA)'),
    ('10623', u'Sebastião Barros (PI)'),
    ('10631', u'Sebastião Leal (PI)'),
    ('10652', u'Itati (RS)'),
    ('10656', u'Iracema do Oeste (PR)'),
    ('10656', u'Sigefredo Pacheco (PI)'),
    ('10658', u'São Domingos do Azeitão (MA)'),
    ('10659', u'Parari (PB)'),
    ('10701', u'Euclides da Cunha (BA)'),
    ('10702', u'Riacho da Cruz (RN)'),
    ('10702', u'Itatiba do Sul (RS)'),
    ('10704', u'Matos Costa (SC)'),
    ('10704', u'Pentecoste (CE)'),
    ('10706', u'Itaguatins (TO)'),
    ('10706', u'Irati (PR)'),
    ('10706', u'Simões (PI)'),
    ('10707', u'Cambuquira (MG)'),
    ('10707', u'Paulista * (PE)'),
    ('10708', u'Cardoso (SP)'),
    ('10708', u'São Domingos do Maranhão (MA)'),
    ('10709', u'Passagem (PB)'),
    ('10727', u'Eunápolis (BA)'),
    ('10750', u'Fátima (BA)'),
    ('10751', u'Ivorá (RS)'),
    ('10776', u'Feira da Mata (BA)'),
    ('10800', u'Feira de Santana * (BA)'),
    ('10801', u'Riacho de Santana (RN)'),
    ('10801', u'Ivoti (RS)'),
    ('10802', u'Itajá (GO)'),
    ('10803', u'Meleiro (SC)'),
    ('10803', u'Pereiro (CE)'),
    ('10805', u'Simplício Mendes (PI)'),
    ('10805', u'Iretama (PR)'),
    ('10806', u'Pedra (PE)'),
    ('10806', u'Campanário (MG)'),
    ('10807', u'Casa Branca (SP)'),
    ('10807', u'São Félix de Balsas (MA)'),
    ('10808', u'Patos (PB)'),
    ('10850', u'Jaboticaba (RS)'),
    ('10852', u'Mirim Doce (SC)'),
    ('10852', u'Pindoretama (CE)'),
    ('10856', u'São Francisco do Brejão (MA)'),
    ('10859', u'Filadélfia (BA)'),
    ('10876', u'Jacuizinho (RS)'),
    ('10900', u'Jacutinga (RS)'),
    ('10900', u'Riachuelo (RN)'),
    ('10901', u'Itapaci (GO)'),
    ('10902', u'Modelo (SC)'),
    ('10902', u'Piquet Carneiro (CE)'),
    ('10904', u'Itaguajé (PR)'),
    ('10904', u'Socorro do Piauí (PI)'),
    ('10904', u'Itapiratins (TO)'),
    ('10905', u'Pesqueira (PE)'),
    ('10905', u'Campanha (MG)'),
    ('10906', u'Cássia dos Coqueiros (SP)'),
    ('10906', u'São Francisco do Maranhão (MA)'),
    ('10907', u'Paulista (PB)'),
    ('10909', u'Firmino Alves (BA)'),
    ('10938', u'Sussuapara (PI)'),
    ('10951', u'Pires Ferreira (CE)'),
    ('10953', u'Itaipulândia (PR)'),
    ('10953', u'Tamboril do Piauí (PI)'),
    ('10979', u'Tanque do Piauí (PI)'),
    ('11001', u'Teresina (PI)'),
    ('11001', u'Itambaracá (PR)'),
    ('11002', u'Campestre (MG)'),
    ('11002', u'Petrolândia (PE)'),
    ('11003', u'Castilho (SP)'),
    ('11003', u'São João Batista (MA)'),
    ('11004', u'Pedra Branca (PB)'),
    ('11006', u'Floresta Azul (BA)'),
    ('11007', u'Jaguarão (RS)'),
    ('11007', u'Rodolfo Fernandes (RN)'),
    ('11008', u'Itapirapuã (GO)'),
    ('11009', u'Poranga (CE)'),
    ('11009', u'Mondaí (SC)'),
    ('11029', u'São João do Carú (MA)'),
    ('11052', u'São João do Paraíso (MA)'),
    ('11056', u'Tibau (RN)'),
    ('11058', u'Monte Carlo (SC)'),
    ('11078', u'São João do Soter (MA)'),
    ('11100', u'Itambé (PR)'),
    ('11100', u'Itaporã do Tocantins (TO)'),
    ('11100', u'União (PI)'),
    ('11101', u'Petrolina * (PE)'),
    ('11101', u'Campina Verde (MG)'),
    ('11102', u'Catanduva (SP)'),
    ('11102', u'São João dos Patos (MA)'),
    ('11103', u'Pedra Lavrada (PB)'),
    ('11105', u'Formosa do Rio Preto (BA)'),
    ('11106', u'Ruy Barbosa (RN)'),
    ('11106', u'Jaguari (RS)'),
    ('11108', u'Monte Castelo (SC)'),
    ('11108', u'Porteiras (CE)'),
    ('11122', u'Jaquirana (RS)'),
    ('11130', u'Jari (RS)'),
    ('11150', u'Campo Azul (MG)'),
    ('11155', u'Jóia (RS)'),
    ('11200', u'Poção (PE)'),
    ('11200', u'Campo Belo (MG)'),
    ('11201', u'São José de Ribamar (MA)'),
    ('11201', u'Catiguá (SP)'),
    ('11202', u'Pedras de Fogo (PB)'),
    ('11204', u'Gandu (BA)'),
    ('11205', u'Santa Cruz (RN)'),
    ('11205', u'Júlio de Castilhos (RS)'),
    ('11206', u'Itapuranga (GO)'),
    ('11207', u'Potengi (CE)'),
    ('11207', u'Morro da Fumaça (SC)'),
    ('11209', u'Itapejara d`Oeste (PR)'),
    ('11209', u'Uruçuí (PI)'),
    ('11231', u'Potiretama (CE)'),
    ('11239', u'Lagoa Bonita do Sul (RS)'),
    ('11250', u'São José dos Basílios (MA)'),
    ('11253', u'Gavião (BA)'),
    ('11254', u'Lagoão (RS)'),
    ('11256', u'Morro Grande (SC)'),
    ('11258', u'Itaperuçu (PR)'),
    ('11264', u'Quiterianópolis (CE)'),
    ('11270', u'Lagoa dos Três Cantos (RS)'),
    ('11300', u'São Luís (MA)'),
    ('11300', u'Cedral (SP)'),
    ('11301', u'Piancó (PB)'),
    ('11303', u'Gentio do Ouro (BA)'),
    ('11304', u'Lagoa Vermelha (RS)'),
    ('11305', u'Itarumã (GO)'),
    ('11306', u'Quixadá (CE)'),
    ('11306', u'Navegantes (SC)'),
    ('11308', u'Itaúna do Sul (PR)'),
    ('11308', u'Valença do Piauí (PI)'),
    ('11309', u'Campo do Meio (MG)'),
    ('11309', u'Pombos (PE)'),
    ('11355', u'Quixelô (CE)'),
    ('11357', u'Várzea Branca (PI)'),
    ('11400', u'Picuí (PB)'),
    ('11402', u'Glória (BA)'),
    ('11403', u'Lajeado (RS)'),
    ('11403', u'Santana do Matos (RN)'),
    ('11404', u'Itauçu (GO)'),
    ('11405', u'Nova Erechim (SC)'),
    ('11405', u'Quixeramobim (CE)'),
    ('11407', u'Ivaí (PR)'),
    ('11407', u'Várzea Grande (PI)'),
    ('11408', u'Campo Florido (MG)'),
    ('11408', u'Primavera (PE)'),
    ('11409', u'São Luís Gonzaga do Maranhão (MA)'),
    ('11409', u'Cerqueira César (SP)'),
    ('11429', u'Lajeado do Bugre (RS)'),
    ('11429', u'Santana do Seridó (RN)'),
    ('11454', u'Nova Itaberaba (SC)'),
    ('11501', u'Gongogi (BA)'),
    ('11502', u'Lavras do Sul (RS)'),
    ('11502', u'Santo Antônio (RN)'),
    ('11503', u'Itumbiara (GO)'),
    ('11504', u'Nova Trento (SC)'),
    ('11504', u'Quixeré (CE)'),
    ('11506', u'Jaú do Tocantins (TO)'),
    ('11506', u'Ivaiporã (PR)'),
    ('11506', u'Vera Mendes (PI)'),
    ('11507', u'Quipapá (PE)'),
    ('11507', u'Campos Altos (MG)'),
    ('11508', u'São Mateus do Maranhão (MA)'),
    ('11508', u'Cerquilho (SP)'),
    ('11509', u'Pilar (PB)'),
    ('11532', u'São Pedro da Água Branca (MA)'),
    ('11533', u'Quixaba (PE)'),
    ('11555', u'Ivaté (PR)'),
    ('11573', u'São Pedro dos Crentes (MA)'),
    ('11600', u'Governador Mangabeira (BA)'),
    ('11601', u'Liberato Salzano (RS)'),
    ('11601', u'São Bento do Norte (RN)'),
    ('11602', u'Ivolândia (GO)'),
    ('11603', u'Redenção (CE)'),
    ('11603', u'Nova Veneza (SC)'),
    ('11605', u'Vila Nova do Piauí (PI)'),
    ('11605', u'Ivatuba (PR)'),
    ('11606', u'Recife * (PE)'),
    ('11606', u'Campos Gerais (MG)'),
    ('11607', u'Cesário Lange (SP)'),
    ('11607', u'São Raimundo das Mangabeiras (MA)'),
    ('11608', u'Pilões (PB)'),
    ('11627', u'Lindolfo Collor (RS)'),
    ('11631', u'São Raimundo do Doca Bezerra (MA)'),
    ('11643', u'Linha Nova (RS)'),
    ('11652', u'Novo Horizonte (SC)'),
    ('11659', u'Guajeru (BA)'),
    ('11672', u'São Roberto (MA)'),
    ('11700', u'Machadinho (RS)'),
    ('11700', u'São Bento do Trairí (RN)'),
    ('11701', u'Jandaia (GO)'),
    ('11702', u'Orleans (SC)'),
    ('11702', u'Reriutaba (CE)'),
    ('11704', u'Jaboti (PR)'),
    ('11704', u'Wall Ferraz (PI)'),
    ('11705', u'Riacho das Almas (PE)'),
    ('11705', u'Canaã (MG)'),
    ('11706', u'Charqueada (SP)'),
    ('11706', u'São Vicente Ferrer (MA)'),
    ('11707', u'Pilõezinhos (PB)'),
    ('11709', u'Guanambi (BA)'),
    ('11718', u'Maçambara (RS)'),
    ('11722', u'Satubinha (MA)'),
    ('11734', u'Mampituba (RS)'),
    ('11748', u'Senador Alexandre Costa (MA)'),
    ('11751', u'Otacílio Costa (SC)'),
    ('11759', u'Manoel Viana (RS)'),
    ('11763', u'Senador La Rocque (MA)'),
    ('11775', u'Maquiné (RS)'),
    ('11789', u'Serrano do Maranhão (MA)'),
    ('11791', u'Maratá (RS)'),
    ('11800', u'Jaraguá (GO)'),
    ('11801', u'Russas (CE)'),
    ('11801', u'Ouro (SC)'),
    ('11803', u'Jacarezinho (PR)'),
    ('11803', u'Juarina (TO)'),
    ('11804', u'Ribeirão (PE)'),
    ('11804', u'Canápolis (MG)'),
    ('11805', u'Sítio Novo (MA)'),
    ('11806', u'Pirpirituba (PB)'),
    ('11808', u'Guaratinga (BA)'),
    ('11809', u'Marau (RS)'),
    ('11809', u'São Fernando (RN)'),
    ('11850', u'Ouro Verde (SC)'),
    ('11857', u'Heliópolis (BA)'),
    ('11876', u'Paial (SC)'),
    ('11892', u'Painel (SC)'),
    ('11900', u'Saboeiro (CE)'),
    ('11900', u'Palhoça (SC)'),
    ('11902', u'Jaguapitã (PR)'),
    ('11902', u'Lagoa da Confusão (TO)'),
    ('11903', u'Rio Formoso (PE)'),
    ('11903', u'Cana Verde (MG)'),
    ('11904', u'Clementina (SP)'),
    ('11904', u'Sucupira do Norte (MA)'),
    ('11905', u'Pitimbu (PB)'),
    ('11907', u'Iaçu (BA)'),
    ('11908', u'Marcelino Ramos (RS)'),
    ('11908', u'São Francisco do Oeste (RN)'),
    ('11909', u'Jataí (GO)'),
    ('11951', u'Lagoa do Tocantins (TO)'),
    ('11953', u'Sucupira do Riachão (MA)'),
    ('11959', u'Salitre (CE)'),
    ('11981', u'Mariana Pimentel (RS)'),
    ('12000', u'Candeias (MG)'),
    ('12000', u'Sairé (PE)'),
    ('12001', u'Colina (SP)'),
    ('12001', u'Tasso Fragoso (MA)'),
    ('12002', u'Pocinhos (PB)'),
    ('12004', u'Ibiassucê (BA)'),
    ('12005', u'Mariano Moro (RS)'),
    ('12005', u'São Gonçalo do Amarante (RN)'),
    ('12006', u'Jaupaci (GO)'),
    ('12007', u'Santana do Acaraú (CE)'),
    ('12007', u'Palma Sola (SC)'),
    ('12009', u'Lajeado (TO)'),
    ('12009', u'Jaguariaíva (PR)'),
    ('12036', u'Poço Dantas (PB)'),
    ('12054', u'Marques de Souza (RS)'),
    ('12055', u'Jesúpolis (GO)'),
    ('12056', u'Palmeira (SC)'),
    ('12059', u'Cantagalo (MG)'),
    ('12077', u'Poço de José de Moura (PB)'),
    ('12100', u'Colômbia (SP)'),
    ('12100', u'Timbiras (MA)'),
    ('12101', u'Pombal (PB)'),
    ('12103', u'Ibicaraí (BA)'),
    ('12104', u'São João do Sabugi (RN)'),
    ('12104', u'Mata (RS)'),
    ('12105', u'Joviânia (GO)'),
    ('12106', u'Santana do Cariri (CE)'),
    ('12106', u'Palmitos (SC)'),
    ('12108', u'Jandaia do Sul (PR)'),
    ('12109', u'Salgadinho (PE)'),
    ('12109', u'Caparaó (MG)'),
    ('12138', u'Mato Castelhano (RS)'),
    ('12153', u'Mato Leitão (RS)'),
    ('12157', u'Lavandeira (TO)'),
    ('12179', u'Mato Queimado (RS)'),
    ('12200', u'Prata (PB)'),
    ('12202', u'Ibicoara (BA)'),
    ('12203', u'São José de Mipibu (RN)'),
    ('12203', u'Maximiliano de Almeida (RS)'),
    ('12204', u'Jussara (GO)'),
    ('12205', u'Santa Quitéria (CE)'),
    ('12205', u'Papanduva (SC)'),
    ('12207', u'Janiópolis (PR)'),
    ('12208', u'Salgueiro (PE)'),
    ('12208', u'Capela Nova (MG)'),
    ('12209', u'Timon (MA)'),
    ('12209', u'Conchal (SP)'),
    ('12233', u'Trizidela do Vale (MA)'),
    ('12239', u'Paraíso (SC)'),
    ('12252', u'Minas do Leão (RS)'),
    ('12253', u'Lagoa Santa (GO)'),
    ('12254', u'Passo de Torres (SC)'),
    ('12270', u'Passos Maia (SC)'),
    ('12274', u'Tufilândia (MA)'),
    ('12301', u'Ibicuí (BA)'),
    ('12302', u'Miraguaí (RS)'),
    ('12302', u'São José do Campestre (RN)'),
    ('12303', u'Leopoldo de Bulhões (GO)'),
    ('12304', u'São Benedito (CE)'),
    ('12304', u'Paulo Lopes (SC)'),
    ('12306', u'Japira (PR)'),
    ('12307', u'Saloá (PE)'),
    ('12307', u'Capelinha (MG)'),
    ('12308', u'Tuntum (MA)'),
    ('12308', u'Conchas (SP)'),
    ('12309', u'Princesa Isabel (PB)'),
    ('12351', u'Montauri (RS)'),
    ('12377', u'Monte Alegre dos Campos (RS)'),
    ('12385', u'Monte Belo do Sul (RS)'),
    ('12400', u'Ibipeba (BA)'),
    ('12401', u'Montenegro (RS)'),
    ('12401', u'São José do Seridó (RN)'),
    ('12403', u'São Gonçalo do Amarante (CE)'),
    ('12403', u'Pedras Grandes (SC)'),
    ('12405', u'Lizarda (TO)'),
    ('12405', u'Japurá (PR)'),
    ('12406', u'Sanharó (PE)'),
    ('12406', u'Capetinga (MG)'),
    ('12407', u'Cordeirópolis (SP)'),
    ('12407', u'Turiaçu (MA)'),
    ('12408', u'Puxinanã (PB)'),
    ('12427', u'Mormaço (RS)'),
    ('12443', u'Morrinhos do Sul (RS)'),
    ('12450', u'Morro Redondo (RS)'),
    ('12454', u'Luzinópolis (TO)'),
    ('12455', u'Santa Cruz (PE)'),
    ('12456', u'Turilândia (MA)'),
    ('12471', u'Santa Cruz da Baixa Verde (PE)'),
    ('12476', u'Morro Reuter (RS)'),
    ('12500', u'São Miguel (RN)'),
    ('12500', u'Mostardas (RS)'),
    ('12501', u'Luziânia * (GO)'),
    ('12502', u'São João do Jaguaribe (CE)'),
    ('12502', u'Penha (SC)'),
    ('12504', u'Marianópolis do Tocantins (TO)'),
    ('12504', u'Jardim Alegre (PR)'),
    ('12505', u'Capim Branco (MG)'),
    ('12505', u'Santa Cruz do Capibaribe (PE)'),
    ('12506', u'Tutóia (MA)'),
    ('12506', u'Coroados (SP)'),
    ('12507', u'Queimadas (PB)'),
    ('12509', u'Ibipitanga (BA)'),
    ('12554', u'Santa Filomena (PE)'),
    ('12559', u'São Miguel do Gostoso (RN)'),
    ('12600', u'Mairipotaba (GO)'),
    ('12601', u'São Luís do Curu (CE)'),
    ('12601', u'Peritiba (SC)'),
    ('12603', u'Jardim Olinda (PR)'),
    ('12604', u'Capinópolis (MG)'),
    ('12604', u'Santa Maria da Boa Vista (PE)'),
    ('12605', u'Coronel Macedo (SP)'),
    ('12605', u'Urbano Santos (MA)'),
    ('12606', u'Quixabá (PB)'),
    ('12608', u'Ibiquera (BA)'),
    ('12609', u'São Paulo do Potengi (RN)'),
    ('12609', u'Muçum (RS)'),
    ('12617', u'Muitos Capões (RS)'),
    ('12625', u'Muliterno (RS)'),
    ('12653', u'Capitão Andrade (MG)'),
    ('12658', u'Não-Me-Toque (RS)'),
    ('12674', u'Nicolau Vergueiro (RS)'),
    ('12700', u'Petrolândia (SC)'),
    ('12700', u'Senador Pompeu (CE)'),
    ('12702', u'Jataizinho (PR)'),
    ('12702', u'Mateiros (TO)'),
    ('12703', u'Capitão Enéas (MG)'),
    ('12703', u'Santa Maria do Cambucá (PE)'),
    ('12704', u'Corumbataí (SP)'),
    ('12704', u'Vargem Grande (MA)'),
    ('12705', u'Remígio (PB)'),
    ('12707', u'Ibirapitanga (BA)'),
    ('12708', u'São Pedro (RN)'),
    ('12708', u'Nonoai (RS)'),
    ('12709', u'Mambaí (GO)'),
    ('12721', u'Pedro Régis (PB)'),
    ('12747', u'Riachão (PB)'),
    ('12751', u'Jesuítas (PR)'),
    ('12754', u'Riachão do Bacamarte (PB)'),
    ('12757', u'Nova Alvorada (RS)'),
    ('12762', u'Riachão do Poço (PB)'),
    ('12788', u'Riacho de Santo Antônio (PB)'),
    ('12801', u'Maurilândia do Tocantins (TO)'),
    ('12801', u'Joaquim Távora (PR)'),
    ('12802', u'Capitólio (MG)'),
    ('12802', u'Santa Terezinha (PE)'),
    ('12803', u'Cosmópolis (SP)'),
    ('12803', u'Viana (MA)'),
    ('12804', u'Riacho dos Cavalos (PB)'),
    ('12806', u'Ibirapuã (BA)'),
    ('12807', u'Nova Araçá (RS)'),
    ('12807', u'São Rafael (RN)'),
    ('12808', u'Mara Rosa (GO)'),
    ('12809', u'Balneário Piçarras (SC)'),
    ('12809', u'Senador Sá (CE)'),
    ('12852', u'Vila Nova dos Martírios (MA)'),
    ('12900', u'Jundiaí do Sul (PR)'),
    ('12901', u'Caputira (MG)'),
    ('12901', u'São Benedito do Sul (PE)'),
    ('12902', u'Vitória do Mearim (MA)'),
    ('12902', u'Cosmorama (SP)'),
    ('12903', u'Rio Tinto (PB)'),
    ('12905', u'Ibirataia (BA)'),
    ('12906', u'Nova Bassano (RS)'),
    ('12906', u'São Tomé (RN)'),
    ('12907', u'Marzagão (GO)'),
    ('12908', u'Sobral * (CE)'),
    ('12908', u'Pinhalzinho (SC)'),
    ('12955', u'Nova Boa Vista (RS)'),
    ('12956', u'Matrinchã (GO)'),
    ('12959', u'Juranda (PR)'),
    ('13000', u'Salgadinho (PB)'),
    ('13002', u'Ibitiara (BA)'),
    ('13003', u'São Vicente (RN)'),
    ('13003', u'Nova Bréscia (RS)'),
    ('13004', u'Maurilândia (GO)'),
    ('13005', u'Solonópole (CE)'),
    ('13005', u'Pinheiro Preto (SC)'),
    ('13007', u'Jussara (PR)'),
    ('13008', u'Caraí (MG)'),
    ('13008', u'São Bento do Una (PE)'),
    ('13009', u'Cotia * (SP)'),
    ('13009', u'Vitorino Freire (MA)'),
    ('13011', u'Nova Candelária (RS)'),
    ('13037', u'Nova Esperança do Sul (RS)'),
    ('13053', u'Mimoso de Goiás (GO)'),
    ('13060', u'Nova Hartz (RS)'),
    ('13086', u'Nova Pádua (RS)'),
    ('13087', u'Minaçu (GO)'),
    ('13101', u'Ibititá (BA)'),
    ('13102', u'Nova Palma (RS)'),
    ('13102', u'Senador Elói de Souza (RN)'),
    ('13103', u'Mineiros (GO)'),
    ('13104', u'Tabuleiro do Norte (CE)'),
    ('13104', u'Piratuba (SC)'),
    ('13106', u'Kaloré (PR)'),
    ('13107', u'São Caitano (PE)'),
    ('13107', u'Caranaíba (MG)'),
    ('13108', u'Cravinhos (SP)'),
    ('13109', u'Salgado de São Félix (PB)'),
    ('13153', u'Planalto Alegre (SC)'),
    ('13158', u'Santa Cecília (PB)'),
    ('13200', u'Ibotirama (BA)'),
    ('13201', u'Nova Petrópolis (RS)'),
    ('13201', u'Senador Georgino Avelino (RN)'),
    ('13203', u'Tamboril (CE)'),
    ('13203', u'Pomerode (SC)'),
    ('13205', u'Lapa (PR)'),
    ('13205', u'Miracema do Tocantins (TO)'),
    ('13206', u'Carandaí (MG)'),
    ('13206', u'São João (PE)'),
    ('13207', u'Cristais Paulista (SP)'),
    ('13208', u'Santa Cruz (PB)'),
    ('13252', u'Tarrafas (CE)'),
    ('13254', u'Laranjal (PR)'),
    ('13300', u'Nova Prata (RS)'),
    ('13300', u'Serra de São Bento (RN)'),
    ('13302', u'Tauá (CE)'),
    ('13302', u'Ponte Alta (SC)'),
    ('13304', u'Miranorte (TO)'),
    ('13304', u'Laranjeiras do Sul (PR)'),
    ('13305', u'Carangola (MG)'),
    ('13305', u'São Joaquim do Monte (PE)'),
    ('13306', u'Cruzália (SP)'),
    ('13307', u'Santa Helena (PB)'),
    ('13309', u'Ichu (BA)'),
    ('13334', u'Nova Ramada (RS)'),
    ('13351', u'Tejuçuoca (CE)'),
    ('13351', u'Ponte Alta do Norte (SC)'),
    ('13356', u'Santa Inês (PB)'),
    ('13359', u'Serra do Mel (RN)'),
    ('13359', u'Nova Roma do Sul (RS)'),
    ('13375', u'Nova Santa Rita (RS)'),
    ('13391', u'Novo Cabrais (RS)'),
    ('13400', u'Moiporá (GO)'),
    ('13401', u'Ponte Serrada (SC)'),
    ('13401', u'Tianguá (CE)'),
    ('13403', u'Leópolis (PR)'),
    ('13404', u'Caratinga (MG)'),
    ('13404', u'São José da Coroa Grande (PE)'),
    ('13405', u'Cruzeiro (SP)'),
    ('13406', u'Santa Luzia (PB)'),
    ('13408', u'Igaporã (BA)'),
    ('13409', u'Serra Negra do Norte (RN)'),
    ('13409', u'Novo Hamburgo * (RS)'),
    ('13425', u'Novo Machado (RS)'),
    ('13429', u'Lidianópolis (PR)'),
    ('13441', u'Novo Tiradentes (RS)'),
    ('13452', u'Lindoeste (PR)'),
    ('13457', u'Igrapiúna (BA)'),
    ('13466', u'Novo Xingu (RS)'),
    ('13490', u'Novo Barreiro (RS)'),
    ('13500', u'Trairi (CE)'),
    ('13500', u'Porto Belo (SC)'),
    ('13502', u'Loanda (PR)'),
    ('13503', u'São José do Belmonte (PE)'),
    ('13503', u'Carbonita (MG)'),
    ('13504', u'Cubatão (SP)'),
    ('13505', u'Santana de Mangueira (PB)'),
    ('13507', u'Iguaí (BA)'),
    ('13508', u'Osório (RS)'),
    ('13508', u'Serrinha (RN)'),
    ('13509', u'Monte Alegre de Goiás (GO)'),
    ('13557', u'Serrinha dos Pintos (RN)'),
    ('13559', u'Tururu (CE)'),
    ('13601', u'Lobato (PR)'),
    ('13601', u'Monte do Carmo (TO)'),
    ('13602', u'Careaçu (MG)'),
    ('13602', u'São José do Egito (PE)'),
    ('13603', u'Cunha (SP)'),
    ('13604', u'Santana dos Garrotes (PB)'),
    ('13606', u'Ilhéus * (BA)'),
    ('13607', u'Paim Filho (RS)'),
    ('13607', u'Severiano Melo (RN)'),
    ('13609', u'Ubajara (CE)'),
    ('13609', u'Porto União (SC)'),
    ('13653', u'Santarém (PB)'),
    ('13656', u'Palmares do Sul (RS)'),
    ('13700', u'Londrina * (PR)'),
    ('13700', u'Monte Santo do Tocantins (TO)'),
    ('13701', u'Carlos Chagas (MG)'),
    ('13701', u'São Lourenço da Mata (PE)'),
    ('13702', u'Descalvado (SP)'),
    ('13703', u'Santa Rita (PB)'),
    ('13705', u'Inhambupe (BA)'),
    ('13706', u'Sítio Novo (RN)'),
    ('13706', u'Palmeira das Missões (RS)'),
    ('13707', u'Montes Claros de Goiás (GO)'),
    ('13708', u'Pouso Redondo (SC)'),
    ('13708', u'Umari (CE)'),
    ('13734', u'Luiziana (PR)'),
    ('13756', u'Montividiu (GO)'),
    ('13757', u'Umirim (CE)'),
    ('13759', u'Lunardelli (PR)'),
    ('13772', u'Montividiu do Norte (GO)'),
    ('13800', u'Carmésia (MG)'),
    ('13800', u'São Vicente Ferrer (PE)'),
    ('13801', u'Diadema * (SP)'),
    ('13802', u'Santa Teresinha (PB)'),
    ('13804', u'Ipecaetá (BA)'),
    ('13805', u'Taboleiro Grande (RN)'),
    ('13805', u'Palmitinho (RS)'),
    ('13806', u'Morrinhos (GO)'),
    ('13807', u'Uruburetama (CE)'),
    ('13807', u'Praia Grande (SC)'),
    ('13809', u'Lupionópolis (PR)'),
    ('13809', u'Palmeiras do Tocantins (TO)'),
    ('13850', u'Dirce Reis (SP)'),
    ('13851', u'Santo André (PB)'),
    ('13855', u'Morro Agudo de Goiás (GO)'),
    ('13900', u'Divinolândia (SP)'),
    ('13901', u'São Bento (PB)'),
    ('13903', u'Ipiaú (BA)'),
    ('13904', u'Taipu (RN)'),
    ('13904', u'Panambi (RS)'),
    ('13905', u'Mossâmedes (GO)'),
    ('13906', u'Presidente Castello Branco (SC)'),
    ('13906', u'Uruoca (CE)'),
    ('13908', u'Mallet (PR)'),
    ('13909', u'Carmo da Cachoeira (MG)'),
    ('13909', u'Serra Talhada (PE)'),
    ('13927', u'São Bentinho (PB)'),
    ('13943', u'São Domingos do Cariri (PB)'),
    ('13953', u'Pantano Grande (RS)'),
    ('13955', u'Varjota (CE)'),
    ('13957', u'Muricilândia (TO)'),
    ('13968', u'São Domingos de Pombal (PB)'),
    ('13984', u'São Francisco (PB)'),
    ('14000', u'Ipirá (BA)'),
    ('14001', u'Tangará (RN)'),
    ('14001', u'Paraí (RS)'),
    ('14002', u'Mozarlândia (GO)'),
    ('14003', u'Presidente Getúlio (SC)'),
    ('14003', u'Várzea Alegre (CE)'),
    ('14005', u'Mamborê (PR)'),
    ('14006', u'Carmo da Mata (MG)'),
    ('14006', u'Serrita (PE)'),
    ('14007', u'Dobrada (SP)'),
    ('14007', u'Zé Doca (MA)'),
    ('14008', u'São João do Cariri (PB)'),
    ('14027', u'Paraíso do Sul (RS)'),
    ('14035', u'Pareci Novo (RS)'),
    ('14050', u'Parobé (RS)'),
    ('14051', u'Mundo Novo (GO)'),
    ('14068', u'Passa Sete (RS)'),
    ('14076', u'Passo do Sobrado (RS)'),
    ('14100', u'Tenente Ananias (RN)'),
    ('14100', u'Passo Fundo * (RS)'),
    ('14101', u'Mutunópolis (GO)'),
    ('14102', u'Viçosa do Ceará (CE)'),
    ('14102', u'Presidente Nereu (SC)'),
    ('14104', u'Mandaguaçu (PR)'),
    ('14105', u'Carmo de Minas (MG)'),
    ('14105', u'Sertânia (PE)'),
    ('14106', u'Dois Córregos (SP)'),
    ('14107', u'São João do Tigre (PB)'),
    ('14109', u'Ipupiara (BA)'),
    ('14134', u'Paulo Bento (RS)'),
    ('14151', u'Princesa (SC)'),
    ('14159', u'Paverama (RS)'),
    ('14159', u'Tenente Laurentino Cruz (RN)'),
    ('14175', u'Pedras Altas (RS)'),
    ('14201', u'Quilombo (SC)'),
    ('14203', u'Mandaguari (PR)'),
    ('14203', u'Natividade (TO)'),
    ('14204', u'Carmo do Cajuru (MG)'),
    ('14204', u'Sirinhaém (PE)'),
    ('14205', u'Dolcinópolis (SP)'),
    ('14206', u'São José da Lagoa Tapada (PB)'),
    ('14208', u'Irajuba (BA)'),
    ('14209', u'Tibau do Sul (RN)'),
    ('14209', u'Pedro Osório (RS)'),
    ('14300', u'Rancho Queimado (SC)'),
    ('14302', u'Nazaré (TO)'),
    ('14302', u'Mandirituba (PR)'),
    ('14303', u'Carmo do Paranaíba (MG)'),
    ('14303', u'Moreilândia (PE)'),
    ('14304', u'Dourado (SP)'),
    ('14305', u'São José de Caiana (PB)'),
    ('14307', u'Iramaia (BA)'),
    ('14308', u'Pejuçara (RS)'),
    ('14308', u'Timbaúba dos Batistas (RN)'),
    ('14351', u'Manfrinópolis (PR)'),
    ('14401', u'Mangueirinha (PR)'),
    ('14402', u'Carmo do Rio Claro (MG)'),
    ('14402', u'Solidão (PE)'),
    ('14403', u'Dracena (SP)'),
    ('14404', u'São José de Espinharas (PB)'),
    ('14406', u'Iraquara (BA)'),
    ('14407', u'Touros (RN)'),
    ('14407', u'Pelotas * (RS)'),
    ('14408', u'Nazário (GO)'),
    ('14409', u'Rio das Antas (SC)'),
    ('14423', u'Picada Café (RS)'),
    ('14453', u'São José dos Ramos (PB)'),
    ('14456', u'Triunfo Potiguar (RN)'),
    ('14456', u'Pinhal (RS)'),
    ('14464', u'Pinhal da Serra (RS)'),
    ('14472', u'Pinhal Grande (RS)'),
    ('14498', u'Pinheirinho do Vale (RS)'),
    ('14500', u'Manoel Ribas (PR)'),
    ('14501', u'Carmópolis de Minas (MG)'),
    ('14501', u'Surubim (PE)'),
    ('14502', u'Duartina (SP)'),
    ('14503', u'São José de Piranhas (PB)'),
    ('14505', u'Irará (BA)'),
    ('14506', u'Umarizal (RN)'),
    ('14506', u'Pinheiro Machado (RS)'),
    ('14507', u'Nerópolis (GO)'),
    ('14508', u'Rio do Campo (SC)'),
    ('14550', u'Carneirinho (MG)'),
    ('14552', u'São José de Princesa (PB)'),
    ('14555', u'Pirapó (RS)'),
    ('14600', u'Tabira (PE)'),
    ('14600', u'Carrancas (MG)'),
    ('14601', u'Dumont (SP)'),
    ('14602', u'São José do Bonfim (PB)'),
    ('14604', u'Irecê (BA)'),
    ('14605', u'Upanema (RN)'),
    ('14605', u'Piratini (RS)'),
    ('14606', u'Niquelândia (GO)'),
    ('14607', u'Rio do Oeste (SC)'),
    ('14609', u'Marechal Cândido Rondon (PR)'),
    ('14651', u'São José do Brejo do Cruz (PB)'),
    ('14653', u'Itabela (BA)'),
    ('14700', u'Echaporã (SP)'),
    ('14701', u'São José do Sabugi (PB)'),
    ('14703', u'Itaberaba (BA)'),
    ('14704', u'Planalto (RS)'),
    ('14704', u'Várzea (RN)'),
    ('14705', u'Nova América (GO)'),
    ('14706', u'Rio dos Cedros (SC)'),
    ('14708', u'Maria Helena (PR)'),
    ('14709', u'Carvalhópolis (MG)'),
    ('14709', u'Tacaimbó (PE)'),
    ('14753', u'Venha-Ver (RN)'),
    ('14753', u'Poço das Antas (RS)'),
    ('14779', u'Pontão (RS)'),
    ('14787', u'Ponte Preta (RS)'),
    ('14800', u'São José dos Cordeiros (PB)'),
    ('14802', u'Itabuna * (BA)'),
    ('14803', u'Vera Cruz (RN)'),
    ('14803', u'Portão (RS)'),
    ('14804', u'Nova Aurora (GO)'),
    ('14805', u'Rio do Sul (SC)'),
    ('14807', u'Marialva (PR)'),
    ('14808', u'Tacaratu (PE)'),
    ('14808', u'Carvalhos (MG)'),
    ('14809', u'Eldorado (SP)'),
    ('14838', u'Nova Crixás (GO)'),
    ('14857', u'Tamandaré (PE)'),
    ('14861', u'Nova Glória (GO)'),
    ('14879', u'Nova Iguaçu de Goiás (GO)'),
    ('14880', u'Nova Olinda (TO)'),
    ('14901', u'Itacaré (BA)'),
    ('14902', u'Porto Alegre * (RS)'),
    ('14902', u'Viçosa (RN)'),
    ('14903', u'Nova Roma (GO)'),
    ('14904', u'Rio Fortuna (SC)'),
    ('14906', u'Marilândia do Sul (PR)'),
    ('14907', u'Casa Grande (MG)'),
    ('14908', u'Elias Fausto (SP)'),
    ('14909', u'São Mamede (PB)'),
    ('14924', u'Elisiário (SP)'),
    ('14957', u'Embaúba (SP)'),
    ('15000', u'Rio Negrinho (SC)'),
    ('15002', u'Marilena (PR)'),
    ('15002', u'Nova Rosalândia (TO)'),
    ('15003', u'Taquaritinga do Norte (PE)'),
    ('15003', u'Cascalho Rico (MG)'),
    ('15004', u'Embu * (SP)'),
    ('15005', u'São Miguel de Taipu (PB)'),
    ('15007', u'Itaeté (BA)'),
    ('15008', u'Porto Lucena (RS)'),
    ('15008', u'Vila Flor (RN)'),
    ('15009', u'Nova Veneza (GO)'),
    ('15057', u'Porto Mauá (RS)'),
    ('15059', u'Rio Rufino (SC)'),
    ('15073', u'Porto Vera Cruz (RS)'),
    ('15075', u'Riqueza (SC)'),
    ('15101', u'Mariluz (PR)'),
    ('15101', u'Novo Acordo (TO)'),
    ('15102', u'Terezinha (PE)'),
    ('15102', u'Cássia (MG)'),
    ('15103', u'Embu-Guaçu (SP)'),
    ('15104', u'São Sebastião de Lagoa de Roça (PB)'),
    ('15106', u'Itagi (BA)'),
    ('15107', u'Porto Xavier (RS)'),
    ('15109', u'Rodeio (SC)'),
    ('15129', u'Emilianópolis (SP)'),
    ('15131', u'Pouso Novo (RS)'),
    ('15149', u'Presidente Lucena (RS)'),
    ('15150', u'Novo Alegre (TO)'),
    ('15152', u'Engenheiro Coelho (SP)'),
    ('15156', u'Progresso (RS)'),
    ('15172', u'Protásio Alves (RS)'),
    ('15186', u'Espírito Santo do Pinhal (SP)'),
    ('15194', u'Espírito Santo do Turvo (SP)'),
    ('15200', u'Maringá * (PR)'),
    ('15201', u'Conceição da Barra de Minas (MG)'),
    ('15201', u'Terra Nova (PE)'),
    ('15202', u'Estrela d`Oeste (SP)'),
    ('15203', u'São Sebastião do Umbuzeiro (PB)'),
    ('15205', u'Itagibá (BA)'),
    ('15206', u'Putinga (RS)'),
    ('15207', u'Novo Brasil (GO)'),
    ('15208', u'Romelândia (SC)'),
    ('15231', u'Novo Gama (GO)'),
    ('15256', u'Novo Planalto (GO)'),
    ('15259', u'Novo Jardim (TO)'),
    ('15300', u'Timbaúba (PE)'),
    ('15300', u'Cataguases (MG)'),
    ('15301', u'Estrela do Norte (SP)'),
    ('15302', u'Sapé (PB)'),
    ('15304', u'Itagimirim (BA)'),
    ('15305', u'Quaraí (RS)'),
    ('15306', u'Orizona (GO)'),
    ('15307', u'Salete (SC)'),
    ('15309', u'Mariópolis (PR)'),
    ('15313', u'Quatro Irmãos (RS)'),
    ('15321', u'Quevedos (RS)'),
    ('15350', u'Euclides da Cunha Paulista (SP)'),
    ('15353', u'Itaguaçu da Bahia (BA)'),
    ('15354', u'Quinze de Novembro (RS)'),
    ('15356', u'Saltinho (SC)'),
    ('15358', u'Maripá (PR)'),
    ('15359', u'Catas Altas (MG)'),
    ('15400', u'Fartura (SP)'),
    ('15401', u'Seridó (PB)'),
    ('15403', u'Itaju do Colônia (BA)'),
    ('15404', u'Redentora (RS)'),
    ('15405', u'Ouro Verde de Goiás (GO)'),
    ('15406', u'Salto Veloso (SC)'),
    ('15408', u'Marmeleiro (PR)'),
    ('15409', u'Catas Altas da Noruega (MG)'),
    ('15409', u'Toritama (PE)'),
    ('15453', u'Relvado (RS)'),
    ('15455', u'Sangão (SC)'),
    ('15457', u'Marquinho (PR)'),
    ('15458', u'Catuji (MG)'),
    ('15474', u'Catuti (MG)'),
    ('15500', u'Serra Branca (PB)'),
    ('15502', u'Itajuípe (BA)'),
    ('15503', u'Restinga Seca (RS)'),
    ('15504', u'Ouvidor (GO)'),
    ('15505', u'Santa Cecília (SC)'),
    ('15507', u'Oliveira de Fátima (TO)'),
    ('15507', u'Marumbi (PR)'),
    ('15508', u'Tracunhaém (PE)'),
    ('15508', u'Caxambu (MG)'),
    ('15509', u'Fernandópolis (SP)'),
    ('15552', u'Rio dos Índios (RS)'),
    ('15554', u'Santa Helena (SC)'),
    ('15601', u'Itamaraju (BA)'),
    ('15602', u'Rio Grande * (RS)'),
    ('15603', u'Padre Bernardo (GO)'),
    ('15604', u'Santa Rosa de Lima (SC)'),
    ('15606', u'Matelândia (PR)'),
    ('15607', u'Trindade (PE)'),
    ('15607', u'Cedro do Abaeté (MG)'),
    ('15608', u'Fernando Prestes (SP)'),
    ('15609', u'Serra da Raiz (PB)'),
    ('15652', u'Palestina de Goiás (GO)'),
    ('15653', u'Santa Rosa do Sul (SC)'),
    ('15657', u'Fernão (SP)'),
    ('15679', u'Santa Terezinha (SC)'),
    ('15687', u'Santa Terezinha do Progresso (SC)'),
    ('15695', u'Santiago do Sul (SC)'),
    ('15700', u'Itamari (BA)'),
    ('15701', u'Rio Pardo (RS)'),
    ('15702', u'Palmeiras de Goiás (GO)'),
    ('15703', u'Santo Amaro da Imperatriz (SC)'),
    ('15705', u'Palmeirante (TO)'),
    ('15705', u'Matinhos (PR)'),
    ('15706', u'Central de Minas (MG)'),
    ('15706', u'Triunfo (PE)'),
    ('15707', u'Ferraz de Vasconcelos * (SP)'),
    ('15708', u'Serra Grande (PB)'),
    ('15739', u'Mato Rico (PR)'),
    ('15750', u'Riozinho (RS)'),
    ('15752', u'São Bernardino (SC)'),
    ('15754', u'Mauá da Serra (PR)'),
    ('15754', u'Palmeirópolis (TO)'),
    ('15800', u'Roca Sales (RS)'),
    ('15801', u'Palmelo (GO)'),
    ('15802', u'São Bento do Sul (SC)'),
    ('15804', u'Medianeira (PR)'),
    ('15805', u'Centralina (MG)'),
    ('15805', u'Tupanatinga (PE)'),
    ('15806', u'Flora Rica (SP)'),
    ('15807', u'Serra Redonda (PB)'),
    ('15809', u'Itambé (BA)'),
    ('15853', u'Mercedes (PR)'),
    ('15900', u'Palminópolis (GO)'),
    ('15901', u'São Bonifácio (SC)'),
    ('15903', u'Mirador (PR)'),
    ('15904', u'Chácara (MG)'),
    ('15904', u'Tuparetama (PE)'),
    ('15905', u'Floreal (SP)'),
    ('15906', u'Serraria (PB)'),
    ('15908', u'Itanagra (BA)'),
    ('15909', u'Rodeio Bonito (RS)'),
    ('15930', u'Sertãozinho (PB)'),
    ('15958', u'Rolador (RS)'),
    ('15971', u'Sobrado (PB)'),
    ('16000', u'Miraselva (PR)'),
    ('16001', u'Venturosa (PE)'),
    ('16001', u'Chalé (MG)'),
    ('16002', u'Flórida Paulista (SP)'),
    ('16003', u'Solânea (PB)'),
    ('16005', u'Itanhém (BA)'),
    ('16006', u'Rolante (RS)'),
    ('16007', u'Panamá (GO)'),
    ('16008', u'São Carlos (SC)'),
    ('16057', u'São Cristovão do Sul (SC)'),
    ('16059', u'Missal (PR)'),
    ('16100', u'Verdejante (PE)'),
    ('16100', u'Chapada do Norte (MG)'),
    ('16101', u'Florínia (SP)'),
    ('16102', u'Soledade (PB)'),
    ('16104', u'Itaparica (BA)'),
    ('16105', u'Ronda Alta (RS)'),
    ('16107', u'São Domingos (SC)'),
    ('16109', u'Paraíso do Tocantins (TO)'),
    ('16109', u'Moreira Sales (PR)'),
    ('16151', u'Sossêgo (PB)'),
    ('16159', u'Chapada Gaúcha (MG)'),
    ('16183', u'Vertente do Lério (PE)'),
    ('16200', u'Franca * (SP)'),
    ('16201', u'Sousa (PB)'),
    ('16203', u'Itapé (BA)'),
    ('16204', u'Rondinha (RS)'),
    ('16206', u'São Francisco do Sul (SC)'),
    ('16208', u'Morretes (PR)'),
    ('16208', u'Paranã (TO)'),
    ('16209', u'Chiador (MG)'),
    ('16209', u'Vertentes (PE)'),
    ('16255', u'São João do Oeste (SC)'),
    ('16300', u'Sumé (PB)'),
    ('16302', u'Itapebi (BA)'),
    ('16303', u'Roque Gonzales (RS)'),
    ('16304', u'Paranaiguara (GO)'),
    ('16305', u'São João Batista (SC)'),
    ('16307', u'Pau D`Arco (TO)'),
    ('16307', u'Munhoz de Melo (PR)'),
    ('16308', u'Vicência (PE)'),
    ('16308', u'Cipotânea (MG)'),
    ('16309', u'Francisco Morato (SP)'),
    ('16354', u'São João do Itaperiú (SC)'),
    ('16401', u'Itapetinga (BA)'),
    ('16402', u'Rosário do Sul (RS)'),
    ('16403', u'Paraúna (GO)'),
    ('16404', u'São João do Sul (SC)'),
    ('16406', u'Nossa Senhora das Graças (PR)'),
    ('16407', u'Vitória de Santo Antão (PE)'),
    ('16407', u'Claraval (MG)'),
    ('16408', u'Franco da Rocha (SP)'),
    ('16409', u'Campo de Santana (PB)'),
    ('16428', u'Sagrada Família (RS)'),
    ('16436', u'Saldanha Marinho (RS)'),
    ('16451', u'Salto do Jacuí (RS)'),
    ('16452', u'Perolândia (GO)'),
    ('16477', u'Salvador das Missões (RS)'),
    ('16500', u'Itapicuru (BA)'),
    ('16501', u'Salvador do Sul (RS)'),
    ('16503', u'São Joaquim (SC)'),
    ('16505', u'Pedro Afonso (TO)'),
    ('16505', u'Nova Aliança do Ivaí (PR)'),
    ('16506', u'Xexéu (PE)'),
    ('16506', u'Claro dos Poções (MG)'),
    ('16507', u'Gabriel Monteiro (SP)'),
    ('16508', u'Taperoá (PB)'),
    ('16600', u'Sananduva (RS)'),
    ('16602', u'São José * (SC)'),
    ('16604', u'Peixe (TO)'),
    ('16604', u'Nova América da Colina (PR)'),
    ('16605', u'Cláudio (MG)'),
    ('16606', u'Gália (SP)'),
    ('16607', u'Tavares (PB)'),
    ('16609', u'Itapitanga (BA)'),
    ('16653', u'Pequizeiro (TO)'),
    ('16701', u'São José do Cedro (SC)'),
    ('16703', u'Nova Aurora (PR)'),
    ('16703', u'Colméia (TO)'),
    ('16704', u'Coimbra (MG)'),
    ('16705', u'Garça (SP)'),
    ('16706', u'Teixeira (PB)'),
    ('16708', u'Itaquara (BA)'),
    ('16709', u'Santa Bárbara do Sul (RS)'),
    ('16733', u'Santa Cecília do Sul (RS)'),
    ('16755', u'Tenório (PB)'),
    ('16758', u'Santa Clara do Sul (RS)'),
    ('16800', u'São José do Cerrito (SC)'),
    ('16802', u'Nova Cantu (PR)'),
    ('16803', u'Coluna (MG)'),
    ('16804', u'Gastão Vidigal (SP)'),
    ('16805', u'Triunfo (PB)'),
    ('16807', u'Itarantim (BA)'),
    ('16808', u'Santa Cruz do Sul (RS)'),
    ('16809', u'Petrolina de Goiás (GO)'),
    ('16853', u'Gavião Peixoto (SP)'),
    ('16856', u'Itatim (BA)'),
    ('16901', u'Nova Esperança (PR)'),
    ('16902', u'Comendador Gomes (MG)'),
    ('16903', u'General Salgado (SP)'),
    ('16904', u'Uiraúna (PB)'),
    ('16906', u'Itiruçu (BA)'),
    ('16907', u'Santa Maria * (RS)'),
    ('16908', u'Pilar de Goiás (GO)'),
    ('16909', u'São Lourenço do Oeste (SC)'),
    ('16950', u'Nova Esperança do Sudoeste (PR)'),
    ('16956', u'Santa Maria do Herval (RS)'),
    ('16972', u'Santa Margarida do Sul (RS)'),
    ('17000', u'Getulina (SP)'),
    ('17001', u'Umbuzeiro (PB)'),
    ('17003', u'Itiúba (BA)'),
    ('17004', u'Santana da Boa Vista (RS)'),
    ('17006', u'São Ludgero (SC)'),
    ('17008', u'Nova Fátima (PR)'),
    ('17008', u'Pindorama do Tocantins (TO)'),
    ('17009', u'Comercinho (MG)'),
    ('17057', u'Nova Laranjeiras (PR)'),
    ('17100', u'Várzea (PB)'),
    ('17102', u'Itororó (BA)'),
    ('17103', u'Santana do Livramento (RS)'),
    ('17104', u'Piracanjuba (GO)'),
    ('17105', u'São Martinho (SC)'),
    ('17107', u'Nova Londrina (PR)'),
    ('17108', u'Conceição da Aparecida (MG)'),
    ('17109', u'Glicério (SP)'),
    ('17154', u'São Miguel da Boa Vista (SC)'),
    ('17201', u'Ituaçu (BA)'),
    ('17202', u'Santa Rosa (RS)'),
    ('17203', u'Piranhas (GO)'),
    ('17204', u'São Miguel do Oeste (SC)'),
    ('17206', u'Nova Olímpia (PR)'),
    ('17206', u'Piraquê (TO)'),
    ('17207', u'Conceição das Pedras (MG)'),
    ('17208', u'Guaiçara (SP)'),
    ('17209', u'Vieirópolis (PB)'),
    ('17214', u'Nova Santa Bárbara (PR)'),
    ('17222', u'Nova Santa Rosa (PR)'),
    ('17251', u'Santa Tereza (RS)'),
    ('17253', u'São Pedro de Alcântara (SC)'),
    ('17255', u'Nova Prata do Iguaçu (PR)'),
    ('17271', u'Nova Tebas (PR)'),
    ('17297', u'Novo Itacolomi (PR)'),
    ('17300', u'Ituberá (BA)'),
    ('17301', u'Santa Vitória do Palmar (RS)'),
    ('17302', u'Pirenópolis (GO)'),
    ('17303', u'Saudades (SC)'),
    ('17305', u'Ortigueira (PR)'),
    ('17306', u'Conceição das Alagoas (MG)'),
    ('17307', u'Guaimbê (SP)'),
    ('17334', u'Iuiú (BA)'),
    ('17359', u'Jaborandi (BA)'),
    ('17400', u'Santiago (RS)'),
    ('17401', u'Pires do Rio (GO)'),
    ('17402', u'Schroeder (SC)'),
    ('17404', u'Ourizona (PR)'),
    ('17405', u'Conceição de Ipanema (MG)'),
    ('17406', u'Guaíra (SP)'),
    ('17407', u'Zabelê (PB)'),
    ('17409', u'Jacaraci (BA)'),
    ('17453', u'Ouro Verde do Oeste (PR)'),
    ('17501', u'Seara (SC)'),
    ('17503', u'Paiçandu (PR)'),
    ('17503', u'Pium (TO)'),
    ('17504', u'Conceição do Mato Dentro (MG)'),
    ('17505', u'Guapiaçu (SP)'),
    ('17508', u'Jacobina (BA)'),
    ('17509', u'Santo Ângelo (RS)'),
    ('17550', u'Serra Alta (SC)'),
    ('17558', u'Santo Antônio do Palma (RS)'),
    ('17600', u'Siderópolis (SC)'),
    ('17602', u'Palmas (PR)'),
    ('17603', u'Conceição do Pará (MG)'),
    ('17604', u'Guapiara (SP)'),
    ('17607', u'Jaguaquara (BA)'),
    ('17608', u'Santo Antônio da Patrulha (RS)'),
    ('17609', u'Planaltina (GO)'),
    ('17701', u'Palmeira (PR)'),
    ('17702', u'Conceição do Rio Verde (MG)'),
    ('17703', u'Guará (SP)'),
    ('17706', u'Jaguarari (BA)'),
    ('17707', u'Santo Antônio das Missões (RS)'),
    ('17708', u'Pontalina (GO)'),
    ('17709', u'Sombrio (SC)'),
    ('17756', u'Santo Antônio do Planalto (RS)'),
    ('17758', u'Sul Brasil (SC)'),
    ('17800', u'Palmital (PR)'),
    ('17800', u'Ponte Alta do Bom Jesus (TO)'),
    ('17801', u'Conceição dos Ouros (MG)'),
    ('17802', u'Guaraçaí (SP)'),
    ('17805', u'Jaguaripe (BA)'),
    ('17806', u'Santo Augusto (RS)'),
    ('17808', u'Taió (SC)'),
    ('17836', u'Cônego Marinho (MG)'),
    ('17876', u'Confins (MG)'),
    ('17900', u'Congonhal (MG)'),
    ('17901', u'Guaraci (SP)'),
    ('17904', u'Jandaíra (BA)'),
    ('17905', u'Santo Cristo (RS)'),
    ('17907', u'Tangará (SC)'),
    ('17909', u'Palotina (PR)'),
    ('17909', u'Ponte Alta do Tocantins (TO)'),
    ('17954', u'Santo Expedito do Sul (RS)'),
    ('17956', u'Tigrinhos (SC)'),
    ('18001', u'Jequié (BA)'),
    ('18002', u'São Borja (RS)'),
    ('18003', u'Porangatu (GO)'),
    ('18004', u'Tijucas (SC)'),
    ('18006', u'Porto Alegre do Tocantins (TO)'),
    ('18006', u'Paraíso do Norte (PR)'),
    ('18007', u'Congonhas (MG)'),
    ('18008', u'Guarani d`Oeste (SP)'),
    ('18051', u'São Domingos do Sul (RS)'),
    ('18052', u'Porteirão (GO)'),
    ('18100', u'Jeremoabo (BA)'),
    ('18101', u'São Francisco de Assis (RS)'),
    ('18102', u'Portelândia (GO)'),
    ('18103', u'Timbé do Sul (SC)'),
    ('18105', u'Paranacity (PR)'),
    ('18106', u'Congonhas do Norte (MG)'),
    ('18107', u'Guarantã (SP)'),
    ('18200', u'São Francisco de Paula (RS)'),
    ('18202', u'Timbó (SC)'),
    ('18204', u'Paranaguá (PR)'),
    ('18204', u'Porto Nacional (TO)'),
    ('18205', u'Conquista (MG)'),
    ('18206', u'Guararapes (SP)'),
    ('18209', u'Jiquiriçá (BA)'),
    ('18251', u'Timbó Grande (SC)'),
    ('18300', u'Posse (GO)'),
    ('18301', u'Três Barras (SC)'),
    ('18303', u'Paranapoema (PR)'),
    ('18303', u'Praia Norte (TO)'),
    ('18304', u'Conselheiro Lafaiete (MG)'),
    ('18305', u'Guararema (SP)'),
    ('18308', u'Jitaúna (BA)'),
    ('18309', u'São Gabriel (RS)'),
    ('18350', u'Treviso (SC)'),
    ('18357', u'João Dourado (BA)'),
    ('18391', u'Professor Jamil (GO)'),
    ('18400', u'Treze de Maio (SC)'),
    ('18402', u'Presidente Kennedy (TO)'),
    ('18402', u'Paranavaí (PR)'),
    ('18403', u'Conselheiro Pena (MG)'),
    ('18404', u'Guaratinguetá (SP)'),
    ('18407', u'Juazeiro * (BA)'),
    ('18408', u'São Jerônimo (RS)'),
    ('18424', u'São João da Urtiga (RS)'),
    ('18432', u'São João do Polêsine (RS)'),
    ('18440', u'São Jorge (RS)'),
    ('18451', u'Pato Bragado (PR)'),
    ('18451', u'Pugmil (TO)'),
    ('18456', u'Jucuruçu (BA)'),
    ('18457', u'São José das Missões (RS)'),
    ('18465', u'São José do Herval (RS)'),
    ('18481', u'São José do Hortêncio (RS)'),
    ('18499', u'São José do Inhacorá (RS)'),
    ('18501', u'Pato Branco (PR)'),
    ('18501', u'Recursolândia (TO)'),
    ('18502', u'Consolação (MG)'),
    ('18503', u'Guareí (SP)'),
    ('18506', u'Jussara (BA)'),
    ('18507', u'São José do Norte (RS)'),
    ('18508', u'Quirinópolis (GO)'),
    ('18509', u'Treze Tílias (SC)'),
    ('18550', u'Riachinho (TO)'),
    ('18555', u'Jussari (BA)'),
    ('18600', u'Paula Freitas (PR)'),
    ('18601', u'Contagem * (MG)'),
    ('18602', u'Guariba (SP)'),
    ('18605', u'Jussiape (BA)'),
    ('18606', u'São José do Ouro (RS)'),
    ('18607', u'Rialma (GO)'),
    ('18608', u'Trombudo Central (SC)'),
    ('18614', u'São José do Sul (RS)'),
    ('18622', u'São José dos Ausentes (RS)'),
    ('18659', u'Rio da Conceição (TO)'),
    ('18700', u'Coqueiral (MG)'),
    ('18701', u'Guarujá * (SP)'),
    ('18704', u'Lafaiete Coutinho (BA)'),
    ('18705', u'São Leopoldo * (RS)'),
    ('18706', u'Rianápolis (GO)'),
    ('18707', u'Tubarão (SC)'),
    ('18709', u'Rio dos Bois (TO)'),
    ('18709', u'Paulo Frontin (PR)'),
    ('18753', u'Lagoa Real (BA)'),
    ('18756', u'Tunápolis (SC)'),
    ('18758', u'Rio Sono (TO)'),
    ('18789', u'Rio Quente (GO)'),
    ('18800', u'Guarulhos * (SP)'),
    ('18803', u'Laje (BA)'),
    ('18804', u'São Lourenço do Sul (RS)'),
    ('18805', u'Rio Verde (GO)'),
    ('18806', u'Turvo (SC)'),
    ('18808', u'Peabiru (PR)'),
    ('18808', u'Sampaio (TO)'),
    ('18809', u'Coração de Jesus (MG)'),
    ('18840', u'Sandolândia (TO)'),
    ('18855', u'União do Oeste (SC)'),
    ('18857', u'Perobal (PR)'),
    ('18859', u'Guatapará (SP)'),
    ('18865', u'Santa Fé do Araguaia (TO)'),
    ('18881', u'Santa Maria do Tocantins (TO)'),
    ('18899', u'Santa Rita do Tocantins (TO)'),
    ('18902', u'Lajedão (BA)'),
    ('18903', u'São Luiz Gonzaga (RS)'),
    ('18904', u'Rubiataba (GO)'),
    ('18905', u'Urubici (SC)'),
    ('18907', u'Santa Rosa do Tocantins (TO)'),
    ('18907', u'Pérola (PR)'),
    ('18908', u'Cordisburgo (MG)'),
    ('18909', u'Guzolândia (SP)'),
    ('18954', u'Urupema (SC)'),
    ('19000', u'São Marcos (RS)'),
    ('19001', u'Sanclerlândia (GO)'),
    ('19002', u'Urussanga (SC)'),
    ('19004', u'Pérola d`Oeste (PR)'),
    ('19004', u'Santa Tereza do Tocantins (TO)'),
    ('19005', u'Cordislândia (MG)'),
    ('19006', u'Herculândia (SP)'),
    ('19009', u'Lajedinho (BA)'),
    ('19055', u'Holambra (SP)'),
    ('19058', u'Lajedo do Tabocal (BA)'),
    ('19071', u'Hortolândia * (SP)'),
    ('19100', u'Santa Bárbara de Goiás (GO)'),
    ('19101', u'Vargeão (SC)'),
    ('19103', u'Piên (PR)'),
    ('19104', u'Corinto (MG)'),
    ('19105', u'Iacanga (SP)'),
    ('19108', u'Lamarão (BA)'),
    ('19109', u'São Martinho (RS)'),
    ('19125', u'São Martinho da Serra (RS)'),
    ('19150', u'Vargem (SC)'),
    ('19152', u'Pinhais (PR)'),
    ('19157', u'Lapão (BA)'),
    ('19158', u'São Miguel das Missões (RS)'),
    ('19176', u'Vargem Bonita (SC)'),
    ('19200', u'Vidal Ramos (SC)'),
    ('19202', u'Pinhalão (PR)'),
    ('19203', u'Coroaci (MG)'),
    ('19204', u'Iacri (SP)'),
    ('19207', u'Lauro de Freitas (BA)'),
    ('19208', u'São Nicolau (RS)'),
    ('19209', u'Santa Cruz de Goiás (GO)'),
    ('19251', u'Pinhal de São Bento (PR)'),
    ('19253', u'Iaras (SP)'),
    ('19258', u'Santa Fé de Goiás (GO)'),
    ('19301', u'Pinhão (PR)'),
    ('19302', u'Coromandel (MG)'),
    ('19303', u'Ibaté (SP)'),
    ('19306', u'Lençóis (BA)'),
    ('19307', u'São Paulo das Missões (RS)'),
    ('19308', u'Santa Helena de Goiás (GO)'),
    ('19309', u'Videira (SC)'),
    ('19356', u'São Pedro da Serra (RS)'),
    ('19357', u'Santa Isabel (GO)'),
    ('19358', u'Vitor Meireles (SC)'),
    ('19364', u'São Pedro das Missões (RS)'),
    ('19372', u'São Pedro do Butiá (RS)'),
    ('19400', u'Piraí do Sul (PR)'),
    ('19401', u'Coronel Fabriciano (MG)'),
    ('19402', u'Ibirá (SP)'),
    ('19405', u'Licínio de Almeida (BA)'),
    ('19406', u'São Pedro do Sul (RS)'),
    ('19407', u'Santa Rita do Araguaia (GO)'),
    ('19408', u'Witmarsum (SC)'),
    ('19456', u'Santa Rita do Novo Destino (GO)'),
    ('19500', u'Coronel Murta (MG)'),
    ('19501', u'Ibirarema (SP)'),
    ('19504', u'Livramento de Nossa Senhora (BA)'),
    ('19505', u'São Sebastião do Caí (RS)'),
    ('19506', u'Santa Rosa de Goiás (GO)'),
    ('19507', u'Xanxerê (SC)'),
    ('19509', u'Piraquara (PR)'),
    ('19553', u'Luís Eduardo Magalhães (BA)'),
    ('19600', u'Ibitinga (SP)'),
    ('19603', u'Macajuba (BA)'),
    ('19604', u'São Sepé (RS)'),
    ('19605', u'Santa Tereza de Goiás (GO)'),
    ('19606', u'Xavantina (SC)'),
    ('19608', u'Pitanga (PR)'),
    ('19609', u'Coronel Pacheco (MG)'),
    ('19657', u'Pitangueiras (PR)'),
    ('19702', u'Macarani (BA)'),
    ('19703', u'São Valentim (RS)'),
    ('19704', u'Santa Terezinha de Goiás (GO)'),
    ('19705', u'Xaxim (SC)'),
    ('19707', u'Planaltina do Paraná (PR)'),
    ('19708', u'Coronel Xavier Chaves (MG)'),
    ('19709', u'Ibiúna (SP)'),
    ('19711', u'São Valentim do Sul (RS)'),
    ('19712', u'Santo Antônio da Barra (GO)'),
    ('19737', u'São Valério do Sul (RS)'),
    ('19738', u'Santo Antônio de Goiás (GO)'),
    ('19752', u'São Vendelino (RS)'),
    ('19753', u'Santo Antônio do Descoberto (GO)'),
    ('19801', u'Macaúbas (BA)'),
    ('19802', u'São Vicente do Sul (RS)'),
    ('19803', u'São Domingos (GO)'),
    ('19806', u'Planalto (PR)'),
    ('19807', u'Córrego Danta (MG)'),
    ('19808', u'Icém (SP)'),
    ('19853', u'Zortéa (SC)'),
    ('19900', u'Macururé (BA)'),
    ('19901', u'Sapiranga (RS)'),
    ('19902', u'São Francisco de Goiás (GO)'),
    ('19905', u'Ponta Grossa * (PR)'),
    ('19906', u'Córrego do Bom Jesus (MG)'),
    ('19907', u'Iepê (SP)'),
    ('19926', u'Madre de Deus (BA)'),
    ('19954', u'Pontal do Paraná (PR)'),
    ('19955', u'Córrego Fundo (MG)'),
    ('19959', u'Maetinga (BA)'),
    ('20002', u'Porecatu (PR)'),
    ('20002', u'Santa Terezinha do Tocantins (TO)'),
    ('20003', u'Córrego Novo (MG)'),
    ('20004', u'Igaraçu do Tietê (SP)'),
    ('20007', u'Maiquinique (BA)'),
    ('20008', u'Sapucaia do Sul (RS)'),
    ('20009', u'São João d`Aliança (GO)'),
    ('20058', u'São João da Paraúna (GO)'),
    ('20101', u'São Bento do Tocantins (TO)'),
    ('20101', u'Porto Amazonas (PR)'),
    ('20102', u'Couto de Magalhães de Minas (MG)'),
    ('20103', u'Igarapava (SP)'),
    ('20106', u'Mairi (BA)'),
    ('20107', u'Sarandi (RS)'),
    ('20108', u'São Luís de Montes Belos (GO)'),
    ('20150', u'Porto Barreiro (PR)'),
    ('20150', u'São Félix do Tocantins (TO)'),
    ('20151', u'Crisólita (MG)'),
    ('20157', u'São Luíz do Norte (GO)'),
    ('20200', u'São Miguel do Tocantins (TO)'),
    ('20200', u'Porto Rico (PR)'),
    ('20201', u'Cristais (MG)'),
    ('20202', u'Igaratá (SP)'),
    ('20205', u'Malhada (BA)'),
    ('20206', u'Seberi (RS)'),
    ('20207', u'São Miguel do Araguaia (GO)'),
    ('20230', u'Sede Nova (RS)'),
    ('20259', u'São Salvador do Tocantins (TO)'),
    ('20263', u'Segredo (RS)'),
    ('20264', u'São Miguel do Passa Quatro (GO)'),
    ('20280', u'São Patrício (GO)'),
    ('20300', u'Cristália (MG)'),
    ('20301', u'Iguape (SP)'),
    ('20304', u'Malhada de Pedras (BA)'),
    ('20305', u'Selbach (RS)'),
    ('20309', u'São Sebastião do Tocantins (TO)'),
    ('20309', u'Porto Vitória (PR)'),
    ('20321', u'Senador Salgado Filho (RS)'),
    ('20333', u'Prado Ferreira (PR)'),
    ('20354', u'Sentinela do Sul (RS)'),
    ('20358', u'Pranchita (PR)'),
    ('20400', u'Ilhabela (SP)'),
    ('20403', u'Manoel Vitorino (BA)'),
    ('20404', u'Serafina Corrêa (RS)'),
    ('20405', u'São Simão (GO)'),
    ('20408', u'Presidente Castelo Branco (PR)'),
    ('20409', u'Cristiano Otoni (MG)'),
    ('20426', u'Ilha Comprida (SP)'),
    ('20442', u'Ilha Solteira (SP)'),
    ('20452', u'Mansidão (BA)'),
    ('20453', u'Sério (RS)'),
    ('20454', u'Senador Canedo (GO)'),
    ('20499', u'São Valério da Natividade (TO)'),
    ('20502', u'Maracás (BA)'),
    ('20503', u'Sertão (RS)'),
    ('20504', u'Serranópolis (GO)'),
    ('20507', u'Primeiro de Maio (PR)'),
    ('20508', u'Cristina (MG)'),
    ('20509', u'Indaiatuba * (SP)'),
    ('20552', u'Sertão Santana (RS)'),
    ('20578', u'Sete de Setembro (RS)'),
    ('20601', u'Maragogipe (BA)'),
    ('20602', u'Severiano de Almeida (RS)'),
    ('20603', u'Silvânia (GO)'),
    ('20606', u'Prudentópolis (PR)'),
    ('20607', u'Crucilândia (MG)'),
    ('20608', u'Indiana (SP)'),
    ('20651', u'Silveira Martins (RS)'),
    ('20655', u'Quarto Centenário (PR)'),
    ('20655', u'Silvanópolis (TO)'),
    ('20677', u'Sinimbu (RS)'),
    ('20686', u'Simolândia (GO)'),
    ('20700', u'Maraú (BA)'),
    ('20701', u'Sobradinho (RS)'),
    ('20702', u'Sítio d`Abadia (GO)'),
    ('20705', u'Quatiguá (PR)'),
    ('20706', u'Cruzeiro da Fortaleza (MG)'),
    ('20707', u'Indiaporã (SP)'),
    ('20800', u'Soledade (RS)'),
    ('20804', u'Sítio Novo do Tocantins (TO)'),
    ('20804', u'Quatro Barras (PR)'),
    ('20805', u'Cruzília (MG)'),
    ('20806', u'Inúbia Paulista (SP)'),
    ('20809', u'Marcionílio Souza (BA)'),
    ('20839', u'Cuparaque (MG)'),
    ('20853', u'Sucupira (TO)'),
    ('20853', u'Quatro Pontes (PR)'),
    ('20859', u'Tabaí (RS)'),
    ('20870', u'Curral de Dentro (MG)'),
    ('20903', u'Quedas do Iguaçu (PR)'),
    ('20903', u'Taguatinga (TO)'),
    ('20904', u'Curvelo (MG)'),
    ('20905', u'Ipaussu (SP)'),
    ('20908', u'Mascote (BA)'),
    ('20909', u'Tapejara (RS)'),
    ('20937', u'Taipas do Tocantins (TO)'),
    ('20978', u'Talismã (TO)'),
    ('21000', u'Palmas (TO)'),
    ('21000', u'Querência do Norte (PR)'),
    ('21001', u'Datas (MG)'),
    ('21002', u'Iperó (SP)'),
    ('21005', u'Mata de São João (BA)'),
    ('21006', u'Tapera (RS)'),
    ('21007', u'Taquaral de Goiás (GO)'),
    ('21054', u'Matina (BA)'),
    ('21080', u'Teresina de Goiás (GO)'),
    ('21100', u'Delfim Moreira (MG)'),
    ('21101', u'Ipeúna (SP)'),
    ('21104', u'Medeiros Neto (BA)'),
    ('21105', u'Tapes (RS)'),
    ('21109', u'Quinta do Sol (PR)'),
    ('21109', u'Tocantínia (TO)'),
    ('21150', u'Ipiguá (SP)'),
    ('21197', u'Terezópolis de Goiás (GO)'),
    ('21200', u'Iporanga (SP)'),
    ('21203', u'Miguel Calmon (BA)'),
    ('21204', u'Taquara (RS)'),
    ('21208', u'Tocantinópolis (TO)'),
    ('21208', u'Quitandinha (PR)'),
    ('21209', u'Delfinópolis (MG)'),
    ('21257', u'Tupirama (TO)'),
    ('21257', u'Ramilândia (PR)'),
    ('21258', u'Delta (MG)'),
    ('21302', u'Milagres (BA)'),
    ('21303', u'Taquari (RS)'),
    ('21304', u'Três Ranchos (GO)'),
    ('21307', u'Tupiratins (TO)'),
    ('21307', u'Rancho Alegre (PR)'),
    ('21308', u'Descoberto (MG)'),
    ('21309', u'Ipuã (SP)'),
    ('21329', u'Taquaruçu do Sul (RS)'),
    ('21352', u'Tavares (RS)'),
    ('21356', u'Rancho Alegre D`Oeste (PR)'),
    ('21401', u'Mirangaba (BA)'),
    ('21402', u'Tenente Portela (RS)'),
    ('21403', u'Trindade (GO)'),
    ('21406', u'Realeza (PR)'),
    ('21407', u'Desterro de Entre Rios (MG)'),
    ('21408', u'Iracemápolis (SP)'),
    ('21436', u'Terra de Areia (RS)'),
    ('21450', u'Mirante (BA)'),
    ('21451', u'Teutônia (RS)'),
    ('21452', u'Trombas (GO)'),
    ('21469', u'Tio Hugo (RS)'),
    ('21477', u'Tiradentes do Sul (RS)'),
    ('21493', u'Toropi (RS)'),
    ('21500', u'Monte Santo (BA)'),
    ('21501', u'Torres (RS)'),
    ('21502', u'Turvânia (GO)'),
    ('21505', u'Rebouças (PR)'),
    ('21506', u'Desterro do Melo (MG)'),
    ('21507', u'Irapuã (SP)'),
    ('21551', u'Turvelândia (GO)'),
    ('21577', u'Uirapuru (GO)'),
    ('21600', u'Tramandaí (RS)'),
    ('21601', u'Uruaçu (GO)'),
    ('21604', u'Renascença (PR)'),
    ('21605', u'Diamantina (MG)'),
    ('21606', u'Irapuru (SP)'),
    ('21609', u'Morpará (BA)'),
    ('21626', u'Travesseiro (RS)'),
    ('21634', u'Três Arroios (RS)'),
    ('21667', u'Três Cachoeiras (RS)'),
    ('21700', u'Uruana (GO)'),
    ('21703', u'Reserva (PR)'),
    ('21704', u'Diogo de Vasconcelos (MG)'),
    ('21705', u'Itaberá (SP)'),
    ('21708', u'Morro do Chapéu (BA)'),
    ('21709', u'Três Coroas (RS)'),
    ('21752', u'Reserva do Iguaçu (PR)'),
    ('21802', u'Ribeirão Claro (PR)'),
    ('21803', u'Dionísio (MG)'),
    ('21804', u'Itaí (SP)'),
    ('21807', u'Mortugaba (BA)'),
    ('21808', u'Três de Maio (RS)'),
    ('21809', u'Urutaí (GO)'),
    ('21832', u'Três Forquilhas (RS)'),
    ('21857', u'Três Palmeiras (RS)'),
    ('21858', u'Valparaíso de Goiás (GO)'),
    ('21901', u'Ribeirão do Pinhal (PR)'),
    ('21902', u'Divinésia (MG)'),
    ('21903', u'Itajobi (SP)'),
    ('21906', u'Mucugê (BA)'),
    ('21907', u'Três Passos (RS)'),
    ('21908', u'Varjão (GO)'),
    ('21956', u'Trindade do Sul (RS)'),
    ('22000', u'Itaju (SP)'),
    ('22003', u'Mucuri (BA)'),
    ('22004', u'Triunfo (RS)'),
    ('22005', u'Vianópolis (GO)'),
    ('22008', u'Rio Azul (PR)'),
    ('22009', u'Divino (MG)'),
    ('22052', u'Mulungu do Morro (BA)'),
    ('22054', u'Vicentinópolis (GO)'),
    ('22081', u'Wanderlândia (TO)'),
    ('22102', u'Mundo Novo (BA)'),
    ('22103', u'Tucunduva (RS)'),
    ('22107', u'Xambioá (TO)'),
    ('22107', u'Rio Bom (PR)'),
    ('22108', u'Divino das Laranjeiras (MG)'),
    ('22109', u'Itanhaém (SP)'),
    ('22152', u'Tunas (RS)'),
    ('22156', u'Rio Bonito do Iguaçu (PR)'),
    ('22158', u'Itaóca (SP)'),
    ('22172', u'Rio Branco do Ivaí (PR)'),
    ('22186', u'Tupanci do Sul (RS)'),
    ('22201', u'Muniz Ferreira (BA)'),
    ('22202', u'Tupanciretã (RS)'),
    ('22203', u'Vila Boa (GO)'),
    ('22206', u'Rio Branco do Sul (PR)'),
    ('22207', u'Divinolândia de Minas (MG)'),
    ('22208', u'Itapecerica da Serra (SP)'),
    ('22250', u'Muquém de São Francisco (BA)'),
    ('22251', u'Tupandi (RS)'),
    ('22300', u'Muritiba (BA)'),
    ('22301', u'Tuparendi (RS)'),
    ('22302', u'Vila Propício (GO)'),
    ('22305', u'Rio Negro (PR)'),
    ('22306', u'Divinópolis * (MG)'),
    ('22307', u'Itapetininga (SP)'),
    ('22327', u'Turuçu (RS)'),
    ('22343', u'Ubiretama (RS)'),
    ('22350', u'União da Serra (RS)'),
    ('22355', u'Divisa Alegre (MG)'),
    ('22376', u'Unistalda (RS)'),
    ('22400', u'Uruguaiana (RS)'),
    ('22404', u'Rolândia (PR)'),
    ('22405', u'Divisa Nova (MG)'),
    ('22406', u'Itapeva (SP)'),
    ('22409', u'Mutuípe (BA)'),
    ('22454', u'Divisópolis (MG)'),
    ('22470', u'Dom Bosco (MG)'),
    ('22503', u'Roncador (PR)'),
    ('22504', u'Dom Cavati (MG)'),
    ('22505', u'Itapevi * (SP)'),
    ('22508', u'Nazaré (BA)'),
    ('22509', u'Vacaria (RS)'),
    ('22525', u'Vale Verde (RS)'),
    ('22533', u'Vale do Sol (RS)'),
    ('22541', u'Vale Real (RS)'),
    ('22558', u'Vanini (RS)'),
    ('22602', u'Rondon (PR)'),
    ('22603', u'Dom Joaquim (MG)'),
    ('22604', u'Itapira (SP)'),
    ('22607', u'Nilo Peçanha (BA)'),
    ('22608', u'Venâncio Aires (RS)'),
    ('22651', u'Rosário do Ivaí (PR)'),
    ('22653', u'Itapirapuã Paulista (SP)'),
    ('22656', u'Nordestina (BA)'),
    ('22701', u'Sabáudia (PR)'),
    ('22702', u'Dom Silvério (MG)'),
    ('22703', u'Itápolis (SP)'),
    ('22706', u'Nova Canaã (BA)'),
    ('22707', u'Vera Cruz (RS)'),
    ('22730', u'Nova Fátima (BA)'),
    ('22755', u'Nova Ibiá (BA)'),
    ('22800', u'Salgado Filho (PR)'),
    ('22801', u'Dom Viçoso (MG)'),
    ('22802', u'Itaporanga (SP)'),
    ('22805', u'Nova Itarana (BA)'),
    ('22806', u'Veranópolis (RS)'),
    ('22854', u'Nova Redenção (BA)'),
    ('22855', u'Vespasiano Correa (RS)'),
    ('22900', u'Dona Eusébia (MG)'),
    ('22901', u'Itapuí (SP)'),
    ('22904', u'Nova Soure (BA)'),
    ('22905', u'Viadutos (RS)'),
    ('22909', u'Salto do Itararé (PR)'),
    ('23001', u'Nova Viçosa (BA)'),
    ('23002', u'Viamão * (RS)'),
    ('23006', u'Salto do Lontra (PR)'),
    ('23007', u'Dores de Campos (MG)'),
    ('23008', u'Itapura (SP)'),
    ('23035', u'Novo Horizonte (BA)'),
    ('23050', u'Novo Triunfo (BA)'),
    ('23100', u'Olindina (BA)'),
    ('23101', u'Vicente Dutra (RS)'),
    ('23105', u'Santa Amélia (PR)'),
    ('23106', u'Dores de Guanhães (MG)'),
    ('23107', u'Itaquaquecetuba * (SP)'),
    ('23200', u'Victor Graeff (RS)'),
    ('23204', u'Santa Cecília do Pavão (PR)'),
    ('23205', u'Dores do Indaiá (MG)'),
    ('23206', u'Itararé (SP)'),
    ('23209', u'Oliveira dos Brejinhos (BA)'),
    ('23303', u'Santa Cruz de Monte Castelo (PR)'),
    ('23304', u'Dores do Turvo (MG)'),
    ('23305', u'Itariri (SP)'),
    ('23308', u'Ouriçangas (BA)'),
    ('23309', u'Vila Flores (RS)'),
    ('23357', u'Ourolândia (BA)'),
    ('23358', u'Vila Lângaro (RS)'),
    ('23402', u'Santa Fé (PR)'),
    ('23403', u'Doresópolis (MG)'),
    ('23404', u'Itatiba (SP)'),
    ('23407', u'Palmas de Monte Alto (BA)'),
    ('23408', u'Vila Maria (RS)'),
    ('23457', u'Vila Nova do Sul (RS)'),
    ('23501', u'Santa Helena (PR)'),
    ('23502', u'Douradoquara (MG)'),
    ('23503', u'Itatinga (SP)'),
    ('23506', u'Palmeiras (BA)'),
    ('23507', u'Vista Alegre (RS)'),
    ('23528', u'Durandé (MG)'),
    ('23600', u'Santa Inês (PR)'),
    ('23601', u'Elói Mendes (MG)'),
    ('23602', u'Itirapina (SP)'),
    ('23605', u'Paramirim (BA)'),
    ('23606', u'Vista Alegre do Prata (RS)'),
    ('23700', u'Engenheiro Caldas (MG)'),
    ('23701', u'Itirapuã (SP)'),
    ('23704', u'Paratinga (BA)'),
    ('23705', u'Vista Gaúcha (RS)'),
    ('23709', u'Santa Isabel do Ivaí (PR)'),
    ('23754', u'Vitória das Missões (RS)'),
    ('23770', u'Westfalia (RS)'),
    ('23800', u'Itobi (SP)'),
    ('23803', u'Paripiranga (BA)'),
    ('23804', u'Xangri-lá (RS)'),
    ('23808', u'Santa Izabel do Oeste (PR)'),
    ('23809', u'Engenheiro Navarro (MG)'),
    ('23824', u'Santa Lúcia (PR)'),
    ('23857', u'Santa Maria do Oeste (PR)'),
    ('23858', u'Entre Folhas (MG)'),
    ('23902', u'Pau Brasil (BA)'),
    ('23907', u'Santa Mariana (PR)'),
    ('23908', u'Entre Rios de Minas (MG)'),
    ('23909', u'Itu (SP)'),
    ('23956', u'Santa Mônica (PR)'),
    ('24004', u'Santana do Itararé (PR)'),
    ('24005', u'Ervália (MG)'),
    ('24006', u'Itupeva (SP)'),
    ('24009', u'Paulo Afonso (BA)'),
    ('24020', u'Santa Tereza do Oeste (PR)'),
    ('24053', u'Santa Terezinha de Itaipu (PR)'),
    ('24058', u'Pé de Serra (BA)'),
    ('24103', u'Santo Antônio da Platina (PR)'),
    ('24104', u'Esmeraldas (MG)'),
    ('24105', u'Ituverava (SP)'),
    ('24108', u'Pedrão (BA)'),
    ('24202', u'Santo Antônio do Caiuá (PR)'),
    ('24203', u'Espera Feliz (MG)'),
    ('24204', u'Jaborandi (SP)'),
    ('24207', u'Pedro Alexandre (BA)'),
    ('24301', u'Santo Antônio do Paraíso (PR)'),
    ('24302', u'Espinosa (MG)'),
    ('24303', u'Jaboticabal (SP)'),
    ('24306', u'Piatã (BA)'),
    ('24400', u'Santo Antônio do Sudoeste (PR)'),
    ('24401', u'Espírito Santo do Dourado (MG)'),
    ('24402', u'Jacareí * (SP)'),
    ('24405', u'Pilão Arcado (BA)'),
    ('24500', u'Estiva (MG)'),
    ('24501', u'Jaci (SP)'),
    ('24504', u'Pindaí (BA)'),
    ('24509', u'Santo Inácio (PR)'),
    ('24600', u'Jacupiranga (SP)'),
    ('24603', u'Pindobaçu (BA)'),
    ('24608', u'São Carlos do Ivaí (PR)'),
    ('24609', u'Estrela Dalva (MG)'),
    ('24652', u'Pintadas (BA)'),
    ('24678', u'Piraí do Norte (BA)'),
    ('24702', u'Piripá (BA)'),
    ('24707', u'São Jerônimo da Serra (PR)'),
    ('24708', u'Estrela do Indaiá (MG)'),
    ('24709', u'Jaguariúna (SP)'),
    ('24801', u'Piritiba (BA)'),
    ('24806', u'São João (PR)'),
    ('24807', u'Estrela do Sul (MG)'),
    ('24808', u'Jales (SP)'),
    ('24900', u'Planaltino (BA)'),
    ('24905', u'São João do Caiuá (PR)'),
    ('24906', u'Eugenópolis (MG)'),
    ('24907', u'Jambeiro (SP)'),
    ('25001', u'São João do Ivaí (PR)'),
    ('25002', u'Ewbank da Câmara (MG)'),
    ('25003', u'Jandira (SP)'),
    ('25006', u'Planalto (BA)'),
    ('25100', u'São João do Triunfo (PR)'),
    ('25101', u'Extrema (MG)'),
    ('25102', u'Jardinópolis (SP)'),
    ('25105', u'Poções (BA)'),
    ('25200', u'Fama (MG)'),
    ('25201', u'Jarinu (SP)'),
    ('25204', u'Pojuca (BA)'),
    ('25209', u'São Jorge d`Oeste (PR)'),
    ('25253', u'Ponto Novo (BA)'),
    ('25300', u'Jaú (SP)'),
    ('25303', u'Porto Seguro (BA)'),
    ('25308', u'São Jorge do Ivaí (PR)'),
    ('25309', u'Faria Lemos (MG)'),
    ('25357', u'São Jorge do Patrocínio (PR)'),
    ('25402', u'Potiraguá (BA)'),
    ('25407', u'São José da Boa Vista (PR)'),
    ('25408', u'Felício dos Santos (MG)'),
    ('25409', u'Jeriquara (SP)'),
    ('25456', u'São José das Palmeiras (PR)'),
    ('25501', u'Prado (BA)'),
    ('25506', u'São José dos Pinhais * (PR)'),
    ('25507', u'São Gonçalo do Rio Preto (MG)'),
    ('25508', u'Joanópolis (SP)'),
    ('25555', u'São Manoel do Paraná (PR)'),
    ('25600', u'Presidente Dutra (BA)'),
    ('25605', u'São Mateus do Sul (PR)'),
    ('25606', u'Felisburgo (MG)'),
    ('25607', u'João Ramalho (SP)'),
    ('25704', u'São Miguel do Iguaçu (PR)'),
    ('25705', u'Felixlândia (MG)'),
    ('25706', u'José Bonifácio (SP)'),
    ('25709', u'Presidente Jânio Quadros (BA)'),
    ('25753', u'São Pedro do Iguaçu (PR)'),
    ('25758', u'Presidente Tancredo Neves (BA)'),
    ('25803', u'São Pedro do Ivaí (PR)'),
    ('25804', u'Fernandes Tourinho (MG)'),
    ('25805', u'Júlio Mesquita (SP)'),
    ('25808', u'Queimadas (BA)'),
    ('25854', u'Jumirim (SP)'),
    ('25902', u'São Pedro do Paraná (PR)'),
    ('25903', u'Ferros (MG)'),
    ('25904', u'Jundiaí * (SP)'),
    ('25907', u'Quijingue (BA)'),
    ('25931', u'Quixabeira (BA)'),
    ('25952', u'Fervedouro (MG)'),
    ('25956', u'Rafael Jambeiro (BA)'),
    ('26000', u'Florestal (MG)'),
    ('26001', u'Junqueirópolis (SP)'),
    ('26004', u'Remanso (BA)'),
    ('26009', u'São Sebastião da Amoreira (PR)'),
    ('26100', u'Juquiá (SP)'),
    ('26103', u'Retirolândia (BA)'),
    ('26108', u'São Tomé (PR)'),
    ('26109', u'Formiga (MG)'),
    ('26202', u'Riachão das Neves (BA)'),
    ('26207', u'Sapopema (PR)'),
    ('26208', u'Formoso (MG)'),
    ('26209', u'Juquitiba (SP)'),
    ('26256', u'Sarandi (PR)'),
    ('26272', u'Saudade do Iguaçu (PR)'),
    ('26301', u'Riachão do Jacuípe (BA)'),
    ('26306', u'Sengés (PR)'),
    ('26307', u'Fortaleza de Minas (MG)'),
    ('26308', u'Lagoinha (SP)'),
    ('26355', u'Serranópolis do Iguaçu (PR)'),
    ('26400', u'Riacho de Santana (BA)'),
    ('26405', u'Sertaneja (PR)'),
    ('26406', u'Fortuna de Minas (MG)'),
    ('26407', u'Laranjal Paulista (SP)'),
    ('26504', u'Sertanópolis (PR)'),
    ('26505', u'Francisco Badaró (MG)'),
    ('26506', u'Lavínia (SP)'),
    ('26509', u'Ribeira do Amparo (BA)'),
    ('26603', u'Siqueira Campos (PR)'),
    ('26604', u'Francisco Dumont (MG)'),
    ('26605', u'Lavrinhas (SP)'),
    ('26608', u'Ribeira do Pombal (BA)'),
    ('26652', u'Sulina (PR)'),
    ('26657', u'Ribeirão do Largo (BA)'),
    ('26678', u'Tamarana (PR)'),
    ('26702', u'Tamboara (PR)'),
    ('26703', u'Francisco Sá (MG)'),
    ('26704', u'Leme (SP)'),
    ('26707', u'Rio de Contas (BA)'),
    ('26752', u'Franciscópolis (MG)'),
    ('26801', u'Tapejara (PR)'),
    ('26802', u'Frei Gaspar (MG)'),
    ('26803', u'Lençóis Paulista (SP)'),
    ('26806', u'Rio do Antônio (BA)'),
    ('26900', u'Tapira (PR)'),
    ('26901', u'Frei Inocêncio (MG)'),
    ('26902', u'Limeira * (SP)'),
    ('26905', u'Rio do Pires (BA)'),
    ('26950', u'Frei Lagonegro (MG)'),
    ('27002', u'Rio Real (BA)'),
    ('27007', u'Teixeira Soares (PR)'),
    ('27008', u'Fronteira (MG)'),
    ('27009', u'Lindóia (SP)'),
    ('27057', u'Fronteira dos Vales (MG)'),
    ('27073', u'Fruta de Leite (MG)'),
    ('27101', u'Rodelas (BA)'),
    ('27106', u'Telêmaco Borba (PR)'),
    ('27107', u'Frutal (MG)'),
    ('27108', u'Lins (SP)'),
    ('27200', u'Ruy Barbosa (BA)'),
    ('27205', u'Terra Boa (PR)'),
    ('27206', u'Funilândia (MG)'),
    ('27207', u'Lorena (SP)'),
    ('27256', u'Lourdes (SP)'),
    ('27304', u'Terra Rica (PR)'),
    ('27305', u'Galiléia (MG)'),
    ('27306', u'Louveira (SP)'),
    ('27309', u'Salinas da Margarida (BA)'),
    ('27339', u'Gameleiras (MG)'),
    ('27354', u'Glaucilândia (MG)'),
    ('27370', u'Goiabeira (MG)'),
    ('27388', u'Goianá (MG)'),
    ('27403', u'Terra Roxa (PR)'),
    ('27404', u'Gonçalves (MG)'),
    ('27405', u'Lucélia (SP)'),
    ('27408', u'Salvador * (BA)'),
    ('27502', u'Tibagi (PR)'),
    ('27503', u'Gonzaga (MG)'),
    ('27504', u'Lucianópolis (SP)'),
    ('27507', u'Santa Bárbara (BA)'),
    ('27601', u'Tijucas do Sul (PR)'),
    ('27602', u'Gouveia (MG)'),
    ('27603', u'Luís Antônio (SP)'),
    ('27606', u'Santa Brígida (BA)'),
    ('27700', u'Toledo (PR)'),
    ('27701', u'Governador Valadares * (MG)'),
    ('27702', u'Luiziânia (SP)'),
    ('27705', u'Santa Cruz Cabrália (BA)'),
    ('27800', u'Grão Mogol (MG)'),
    ('27801', u'Lupércio (SP)'),
    ('27804', u'Santa Cruz da Vitória (BA)'),
    ('27809', u'Tomazina (PR)'),
    ('27858', u'Três Barras do Paraná (PR)'),
    ('27882', u'Tunas do Paraná (PR)'),
    ('27900', u'Lutécia (SP)'),
    ('27903', u'Santa Inês (BA)'),
    ('27908', u'Tuneiras do Oeste (PR)'),
    ('27909', u'Grupiara (MG)'),
    ('27957', u'Tupãssi (PR)'),
    ('27965', u'Turvo (PR)'),
    ('28000', u'Santaluz (BA)'),
    ('28005', u'Ubiratã (PR)'),
    ('28006', u'Guanhães (MG)'),
    ('28007', u'Macatuba (SP)'),
    ('28059', u'Santa Luzia (BA)'),
    ('28104', u'Umuarama (PR)'),
    ('28105', u'Guapé (MG)'),
    ('28106', u'Macaubal (SP)'),
    ('28109', u'Santa Maria da Vitória (BA)'),
    ('28203', u'União da Vitória (PR)'),
    ('28204', u'Guaraciaba (MG)'),
    ('28205', u'Macedônia (SP)'),
    ('28208', u'Santana (BA)'),
    ('28253', u'Guaraciama (MG)'),
    ('28302', u'Uniflor (PR)'),
    ('28303', u'Guaranésia (MG)'),
    ('28304', u'Magda (SP)'),
    ('28307', u'Santanópolis (BA)'),
    ('28401', u'Uraí (PR)'),
    ('28402', u'Guarani (MG)'),
    ('28403', u'Mairinque (SP)'),
    ('28406', u'Santa Rita de Cássia (BA)'),
    ('28500', u'Wenceslau Braz (PR)'),
    ('28501', u'Guarará (MG)'),
    ('28502', u'Mairiporã (SP)'),
    ('28505', u'Santa Teresinha (BA)'),
    ('28534', u'Ventania (PR)'),
    ('28559', u'Vera Cruz do Oeste (PR)'),
    ('28600', u'Guarda-Mor (MG)'),
    ('28601', u'Manduri (SP)'),
    ('28604', u'Santo Amaro (BA)'),
    ('28609', u'Verê (PR)'),
    ('28625', u'Alto Paraíso (PR)'),
    ('28633', u'Doutor Ulysses (PR)'),
    ('28658', u'Virmond (PR)'),
    ('28700', u'Marabá Paulista (SP)'),
    ('28703', u'Santo Antônio de Jesus (BA)'),
    ('28708', u'Vitorino (PR)'),
    ('28709', u'Guaxupé (MG)'),
    ('28802', u'Santo Estêvão (BA)'),
    ('28807', u'Xambrê (PR)'),
    ('28808', u'Guidoval (MG)'),
    ('28809', u'Maracaí (SP)'),
    ('28858', u'Marapoama (SP)'),
    ('28901', u'São Desidério (BA)'),
    ('28907', u'Guimarânia (MG)'),
    ('28908', u'Mariápolis (SP)'),
    ('28950', u'São Domingos (BA)'),
    ('29004', u'Guiricema (MG)'),
    ('29005', u'Marília * (SP)'),
    ('29008', u'São Félix (BA)'),
    ('29057', u'São Félix do Coribe (BA)'),
    ('29103', u'Gurinhatã (MG)'),
    ('29104', u'Marinópolis (SP)'),
    ('29107', u'São Felipe (BA)'),
    ('29202', u'Heliodora (MG)'),
    ('29203', u'Martinópolis (SP)'),
    ('29206', u'São Francisco do Conde (BA)'),
    ('29255', u'São Gabriel (BA)'),
    ('29301', u'Iapu (MG)'),
    ('29302', u'Matão (SP)'),
    ('29305', u'São Gonçalo dos Campos (BA)'),
    ('29354', u'São José da Vitória (BA)'),
    ('29370', u'São José do Jacuípe (BA)'),
    ('29400', u'Ibertioga (MG)'),
    ('29401', u'Mauá * (SP)'),
    ('29404', u'São Miguel das Matas (BA)'),
    ('29500', u'Mendonça (SP)'),
    ('29503', u'São Sebastião do Passé (BA)'),
    ('29509', u'Ibiá (MG)'),
    ('29602', u'Sapeaçu (BA)'),
    ('29608', u'Ibiaí (MG)'),
    ('29609', u'Meridiano (SP)'),
    ('29657', u'Ibiracatu (MG)'),
    ('29658', u'Mesópolis (SP)'),
    ('29701', u'Sátiro Dias (BA)'),
    ('29707', u'Ibiraci (MG)'),
    ('29708', u'Miguelópolis (SP)'),
    ('29750', u'Saubara (BA)'),
    ('29800', u'Saúde (BA)'),
    ('29806', u'Ibirité (MG)'),
    ('29807', u'Mineiros do Tietê (SP)'),
    ('29905', u'Ibitiúra de Minas (MG)'),
    ('29906', u'Miracatu (SP)'),
    ('29909', u'Seabra (BA)'),
    ('30002', u'Ibituruna (MG)'),
    ('30003', u'Mira Estrela (SP)'),
    ('30006', u'Sebastião Laranjeiras (BA)'),
    ('30051', u'Icaraí de Minas (MG)'),
    ('30101', u'Igarapé (MG)'),
    ('30102', u'Mirandópolis (SP)'),
    ('30105', u'Senhor do Bonfim (BA)'),
    ('30154', u'Serra do Ramalho (BA)'),
    ('30200', u'Igaratinga (MG)'),
    ('30201', u'Mirante do Paranapanema (SP)'),
    ('30204', u'Sento Sé (BA)'),
    ('30300', u'Mirassol (SP)'),
    ('30303', u'Serra Dourada (BA)'),
    ('30309', u'Iguatama (MG)'),
    ('30402', u'Serra Preta (BA)'),
    ('30408', u'Ijaci (MG)'),
    ('30409', u'Mirassolândia (SP)'),
    ('30501', u'Serrinha (BA)'),
    ('30507', u'Ilicínea (MG)'),
    ('30508', u'Mococa (SP)'),
    ('30556', u'Imbé de Minas (MG)'),
    ('30600', u'Serrolândia (BA)'),
    ('30606', u'Inconfidentes (MG)'),
    ('30607', u'Mogi das Cruzes * (SP)'),
    ('30655', u'Indaiabira (MG)'),
    ('30705', u'Indianópolis (MG)'),
    ('30706', u'Mogi Guaçu (SP)'),
    ('30709', u'Simões Filho (BA)'),
    ('30758', u'Sítio do Mato (BA)'),
    ('30766', u'Sítio do Quinto (BA)'),
    ('30774', u'Sobradinho (BA)'),
    ('30804', u'Ingaí (MG)'),
    ('30805', u'Moji Mirim (SP)'),
    ('30808', u'Souto Soares (BA)'),
    ('30903', u'Inhapim (MG)'),
    ('30904', u'Mombuca (SP)'),
    ('30907', u'Tabocas do Brejo Velho (BA)'),
    ('31000', u'Inhaúma (MG)'),
    ('31001', u'Monções (SP)'),
    ('31004', u'Tanhaçu (BA)'),
    ('31053', u'Tanque Novo (BA)'),
    ('31100', u'Mongaguá (SP)'),
    ('31103', u'Tanquinho (BA)'),
    ('31109', u'Inimutaba (MG)'),
    ('31158', u'Ipaba (MG)'),
    ('31202', u'Taperoá (BA)'),
    ('31208', u'Ipanema (MG)'),
    ('31209', u'Monte Alegre do Sul (SP)'),
    ('31301', u'Tapiramutá (BA)'),
    ('31307', u'Ipatinga * (MG)'),
    ('31308', u'Monte Alto (SP)'),
    ('31350', u'Teixeira de Freitas (BA)'),
    ('31400', u'Teodoro Sampaio (BA)'),
    ('31406', u'Ipiaçu (MG)'),
    ('31407', u'Monte Aprazível (SP)'),
    ('31505', u'Ipuiúna (MG)'),
    ('31506', u'Monte Azul Paulista (SP)'),
    ('31509', u'Teofilândia (BA)'),
    ('31604', u'Iraí de Minas (MG)'),
    ('31605', u'Monte Castelo (SP)'),
    ('31608', u'Teolândia (BA)'),
    ('31703', u'Itabira (MG)'),
    ('31704', u'Monteiro Lobato (SP)'),
    ('31707', u'Terra Nova (BA)'),
    ('31802', u'Itabirinha (MG)'),
    ('31803', u'Monte Mor (SP)'),
    ('31806', u'Tremedal (BA)'),
    ('31901', u'Itabirito (MG)'),
    ('31902', u'Morro Agudo (SP)'),
    ('31905', u'Tucano (BA)'),
    ('32002', u'Uauá (BA)'),
    ('32008', u'Itacambira (MG)'),
    ('32009', u'Morungaba (SP)'),
    ('32058', u'Motuca (SP)'),
    ('32101', u'Ubaíra (BA)'),
    ('32107', u'Itacarambi (MG)'),
    ('32108', u'Murutinga do Sul (SP)'),
    ('32157', u'Nantes (SP)'),
    ('32200', u'Ubaitaba (BA)'),
    ('32206', u'Itaguara (MG)'),
    ('32207', u'Narandiba (SP)'),
    ('32305', u'Itaipé (MG)'),
    ('32306', u'Natividade da Serra (SP)'),
    ('32309', u'Ubatã (BA)'),
    ('32404', u'Itajubá (MG)'),
    ('32405', u'Nazaré Paulista (SP)'),
    ('32408', u'Uibaí (BA)'),
    ('32457', u'Umburanas (BA)'),
    ('32503', u'Itamarandiba (MG)'),
    ('32504', u'Neves Paulista (SP)'),
    ('32507', u'Una (BA)'),
    ('32602', u'Itamarati de Minas (MG)'),
    ('32603', u'Nhandeara (SP)'),
    ('32606', u'Urandi (BA)'),
    ('32701', u'Itambacuri (MG)'),
    ('32702', u'Nipoã (SP)'),
    ('32705', u'Uruçuca (BA)'),
    ('32800', u'Itambé do Mato Dentro (MG)'),
    ('32801', u'Nova Aliança (SP)'),
    ('32804', u'Utinga (BA)'),
    ('32827', u'Nova Campina (SP)'),
    ('32843', u'Nova Canaã Paulista (SP)'),
    ('32868', u'Nova Castilho (SP)'),
    ('32900', u'Nova Europa (SP)'),
    ('32903', u'Valença (BA)'),
    ('32909', u'Itamogi (MG)'),
    ('33000', u'Valente (BA)'),
    ('33006', u'Itamonte (MG)'),
    ('33007', u'Nova Granada (SP)'),
    ('33059', u'Várzea da Roça (BA)'),
    ('33105', u'Itanhandu (MG)'),
    ('33106', u'Nova Guataporanga (SP)'),
    ('33109', u'Várzea do Poço (BA)'),
    ('33158', u'Várzea Nova (BA)'),
    ('33174', u'Varzedo (BA)'),
    ('33204', u'Itanhomi (MG)'),
    ('33205', u'Nova Independência (SP)'),
    ('33208', u'Vera Cruz (BA)'),
    ('33254', u'Novais (SP)'),
    ('33257', u'Vereda (BA)'),
    ('33303', u'Itaobim (MG)'),
    ('33304', u'Nova Luzitânia (SP)'),
    ('33307', u'Vitória da Conquista * (BA)'),
    ('33402', u'Itapagipe (MG)'),
    ('33403', u'Nova Odessa (SP)'),
    ('33406', u'Wagner (BA)'),
    ('33455', u'Wanderley (BA)'),
    ('33501', u'Itapecerica (MG)'),
    ('33502', u'Novo Horizonte (SP)'),
    ('33505', u'Wenceslau Guimarães (BA)'),
    ('33600', u'Itapeva (MG)'),
    ('33601', u'Nuporanga (SP)'),
    ('33604', u'Xique-Xique (BA)'),
    ('33700', u'Ocauçu (SP)'),
    ('33709', u'Itatiaiuçu (MG)'),
    ('33758', u'Itaú de Minas (MG)'),
    ('33808', u'Itaúna (MG)'),
    ('33809', u'Óleo (SP)'),
    ('33907', u'Itaverava (MG)'),
    ('33908', u'Olímpia (SP)'),
    ('34004', u'Itinga (MG)'),
    ('34005', u'Onda Verde (SP)'),
    ('34103', u'Itueta (MG)'),
    ('34104', u'Oriente (SP)'),
    ('34202', u'Ituiutaba (MG)'),
    ('34203', u'Orindiúva (SP)'),
    ('34301', u'Itumirim (MG)'),
    ('34302', u'Orlândia (SP)'),
    ('34400', u'Iturama (MG)'),
    ('34401', u'Osasco * (SP)'),
    ('34500', u'Oscar Bressane (SP)'),
    ('34509', u'Itutinga (MG)'),
    ('34608', u'Jaboticatubas (MG)'),
    ('34609', u'Osvaldo Cruz (SP)'),
    ('34707', u'Jacinto (MG)'),
    ('34708', u'Ourinhos (SP)'),
    ('34757', u'Ouroeste (SP)'),
    ('34806', u'Jacuí (MG)'),
    ('34807', u'Ouro Verde (SP)'),
    ('34905', u'Jacutinga (MG)'),
    ('34906', u'Pacaembu (SP)'),
    ('35001', u'Jaguaraçu (MG)'),
    ('35002', u'Palestina (SP)'),
    ('35050', u'Jaíba (MG)'),
    ('35076', u'Jampruca (MG)'),
    ('35100', u'Janaúba (MG)'),
    ('35101', u'Palmares Paulista (SP)'),
    ('35200', u'Palmeira d`Oeste (SP)'),
    ('35209', u'Januária (MG)'),
    ('35308', u'Japaraíba (MG)'),
    ('35309', u'Palmital (SP)'),
    ('35357', u'Japonvar (MG)'),
    ('35407', u'Jeceaba (MG)'),
    ('35408', u'Panorama (SP)'),
    ('35456', u'Jenipapo de Minas (MG)'),
    ('35506', u'Jequeri (MG)'),
    ('35507', u'Paraguaçu Paulista (SP)'),
    ('35605', u'Jequitaí (MG)'),
    ('35606', u'Paraibuna (SP)'),
    ('35704', u'Jequitibá (MG)'),
    ('35705', u'Paraíso (SP)'),
    ('35803', u'Jequitinhonha (MG)'),
    ('35804', u'Paranapanema (SP)'),
    ('35902', u'Jesuânia (MG)'),
    ('35903', u'Paranapuã (SP)'),
    ('36000', u'Parapuã (SP)'),
    ('36009', u'Joaíma (MG)'),
    ('36108', u'Joanésia (MG)'),
    ('36109', u'Pardinho (SP)'),
    ('36207', u'João Monlevade (MG)'),
    ('36208', u'Pariquera-Açu (SP)'),
    ('36257', u'Parisi (SP)'),
    ('36306', u'João Pinheiro (MG)'),
    ('36307', u'Patrocínio Paulista (SP)'),
    ('36405', u'Joaquim Felício (MG)'),
    ('36406', u'Paulicéia (SP)'),
    ('36504', u'Jordânia (MG)'),
    ('36505', u'Paulínia (SP)'),
    ('36520', u'José Gonçalves de Minas (MG)'),
    ('36553', u'José Raydan (MG)'),
    ('36570', u'Paulistânia (SP)'),
    ('36579', u'Josenópolis (MG)'),
    ('36603', u'Nova União (MG)'),
    ('36604', u'Paulo de Faria (SP)'),
    ('36652', u'Juatuba (MG)'),
    ('36702', u'Juiz de Fora * (MG)'),
    ('36703', u'Pederneiras (SP)'),
    ('36801', u'Juramento (MG)'),
    ('36802', u'Pedra Bela (SP)'),
    ('36900', u'Juruaia (MG)'),
    ('36901', u'Pedranópolis (SP)'),
    ('36959', u'Juvenília (MG)'),
    ('37007', u'Ladainha (MG)'),
    ('37008', u'Pedregulho (SP)'),
    ('37106', u'Lagamar (MG)'),
    ('37107', u'Pedreira (SP)'),
    ('37156', u'Pedrinhas Paulista (SP)'),
    ('37205', u'Lagoa da Prata (MG)'),
    ('37206', u'Pedro de Toledo (SP)'),
    ('37304', u'Lagoa dos Patos (MG)'),
    ('37305', u'Penápolis (SP)'),
    ('37403', u'Lagoa Dourada (MG)'),
    ('37404', u'Pereira Barreto (SP)'),
    ('37502', u'Lagoa Formosa (MG)'),
    ('37503', u'Pereiras (SP)'),
    ('37536', u'Lagoa Grande (MG)'),
    ('37601', u'Lagoa Santa (MG)'),
    ('37602', u'Peruíbe (SP)'),
    ('37700', u'Lajinha (MG)'),
    ('37701', u'Piacatu (SP)'),
    ('37800', u'Piedade (SP)'),
    ('37809', u'Lambari (MG)'),
    ('37908', u'Lamim (MG)'),
    ('37909', u'Pilar do Sul (SP)'),
    ('38005', u'Laranjal (MG)'),
    ('38006', u'Pindamonhangaba (SP)'),
    ('38104', u'Lassance (MG)'),
    ('38105', u'Pindorama (SP)'),
    ('38203', u'Lavras (MG)'),
    ('38204', u'Pinhalzinho (SP)'),
    ('38302', u'Leandro Ferreira (MG)'),
    ('38303', u'Piquerobi (SP)'),
    ('38351', u'Leme do Prado (MG)'),
    ('38401', u'Leopoldina (MG)'),
    ('38500', u'Liberdade (MG)'),
    ('38501', u'Piquete (SP)'),
    ('38600', u'Piracaia (SP)'),
    ('38609', u'Lima Duarte (MG)'),
    ('38625', u'Limeira do Oeste (MG)'),
    ('38658', u'Lontra (MG)'),
    ('38674', u'Luisburgo (MG)'),
    ('38682', u'Luislândia (MG)'),
    ('38708', u'Luminárias (MG)'),
    ('38709', u'Piracicaba * (SP)'),
    ('38807', u'Luz (MG)'),
    ('38808', u'Piraju (SP)'),
    ('38906', u'Machacalis (MG)'),
    ('38907', u'Pirajuí (SP)'),
    ('39003', u'Machado (MG)'),
    ('39004', u'Pirangi (SP)'),
    ('39102', u'Madre de Deus de Minas (MG)'),
    ('39103', u'Pirapora do Bom Jesus (SP)'),
    ('39201', u'Malacacheta (MG)'),
    ('39202', u'Pirapozinho (SP)'),
    ('39250', u'Mamonas (MG)'),
    ('39300', u'Manga (MG)'),
    ('39301', u'Pirassununga (SP)'),
    ('39400', u'Piratininga (SP)'),
    ('39409', u'Manhuaçu (MG)'),
    ('39508', u'Manhumirim (MG)'),
    ('39509', u'Pitangueiras (SP)'),
    ('39607', u'Mantena (MG)'),
    ('39608', u'Planalto (SP)'),
    ('39706', u'Maravilhas (MG)'),
    ('39707', u'Platina (SP)'),
    ('39805', u'Mar de Espanha (MG)'),
    ('39806', u'Poá (SP)'),
    ('39904', u'Maria da Fé (MG)'),
    ('39905', u'Poloni (SP)'),
    ('40001', u'Mariana (MG)'),
    ('40002', u'Pompéia (SP)'),
    ('40100', u'Marilac (MG)'),
    ('40101', u'Pongaí (SP)'),
    ('40159', u'Mário Campos (MG)'),
    ('40200', u'Pontal (SP)'),
    ('40209', u'Maripá de Minas (MG)'),
    ('40259', u'Pontalinda (SP)'),
    ('40308', u'Marliéria (MG)'),
    ('40309', u'Pontes Gestal (SP)'),
    ('40407', u'Marmelópolis (MG)'),
    ('40408', u'Populina (SP)'),
    ('40506', u'Martinho Campos (MG)'),
    ('40507', u'Porangaba (SP)'),
    ('40530', u'Martins Soares (MG)'),
    ('40555', u'Mata Verde (MG)'),
    ('40605', u'Materlândia (MG)'),
    ('40606', u'Porto Feliz (SP)'),
    ('40704', u'Mateus Leme (MG)'),
    ('40705', u'Porto Ferreira (SP)'),
    ('40754', u'Potim (SP)'),
    ('40803', u'Matias Barbosa (MG)'),
    ('40804', u'Potirendaba (SP)'),
    ('40852', u'Matias Cardoso (MG)'),
    ('40853', u'Pracinha (SP)'),
    ('40902', u'Matipó (MG)'),
    ('40903', u'Pradópolis (SP)'),
    ('41000', u'Praia Grande * (SP)'),
    ('41009', u'Mato Verde (MG)'),
    ('41059', u'Pratânia (SP)'),
    ('41108', u'Matozinhos (MG)'),
    ('41109', u'Presidente Alves (SP)'),
    ('41207', u'Matutina (MG)'),
    ('41208', u'Presidente Bernardes (SP)'),
    ('41306', u'Medeiros (MG)'),
    ('41307', u'Presidente Epitácio (SP)'),
    ('41405', u'Medina (MG)'),
    ('41406', u'Presidente Prudente * (SP)'),
    ('41504', u'Mendes Pimentel (MG)'),
    ('41505', u'Presidente Venceslau (SP)'),
    ('41603', u'Mercês (MG)'),
    ('41604', u'Promissão (SP)'),
    ('41653', u'Quadra (SP)'),
    ('41702', u'Mesquita (MG)'),
    ('41703', u'Quatá (SP)'),
    ('41801', u'Minas Novas (MG)'),
    ('41802', u'Queiroz (SP)'),
    ('41900', u'Minduri (MG)'),
    ('41901', u'Queluz (SP)'),
    ('42007', u'Mirabela (MG)'),
    ('42008', u'Quintana (SP)'),
    ('42106', u'Miradouro (MG)'),
    ('42107', u'Rafard (SP)'),
    ('42205', u'Miraí (MG)'),
    ('42206', u'Rancharia (SP)'),
    ('42254', u'Miravânia (MG)'),
    ('42304', u'Moeda (MG)'),
    ('42305', u'Redenção da Serra (SP)'),
    ('42403', u'Moema (MG)'),
    ('42404', u'Regente Feijó (SP)'),
    ('42502', u'Monjolos (MG)'),
    ('42503', u'Reginópolis (SP)'),
    ('42601', u'Monsenhor Paulo (MG)'),
    ('42602', u'Registro (SP)'),
    ('42700', u'Montalvânia (MG)'),
    ('42701', u'Restinga (SP)'),
    ('42800', u'Ribeira (SP)'),
    ('42809', u'Monte Alegre de Minas (MG)'),
    ('42908', u'Monte Azul (MG)'),
    ('42909', u'Ribeirão Bonito (SP)'),
    ('43005', u'Monte Belo (MG)'),
    ('43006', u'Ribeirão Branco (SP)'),
    ('43104', u'Monte Carmelo (MG)'),
    ('43105', u'Ribeirão Corrente (SP)'),
    ('43153', u'Monte Formoso (MG)'),
    ('43203', u'Monte Santo de Minas (MG)'),
    ('43204', u'Ribeirão do Sul (SP)'),
    ('43238', u'Ribeirão dos Índios (SP)'),
    ('43253', u'Ribeirão Grande (SP)'),
    ('43302', u'Montes Claros * (MG)'),
    ('43303', u'Ribeirão Pires (SP)'),
    ('43401', u'Monte Sião (MG)'),
    ('43402', u'Ribeirão Preto * (SP)'),
    ('43450', u'Montezuma (MG)'),
    ('43500', u'Morada Nova de Minas (MG)'),
    ('43501', u'Riversul (SP)'),
    ('43600', u'Rifaina (SP)'),
    ('43609', u'Morro da Garça (MG)'),
    ('43708', u'Morro do Pilar (MG)'),
    ('43709', u'Rincão (SP)'),
    ('43807', u'Munhoz (MG)'),
    ('43808', u'Rinópolis (SP)'),
    ('43906', u'Muriaé (MG)'),
    ('43907', u'Rio Claro * (SP)'),
    ('44003', u'Mutum (MG)'),
    ('44004', u'Rio das Pedras (SP)'),
    ('44102', u'Muzambinho (MG)'),
    ('44103', u'Rio Grande da Serra (SP)'),
    ('44201', u'Nacip Raydan (MG)'),
    ('44202', u'Riolândia (SP)'),
    ('44251', u'Rosana (SP)'),
    ('44300', u'Nanuque (MG)'),
    ('44301', u'Roseira (SP)'),
    ('44359', u'Naque (MG)'),
    ('44375', u'Natalândia (MG)'),
    ('44400', u'Rubiácea (SP)'),
    ('44409', u'Natércia (MG)'),
    ('44508', u'Nazareno (MG)'),
    ('44509', u'Rubinéia (SP)'),
    ('44607', u'Nepomuceno (MG)'),
    ('44608', u'Sabino (SP)'),
    ('44656', u'Ninheira (MG)'),
    ('44672', u'Nova Belém (MG)'),
    ('44706', u'Nova Era (MG)'),
    ('44707', u'Sagres (SP)'),
    ('44805', u'Nova Lima (MG)'),
    ('44806', u'Sales (SP)'),
    ('44904', u'Nova Módica (MG)'),
    ('44905', u'Sales Oliveira (SP)'),
    ('45000', u'Nova Ponte (MG)'),
    ('45001', u'Salesópolis (SP)'),
    ('45059', u'Nova Porteirinha (MG)'),
    ('45100', u'Salmourão (SP)'),
    ('45109', u'Nova Resende (MG)'),
    ('45159', u'Saltinho (SP)'),
    ('45208', u'Nova Serrana (MG)'),
    ('45209', u'Salto (SP)'),
    ('45307', u'Novo Cruzeiro (MG)'),
    ('45308', u'Salto de Pirapora (SP)'),
    ('45356', u'Novo Oriente de Minas (MG)'),
    ('45372', u'Novorizonte (MG)'),
    ('45406', u'Olaria (MG)'),
    ('45407', u'Salto Grande (SP)'),
    ('45455', u'Olhos-d`Água (MG)'),
    ('45505', u'Olímpio Noronha (MG)'),
    ('45506', u'Sandovalina (SP)'),
    ('45604', u'Oliveira (MG)'),
    ('45605', u'Santa Adélia (SP)'),
    ('45703', u'Oliveira Fortes (MG)'),
    ('45704', u'Santa Albertina (SP)'),
    ('45802', u'Onça de Pitangui (MG)'),
    ('45803', u'Santa Bárbara d`Oeste * (SP)'),
    ('45851', u'Oratórios (MG)'),
    ('45877', u'Orizânia (MG)'),
    ('45901', u'Ouro Branco (MG)'),
    ('46008', u'Ouro Fino (MG)'),
    ('46009', u'Santa Branca (SP)'),
    ('46107', u'Ouro Preto (MG)'),
    ('46108', u'Santa Clara d`Oeste (SP)'),
    ('46206', u'Ouro Verde de Minas (MG)'),
    ('46207', u'Santa Cruz da Conceição (SP)'),
    ('46255', u'Padre Carvalho (MG)'),
    ('46256', u'Santa Cruz da Esperança (SP)'),
    ('46305', u'Padre Paraíso (MG)'),
    ('46306', u'Santa Cruz das Palmeiras (SP)'),
    ('46404', u'Paineiras (MG)'),
    ('46405', u'Santa Cruz do Rio Pardo (SP)'),
    ('46503', u'Pains (MG)'),
    ('46504', u'Santa Ernestina (SP)'),
    ('46552', u'Pai Pedro (MG)'),
    ('46602', u'Paiva (MG)'),
    ('46603', u'Santa Fé do Sul (SP)'),
    ('46701', u'Palma (MG)'),
    ('46702', u'Santa Gertrudes (SP)'),
    ('46750', u'Palmópolis (MG)'),
    ('46801', u'Santa Isabel (SP)'),
    ('46900', u'Santa Lúcia (SP)'),
    ('46909', u'Papagaios (MG)'),
    ('47006', u'Paracatu (MG)'),
    ('47007', u'Santa Maria da Serra (SP)'),
    ('47105', u'Pará de Minas (MG)'),
    ('47106', u'Santa Mercedes (SP)'),
    ('47204', u'Paraguaçu (MG)'),
    ('47205', u'Santana da Ponte Pensa (SP)'),
    ('47303', u'Paraisópolis (MG)'),
    ('47304', u'Santana de Parnaíba (SP)'),
    ('47402', u'Paraopeba (MG)'),
    ('47403', u'Santa Rita d`Oeste (SP)'),
    ('47501', u'Passabém (MG)'),
    ('47502', u'Santa Rita do Passa Quatro (SP)'),
    ('47600', u'Passa Quatro (MG)'),
    ('47601', u'Santa Rosa de Viterbo (SP)'),
    ('47650', u'Santa Salete (SP)'),
    ('47700', u'Santo Anastácio (SP)'),
    ('47709', u'Passa Tempo (MG)'),
    ('47808', u'Passa-Vinte (MG)'),
    ('47809', u'Santo André * (SP)'),
    ('47907', u'Passos (MG)'),
    ('47908', u'Santo Antônio da Alegria (SP)'),
    ('47956', u'Patis (MG)'),
    ('48004', u'Patos de Minas (MG)'),
    ('48005', u'Santo Antônio de Posse (SP)'),
    ('48054', u'Santo Antônio do Aracanguá (SP)'),
    ('48103', u'Patrocínio (MG)'),
    ('48104', u'Santo Antônio do Jardim (SP)'),
    ('48202', u'Patrocínio do Muriaé (MG)'),
    ('48203', u'Santo Antônio do Pinhal (SP)'),
    ('48301', u'Paula Cândido (MG)'),
    ('48302', u'Santo Expedito (SP)'),
    ('48400', u'Paulistas (MG)'),
    ('48401', u'Santópolis do Aguapeí (SP)'),
    ('48500', u'Santos * (SP)'),
    ('48509', u'Pavão (MG)'),
    ('48608', u'Peçanha (MG)'),
    ('48609', u'São Bento do Sapucaí (SP)'),
    ('48707', u'Pedra Azul (MG)'),
    ('48708', u'São Bernardo do Campo * (SP)'),
    ('48756', u'Pedra Bonita (MG)'),
    ('48806', u'Pedra do Anta (MG)'),
    ('48807', u'São Caetano do Sul (SP)'),
    ('48905', u'Pedra do Indaiá (MG)'),
    ('48906', u'São Carlos * (SP)'),
    ('49002', u'Pedra Dourada (MG)'),
    ('49003', u'São Francisco (SP)'),
    ('49101', u'Pedralva (MG)'),
    ('49102', u'São João da Boa Vista (SP)'),
    ('49150', u'Pedras de Maria da Cruz (MG)'),
    ('49200', u'Pedrinópolis (MG)'),
    ('49201', u'São João das Duas Pontes (SP)'),
    ('49250', u'São João de Iracema (SP)'),
    ('49300', u'São João do Pau d`Alho (SP)'),
    ('49309', u'Pedro Leopoldo (MG)'),
    ('49408', u'Pedro Teixeira (MG)'),
    ('49409', u'São Joaquim da Barra (SP)'),
    ('49507', u'Pequeri (MG)'),
    ('49508', u'São José da Bela Vista (SP)'),
    ('49606', u'Pequi (MG)'),
    ('49607', u'São José do Barreiro (SP)'),
    ('49705', u'Perdigão (MG)'),
    ('49706', u'São José do Rio Pardo (SP)'),
    ('49804', u'Perdizes (MG)'),
    ('49805', u'São José do Rio Preto * (SP)'),
    ('49903', u'Perdões (MG)'),
    ('49904', u'São José dos Campos * (SP)'),
    ('49952', u'Periquito (MG)'),
    ('49953', u'São Lourenço da Serra (SP)'),
    ('50000', u'Pescador (MG)'),
    ('50001', u'São Luís do Paraitinga (SP)'),
    ('50100', u'São Manuel (SP)'),
    ('50109', u'Piau (MG)'),
    ('50158', u'Piedade de Caratinga (MG)'),
    ('50208', u'Piedade de Ponte Nova (MG)'),
    ('50209', u'São Miguel Arcanjo (SP)'),
    ('50307', u'Piedade do Rio Grande (MG)'),
    ('50308', u'São Paulo * (SP)'),
    ('50406', u'Piedade dos Gerais (MG)'),
    ('50407', u'São Pedro (SP)'),
    ('50505', u'Pimenta (MG)'),
    ('50506', u'São Pedro do Turvo (SP)'),
    ('50539', u'Pingo-d`Água (MG)'),
    ('50570', u'Pintópolis (MG)'),
    ('50604', u'Piracema (MG)'),
    ('50605', u'São Roque (SP)'),
    ('50703', u'Pirajuba (MG)'),
    ('50704', u'São Sebastião (SP)'),
    ('50802', u'Piranga (MG)'),
    ('50803', u'São Sebastião da Grama (SP)'),
    ('50901', u'Piranguçu (MG)'),
    ('50902', u'São Simão (SP)'),
    ('51008', u'Piranguinho (MG)'),
    ('51009', u'São Vicente * (SP)'),
    ('51107', u'Pirapetinga (MG)'),
    ('51108', u'Sarapuí (SP)'),
    ('51206', u'Pirapora (MG)'),
    ('51207', u'Sarutaiá (SP)'),
    ('51305', u'Piraúba (MG)'),
    ('51306', u'Sebastianópolis do Sul (SP)'),
    ('51404', u'Pitangui (MG)'),
    ('51405', u'Serra Azul (SP)'),
    ('51503', u'Piumhi (MG)'),
    ('51504', u'Serrana (SP)'),
    ('51602', u'Planura (MG)'),
    ('51603', u'Serra Negra (SP)'),
    ('51701', u'Poço Fundo (MG)'),
    ('51702', u'Sertãozinho (SP)'),
    ('51800', u'Poços de Caldas (MG)'),
    ('51801', u'Sete Barras (SP)'),
    ('51900', u'Severínia (SP)'),
    ('51909', u'Pocrane (MG)'),
    ('52006', u'Pompéu (MG)'),
    ('52007', u'Silveiras (SP)'),
    ('52105', u'Ponte Nova (MG)'),
    ('52106', u'Socorro (SP)'),
    ('52131', u'Ponto Chique (MG)'),
    ('52170', u'Ponto dos Volantes (MG)'),
    ('52204', u'Porteirinha (MG)'),
    ('52205', u'Sorocaba * (SP)'),
    ('52303', u'Porto Firme (MG)'),
    ('52304', u'Sud Mennucci (SP)'),
    ('52402', u'Poté (MG)'),
    ('52403', u'Sumaré * (SP)'),
    ('52501', u'Pouso Alegre (MG)'),
    ('52502', u'Suzano * (SP)'),
    ('52551', u'Suzanápolis (SP)'),
    ('52600', u'Pouso Alto (MG)'),
    ('52601', u'Tabapuã (SP)'),
    ('52700', u'Tabatinga (SP)'),
    ('52709', u'Prados (MG)'),
    ('52808', u'Prata (MG)'),
    ('52809', u'Taboão da Serra * (SP)'),
    ('52907', u'Pratápolis (MG)'),
    ('52908', u'Taciba (SP)'),
    ('53004', u'Pratinha (MG)'),
    ('53005', u'Taguaí (SP)'),
    ('53103', u'Presidente Bernardes (MG)'),
    ('53104', u'Taiaçu (SP)'),
    ('53202', u'Presidente Juscelino (MG)'),
    ('53203', u'Taiúva (SP)'),
    ('53301', u'Presidente Kubitschek (MG)'),
    ('53302', u'Tambaú (SP)'),
    ('53400', u'Presidente Olegário (MG)'),
    ('53401', u'Tanabi (SP)'),
    ('53500', u'Tapiraí (SP)'),
    ('53509', u'Alto Jequitibá (MG)'),
    ('53608', u'Prudente de Morais (MG)'),
    ('53609', u'Tapiratiba (SP)'),
    ('53658', u'Taquaral (SP)'),
    ('53707', u'Quartel Geral (MG)'),
    ('53708', u'Taquaritinga (SP)'),
    ('53806', u'Queluzito (MG)'),
    ('53807', u'Taquarituba (SP)'),
    ('53856', u'Taquarivaí (SP)'),
    ('53905', u'Raposos (MG)'),
    ('53906', u'Tarabai (SP)'),
    ('53955', u'Tarumã (SP)'),
    ('54002', u'Raul Soares (MG)'),
    ('54003', u'Tatuí (SP)'),
    ('54101', u'Recreio (MG)'),
    ('54102', u'Taubaté * (SP)'),
    ('54150', u'Reduto (MG)'),
    ('54200', u'Resende Costa (MG)'),
    ('54201', u'Tejupá (SP)'),
    ('54300', u'Teodoro Sampaio (SP)'),
    ('54309', u'Resplendor (MG)'),
    ('54408', u'Ressaquinha (MG)'),
    ('54409', u'Terra Roxa (SP)'),
    ('54457', u'Riachinho (MG)'),
    ('54507', u'Riacho dos Machados (MG)'),
    ('54508', u'Tietê (SP)'),
    ('54606', u'Ribeirão das Neves * (MG)'),
    ('54607', u'Timburi (SP)'),
    ('54656', u'Torre de Pedra (SP)'),
    ('54705', u'Ribeirão Vermelho (MG)'),
    ('54706', u'Torrinha (SP)'),
    ('54755', u'Trabiju (SP)'),
    ('54804', u'Rio Acima (MG)'),
    ('54805', u'Tremembé (SP)'),
    ('54903', u'Rio Casca (MG)'),
    ('54904', u'Três Fronteiras (SP)'),
    ('54953', u'Tuiuti (SP)'),
    ('55000', u'Tupã (SP)'),
    ('55009', u'Rio Doce (MG)'),
    ('55108', u'Rio do Prado (MG)'),
    ('55109', u'Tupi Paulista (SP)'),
    ('55207', u'Rio Espera (MG)'),
    ('55208', u'Turiúba (SP)'),
    ('55306', u'Rio Manso (MG)'),
    ('55307', u'Turmalina (SP)'),
    ('55356', u'Ubarana (SP)'),
    ('55405', u'Rio Novo (MG)'),
    ('55406', u'Ubatuba (SP)'),
    ('55504', u'Rio Paranaíba (MG)'),
    ('55505', u'Ubirajara (SP)'),
    ('55603', u'Rio Pardo de Minas (MG)'),
    ('55604', u'Uchoa (SP)'),
    ('55702', u'Rio Piracicaba (MG)'),
    ('55703', u'União Paulista (SP)'),
    ('55801', u'Rio Pomba (MG)'),
    ('55802', u'Urânia (SP)'),
    ('55900', u'Rio Preto (MG)'),
    ('55901', u'Uru (SP)'),
    ('56007', u'Rio Vermelho (MG)'),
    ('56008', u'Urupês (SP)'),
    ('56106', u'Ritápolis (MG)'),
    ('56107', u'Valentim Gentil (SP)'),
    ('56205', u'Rochedo de Minas (MG)'),
    ('56206', u'Valinhos (SP)'),
    ('56304', u'Rodeiro (MG)'),
    ('56305', u'Valparaíso (SP)'),
    ('56354', u'Vargem (SP)'),
    ('56403', u'Romaria (MG)'),
    ('56404', u'Vargem Grande do Sul (SP)'),
    ('56452', u'Rosário da Limeira (MG)'),
    ('56453', u'Vargem Grande Paulista (SP)'),
    ('56502', u'Rubelita (MG)'),
    ('56503', u'Várzea Paulista (SP)'),
    ('56601', u'Rubim (MG)'),
    ('56602', u'Vera Cruz (SP)'),
    ('56700', u'Sabará (MG)'),
    ('56701', u'Vinhedo (SP)'),
    ('56800', u'Viradouro (SP)'),
    ('56809', u'Sabinópolis (MG)'),
    ('56908', u'Sacramento (MG)'),
    ('56909', u'Vista Alegre do Alto (SP)'),
    ('56958', u'Vitória Brasil (SP)'),
    ('57005', u'Salinas (MG)'),
    ('57006', u'Votorantim (SP)'),
    ('57104', u'Salto da Divisa (MG)'),
    ('57105', u'Votuporanga (SP)'),
    ('57154', u'Zacarias (SP)'),
    ('57203', u'Santa Bárbara (MG)'),
    ('57204', u'Chavantes (SP)'),
    ('57252', u'Santa Bárbara do Leste (MG)'),
    ('57278', u'Santa Bárbara do Monte Verde (MG)'),
    ('57302', u'Santa Bárbara do Tugúrio (MG)'),
    ('57303', u'Estiva Gerbi (SP)'),
    ('57336', u'Santa Cruz de Minas (MG)'),
    ('57377', u'Santa Cruz de Salinas (MG)'),
    ('57401', u'Santa Cruz do Escalvado (MG)'),
    ('57500', u'Santa Efigênia de Minas (MG)'),
    ('57609', u'Santa Fé de Minas (MG)'),
    ('57658', u'Santa Helena de Minas (MG)'),
    ('57708', u'Santa Juliana (MG)'),
    ('57807', u'Santa Luzia * (MG)'),
    ('57906', u'Santa Margarida (MG)'),
    ('58003', u'Santa Maria de Itabira (MG)'),
    ('58102', u'Santa Maria do Salto (MG)'),
    ('58201', u'Santa Maria do Suaçuí (MG)'),
    ('58300', u'Santana da Vargem (MG)'),
    ('58409', u'Santana de Cataguases (MG)'),
    ('58508', u'Santana de Pirapama (MG)'),
    ('58607', u'Santana do Deserto (MG)'),
    ('58706', u'Santana do Garambéu (MG)'),
    ('58805', u'Santana do Jacaré (MG)'),
    ('58904', u'Santana do Manhuaçu (MG)'),
    ('58953', u'Santana do Paraíso (MG)'),
    ('59001', u'Santana do Riacho (MG)'),
    ('59100', u'Santana dos Montes (MG)'),
    ('59209', u'Santa Rita de Caldas (MG)'),
    ('59308', u'Santa Rita de Jacutinga (MG)'),
    ('59357', u'Santa Rita de Minas (MG)'),
    ('59407', u'Santa Rita de Ibitipoca (MG)'),
    ('59506', u'Santa Rita do Itueto (MG)'),
    ('59605', u'Santa Rita do Sapucaí (MG)'),
    ('59704', u'Santa Rosa da Serra (MG)'),
    ('59803', u'Santa Vitória (MG)'),
    ('59902', u'Santo Antônio do Amparo (MG)'),
    ('60009', u'Santo Antônio do Aventureiro (MG)'),
    ('60108', u'Santo Antônio do Grama (MG)'),
    ('60207', u'Santo Antônio do Itambé (MG)'),
    ('60306', u'Santo Antônio do Jacinto (MG)'),
    ('60405', u'Santo Antônio do Monte (MG)'),
    ('60454', u'Santo Antônio do Retiro (MG)'),
    ('60504', u'Santo Antônio do Rio Abaixo (MG)'),
    ('60603', u'Santo Hipólito (MG)'),
    ('60702', u'Santos Dumont (MG)'),
    ('60801', u'São Bento Abade (MG)'),
    ('60900', u'São Brás do Suaçuí (MG)'),
    ('60959', u'São Domingos das Dores (MG)'),
    ('61007', u'São Domingos do Prata (MG)'),
    ('61056', u'São Félix de Minas (MG)'),
    ('61106', u'São Francisco (MG)'),
    ('61205', u'São Francisco de Paula (MG)'),
    ('61304', u'São Francisco de Sales (MG)'),
    ('61403', u'São Francisco do Glória (MG)'),
    ('61502', u'São Geraldo (MG)'),
    ('61601', u'São Geraldo da Piedade (MG)'),
    ('61650', u'São Geraldo do Baixio (MG)'),
    ('61700', u'São Gonçalo do Abaeté (MG)'),
    ('61809', u'São Gonçalo do Pará (MG)'),
    ('61908', u'São Gonçalo do Rio Abaixo (MG)'),
    ('62005', u'São Gonçalo do Sapucaí (MG)'),
    ('62104', u'São Gotardo (MG)'),
    ('62203', u'São João Batista do Glória (MG)'),
    ('62252', u'São João da Lagoa (MG)'),
    ('62302', u'São João da Mata (MG)'),
    ('62401', u'São João da Ponte (MG)'),
    ('62450', u'São João das Missões (MG)'),
    ('62500', u'São João del Rei (MG)'),
    ('62559', u'São João do Manhuaçu (MG)'),
    ('62575', u'São João do Manteninha (MG)'),
    ('62609', u'São João do Oriente (MG)'),
    ('62658', u'São João do Pacuí (MG)'),
    ('62708', u'São João do Paraíso (MG)'),
    ('62807', u'São João Evangelista (MG)'),
    ('62906', u'São João Nepomuceno (MG)'),
    ('62922', u'São Joaquim de Bicas (MG)'),
    ('62948', u'São José da Barra (MG)'),
    ('62955', u'São José da Lapa (MG)'),
    ('63003', u'São José da Safira (MG)'),
    ('63102', u'São José da Varginha (MG)'),
    ('63201', u'São José do Alegre (MG)'),
    ('63300', u'São José do Divino (MG)'),
    ('63409', u'São José do Goiabal (MG)'),
    ('63508', u'São José do Jacuri (MG)'),
    ('63607', u'São José do Mantimento (MG)'),
    ('63706', u'São Lourenço (MG)'),
    ('63805', u'São Miguel do Anta (MG)'),
    ('63904', u'São Pedro da União (MG)'),
    ('64001', u'São Pedro dos Ferros (MG)'),
    ('64100', u'São Pedro do Suaçuí (MG)'),
    ('64209', u'São Romão (MG)'),
    ('64308', u'São Roque de Minas (MG)'),
    ('64407', u'São Sebastião da Bela Vista (MG)'),
    ('64431', u'São Sebastião da Vargem Alegre (MG)'),
    ('64472', u'São Sebastião do Anta (MG)'),
    ('64506', u'São Sebastião do Maranhão (MG)'),
    ('64605', u'São Sebastião do Oeste (MG)'),
    ('64704', u'São Sebastião do Paraíso (MG)'),
    ('64803', u'São Sebastião do Rio Preto (MG)'),
    ('64902', u'São Sebastião do Rio Verde (MG)'),
    ('65008', u'São Tiago (MG)'),
    ('65107', u'São Tomás de Aquino (MG)'),
    ('65206', u'São Thomé das Letras (MG)'),
    ('65305', u'São Vicente de Minas (MG)'),
    ('65404', u'Sapucaí-Mirim (MG)'),
    ('65503', u'Sardoá (MG)'),
    ('65537', u'Sarzedo (MG)'),
    ('65552', u'Setubinha (MG)'),
    ('65560', u'Sem-Peixe (MG)'),
    ('65578', u'Senador Amaral (MG)'),
    ('65602', u'Senador Cortes (MG)'),
    ('65701', u'Senador Firmino (MG)'),
    ('65800', u'Senador José Bento (MG)'),
    ('65909', u'Senador Modestino Gonçalves (MG)'),
    ('66006', u'Senhora de Oliveira (MG)'),
    ('66105', u'Senhora do Porto (MG)'),
    ('66204', u'Senhora dos Remédios (MG)'),
    ('66303', u'Sericita (MG)'),
    ('66402', u'Seritinga (MG)'),
    ('66501', u'Serra Azul de Minas (MG)'),
    ('66600', u'Serra da Saudade (MG)'),
    ('66709', u'Serra dos Aimorés (MG)'),
    ('66808', u'Serra do Salitre (MG)'),
    ('66907', u'Serrania (MG)'),
    ('66956', u'Serranópolis de Minas (MG)'),
    ('67004', u'Serranos (MG)'),
    ('67103', u'Serro (MG)'),
    ('67202', u'Sete Lagoas * (MG)'),
    ('67301', u'Silveirânia (MG)'),
    ('67400', u'Silvianópolis (MG)'),
    ('67509', u'Simão Pereira (MG)'),
    ('67608', u'Simonésia (MG)'),
    ('67707', u'Sobrália (MG)'),
    ('67806', u'Soledade de Minas (MG)'),
    ('67905', u'Tabuleiro (MG)'),
    ('68002', u'Taiobeiras (MG)'),
    ('68051', u'Taparuba (MG)'),
    ('68101', u'Tapira (MG)'),
    ('68200', u'Tapiraí (MG)'),
    ('68309', u'Taquaraçu de Minas (MG)'),
    ('68408', u'Tarumirim (MG)'),
    ('68507', u'Teixeiras (MG)'),
    ('68606', u'Teófilo Otoni (MG)'),
    ('68705', u'Timóteo (MG)'),
    ('68804', u'Tiradentes (MG)'),
    ('68903', u'Tiros (MG)'),
    ('69000', u'Tocantins (MG)'),
    ('69059', u'Tocos do Moji (MG)'),
    ('69109', u'Toledo (MG)'),
    ('69208', u'Tombos (MG)'),
    ('69307', u'Três Corações (MG)'),
    ('69356', u'Três Marias (MG)'),
    ('69406', u'Três Pontas (MG)'),
    ('69505', u'Tumiritinga (MG)'),
    ('69604', u'Tupaciguara (MG)'),
    ('69703', u'Turmalina (MG)'),
    ('69802', u'Turvolândia (MG)'),
    ('69901', u'Ubá (MG)'),
    ('70008', u'Ubaí (MG)'),
    ('70057', u'Ubaporanga (MG)'),
    ('70107', u'Uberaba * (MG)'),
    ('70206', u'Uberlândia * (MG)'),
    ('70305', u'Umburatiba (MG)'),
    ('70404', u'Unaí (MG)'),
    ('70438', u'União de Minas (MG)'),
    ('70479', u'Uruana de Minas (MG)'),
    ('70503', u'Urucânia (MG)'),
    ('70529', u'Urucuia (MG)'),
    ('70578', u'Vargem Alegre (MG)'),
    ('70602', u'Vargem Bonita (MG)'),
    ('70651', u'Vargem Grande do Rio Pardo (MG)'),
    ('70701', u'Varginha (MG)'),
    ('70750', u'Varjão de Minas (MG)'),
    ('70800', u'Várzea da Palma (MG)'),
    ('70909', u'Varzelândia (MG)'),
    ('71006', u'Vazante (MG)'),
    ('71030', u'Verdelândia (MG)'),
    ('71071', u'Veredinha (MG)'),
    ('71105', u'Veríssimo (MG)'),
    ('71154', u'Vermelho Novo (MG)'),
    ('71204', u'Vespasiano (MG)'),
    ('71303', u'Viçosa (MG)'),
    ('71402', u'Vieiras (MG)'),
    ('71501', u'Mathias Lobato (MG)'),
    ('71600', u'Virgem da Lapa (MG)'),
    ('71709', u'Virgínia (MG)'),
    ('71808', u'Virginópolis (MG)'),
    ('71907', u'Virgolândia (MG)'),
    ('72004', u'Visconde do Rio Branco (MG)'),
    ('72103', u'Volta Grande (MG)'),
    ('72202', u'Wenceslau Braz (MG)'),
)

CHOICES_S2400_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1260_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S3000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1299_EVTAQPROD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2299_PENSALIM = (
    (0, u'0 - Não existe pensão alimentícia'),
    (1, u'1 - Percentual de pensão alimentícia'),
    (2, u'2 - Valor de pensão alimentícia'),
    (3, u'3 - Percentual e valor de pensão alimentícia'),
)

CHOICES_S2400_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1200_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1300_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2206_TPINSC = (
)

CHOICES_S2399_CODCATEG = (
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

CHOICES_S1300_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1295_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1202_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2200_INDPRIEMPR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1030_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2230_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1207_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1050_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S3000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1250_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2300_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2306_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1080_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1280_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S2250_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S3000_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S5011_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1030_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2210_TPCAT = (
    (1, u'1 - Inicial'),
    (2, u'2 - Reabertura'),
    (3, u'3 - Comunicação de Óbito'),
)

CHOICES_S2230_CODCATEG = (
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

CHOICES_S1000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2206_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2220_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2241_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2299_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2300_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2399_MTVDESLIGTSV = (
    ('01', u'01 - Exoneração do Diretor Não Empregado sem justa causa, por deliberação da assembleia, dos sócios cotistas ou da autoridade competente'),
    ('02', u'02 - Término de Mandato do Diretor Não Empregado que não tenha sido reconduzido ao cargo'),
    ('03', u'03 - Exoneração a pedido de Diretor Não Empregado'),
    ('04', u'04 - Exoneração do Diretor Não Empregado por culpa recíproca ou força maior'),
    ('05', u'05 - Morte do Diretor Não Empregado'),
    ('06', u'06 - Exoneração do Diretor Não Empregado por falência, encerramento ou supressão de parte da empresa'),
    ('99', u'99 - Outros'),
)

CHOICES_S1035_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1010_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1270_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1280_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1040_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1080_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2260_INDLOCAL = (
    (0, u'0 - Prestação de serviços no estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (1, u'1 - Prestação de serviços em apenas um local e fora do estabelecimento informado no grupo {localTrabGeral} do S-2200 ou S-2206, quando for o caso'),
    (2, u'2 - Prestação de serviços de natureza externa ou em mais de um local'),
)

CHOICES_S2206_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

CHOICES_S2299_INDCUMPRPARC = (
    (0, u'0 - Cumprimento total'),
    (1, u'1 - Cumprimento parcial em razão de obtenção de novo emprego pelo empregado'),
    (2, u'2 - Cumprimento parcial por iniciativa do empregador'),
    (3, u'3 - Outras hipóteses de cumprimento parcial do aviso prévio'),
    (4, u'4 - Aviso prévio indenizado ou não exigível'),
)

CHOICES_S1270_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2400_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2206_TPREGPREV = (
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior'),
)

CHOICES_S2299_MTVDESLIG = (
    ('01', u'01 - Rescisão com justa causa, por iniciativa do empregador'),
    ('02', u'02 - Rescisão sem justa causa, por iniciativa do empregador'),
    ('03', u'03 - Rescisão antecipada do contrato a termo por iniciativa do empregador'),
    ('04', u'04 - Rescisão antecipada do contrato a termo por iniciativa do empregado'),
    ('05', u'05 - Rescisão por culpa recíproca'),
    ('06', u'06 - Rescisão por término do contrato a termo'),
    ('07', u'07 - Rescisão do contrato de trabalho por iniciativa do empregado'),
    ('08', u'08 - Rescisão do contrato de trabalho por interesse do(a) empregado(a), nas hipóteses previstas nos arts. 394 e 483, § 1º da CLT'),
    ('09', u'09 - Rescisão por falecimento do empregador individual ou empregador doméstico por opção do empregado'),
    ('10', u'10 - Rescisão por falecimento do empregado'),
    ('11', u'11 - Transferência de empregado para empresa do mesmo grupo empresarial que tenha assumido os encargos trabalhistas, sem que tenha havido rescisão do contrato de trabalho'),
    ('12', u'12 - Transferência de empregado da empresa consorciada para o consórcio que tenha assumido os encargos trabalhistas, e vice-versa, sem que tenha havido rescisão do contrato de trabalho'),
    ('13', u'13 - Transferência de empregado de empresa ou consórcio, para outra empresa ou consórcio que tenha assumido os encargos trabalhistas por motivo de sucessão (fusão, cisão ou incorporação), sem que tenha havido rescisão do contrato de trabalho'),
    ('14', u'14 - Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades ou falecimento do empregador individual ou empregador doméstico sem continuação da atividade'),
    ('15', u'15 - Demissão de Aprendizes por Desempenho Insuficiente ou Inadaptação'),
    ('16', u'16 - Declaração de nulidade do contrato de trabalho por infringência ao inciso II do art. 37 da Constituição Federal, quando mantido o direito ao salário'),
    ('17', u'17 - Rescisão Indireta do Contrato de Trabalho'),
    ('18', u'18 - Aposentadoria Compulsória (somente para categorias de trabalhadores 301 a 309)'),
    ('19', u'19 - Aposentadoria por idade (somente para categorias de trabalhadores 301 a 309)'),
    ('20', u'20 - Aposentadoria por idade e tempo de contribuição (somente categorias 301 a 309)'),
    ('21', u'21 - Reforma Militar (somente para categorias de trabalhadores 301 a 309)'),
    ('22', u'22 - Reserva Militar (somente para categorias de trabalhadores 301 a 309)'),
    ('23', u'23 - Exoneração (somente para categorias de trabalhadores 301 a 309)'),
    ('24', u'24 - Demissão (somente para categorias de trabalhadores 301 a 309)'),
    ('25', u'25 - Vacância para assumir outro cargo efetivo (somente para categorias de trabalhadores 301 a 309)'),
    ('26', u'26 - Rescisão do contrato de trabalho por paralisação temporária ou definitiva da empresa, estabelecimento ou parte das atividades motivada por atos de autoridade municipal, estadual ou federal'),
    ('27', u'27 - Rescisão por motivo de força maior'),
    ('28', u'28 - Término da Cessão/Requisição'),
    ('29', u'29 - Redistribuição'),
    ('30', u'30 - Mudança de Regime Trabalhista'),
    ('31', u'31 - Reversão de Reintegração'),
    ('32', u'32 - Extravio de Militar'),
    ('33', u'33 - Rescisão por acordo entre as partes (art. 484-A da CLT)'),
    ('34', u'34 - Transferência de titularidade do empregado doméstico para outro representante da mesma unidade familiar'),
)

CHOICES_S2298_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1299_EVTCOMPROD = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2298_TPREINT = (
    (1, u'1 - Reintegração por Decisão Judicial'),
    (2, u'2 - Reintegração por Anistia Legal'),
    (3, u'3 - Reversão de Servidor Público'),
    (4, u'4 - Recondução de Servidor Público'),
    (5, u'5 - Reinclusão de Militar'),
    (9, u'9 - Outros'),
)

CHOICES_S1260_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2250_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2298_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1000_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2300_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S5001_TPINSC = (
)

CHOICES_S1050_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2200_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2399_TPINSC = (
)

ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

CHOICES_S1020_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2306_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2220_RESASO = (
    (1, u'1 - Apto'),
    (2, u'2 - Inapto'),
)

CHOICES_S2230_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2230_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1300_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual'),
)

CHOICES_S1299_EVTPGTOS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2230_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1070_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S1250_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2241_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5012_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

TIPO_OCORRENCIA = (
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
)

CHOICES_S2260_INDRETIF = (
    (1, u'1 - arquivo original'),
    (2, u'2 - arquivo de retificação'),
)

CHOICES_S1060_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2260_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2306_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5002_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1202_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1010_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2205_ESTCIV = (
    (1, u'1 - Solteiro'),
    (2, u'2 - Casado'),
    (3, u'3 - Divorciado'),
    (4, u'4 - Separado'),
    (5, u'5 - Viúvo'),
)

CHOICES_S2306_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

TIPO_AMBIENTE = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

EVENTOS_VERSOES = (
    ('v02_04_01', u'Versão 2.04.01'),
    ('v02_04_02', u'Versão 2.04.02'),
)

CHOICES_S2205_RACACOR = (
    (1, u'1 - Branca'),
    (2, u'2 - Negra'),
    (3, u'3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)'),
    (4, u'4 - Amarela (de origem japonesa, chinesa, coreana etc)'),
    (5, u'5 - Indígena'),
    (6, u'6 - Não informado'),
)

CHOICES_S2299_INDPAGTOAPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1299_EVTCONTRATAVNP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2220_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_CADINI = (
    ('N', u'N - Não (Admissão)'),
    ('S', u'S - Sim (Cadastramento Inicial)'),
)

CHOICES_S2210_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2241_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

OPERACOES = (
    (1, u'Incluir'),
    (2, u'Alterar'),
    (3, u'Excluir'),
)

CHOICES_S5011_INDEXISTINFO = (
    (1, u'1 - Há informações com apuração de contribuições sociais'),
    (2, u'2 - Há movimento porém sem apuração de contribuições sociais'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
)

CHOICES_S2200_TPREGTRAB = (
    (1, u'1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas'),
    (2, u'2 - Estatutário'),
)

CHOICES_S2210_INICIATCAT = (
    (1, u'1 - Iniciativa do Registrador (identificado em {ideRegistrador})'),
    (2, u'2 - Ordem judicial'),
    (3, u'3 - Determinação de órgão fiscalizador'),
)

CHOICES_S2250_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2399_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

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

CHOICES_S2206_TPCONTR = (
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado'),
)

CHOICES_S2300_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S1270_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2298_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2300_CODCATEG = (
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

CHOICES_S1250_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1299_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S2210_TPINSC = (
)

CHOICES_S1299_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2210_TPLOCAL = (
    (1, u'1 - Estabelecimento do empregador no Brasil'),
    (2, u'2 - Estabelecimento do empregador no Exterior'),
    (3, u'3 - Estabelecimento de terceiros onde o empregador presta serviços'),
    (4, u'4 - Via pública'),
    (5, u'5 - Área rural'),
    (6, u'6 - Embarcação'),
    (9, u'9 - Outros'),
)

CHOICES_S2241_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1300_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S1280_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1035_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_CLAUASSEC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2399_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1040_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1260_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S5001_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1250_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S1295_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2205_SEXO = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2206_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2210_PAIS = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S2190_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S3000_TPEVENTO = (
    ('S', u'S-5012 - Informações do IRRF consolidadas por Contribuinte'),
    ('S', u'S-5011 - Informações das contribuições sociais consolidadas por contribuinte'),
    ('S', u'S-5002 - Imposto de Renda Retido na Fonte por Trabalhador'),
    ('S', u'S-5001 - Informações das contribuições sociais por Trabalhador'),
    ('S', u'S-3000 - Exclusão de Eventos'),
    ('S', u'S-2400 - Cadastro de Beneficios Previdenciários - RPPS'),
    ('S', u'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'),
    ('S', u'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'),
    ('S', u'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'),
    ('S', u'S-2299 - Desligamento'),
    ('S', u'S-2298 - Reintegração'),
    ('S', u'S-2260 - Convocação para Trabalho Intermitente'),
    ('S', u'S-2250 - Aviso Prévio'),
    ('S', u'S-2241 - Insalubridade/Periculosidade/Aposentadoria Especial'),
    ('S', u'S-2240 - Condições Ambientais do Trabalho - Fatores de Risco'),
    ('S', u'S-2230 - Afastamento Temporário'),
    ('S', u'S-2220 - Monitoramento da saúde do trabalhador'),
    ('S', u'S-2210 - Comunicação de Acidente de Trabalho'),
    ('S', u'S-2206 - Alteração de Contrato de Trabalho'),
    ('S', u'S-2205 - Alteração de Dados Cadastrais do Trabalhador'),
    ('S', u'S-2200 - Admissão / Ingresso de Trabalhador'),
    ('S', u'S-2190 - Admissão de Trabalhador - Registro Preliminar'),
    ('S', u'S-1300 - Contribuição Sindical Patronal'),
    ('S', u'S-1299 - Fechamento dos Eventos Periódicos'),
    ('S', u'S-1298 - Reabertura dos Eventos Periódicos'),
    ('S', u'S-1295 - Solicitação de Totalização para Pagamento em Contingência'),
    ('S', u'S-1280 - Informações Complementares aos Eventos Periódicos'),
    ('S', u'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'),
    ('S', u'S-1260 - Comercialização da Produção Rural Pessoa Física'),
    ('S', u'S-1250 - Aquisição de Produção Rural'),
    ('S', u'S-1210 - Pagamentos de Rendimentos do Trabalho'),
    ('S', u'S-1207 - Benefícios Previdenciários - RPPS'),
    ('S', u'S-1202 - Remuneração do Trabalhador vinculado a Regime Próprio de Previdência Social - RPPS'),
    ('S', u'S-1200 - Remuneração do Trabalhador vinculado ao Regime Geral de Previdência Social - RGPS'),
    ('S', u'S-1080 - Tabela de Operadores Portuários'),
    ('S', u'S-1070 - Tabela de Processos Administrativos/Judiciais'),
    ('S', u'S-1060 - Tabela de Ambientes de Trabalho'),
    ('S', u'S-1050 - Tabela de Horários/Turnos de Trabalho'),
    ('S', u'S-1040 - Tabela de Funções/Cargos em Comissão'),
    ('S', u'S-1035 - Tabela de Carreiras Públicas'),
    ('S', u'S-1030 - Tabela de Cargos/Empregos Públicos'),
    ('S', u'S-1020 - Tabela de Lotações Tributárias'),
    ('S', u'S-1010 - Tabela de Rubricas'),
    ('S', u'S-1005 - Tabela de Estabelecimentos, Obras de Construção Civil ou Unidades de Órgãos Públicos'),
    ('S', u'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'),
)

CHOICES_S1202_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S1000_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2200_GRAUINSTR = (
    ('01', u'01 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou'),
    ('02', u'02 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular'),
    ('03', u'03 - 5º ano completo do Ensino Fundamental'),
    ('04', u'04 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)'),
    ('05', u'05 - Ensino Fundamental Completo'),
    ('06', u'06 - Ensino Médio incompleto'),
    ('07', u'07 - Ensino Médio completo'),
    ('08', u'08 - Educação Superior incompleta'),
    ('09', u'09 - Educação Superior completa'),
    ('10', u'10 - Pós-Graduação completa'),
    ('11', u'11 - Mestrado completo'),
    ('12', u'12 - Doutorado completo'),
)

CHOICES_S1207_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

CHOICES_S2205_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2210_TPACID = (
    ('1.0.01', u'1.0.01 - Lesão corporal que cause a morte ou a perda ou redução, permanente ou temporária, da capacidade para o trabalho, desde que não enquadrada em nenhum dos demais códigos.'),
    ('1.0.02', u'1.0.02 - Perturbação funcional que cause a morte ou a perda ou redução, permanente ou temporária, da capacidade para o trabalho, desde que não enquadrada em nenhum dos demais códigos.'),
    ('2.0.01', u'2.0.01 - Doença profissional, assim entendida a produzida ou desencadeada pelo exercício do trabalho peculiar a determinada atividade e constante da respectiva relação elaborada pelo Ministério do Trabalho e Previdência Social, desde que não enquadrada em nenhum dos demais códigos.'),
    ('2.0.02', u'2.0.02 - Doença do trabalho, assim entendida a adquirida ou desencadeada em função de condições especiais em que o trabalho é realizado e com ele se relacione diretamente, constante da respectiva relação elaborada pelo Ministério do Trabalho e Previdência Social, desde que não enquadrada em nenhum dos demais códigos.'),
    ('2.0.03', u'2.0.03 - Doença proveniente de contaminação acidental do empregado no exercício de sua atividade.'),
    ('2.0.04', u'2.0.04 - Doença endêmica adquirida por segurado habitante de região em que ela se desenvolva quando resultante de exposição ou contato direto determinado pela natureza do trabalho.'),
    ('2.0.05', u'2.0.05 - Doença profissional ou do trabalho não incluída na relação elaborada pelo Ministério do Trabalho e Previdência Social quando resultante das condições especiais em que o trabalho é executado e com ele se relaciona diretamente.'),
    ('2.0.06', u'2.0.06 - Doença profissional ou do trabalho enquadrada na relação elaborada pelo Ministério do Trabalho e Previdência Social relativa nexo técnico epidemiológico previdenciário - NTEP.'),
    ('3.0.01', u'3.0.01 - Acidente ligado ao trabalho que, embora não tenha sido a causa única, haja contribuído diretamente para a morte do segurado, para redução ou perda da sua capacidade para o trabalho, ou produzido lesão que exija atenção médica para a sua recuperação.'),
    ('3.0.02', u'3.0.02 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de agressão, sabotagem ou terrorismo praticado por terceiro ou companheiro de trabalho.'),
    ('3.0.03', u'3.0.03 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ofensa física intencional, inclusive de terceiro, por motivo de disputa relacionada ao trabalho.'),
    ('3.0.04', u'3.0.04 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de imprudência, de negligência ou de imperícia de terceiro ou de companheiro de trabalho.'),
    ('3.0.05', u'3.0.05 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de ato de pessoa privada do uso da razão.'),
    ('3.0.06', u'3.0.06 - Acidente sofrido pelo segurado no local e no horário do trabalho, em consequência de desabamento, inundação, incêndio e outros casos fortuitos ou decorrentes de força maior.'),
    ('3.0.07', u'3.0.07 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho na execução de ordem ou na realização de serviço sob a autoridade da empresa.'),
    ('3.0.08', u'3.0.08 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho na prestação espontânea de qualquer serviço à empresa para lhe evitar prejuízo ou proporcionar proveito.'),
    ('3.0.09', u'3.0.09 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho em viagem a serviço da empresa, inclusive para estudo quando financiada por esta dentro de seus planos para melhor capacitação da mão-de- obra, independentemente do meio de locomoção utilizado, inclusive veículo de propriedade do segurado.'),
    ('3.0.10', u'3.0.10 - Acidente sofrido pelo segurado ainda que fora do local e horário de trabalho no percurso da residência para o local de trabalho ou deste para aquela, qualquer que seja o meio de locomoção, inclusive veículo de propriedade do segurado.'),
    ('3.0.11', u'3.0.11 - Acidente sofrido pelo segurado nos períodos destinados a refeição ou descanso, ou por ocasião da satisfação de outras necessidades fisiológicas, no local do trabalho ou durante este.'),
    ('4.0.01', u'4.0.01 - Suspeita de doenças profissionais ou do trabalho produzidas pelas condições especiais de trabalho, nos termos do art 169 da CLT.'),
    ('4.0.02', u'4.0.02 - Constatação de ocorrência ou agravamento de doenças profissionais, através de exames médicos que incluam os definidos na NR 07; ou sendo verificadas alterações que revelem qualquer tipo de disfunção de órgão ou sistema biológico, através dos exames constantes dos Quadros I (apenas aqueles com interpretação SC) e II, e do item 7.4.2.3 desta NR, mesmo sem sintomatologia, caberá ao médico-coordenador ou encarregado'),
    ('5.0.01', u'5.0.01 - Outros'),
)

CHOICES_S2240_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2400_PAISNASCTO = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S1200_INDRETIF = (
    (1, u'1 - para arquivo original'),
    (2, u'2 - para arquivo de retificação'),
)

CHOICES_S2200_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

CHOICES_S5012_INDEXISTINFO = (
    (1, u'1 - Há informações de Imposto de Renda Retido na Fonte'),
    (2, u'2 - Há movimento, porém não há informações de Imposto de Renda Retido na Fonte'),
    (3, u'3 - Não há movimento no período informado em {perApur}.'),
)

CHOICES_S1210_INDAPURACAO = (
    (1, u'1 - Mensal'),
)

CHOICES_S2300_PAISNAC = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

OPERACOES_INSALPERIC_APOSENTESP = (
    (1, u'Insalubridade/Periculosidade - Incluir'),
    (2, u'Insalubridade/Periculosidade - Alterar'),
    (3, u'Insalubridade/Periculosidade - Excluir'),
    (4, u'Aposentadoria Especial - Incluir'),
    (5, u'Aposentadoria Especial - Alterar'),
    (6, u'Aposentadoria Especial - Excluir'),
)

CHOICES_S1070_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S2220_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

CHOICES_S1250_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2220_TPAMB = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

CHOICES_S2206_PROCEMI = (
    (1, u'1 - Aplicativo do empregador'),
    (2, u'2 - Aplicativo governamental'),
)

class s1000evtInfoEmpregador(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1000_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1000_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1000_evtinfoempregador_custom#
    class Meta:
        db_table = r's1000_evtinfoempregador'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1000evtInfoEmpregadorOcorrencias(models.Model):
    evento = models.ForeignKey('s1000evtInfoEmpregador',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1000_evtinfoempregador_ocorrencias_custom#
    class Meta:
        db_table = r's1000_evtinfoempregador_ocorrencias'
        managed = True


class s1005evtTabEstab(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1005_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1005_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1005_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1005_evttabestab_custom#
    class Meta:
        db_table = r's1005_evttabestab'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1005evtTabEstabOcorrencias(models.Model):
    evento = models.ForeignKey('s1005evtTabEstab',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1005_evttabestab_ocorrencias_custom#
    class Meta:
        db_table = r's1005_evttabestab_ocorrencias'
        managed = True


class s1010evtTabRubrica(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1010_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1010_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1010_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1010_evttabrubrica_custom#
    class Meta:
        db_table = r's1010_evttabrubrica'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1010evtTabRubricaOcorrencias(models.Model):
    evento = models.ForeignKey('s1010evtTabRubrica',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1010_evttabrubrica_ocorrencias_custom#
    class Meta:
        db_table = r's1010_evttabrubrica_ocorrencias'
        managed = True


class s1020evtTabLotacao(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1020_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1020_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1020_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1020_evttablotacao_custom#
    class Meta:
        db_table = r's1020_evttablotacao'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1020evtTabLotacaoOcorrencias(models.Model):
    evento = models.ForeignKey('s1020evtTabLotacao',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1020_evttablotacao_ocorrencias_custom#
    class Meta:
        db_table = r's1020_evttablotacao_ocorrencias'
        managed = True


class s1030evtTabCargo(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1030_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1030_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1030_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1030_evttabcargo_custom#
    class Meta:
        db_table = r's1030_evttabcargo'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1030evtTabCargoOcorrencias(models.Model):
    evento = models.ForeignKey('s1030evtTabCargo',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1030_evttabcargo_ocorrencias_custom#
    class Meta:
        db_table = r's1030_evttabcargo_ocorrencias'
        managed = True


class s1035evtTabCarreira(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1035_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1035_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1035_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1035_evttabcarreira_custom#
    class Meta:
        db_table = r's1035_evttabcarreira'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1035evtTabCarreiraOcorrencias(models.Model):
    evento = models.ForeignKey('s1035evtTabCarreira',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1035_evttabcarreira_ocorrencias_custom#
    class Meta:
        db_table = r's1035_evttabcarreira_ocorrencias'
        managed = True


class s1040evtTabFuncao(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1040_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1040_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1040_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1040_evttabfuncao_custom#
    class Meta:
        db_table = r's1040_evttabfuncao'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1040evtTabFuncaoOcorrencias(models.Model):
    evento = models.ForeignKey('s1040evtTabFuncao',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1040_evttabfuncao_ocorrencias_custom#
    class Meta:
        db_table = r's1040_evttabfuncao_ocorrencias'
        managed = True


class s1050evtTabHorTur(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1050_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1050_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1050_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1050_evttabhortur_custom#
    class Meta:
        db_table = r's1050_evttabhortur'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1050evtTabHorTurOcorrencias(models.Model):
    evento = models.ForeignKey('s1050evtTabHorTur',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1050_evttabhortur_ocorrencias_custom#
    class Meta:
        db_table = r's1050_evttabhortur_ocorrencias'
        managed = True


class s1060evtTabAmbiente(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1060_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1060_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1060_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1060_evttabambiente_custom#
    class Meta:
        db_table = r's1060_evttabambiente'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1060evtTabAmbienteOcorrencias(models.Model):
    evento = models.ForeignKey('s1060evtTabAmbiente',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1060_evttabambiente_ocorrencias_custom#
    class Meta:
        db_table = r's1060_evttabambiente_ocorrencias'
        managed = True


class s1070evtTabProcesso(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1070_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1070_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1070_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1070_evttabprocesso_custom#
    class Meta:
        db_table = r's1070_evttabprocesso'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1070evtTabProcessoOcorrencias(models.Model):
    evento = models.ForeignKey('s1070evtTabProcesso',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1070_evttabprocesso_ocorrencias_custom#
    class Meta:
        db_table = r's1070_evttabprocesso_ocorrencias'
        managed = True


class s1080evtTabOperPort(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S1080_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1080_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1080_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1080_evttaboperport_custom#
    class Meta:
        db_table = r's1080_evttaboperport'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1080evtTabOperPortOcorrencias(models.Model):
    evento = models.ForeignKey('s1080evtTabOperPort',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1080_evttaboperport_ocorrencias_custom#
    class Meta:
        db_table = r's1080_evttaboperport_ocorrencias'
        managed = True


class s1200evtRemun(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1200_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1200_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1200_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1200_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab)
    #s1200_evtremun_custom#
    class Meta:
        db_table = r's1200_evtremun'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab']


class s1200evtRemunOcorrencias(models.Model):
    evento = models.ForeignKey('s1200evtRemun',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1200_evtremun_ocorrencias_custom#
    class Meta:
        db_table = r's1200_evtremun_ocorrencias'
        managed = True


class s1202evtRmnRPPS(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1202_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1202_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1202_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1202_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1202_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    qtddepfp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.qtddepfp)
    #s1202_evtrmnrpps_custom#
    class Meta:
        db_table = r's1202_evtrmnrpps'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'qtddepfp']


class s1202evtRmnRPPSOcorrencias(models.Model):
    evento = models.ForeignKey('s1202evtRmnRPPS',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1202_evtrmnrpps_ocorrencias_custom#
    class Meta:
        db_table = r's1202_evtrmnrpps_ocorrencias'
        managed = True


class s1207evtBenPrRP(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1207_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1207_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1207_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1207_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1207_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef)
    #s1207_evtbenprrp_custom#
    class Meta:
        db_table = r's1207_evtbenprrp'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef']


class s1207evtBenPrRPOcorrencias(models.Model):
    evento = models.ForeignKey('s1207evtBenPrRP',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1207_evtbenprrp_ocorrencias_custom#
    class Meta:
        db_table = r's1207_evtbenprrp_ocorrencias'
        managed = True


class s1210evtPgtos(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1210_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1210_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1210_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1210_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1210_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef)
    #s1210_evtpgtos_custom#
    class Meta:
        db_table = r's1210_evtpgtos'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef']


class s1210evtPgtosOcorrencias(models.Model):
    evento = models.ForeignKey('s1210evtPgtos',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1210_evtpgtos_ocorrencias_custom#
    class Meta:
        db_table = r's1210_evtpgtos_ocorrencias'
        managed = True


class s1250evtAqProd(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1250_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1250_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1250_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1250_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1250_TPINSC)
    nrinsc = models.CharField(max_length=15)
    tpinscadq = models.IntegerField(choices=CHOICES_S1250_TPINSCADQ)
    nrinscadq = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinscadq) + ' - ' + unicode(self.nrinscadq)
    #s1250_evtaqprod_custom#
    class Meta:
        db_table = r's1250_evtaqprod'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpinscadq', 'nrinscadq']


class s1250evtAqProdOcorrencias(models.Model):
    evento = models.ForeignKey('s1250evtAqProd',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1250_evtaqprod_ocorrencias_custom#
    class Meta:
        db_table = r's1250_evtaqprod_ocorrencias'
        managed = True


class s1260evtComProd(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1260_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1260_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1260_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1260_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1260_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrinscestabrural = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrinscestabrural)
    #s1260_evtcomprod_custom#
    class Meta:
        db_table = r's1260_evtcomprod'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'nrinscestabrural']


class s1260evtComProdOcorrencias(models.Model):
    evento = models.ForeignKey('s1260evtComProd',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1260_evtcomprod_ocorrencias_custom#
    class Meta:
        db_table = r's1260_evtcomprod_ocorrencias'
        managed = True


class s1270evtContratAvNP(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1270_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1270_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1270_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1270_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1270_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1270_evtcontratavnp_custom#
    class Meta:
        db_table = r's1270_evtcontratavnp'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1270evtContratAvNPOcorrencias(models.Model):
    evento = models.ForeignKey('s1270evtContratAvNP',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1270_evtcontratavnp_ocorrencias_custom#
    class Meta:
        db_table = r's1270_evtcontratavnp_ocorrencias'
        managed = True


class s1280evtInfoComplPer(models.Model):
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1280_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1280_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1280_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1280_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1280_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    codigo = models.IntegerField()
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    modificado_em = models.DateTimeField(blank=True, null=True)
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1280_evtinfocomplper_custom#
    class Meta:
        db_table = r's1280_evtinfocomplper'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1280evtInfoComplPerOcorrencias(models.Model):
    evento = models.ForeignKey('s1280evtInfoComplPer',
        related_name='%(class)s_evento')
    #s1280_evtinfocomplper_ocorrencias_custom#
    class Meta:
        db_table = r's1280_evtinfocomplper_ocorrencias'
        managed = True


class s1295evtTotConting(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1295_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1295_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1295_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1295_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1295_evttotconting_custom#
    class Meta:
        db_table = r's1295_evttotconting'
        managed = True
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1295evtTotContingOcorrencias(models.Model):
    evento = models.ForeignKey('s1295evtTotConting',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1295_evttotconting_ocorrencias_custom#
    class Meta:
        db_table = r's1295_evttotconting_ocorrencias'
        managed = True


class s1298evtReabreEvPer(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1298_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1298_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1298_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1298_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1298_evtreabreevper_custom#
    class Meta:
        db_table = r's1298_evtreabreevper'
        managed = True
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1298evtReabreEvPerOcorrencias(models.Model):
    evento = models.ForeignKey('s1298evtReabreEvPer',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1298_evtreabreevper_ocorrencias_custom#
    class Meta:
        db_table = r's1298_evtreabreevper_ocorrencias'
        managed = True


class s1299evtFechaEvPer(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1299_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1299_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1299_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1299_TPINSC)
    nrinsc = models.CharField(max_length=15)
    evtremun = models.CharField(choices=CHOICES_S1299_EVTREMUN, max_length=1)
    evtpgtos = models.CharField(choices=CHOICES_S1299_EVTPGTOS, max_length=1)
    evtaqprod = models.CharField(choices=CHOICES_S1299_EVTAQPROD, max_length=1)
    evtcomprod = models.CharField(choices=CHOICES_S1299_EVTCOMPROD, max_length=1)
    evtcontratavnp = models.CharField(choices=CHOICES_S1299_EVTCONTRATAVNP, max_length=1)
    evtinfocomplper = models.CharField(choices=CHOICES_S1299_EVTINFOCOMPLPER, max_length=1)
    compsemmovto = models.CharField(max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.evtremun) + ' - ' + unicode(self.evtpgtos) + ' - ' + unicode(self.evtaqprod) + ' - ' + unicode(self.evtcomprod) + ' - ' + unicode(self.evtcontratavnp) + ' - ' + unicode(self.evtinfocomplper) + ' - ' + unicode(self.compsemmovto)
    #s1299_evtfechaevper_custom#
    class Meta:
        db_table = r's1299_evtfechaevper'
        managed = True
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'evtremun', 'evtpgtos', 'evtaqprod', 'evtcomprod', 'evtcontratavnp', 'evtinfocomplper', 'compsemmovto']


class s1299evtFechaEvPerOcorrencias(models.Model):
    evento = models.ForeignKey('s1299evtFechaEvPer',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1299_evtfechaevper_ocorrencias_custom#
    class Meta:
        db_table = r's1299_evtfechaevper_ocorrencias'
        managed = True


class s1300evtContrSindPatr(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S1300_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S1300_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpamb = models.IntegerField(choices=CHOICES_S1300_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S1300_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S1300_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1300_evtcontrsindpatr_custom#
    class Meta:
        db_table = r's1300_evtcontrsindpatr'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'indapuracao', 'perapur', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc']


class s1300evtContrSindPatrOcorrencias(models.Model):
    evento = models.ForeignKey('s1300evtContrSindPatr',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s1300_evtcontrsindpatr_ocorrencias_custom#
    class Meta:
        db_table = r's1300_evtcontrsindpatr_ocorrencias'
        managed = True


class s2190evtAdmPrelim(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2190_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2190_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2190_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    dtnascto = models.DateField()
    dtadm = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.dtadm)
    #s2190_evtadmprelim_custom#
    class Meta:
        db_table = r's2190_evtadmprelim'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtnascto', 'dtadm']


class s2190evtAdmPrelimOcorrencias(models.Model):
    evento = models.ForeignKey('s2190evtAdmPrelim',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2190_evtadmprelim_ocorrencias_custom#
    class Meta:
        db_table = r's2190_evtadmprelim_ocorrencias'
        managed = True


class s2200evtAdmissao(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2200_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2200_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2200_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2200_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2200_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2200_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2200_GRAUINSTR, max_length=2)
    indpriempr = models.CharField(choices=CHOICES_S2200_INDPRIEMPR, max_length=1, blank=True, null=True)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.CharField(choices=MUNICIPIOS, max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.CharField(choices=CHOICES_S2200_PAISNASCTO, max_length=3)
    paisnac = models.CharField(choices=CHOICES_S2200_PAISNAC, max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    matricula = models.CharField(max_length=30)
    tpregtrab = models.IntegerField(choices=CHOICES_S2200_TPREGTRAB)
    tpregprev = models.IntegerField(choices=CHOICES_S2200_TPREGPREV)
    nrrecinfprelim = models.CharField(max_length=40, blank=True, null=True)
    cadini = models.CharField(choices=CHOICES_S2200_CADINI, max_length=1)
    codcargo = models.CharField(max_length=30, blank=True, null=True)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.IntegerField()
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    dtingrcarr = models.DateField(blank=True, null=True)
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2200_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    tpcontr = models.IntegerField(choices=CHOICES_S2200_TPCONTR)
    dtterm = models.DateField(blank=True, null=True)
    clauassec = models.CharField(choices=CHOICES_S2200_CLAUASSEC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.estciv) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.indpriempr) + ' - ' + unicode(self.nmsoc) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.nmmae) + ' - ' + unicode(self.nmpai) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.tpregtrab) + ' - ' + unicode(self.tpregprev) + ' - ' + unicode(self.nrrecinfprelim) + ' - ' + unicode(self.cadini) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.codfuncao) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.dtingrcarr) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo) + ' - ' + unicode(self.dscsalvar) + ' - ' + unicode(self.tpcontr) + ' - ' + unicode(self.dtterm) + ' - ' + unicode(self.clauassec)
    #s2200_evtadmissao_custom#
    class Meta:
        db_table = r's2200_evtadmissao'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'nmtrab', 'sexo', 'racacor', 'estciv', 'grauinstr', 'indpriempr', 'nmsoc', 'dtnascto', 'codmunic', 'uf', 'paisnascto', 'paisnac', 'nmmae', 'nmpai', 'matricula', 'tpregtrab', 'tpregprev', 'nrrecinfprelim', 'cadini', 'codcargo', 'codfuncao', 'codcateg', 'codcarreira', 'dtingrcarr', 'vrsalfx', 'undsalfixo', 'dscsalvar', 'tpcontr', 'dtterm', 'clauassec']


class s2200evtAdmissaoOcorrencias(models.Model):
    evento = models.ForeignKey('s2200evtAdmissao',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2200_evtadmissao_ocorrencias_custom#
    class Meta:
        db_table = r's2200_evtadmissao_ocorrencias'
        managed = True


class s2205evtAltCadastral(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2205_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2205_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2205_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2205_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    dtalteracao = models.DateField()
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2205_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2205_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2205_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2205_GRAUINSTR, max_length=2)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.CharField(choices=MUNICIPIOS, max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.CharField(max_length=3)
    paisnac = models.CharField(max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.estciv) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.nmsoc) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.nmmae) + ' - ' + unicode(self.nmpai)
    #s2205_evtaltcadastral_custom#
    class Meta:
        db_table = r's2205_evtaltcadastral'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'dtalteracao', 'nistrab', 'nmtrab', 'sexo', 'racacor', 'estciv', 'grauinstr', 'nmsoc', 'dtnascto', 'codmunic', 'uf', 'paisnascto', 'paisnac', 'nmmae', 'nmpai']


class s2205evtAltCadastralOcorrencias(models.Model):
    evento = models.ForeignKey('s2205evtAltCadastral',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2205_evtaltcadastral_ocorrencias_custom#
    class Meta:
        db_table = r's2205_evtaltcadastral_ocorrencias'
        managed = True


class s2206evtAltContratual(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2206_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2206_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2206_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    dtalteracao = models.DateField()
    dtef = models.DateField(blank=True, null=True)
    dscalt = models.CharField(max_length=150, blank=True, null=True)
    tpregprev = models.IntegerField(choices=CHOICES_S2206_TPREGPREV)
    codcargo = models.CharField(max_length=30, blank=True, null=True)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.IntegerField()
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    dtingrcarr = models.DateField(blank=True, null=True)
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2206_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    tpcontr = models.IntegerField(choices=CHOICES_S2206_TPCONTR)
    dtterm = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.dtef) + ' - ' + unicode(self.dscalt) + ' - ' + unicode(self.tpregprev) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.codfuncao) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.dtingrcarr) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo) + ' - ' + unicode(self.dscsalvar) + ' - ' + unicode(self.tpcontr) + ' - ' + unicode(self.dtterm)
    #s2206_evtaltcontratual_custom#
    class Meta:
        db_table = r's2206_evtaltcontratual'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'dtalteracao', 'dtef', 'dscalt', 'tpregprev', 'codcargo', 'codfuncao', 'codcateg', 'codcarreira', 'dtingrcarr', 'vrsalfx', 'undsalfixo', 'dscsalvar', 'tpcontr', 'dtterm']


class s2206evtAltContratualOcorrencias(models.Model):
    evento = models.ForeignKey('s2206evtAltContratual',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2206_evtaltcontratual_ocorrencias_custom#
    class Meta:
        db_table = r's2206_evtaltcontratual_ocorrencias'
        managed = True


class s2210evtCAT(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2210_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2210_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2210_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpregistrador = models.IntegerField(choices=CHOICES_S2210_TPREGISTRADOR)
    tpinsc = models.IntegerField(choices=CHOICES_S2210_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
    tpinsc = models.IntegerField(choices=CHOICES_S2210_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    dtacid = models.DateField()
    tpacid = models.CharField(choices=CHOICES_S2210_TPACID, max_length=6)
    hracid = models.CharField(max_length=4)
    hrstrabantesacid = models.CharField(max_length=4)
    tpcat = models.IntegerField(choices=CHOICES_S2210_TPCAT)
    indcatobito = models.CharField(choices=CHOICES_S2210_INDCATOBITO, max_length=1)
    dtobito = models.DateField(blank=True, null=True)
    indcomunpolicia = models.CharField(choices=CHOICES_S2210_INDCOMUNPOLICIA, max_length=1)
    codsitgeradora = models.IntegerField(choices=CHOICES_S2210_CODSITGERADORA, blank=True, null=True)
    iniciatcat = models.IntegerField(choices=CHOICES_S2210_INICIATCAT)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    tplocal = models.IntegerField(choices=CHOICES_S2210_TPLOCAL)
    dsclocal = models.CharField(max_length=80, blank=True, null=True)
    dsclograd = models.CharField(max_length=80, blank=True, null=True)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    codmunic = models.CharField(choices=MUNICIPIOS, max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    cnpjlocalacid = models.CharField(max_length=14, blank=True, null=True)
    pais = models.CharField(choices=CHOICES_S2210_PAIS, max_length=3, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpregistrador) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.dtacid) + ' - ' + unicode(self.tpacid) + ' - ' + unicode(self.hracid) + ' - ' + unicode(self.hrstrabantesacid) + ' - ' + unicode(self.tpcat) + ' - ' + unicode(self.indcatobito) + ' - ' + unicode(self.dtobito) + ' - ' + unicode(self.indcomunpolicia) + ' - ' + unicode(self.codsitgeradora) + ' - ' + unicode(self.iniciatcat) + ' - ' + unicode(self.observacao) + ' - ' + unicode(self.tplocal) + ' - ' + unicode(self.dsclocal) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.cnpjlocalacid) + ' - ' + unicode(self.pais) + ' - ' + unicode(self.codpostal)
    #s2210_evtcat_custom#
    class Meta:
        db_table = r's2210_evtcat'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpregistrador', 'tpinsc', 'nrinsc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'dtacid', 'tpacid', 'hracid', 'hrstrabantesacid', 'tpcat', 'indcatobito', 'dtobito', 'indcomunpolicia', 'codsitgeradora', 'iniciatcat', 'observacao', 'tplocal', 'dsclocal', 'dsclograd', 'nrlograd', 'codmunic', 'uf', 'cnpjlocalacid', 'pais', 'codpostal']


class s2210evtCATOcorrencias(models.Model):
    evento = models.ForeignKey('s2210evtCAT',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2210_evtcat_ocorrencias_custom#
    class Meta:
        db_table = r's2210_evtcat_ocorrencias'
        managed = True


class s2220evtMonit(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2220_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2220_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2220_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2220_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    dtaso = models.DateField()
    tpaso = models.IntegerField(choices=CHOICES_S2220_TPASO)
    resaso = models.IntegerField(choices=CHOICES_S2220_RESASO)
    codcnes = models.CharField(max_length=7, blank=True, null=True)
    frmctt = models.CharField(max_length=100)
    email = models.CharField(max_length=60, blank=True, null=True)
    nmmed = models.CharField(max_length=70)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.dtaso) + ' - ' + unicode(self.tpaso) + ' - ' + unicode(self.resaso) + ' - ' + unicode(self.codcnes) + ' - ' + unicode(self.frmctt) + ' - ' + unicode(self.email) + ' - ' + unicode(self.nmmed)
    #s2220_evtmonit_custom#
    class Meta:
        db_table = r's2220_evtmonit'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'dtaso', 'tpaso', 'resaso', 'codcnes', 'frmctt', 'email', 'nmmed']


class s2220evtMonitOcorrencias(models.Model):
    evento = models.ForeignKey('s2220evtMonit',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2220_evtmonit_ocorrencias_custom#
    class Meta:
        db_table = r's2220_evtmonit_ocorrencias'
        managed = True


class s2230evtAfastTemp(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2230_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2230_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2230_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2230_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.IntegerField(choices=CHOICES_S2230_CODCATEG, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codcateg)
    #s2230_evtafasttemp_custom#
    class Meta:
        db_table = r's2230_evtafasttemp'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'codcateg']


class s2230evtAfastTempOcorrencias(models.Model):
    evento = models.ForeignKey('s2230evtAfastTemp',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2230_evtafasttemp_ocorrencias_custom#
    class Meta:
        db_table = r's2230_evtafasttemp_ocorrencias'
        managed = True


class s2240evtExpRisco(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2240_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2240_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2240_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2240_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula)
    #s2240_evtexprisco_custom#
    class Meta:
        db_table = r's2240_evtexprisco'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula']


class s2240evtExpRiscoOcorrencias(models.Model):
    evento = models.ForeignKey('s2240evtExpRisco',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2240_evtexprisco_ocorrencias_custom#
    class Meta:
        db_table = r's2240_evtexprisco_ocorrencias'
        managed = True


class s2241evtInsApo(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2241_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2241_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2241_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2241_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES_INSALPERIC_APOSENTESP)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula)
    #s2241_evtinsapo_custom#
    class Meta:
        db_table = r's2241_evtinsapo'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula']


class s2241evtInsApoOcorrencias(models.Model):
    evento = models.ForeignKey('s2241evtInsApo',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2241_evtinsapo_ocorrencias_custom#
    class Meta:
        db_table = r's2241_evtinsapo_ocorrencias'
        managed = True


class s2250evtAvPrevio(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2250_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2250_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2250_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2250_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula)
    #s2250_evtavprevio_custom#
    class Meta:
        db_table = r's2250_evtavprevio'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula']


class s2250evtAvPrevioOcorrencias(models.Model):
    evento = models.ForeignKey('s2250evtAvPrevio',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2250_evtavprevio_ocorrencias_custom#
    class Meta:
        db_table = r's2250_evtavprevio_ocorrencias'
        managed = True


class s2260evtConvInterm(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2260_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2260_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2260_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2260_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    codconv = models.CharField(max_length=30)
    dtinicio = models.DateField()
    dtfim = models.DateField()
    dtprevpgto = models.DateField()
    codhorcontrat = models.CharField(max_length=30, blank=True, null=True)
    dscjornada = models.CharField(max_length=999, blank=True, null=True)
    indlocal = models.IntegerField(choices=CHOICES_S2260_INDLOCAL)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codconv) + ' - ' + unicode(self.dtinicio) + ' - ' + unicode(self.dtfim) + ' - ' + unicode(self.dtprevpgto) + ' - ' + unicode(self.codhorcontrat) + ' - ' + unicode(self.dscjornada) + ' - ' + unicode(self.indlocal)
    #s2260_evtconvinterm_custom#
    class Meta:
        db_table = r's2260_evtconvinterm'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'codconv', 'dtinicio', 'dtfim', 'dtprevpgto', 'codhorcontrat', 'dscjornada', 'indlocal']


class s2260evtConvIntermOcorrencias(models.Model):
    evento = models.ForeignKey('s2260evtConvInterm',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2260_evtconvinterm_ocorrencias_custom#
    class Meta:
        db_table = r's2260_evtconvinterm_ocorrencias'
        managed = True


class s2298evtReintegr(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2298_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2298_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2298_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2298_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    tpreint = models.IntegerField(choices=CHOICES_S2298_TPREINT)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    nrleianistia = models.CharField(max_length=13, blank=True, null=True)
    dtefetretorno = models.DateField()
    dtefeito = models.DateField()
    indpagtojuizo = models.CharField(choices=CHOICES_S2298_INDPAGTOJUIZO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.tpreint) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.nrleianistia) + ' - ' + unicode(self.dtefetretorno) + ' - ' + unicode(self.dtefeito) + ' - ' + unicode(self.indpagtojuizo)
    #s2298_evtreintegr_custom#
    class Meta:
        db_table = r's2298_evtreintegr'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'tpreint', 'nrprocjud', 'nrleianistia', 'dtefetretorno', 'dtefeito', 'indpagtojuizo']


class s2298evtReintegrOcorrencias(models.Model):
    evento = models.ForeignKey('s2298evtReintegr',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2298_evtreintegr_ocorrencias_custom#
    class Meta:
        db_table = r's2298_evtreintegr_ocorrencias'
        managed = True


class s2299evtDeslig(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2299_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2299_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2299_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2299_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11)
    matricula = models.CharField(max_length=30)
    mtvdeslig = models.CharField(choices=CHOICES_S2299_MTVDESLIG, max_length=2)
    dtdeslig = models.DateField()
    indpagtoapi = models.CharField(choices=CHOICES_S2299_INDPAGTOAPI, max_length=1)
    dtprojfimapi = models.DateField(blank=True, null=True)
    pensalim = models.IntegerField(choices=CHOICES_S2299_PENSALIM)
    percaliment = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vralim = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    nrcertobito = models.CharField(max_length=32, blank=True, null=True)
    nrproctrab = models.CharField(max_length=20, blank=True, null=True)
    indcumprparc = models.IntegerField(choices=CHOICES_S2299_INDCUMPRPARC)
    qtddiasinterm = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.mtvdeslig) + ' - ' + unicode(self.dtdeslig) + ' - ' + unicode(self.indpagtoapi) + ' - ' + unicode(self.dtprojfimapi) + ' - ' + unicode(self.pensalim) + ' - ' + unicode(self.percaliment) + ' - ' + unicode(self.vralim) + ' - ' + unicode(self.nrcertobito) + ' - ' + unicode(self.nrproctrab) + ' - ' + unicode(self.indcumprparc) + ' - ' + unicode(self.qtddiasinterm)
    #s2299_evtdeslig_custom#
    class Meta:
        db_table = r's2299_evtdeslig'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'matricula', 'mtvdeslig', 'dtdeslig', 'indpagtoapi', 'dtprojfimapi', 'pensalim', 'percaliment', 'vralim', 'nrcertobito', 'nrproctrab', 'indcumprparc', 'qtddiasinterm']


class s2299evtDesligOcorrencias(models.Model):
    evento = models.ForeignKey('s2299evtDeslig',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2299_evtdeslig_ocorrencias_custom#
    class Meta:
        db_table = r's2299_evtdeslig_ocorrencias'
        managed = True


class s2300evtTSVInicio(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2300_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2300_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2300_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2300_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    nmtrab = models.CharField(max_length=70)
    sexo = models.CharField(choices=CHOICES_S2300_SEXO, max_length=1)
    racacor = models.IntegerField(choices=CHOICES_S2300_RACACOR)
    estciv = models.IntegerField(choices=CHOICES_S2300_ESTCIV, blank=True, null=True)
    grauinstr = models.CharField(choices=CHOICES_S2300_GRAUINSTR, max_length=2)
    nmsoc = models.CharField(max_length=70, blank=True, null=True)
    dtnascto = models.DateField()
    codmunic = models.CharField(choices=MUNICIPIOS, max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.CharField(choices=CHOICES_S2300_PAISNASCTO, max_length=3)
    paisnac = models.CharField(choices=CHOICES_S2300_PAISNAC, max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    cadini = models.CharField(choices=CHOICES_S2300_CADINI, max_length=1)
    codcateg = models.IntegerField(choices=CHOICES_S2300_CODCATEG)
    dtinicio = models.DateField()
    natatividade = models.IntegerField(choices=CHOICES_S2300_NATATIVIDADE, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.sexo) + ' - ' + unicode(self.racacor) + ' - ' + unicode(self.estciv) + ' - ' + unicode(self.grauinstr) + ' - ' + unicode(self.nmsoc) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.nmmae) + ' - ' + unicode(self.nmpai) + ' - ' + unicode(self.cadini) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtinicio) + ' - ' + unicode(self.natatividade)
    #s2300_evttsvinicio_custom#
    class Meta:
        db_table = r's2300_evttsvinicio'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'nmtrab', 'sexo', 'racacor', 'estciv', 'grauinstr', 'nmsoc', 'dtnascto', 'codmunic', 'uf', 'paisnascto', 'paisnac', 'nmmae', 'nmpai', 'cadini', 'codcateg', 'dtinicio', 'natatividade']


class s2300evtTSVInicioOcorrencias(models.Model):
    evento = models.ForeignKey('s2300evtTSVInicio',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2300_evttsvinicio_ocorrencias_custom#
    class Meta:
        db_table = r's2300_evttsvinicio_ocorrencias'
        managed = True


class s2306evtTSVAltContr(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2306_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2306_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2306_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2306_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    codcateg = models.IntegerField(choices=CHOICES_S2306_CODCATEG)
    dtalteracao = models.DateField()
    natatividade = models.IntegerField(choices=CHOICES_S2306_NATATIVIDADE, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtalteracao) + ' - ' + unicode(self.natatividade)
    #s2306_evttsvaltcontr_custom#
    class Meta:
        db_table = r's2306_evttsvaltcontr'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'codcateg', 'dtalteracao', 'natatividade']


class s2306evtTSVAltContrOcorrencias(models.Model):
    evento = models.ForeignKey('s2306evtTSVAltContr',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2306_evttsvaltcontr_ocorrencias_custom#
    class Meta:
        db_table = r's2306_evttsvaltcontr_ocorrencias'
        managed = True


class s2399evtTSVTermino(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2399_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2399_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2399_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    codcateg = models.IntegerField(choices=CHOICES_S2399_CODCATEG)
    dtterm = models.DateField()
    mtvdesligtsv = models.CharField(choices=CHOICES_S2399_MTVDESLIGTSV, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtterm) + ' - ' + unicode(self.mtvdesligtsv)
    #s2399_evttsvtermino_custom#
    class Meta:
        db_table = r's2399_evttsvtermino'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpftrab', 'nistrab', 'codcateg', 'dtterm', 'mtvdesligtsv']


class s2399evtTSVTerminoOcorrencias(models.Model):
    evento = models.ForeignKey('s2399evtTSVTermino',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2399_evttsvtermino_ocorrencias_custom#
    class Meta:
        db_table = r's2399_evttsvtermino_ocorrencias'
        managed = True


class s2400evtCdBenPrRP(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indretif = models.IntegerField(choices=CHOICES_S2400_INDRETIF)
    nrrecibo = models.CharField(max_length=40, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S2400_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S2400_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S2400_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpfbenef = models.CharField(max_length=11)
    nmbenefic = models.CharField(max_length=70)
    dtnascto = models.DateField()
    codmunic = models.CharField(choices=MUNICIPIOS, max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    paisnascto = models.CharField(choices=CHOICES_S2400_PAISNASCTO, max_length=3)
    paisnac = models.CharField(choices=CHOICES_S2400_PAISNAC, max_length=3)
    nmmae = models.CharField(max_length=70, blank=True, null=True)
    nmpai = models.CharField(max_length=70, blank=True, null=True)
    tpplanrp = models.IntegerField(choices=CHOICES_S2400_TPPLANRP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    operacao = models.IntegerField(choices=OPERACOES)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indretif) + ' - ' + unicode(self.nrrecibo) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.paisnascto) + ' - ' + unicode(self.paisnac) + ' - ' + unicode(self.nmmae) + ' - ' + unicode(self.nmpai) + ' - ' + unicode(self.tpplanrp)
    #s2400_evtcdbenprrp_custom#
    class Meta:
        db_table = r's2400_evtcdbenprrp'
        managed = True
        ordering = ['identidade', 'indretif', 'nrrecibo', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'cpfbenef', 'nmbenefic', 'dtnascto', 'codmunic', 'uf', 'paisnascto', 'paisnac', 'nmmae', 'nmpai', 'tpplanrp']


class s2400evtCdBenPrRPOcorrencias(models.Model):
    evento = models.ForeignKey('s2400evtCdBenPrRP',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s2400_evtcdbenprrp_ocorrencias_custom#
    class Meta:
        db_table = r's2400_evtcdbenprrp_ocorrencias'
        managed = True


class s3000evtExclusao(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    tpamb = models.IntegerField(choices=CHOICES_S3000_TPAMB)
    procemi = models.IntegerField(choices=CHOICES_S3000_PROCEMI, default=1)
    verproc = models.CharField(max_length=20)
    tpinsc = models.IntegerField(choices=CHOICES_S3000_TPINSC)
    nrinsc = models.CharField(max_length=15)
    tpevento = models.CharField(choices=CHOICES_S3000_TPEVENTO, max_length=6)
    nrrecevt = models.CharField(max_length=40)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.tpamb) + ' - ' + unicode(self.procemi) + ' - ' + unicode(self.verproc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.tpevento) + ' - ' + unicode(self.nrrecevt)
    #s3000_evtexclusao_custom#
    class Meta:
        db_table = r's3000_evtexclusao'
        managed = True
        ordering = ['identidade', 'tpamb', 'procemi', 'verproc', 'tpinsc', 'nrinsc', 'tpevento', 'nrrecevt']


class s3000evtExclusaoOcorrencias(models.Model):
    evento = models.ForeignKey('s3000evtExclusao',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s3000_evtexclusao_ocorrencias_custom#
    class Meta:
        db_table = r's3000_evtexclusao_ocorrencias'
        managed = True


class s5001evtBasesTrab(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    nrrecarqbase = models.CharField(max_length=40, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S5001_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5001_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s5001_evtbasestrab_custom#
    class Meta:
        db_table = r's5001_evtbasestrab'
        managed = True
        ordering = ['identidade', 'nrrecarqbase', 'indapuracao', 'perapur', 'tpinsc', 'nrinsc', 'cpftrab']


class s5001evtBasesTrabOcorrencias(models.Model):
    evento = models.ForeignKey('s5001evtBasesTrab',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s5001_evtbasestrab_ocorrencias_custom#
    class Meta:
        db_table = r's5001_evtbasestrab_ocorrencias'
        managed = True


class s5002evtIrrfBenef(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    nrrecarqbase = models.CharField(max_length=40, blank=True, null=True)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5002_TPINSC)
    nrinsc = models.CharField(max_length=15)
    cpftrab = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.cpftrab)
    #s5002_evtirrfbenef_custom#
    class Meta:
        db_table = r's5002_evtirrfbenef'
        managed = True
        ordering = ['identidade', 'nrrecarqbase', 'perapur', 'tpinsc', 'nrinsc', 'cpftrab']


class s5002evtIrrfBenefOcorrencias(models.Model):
    evento = models.ForeignKey('s5002evtIrrfBenef',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s5002_evtirrfbenef_ocorrencias_custom#
    class Meta:
        db_table = r's5002_evtirrfbenef_ocorrencias'
        managed = True


class s5011evtCS(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    indapuracao = models.IntegerField(choices=CHOICES_S5011_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5011_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrrecarqbase = models.CharField(max_length=40, blank=True, null=True)
    indexistinfo = models.IntegerField(choices=CHOICES_S5011_INDEXISTINFO)
    classtrib = models.CharField(choices=CHOICES_S5011_CLASSTRIB, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo) + ' - ' + unicode(self.classtrib)
    #s5011_evtcs_custom#
    class Meta:
        db_table = r's5011_evtcs'
        managed = True
        ordering = ['identidade', 'indapuracao', 'perapur', 'tpinsc', 'nrinsc', 'nrrecarqbase', 'indexistinfo', 'classtrib']


class s5011evtCSOcorrencias(models.Model):
    evento = models.ForeignKey('s5011evtCS',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s5011_evtcs_ocorrencias_custom#
    class Meta:
        db_table = r's5011_evtcs_ocorrencias'
        managed = True


class s5012evtIrrf(models.Model):
    transmissor_lote = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor_lote', blank=True, null=True)
    versao = models.CharField(choices=EVENTOS_VERSOES, max_length=20, default='v02_04_02')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    perapur = models.CharField(max_length=7)
    tpinsc = models.IntegerField(choices=CHOICES_S5012_TPINSC)
    nrinsc = models.CharField(max_length=15)
    nrrecarqbase = models.CharField(max_length=40, blank=True, null=True)
    indexistinfo = models.IntegerField(choices=CHOICES_S5012_INDEXISTINFO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.IntegerField(choices=CODIGO_RESPOSTA, default=0)
    processamento_descricao_resposta = models.TextField(blank=True, null=True, default='Cadastrado (Aguardando envio)')
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.identidade) + ' - ' + unicode(self.perapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo)
    #s5012_evtirrf_custom#
    class Meta:
        db_table = r's5012_evtirrf'
        managed = True
        ordering = ['identidade', 'perapur', 'tpinsc', 'nrinsc', 'nrrecarqbase', 'indexistinfo']


class s5012evtIrrfOcorrencias(models.Model):
    evento = models.ForeignKey('s5012evtIrrf',
        related_name='%(class)s_evento')
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA)
    codigo = models.IntegerField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    #s5012_evtirrf_ocorrencias_custom#
    class Meta:
        db_table = r's5012_evtirrf_ocorrencias'
        managed = True


#VIEWS_MODELS
