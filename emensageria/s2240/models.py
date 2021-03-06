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

CHOICES_S2240_ALTEXPRISCO_CODFATRIS = (
    ('01.01.001', u'01.01.001 - Infrassom e sons de baixa frequência'),
    ('01.01.002', u'01.01.002 - Ruído contínuo ou Intermitente'),
    ('01.01.003', u'01.01.003 - Ruído impulsivo ou de Impacto'),
    ('01.01.004', u'01.01.004 - Ultrassom'),
    ('01.01.005', u'01.01.005 - Campos magnéticos estáticos'),
    ('01.01.006', u'01.01.006 - Campos magnéticos de sub-radiofrequência (30 kHz e abaixo)'),
    ('01.01.007', u'01.01.007 - Sub-Radiofrequência (30 kHz e abaixo) e campos eletrostáticos'),
    ('01.01.008', u'01.01.008 - Radiação de radiofrequência e micro-ondas'),
    ('01.01.009', u'01.01.009 - Radiação visível e infravermelho próximo'),
    ('01.01.010', u'01.01.010 - Radiação ultravioleta'),
    ('01.01.011', u'01.01.011 - LASERS'),
    ('01.01.012', u'01.01.012 - Radiações Ionizantes'),
    ('01.01.013', u'01.01.013 - Vibrações Localizadas (Mão-Braço)'),
    ('01.01.014', u'01.01.014 - Vibração de corpo inteiro'),
    ('01.01.015', u'01.01.015 - Estresse por frio (Hipotermia)'),
    ('01.01.016', u'01.01.016 - Estresse e sobrecarga fisiológica por calor'),
    ('01.01.017', u'01.01.017 - Pressão Hiperbárica'),
    ('01.01.018', u'01.01.018 - Pressão Hipobárica'),
    ('01.01.019', u'01.01.019 - Umidade'),
    ('01.01.999', u'01.01.999 - Outros'),
    ('02.01.001', u'02.01.001 - Acetaldeído'),
    ('02.01.002', u'02.01.002 - Acetato de benzila'),
    ('02.01.003', u'02.01.003 - Acetato de n-butila'),
    ('02.01.004', u'02.01.004 - Acetato de sec-butila'),
    ('02.01.005', u'02.01.005 - Acetato de terc-butila'),
    ('02.01.006', u'02.01.006 - Acetato de 2-butoxietila'),
    ('02.01.007', u'02.01.007 - Acetato de cellosolve'),
    ('02.01.008', u'02.01.008 - Acetato de éter monoetílico de etileno glicol'),
    ('02.01.009', u'02.01.009 - Sais de Cianeto'),
    ('02.01.010', u'02.01.010 - Acetato de 2-etoxietila'),
    ('02.01.011', u'02.01.011 - Acetato de sec-hexila'),
    ('02.01.012', u'02.01.012 - Acetato de isobutila'),
    ('02.01.013', u'02.01.013 - Acetato de isopropila'),
    ('02.01.014', u'02.01.014 - Acetato de metila'),
    ('02.01.015', u'02.01.015 - Acetato de 2-metoxietila (EGMEA)'),
    ('02.01.016', u'02.01.016 - Acetato de n-propila'),
    ('02.01.017', u'02.01.017 - Acetato de pentila, todos os isômeros'),
    ('02.01.018', u'02.01.018 - Acetato de vinila'),
    ('02.01.019', u'02.01.019 - Acetileno'),
    ('02.01.020', u'02.01.020 - Acetofenona'),
    ('02.01.021', u'02.01.021 - Acetona'),
    ('02.01.022', u'02.01.022 - Acetona cianidrina'),
    ('02.01.023', u'02.01.023 - Acetonitrila'),
    ('02.01.024', u'02.01.024 - Ácido acético'),
    ('02.01.025', u'02.01.025 - Ácido acetilsalicílico (Aspirina)'),
    ('02.01.026', u'02.01.026 - Ácido acrílico'),
    ('02.01.027', u'02.01.027 - Ácido adípico'),
    ('02.01.028', u'02.01.028 - Ácido Aristólico'),
    ('02.01.029', u'02.01.029 - Ácido bromídrico'),
    ('02.01.030', u'02.01.030 - ácido carbônico'),
    ('02.01.031', u'02.01.031 - Ácido cianídrico'),
    ('02.01.032', u'02.01.032 - Ácido clorídrico'),
    ('02.01.033', u'02.01.033 - Ácido 2-cloropropiônico'),
    ('02.01.034', u'02.01.034 - Ácido crômico (névoa)'),
    ('02.01.035', u'02.01.035 - Ácido dicloroacético'),
    ('02.01.036', u'02.01.036 - Ácido 2,2-dicloropropiônico'),
    ('02.01.037', u'02.01.037 - Ácido etanóico'),
    ('02.01.038', u'02.01.038 - Ácido 2-etil hexanoico'),
    ('02.01.039', u'02.01.039 - Ácido fluorídrico'),
    ('02.01.040', u'02.01.040 - Ácido fórmico'),
    ('02.01.041', u'02.01.041 - Ácido fosfórico'),
    ('02.01.042', u'02.01.042 - Ácido metacrílico'),
    ('02.01.043', u'02.01.043 - Ácido metanóico'),
    ('02.01.044', u'02.01.044 - Ácido monocloroacético'),
    ('02.01.045', u'02.01.045 - Ácido nítrico'),
    ('02.01.046', u'02.01.046 - Ácido oxálico'),
    ('02.01.047', u'02.01.047 - Ácido peracético'),
    ('02.01.048', u'02.01.048 - Ácido pícrico'),
    ('02.01.049', u'02.01.049 - Ácido propiônico'),
    ('02.01.050', u'02.01.050 - Ácido sulfúrico'),
    ('02.01.051', u'02.01.051 - Ácido tereftálico'),
    ('02.01.052', u'02.01.052 - Ácido tioglicólico'),
    ('02.01.053', u'02.01.053 - Ácido tricloroacético'),
    ('02.01.054', u'02.01.054 - Acrilamida'),
    ('02.01.055', u'02.01.055 - Acrilato de n-butila'),
    ('02.01.056', u'02.01.056 - Acrilato de etila'),
    ('02.01.057', u'02.01.057 - Acrilato de 2-hidroxipropila'),
    ('02.01.058', u'02.01.058 - Acrilato de metila'),
    ('02.01.059', u'02.01.059 - Acrilonitrila'),
    ('02.01.060', u'02.01.060 - Acroleína'),
    ('02.01.061', u'02.01.061 - Acronitrila'),
    ('02.01.062', u'02.01.062 - Adiponitrila'),
    ('02.01.063', u'02.01.063 - Aflatoxinas'),
    ('02.01.064', u'02.01.064 - Aguarrás mineral (Solvente de Stoddard)'),
    ('02.01.065', u'02.01.065 - Alaclor'),
    ('02.01.066', u'02.01.066 - álcalis cáusticos'),
    ('02.01.067', u'02.01.067 - Alcatrão de hulha, produtos voláteis como aerossóis solúveis em benzeno'),
    ('02.01.068', u'02.01.068 - Álcool alílico'),
    ('02.01.069', u'02.01.069 - Álcool n-butílico'),
    ('02.01.070', u'02.01.070 - Álcool sec-butílico'),
    ('02.01.071', u'02.01.071 - Álcool terc-butílico'),
    ('02.01.072', u'02.01.072 - Álcool etílico'),
    ('02.01.073', u'02.01.073 - Álcool furfurílico'),
    ('02.01.074', u'02.01.074 - Álcool isoamílico'),
    ('02.01.075', u'02.01.075 - Álcool isobutílico'),
    ('02.01.076', u'02.01.076 - Álcool isooctílico'),
    ('02.01.077', u'02.01.077 - Álcool isopropílico'),
    ('02.01.078', u'02.01.078 - Álcool propargílico'),
    ('02.01.079', u'02.01.079 - Álcool metil amílico'),
    ('02.01.080', u'02.01.080 - Álcool metílico'),
    ('02.01.081', u'02.01.081 - Álcool n-propílico (n-propanol)'),
    ('02.01.082', u'02.01.082 - Aldrin'),
    ('02.01.083', u'02.01.083 - Aldeído acético'),
    ('02.01.084', u'02.01.084 - Aldeído fórmico'),
    ('02.01.085', u'02.01.085 - Algodão, bruto, sem tratamento, poeira'),
    ('02.01.086', u'02.01.086 - Alumínio metal e compostos insolúveis'),
    ('02.01.087', u'02.01.087 - Amido'),
    ('02.01.088', u'02.01.088 - Aminas aromáticas'),
    ('02.01.089', u'02.01.089 - 4 - Aminodifenil (p-xenilamina)'),
    ('02.01.090', u'02.01.090 - Aminobifenila'),
    ('02.01.091', u'02.01.091 - aminoderivados'),
    ('02.01.092', u'02.01.092 - 4-Aminodifenil'),
    ('02.01.093', u'02.01.093 - 2-Aminopiridina'),
    ('02.01.094', u'02.01.094 - Amitrol (3-amina-1,2,4-triazol)'),
    ('02.01.095', u'02.01.095 - Amônia'),
    ('02.01.096', u'02.01.096 - Anidro sulfuroso'),
    ('02.01.097', u'02.01.097 - Anidrido acético'),
    ('02.01.098', u'02.01.098 - Anidrido ftálico'),
    ('02.01.099', u'02.01.099 - Anidrido hexahidroftálico todos os isômeros'),
    ('02.01.100', u'02.01.100 - Anidrido maleico'),
    ('02.01.101', u'02.01.101 - Anidrido trimelítico'),
    ('02.01.102', u'02.01.102 - Anilina'),
    ('02.01.103', u'02.01.103 - o-Anisidina'),
    ('02.01.104', u'02.01.104 - p-Anisidina'),
    ('02.01.105', u'02.01.105 - Antimônio e seus compostos'),
    ('02.01.106', u'02.01.106 - antraceno'),
    ('02.01.107', u'02.01.107 - ANTU'),
    ('02.01.108', u'02.01.108 - Argônio'),
    ('02.01.109', u'02.01.109 - Arseneto de gálio'),
    ('02.01.110', u'02.01.110 - Arsênio e seus compostos'),
    ('02.01.111', u'02.01.111 - Arsina'),
    ('02.01.112', u'02.01.112 - Asbestos, todas as formas'),
    ('02.01.113', u'02.01.113 - Asfalto (betume), fumos, como aerossol solúvel em benzeno'),
    ('02.01.114', u'02.01.114 - Atrazine (e triazinas simétricas relacionadas)'),
    ('02.01.115', u'02.01.115 - Auramina'),
    ('02.01.116', u'02.01.116 - Azatioprina'),
    ('02.01.117', u'02.01.117 - Azida de sódio'),
    ('02.01.118', u'02.01.118 - Azinfos metil'),
    ('02.01.119', u'02.01.119 - Bário e compostos solúveis'),
    ('02.01.120', u'02.01.120 - Benomil'),
    ('02.01.121', u'02.01.121 - Benzeno e seus compostos'),
    ('02.01.122', u'02.01.122 - Benzidina'),
    ('02.01.123', u'02.01.123 - Benzo[a]antraceno'),
    ('02.01.124', u'02.01.124 - Benzo[b]fluoranteno'),
    ('02.01.125', u'02.01.125 - Benzopireno (Benzo[a]pireno)'),
    ('02.01.126', u'02.01.126 - Berílio e seus compostos'),
    ('02.01.127', u'02.01.127 - betume'),
    ('02.01.128', u'02.01.128 - BHC (hexacloreto de benzeno)'),
    ('02.01.129', u'02.01.129 - Bifenil'),
    ('02.01.130', u'02.01.130 - Bifenis policlorados'),
    ('02.01.131', u'02.01.131 - Biscloroetileter'),
    ('02.01.132', u'02.01.132 - Bisclorometil'),
    ('02.01.133', u'02.01.133 - Bissulfito de sódio'),
    ('02.01.134', u'02.01.134 - Borracha natural, látex como proteínas alergênicas inaláveis'),
    ('02.01.135', u'02.01.135 - Borato, compostos inorgânicos'),
    ('02.01.136', u'02.01.136 - breu'),
    ('02.01.137', u'02.01.137 - Bromacil'),
    ('02.01.138', u'02.01.138 - Brometo de alila'),
    ('02.01.139', u'02.01.139 - Brometo de etila'),
    ('02.01.140', u'02.01.140 - Brometo de hidrogênio'),
    ('02.01.141', u'02.01.141 - Brometo de metila'),
    ('02.01.142', u'02.01.142 - Brometo de vinila'),
    ('02.01.143', u'02.01.143 - Bromo e seus compostos'),
    ('02.01.144', u'02.01.144 - Bromoetano'),
    ('02.01.145', u'02.01.145 - Bromofórmio'),
    ('02.01.146', u'02.01.146 - Bromometano'),
    ('02.01.147', u'02.01.147 - 1-Bromopropano'),
    ('02.01.148', u'02.01.148 - Bussulfano'),
    ('02.01.149', u'02.01.149 - 1,3-Butadieno'),
    ('02.01.150', u'02.01.150 - Butadieno-estireno'),
    ('02.01.151', u'02.01.151 - n-Butano'),
    ('02.01.152', u'02.01.152 - Butano, todos os isômeros'),
    ('02.01.153', u'02.01.153 - 1-4 Butanodiol'),
    ('02.01.154', u'02.01.154 - Butenos, todos os isômeros'),
    ('02.01.155', u'02.01.155 - sec-Butanol'),
    ('02.01.156', u'02.01.156 - Butanona'),
    ('02.01.157', u'02.01.157 - 1-Butanotiol'),
    ('02.01.158', u'02.01.158 - Butil cellosolve'),
    ('02.01.159', u'02.01.159 - n-Butil mercaptana'),
    ('02.01.160', u'02.01.160 - n-Butilamina'),
    ('02.01.161', u'02.01.161 - o-sec Butilfenol'),
    ('02.01.162', u'02.01.162 - p-terc-Butiltolueno'),
    ('02.01.163', u'02.01.163 - 2-Butóxi etanol (EGBE)'),
    ('02.01.164', u'02.01.164 - Cádmio e seus compostos'),
    ('02.01.165', u'02.01.165 - Canfeno clorado'),
    ('02.01.166', u'02.01.166 - Cânfora, sintética'),
    ('02.01.167', u'02.01.167 - Caolim'),
    ('02.01.168', u'02.01.168 - Caprolactama'),
    ('02.01.169', u'02.01.169 - Captafol'),
    ('02.01.170', u'02.01.170 - Captan'),
    ('02.01.171', u'02.01.171 - Carbaril'),
    ('02.01.172', u'02.01.172 - Carbeto de silício'),
    ('02.01.173', u'02.01.173 - Carbofuran'),
    ('02.01.174', u'02.01.174 - Carvão mineral e seus derivados'),
    ('02.01.175', u'02.01.175 - Catecol'),
    ('02.01.176', u'02.01.176 - Cellosolve'),
    ('02.01.177', u'02.01.177 - Celulose'),
    ('02.01.178', u'02.01.178 - Cereais, poeira (aveia, cevada, trigo)'),
    ('02.01.179', u'02.01.179 - Ceteno'),
    ('02.01.180', u'02.01.180 - Chumbo e seus compostos'),
    ('02.01.181', u'02.01.181 - Chumbo tetraetila'),
    ('02.01.182', u'02.01.182 - Chumbo tetrametila'),
    ('02.01.183', u'02.01.183 - Cianamida'),
    ('02.01.184', u'02.01.184 - Cianamida de cálcio'),
    ('02.01.185', u'02.01.185 - Cianeto de hidrogênio'),
    ('02.01.186', u'02.01.186 - Cianeto de metila'),
    ('02.01.187', u'02.01.187 - Cianeto de vinila'),
    ('02.01.188', u'02.01.188 - Cianoacrilato de etila'),
    ('02.01.189', u'02.01.189 - 2-Cianoacrilato de metila'),
    ('02.01.190', u'02.01.190 - Cianogênio'),
    ('02.01.191', u'02.01.191 - Ciclofosfamida'),
    ('02.01.192', u'02.01.192 - Ciclohexano'),
    ('02.01.193', u'02.01.193 - Ciclohexanol'),
    ('02.01.194', u'02.01.194 - Ciclohexanona'),
    ('02.01.195', u'02.01.195 - Ciclohexeno'),
    ('02.01.196', u'02.01.196 - Ciclohexilamina'),
    ('02.01.197', u'02.01.197 - Ciclonita'),
    ('02.01.198', u'02.01.198 - Ciclopentadieno'),
    ('02.01.199', u'02.01.199 - Ciclopentano'),
    ('02.01.200', u'02.01.200 - Ciclosporina'),
    ('02.01.201', u'02.01.201 - Cihexatin'),
    ('02.01.202', u'02.01.202 - Cimento portland'),
    ('02.01.203', u'02.01.203 - Citral'),
    ('02.01.204', u'02.01.204 - Clopidol'),
    ('02.01.205', u'02.01.205 - Clorambucil'),
    ('02.01.206', u'02.01.206 - Clordane'),
    ('02.01.207', u'02.01.207 - Cloreto de alila'),
    ('02.01.208', u'02.01.208 - Cloreto de amônio - fumos'),
    ('02.01.209', u'02.01.209 - Cloreto de benzila'),
    ('02.01.210', u'02.01.210 - Cloreto de benzoíla'),
    ('02.01.211', u'02.01.211 - Cloreto de carbonila'),
    ('02.01.212', u'02.01.212 - Cloreto de cianogênio'),
    ('02.01.213', u'02.01.213 - Cloreto de cloroacetila'),
    ('02.01.214', u'02.01.214 - Cloreto de cromila'),
    ('02.01.215', u'02.01.215 - Cloreto de dimetil carbamoila'),
    ('02.01.216', u'02.01.216 - Cloreto de enxofre'),
    ('02.01.217', u'02.01.217 - Cloreto de etila'),
    ('02.01.218', u'02.01.218 - Cloreto de fenila'),
    ('02.01.219', u'02.01.219 - Cloreto de hidrogênio'),
    ('02.01.220', u'02.01.220 - Cloreto de metila'),
    ('02.01.221', u'02.01.221 - Cloreto de metileno'),
    ('02.01.222', u'02.01.222 - Cloreto de polivinila'),
    ('02.01.223', u'02.01.223 - Cloreto de tionila'),
    ('02.01.224', u'02.01.224 - Cloreto de vinila'),
    ('02.01.225', u'02.01.225 - Cloreto de vinilideno'),
    ('02.01.226', u'02.01.226 - Cloreto de zinco, fumos'),
    ('02.01.227', u'02.01.227 - Clornafazina'),
    ('02.01.228', u'02.01.228 - Cloro'),
    ('02.01.229', u'02.01.229 - Cloroacetaldeído'),
    ('02.01.230', u'02.01.230 - 2-Cloroacetofenona'),
    ('02.01.231', u'02.01.231 - Cloroacetona'),
    ('02.01.232', u'02.01.232 - Cloroambucil'),
    ('02.01.233', u'02.01.233 - Clorobenzeno'),
    ('02.01.234', u'02.01.234 - o-Clorobenzilideno malononitrila'),
    ('02.01.235', u'02.01.235 - Clorobromometano'),
    ('02.01.236', u'02.01.236 - Clorodifenil (42% de Cloro)'),
    ('02.01.237', u'02.01.237 - Clorodifenil (54% de Cloro)'),
    ('02.01.238', u'02.01.238 - Clorodifluormetano'),
    ('02.01.239', u'02.01.239 - o-Cloroestireno'),
    ('02.01.240', u'02.01.240 - Cloroetano'),
    ('02.01.241', u'02.01.241 - Cloroetílico'),
    ('02.01.242', u'02.01.242 - Clorofórmio'),
    ('02.01.243', u'02.01.243 - 1-Cloro-1-nitropropano'),
    ('02.01.244', u'02.01.244 - 1-Cloro-2'),
    ('02.01.245', u'02.01.245 - Clorometileter'),
    ('02.01.246', u'02.01.246 - Cloropentafluoretano'),
    ('02.01.247', u'02.01.247 - Cloropicrina'),
    ('02.01.248', u'02.01.248 - Cloropirifos'),
    ('02.01.249', u'02.01.249 - Cloroprene'),
    ('02.01.250', u'02.01.250 - Cloropreno'),
    ('02.01.251', u'02.01.251 - ß-Cloropreno'),
    ('02.01.252', u'02.01.252 - 1-Cloro-2-propanol'),
    ('02.01.253', u'02.01.253 - 2-Cloro-1-propanol'),
    ('02.01.254', u'02.01.254 - o-Clorotolueno'),
    ('02.01.255', u'02.01.255 - Cobalto e seus compostos inorgânicos'),
    ('02.01.256', u'02.01.256 - Cobalto carbonila'),
    ('02.01.257', u'02.01.257 - Cobalto hidrocarbonila'),
    ('02.01.258', u'02.01.258 - Cobre'),
    ('02.01.259', u'02.01.259 - Coumafos'),
    ('02.01.260', u'02.01.260 - Cresol, todos os isômeros'),
    ('02.01.261', u'02.01.261 - Creosoto'),
    ('02.01.262', u'02.01.262 - Criseno'),
    ('02.01.263', u'02.01.263 - Cromato de terc-butila'),
    ('02.01.264', u'02.01.264 - Cromato de cálcio'),
    ('02.01.265', u'02.01.265 - Cromato de chumbo'),
    ('02.01.266', u'02.01.266 - Cromato de estrôncio'),
    ('02.01.267', u'02.01.267 - Cromatos de zinco'),
    ('02.01.268', u'02.01.268 - Cromita - processamento do minério (Cromato)'),
    ('02.01.269', u'02.01.269 - Cromo e seus compostos inorgânicos'),
    ('02.01.270', u'02.01.270 - Crotonaldeído'),
    ('02.01.271', u'02.01.271 - Crufomate'),
    ('02.01.272', u'02.01.272 - Cumeno'),
    ('02.01.273', u'02.01.273 - 2,4 D'),
    ('02.01.274', u'02.01.274 - DDD (diclorodifenildicloretano)'),
    ('02.01.275', u'02.01.275 - DDT'),
    ('02.01.276', u'02.01.276 - Decaborano'),
    ('02.01.277', u'02.01.277 - Demeton'),
    ('02.01.278', u'02.01.278 - Demeton-S-metila'),
    ('02.01.279', u'02.01.279 - Destilação do alcatrão de hulha'),
    ('02.01.280', u'02.01.280 - Diacetil'),
    ('02.01.281', u'02.01.281 - Diacetona álcool'),
    ('02.01.282', u'02.01.282 - Diamina'),
    ('02.01.283', u'02.01.283 - α,α"Diamina m-xileno'),
    ('02.01.284', u'02.01.284 - Dianizidina'),
    ('02.01.285', u'02.01.285 - Diazinon'),
    ('02.01.286', u'02.01.286 - Diazometano'),
    ('02.01.287', u'02.01.287 - Diborano'),
    ('02.01.288', u'02.01.288 - 1,2-Dibramoetano'),
    ('02.01.289', u'02.01.289 - Dibrometo de etileno'),
    ('02.01.290', u'02.01.290 - 2-N-Dibutilaminoetanol'),
    ('02.01.291', u'02.01.291 - Dibutilftalato'),
    ('02.01.292', u'02.01.292 - Diciclopentadieno'),
    ('02.01.293', u'02.01.293 - 1,1 Dicloreotileno'),
    ('02.01.294', u'02.01.294 - Dicloreto de etileno'),
    ('02.01.295', u'02.01.295 - Dicloreto de propileno'),
    ('02.01.296', u'02.01.296 - o-Diclorobenzeno'),
    ('02.01.297', u'02.01.297 - p-Diclorobenzeno'),
    ('02.01.298', u'02.01.298 - Diclorobenzidina'),
    ('02.01.299', u'02.01.299 - 3,3" -Diclorobenzidina'),
    ('02.01.300', u'02.01.300 - 1,4-Dicloro-2-buteno'),
    ('02.01.301', u'02.01.301 - Diclorodifluormetano'),
    ('02.01.302', u'02.01.302 - 1,3-Dicloro-5,5-dimetil hidantoina'),
    ('02.01.303', u'02.01.303 - 1,1-Dicloroetano'),
    ('02.01.304', u'02.01.304 - 1,2 Dicloroetano'),
    ('02.01.305', u'02.01.305 - 1,2 Dicloroetileno, todos os isômeros'),
    ('02.01.306', u'02.01.306 - Diclorofluormetano'),
    ('02.01.307', u'02.01.307 - Diclorometano'),
    ('02.01.308', u'02.01.308 - 1,1-Dicloro-1-nitroetano'),
    ('02.01.309', u'02.01.309 - 1,2 Dicloropropano (Dicloroacetileno)'),
    ('02.01.310', u'02.01.310 - 1,3-Dicloropropeno'),
    ('02.01.311', u'02.01.311 - Diclorotetrafluoretano'),
    ('02.01.312', u'02.01.312 - Diclorvos (DDVP)'),
    ('02.01.313', u'02.01.313 - Dicrotofós'),
    ('02.01.314', u'02.01.314 - Dieldrin'),
    ('02.01.315', u'02.01.315 - Diesel, combustível, como hidrocarbonetos totais'),
    ('02.01.316', u'02.01.316 - Dietanolamina'),
    ('02.01.317', u'02.01.317 - Dietilamina'),
    ('02.01.318', u'02.01.318 - 2-Dietilaminoetanol'),
    ('02.01.319', u'02.01.319 - Dietilcetona'),
    ('02.01.320', u'02.01.320 - Dietil éter'),
    ('02.01.321', u'02.01.321 - Dietileno triamina'),
    ('02.01.322', u'02.01.322 - Dietilestil-bestrol'),
    ('02.01.323', u'02.01.323 - Dietilestilbestrol'),
    ('02.01.324', u'02.01.324 - Dietilftalato'),
    ('02.01.325', u'02.01.325 - Dietilsulfato'),
    ('02.01.326', u'02.01.326 - Difenilamina'),
    ('02.01.327', u'02.01.327 - Difluordibromometano'),
    ('02.01.328', u'02.01.328 - Difluoreto de oxigênio'),
    ('02.01.329', u'02.01.329 - Dihidrocloreto de piperazina'),
    ('02.01.330', u'02.01.330 - Diisobutil cetona'),
    ('02.01.331', u'02.01.331 - Diisocianato de isoforona'),
    ('02.01.332', u'02.01.332 - 2,4 Diisocianato de tolueno (TDI)'),
    ('02.01.333', u'02.01.333 - Diisopropilamina'),
    ('02.01.334', u'02.01.334 - N,N-Dietilhidroxilamina'),
    ('02.01.335', u'02.01.335 - Dimetanosulfonato (MILERAN)'),
    ('02.01.336', u'02.01.336 - N,N-Dimetilacetamida'),
    ('02.01.337', u'02.01.337 - Dimetilacetamida'),
    ('02.01.338', u'02.01.338 - Dimetilamina'),
    ('02.01.339', u'02.01.339 - Dimetilanilina'),
    ('02.01.340', u'02.01.340 - Dimetiletoxisilano'),
    ('02.01.341', u'02.01.341 - Dimetilformamida'),
    ('02.01.342', u'02.01.342 - Dimetilftalato'),
    ('02.01.343', u'02.01.343 - 1,1-Dimetilhidrazina'),
    ('02.01.344', u'02.01.344 - Dimetilsulfato'),
    ('02.01.345', u'02.01.345 - Dinitrato de etileno glicol'),
    ('02.01.346', u'02.01.346 - Dinitrato de propileno glicol'),
    ('02.01.347', u'02.01.347 - Dinitrobenzeno, todos os isômeros'),
    ('02.01.348', u'02.01.348 - Dinitro-o-cresol'),
    ('02.01.349', u'02.01.349 - 3,5-Dinitro-o-toluamida'),
    ('02.01.350', u'02.01.350 - Dinitrotolueno'),
    ('02.01.351', u'02.01.351 - 1,4-Dioxano'),
    ('02.01.352', u'02.01.352 - Dioxation'),
    ('02.01.353', u'02.01.353 - Dióxido de carbono'),
    ('02.01.354', u'02.01.354 - Dióxido de cloro'),
    ('02.01.355', u'02.01.355 - Dióxido de enxofre'),
    ('02.01.356', u'02.01.356 - 1,3-Dioxolane'),
    ('02.01.357', u'02.01.357 - Dióxido de nitrogênio'),
    ('02.01.358', u'02.01.358 - Dióxido de titânio'),
    ('02.01.359', u'02.01.359 - Dióxido de vinilciclohexano'),
    ('02.01.360', u'02.01.360 - Dipropil cetona'),
    ('02.01.361', u'02.01.361 - Diquat'),
    ('02.01.362', u'02.01.362 - Dissulfeto de alil propila'),
    ('02.01.363', u'02.01.363 - Dissulfeto de carbono'),
    ('02.01.364', u'02.01.364 - Dissulfeto de dimetila'),
    ('02.01.365', u'02.01.365 - Dissulfiram'),
    ('02.01.366', u'02.01.366 - Dissulfoton'),
    ('02.01.367', u'02.01.367 - Diuron'),
    ('02.01.368', u'02.01.368 - Divinil benzeno'),
    ('02.01.369', u'02.01.369 - Dodecil mercaptana'),
    ('02.01.370', u'02.01.370 - Endosulfan'),
    ('02.01.371', u'02.01.371 - Endrin'),
    ('02.01.372', u'02.01.372 - Enflurano'),
    ('02.01.373', u'02.01.373 - Epicloridrina'),
    ('02.01.374', u'02.01.374 - EPN'),
    ('02.01.375', u'02.01.375 - Erionita'),
    ('02.01.376', u'02.01.376 - Estanho e seus compostos'),
    ('02.01.377', u'02.01.377 - Estearatos(J)'),
    ('02.01.378', u'02.01.378 - Estibina'),
    ('02.01.379', u'02.01.379 - Estilbenzeno'),
    ('02.01.380', u'02.01.380 - Estireno'),
    ('02.01.381', u'02.01.381 - Estriquinina'),
    ('02.01.382', u'02.01.382 - Etano'),
    ('02.01.383', u'02.01.383 - Etanol'),
    ('02.01.384', u'02.01.384 - Etanolamina'),
    ('02.01.385', u'02.01.385 - Etanotiol'),
    ('02.01.386', u'02.01.386 - Éter alil glicidílico'),
    ('02.01.387', u'02.01.387 - Éter n-Butil glicidílico'),
    ('02.01.388', u'02.01.388 - Éter bis-(Clorometílico) ou Bis (cloro metil) éter'),
    ('02.01.389', u'02.01.389 - Éter bis (2-dimetilaminoetil)'),
    ('02.01.390', u'02.01.390 - Éter dicloroetílico'),
    ('02.01.391', u'02.01.391 - Éter diglicidílico'),
    ('02.01.392', u'02.01.392 - Éter etil terc-butílico'),
    ('02.01.393', u'02.01.393 - Éter etílico'),
    ('02.01.394', u'02.01.394 - Éter fenílico, vapor'),
    ('02.01.395', u'02.01.395 - Éter fenil glicidílico'),
    ('02.01.396', u'02.01.396 - Éter isopropil glicidílico (IGE)'),
    ('02.01.397', u'02.01.397 - Éter isopropílico'),
    ('02.01.398', u'02.01.398 - Éter isopropílico de monoetileno glicol'),
    ('02.01.399', u'02.01.399 - Éter metil terc-amílico'),
    ('02.01.400', u'02.01.400 - Éter metil terc-butílico (MTBE)'),
    ('02.01.401', u'02.01.401 - Éter metílico de clorometila'),
    ('02.01.402', u'02.01.402 - Éter metílico de dipropilenoglicol (DPGME)'),
    ('02.01.403', u'02.01.403 - Éter monobutílico de dietileno glicol'),
    ('02.01.404', u'02.01.404 - Éter monobutílico do etileno glicol'),
    ('02.01.405', u'02.01.405 - Éter monoetílico do etileno glicol'),
    ('02.01.406', u'02.01.406 - Éter monometílico do etileno glicol'),
    ('02.01.407', u'02.01.407 - Etil amil cetona'),
    ('02.01.408', u'02.01.408 - Etil butil cetona'),
    ('02.01.409', u'02.01.409 - Etil mercaptana'),
    ('02.01.410', u'02.01.410 - n-Etil morfolina'),
    ('02.01.411', u'02.01.411 - Etilamina'),
    ('02.01.412', u'02.01.412 - Etilbenzeno'),
    ('02.01.413', u'02.01.413 - Etileno'),
    ('02.01.414', u'02.01.414 - Etilenoamina'),
    ('02.01.415', u'02.01.415 - Etilenotiureia'),
    ('02.01.416', u'02.01.416 - Etileno cloridrina'),
    ('02.01.417', u'02.01.417 - Etileno diamina'),
    ('02.01.418', u'02.01.418 - Etileno glicol'),
    ('02.01.419', u'02.01.419 - Etilideno norborneno'),
    ('02.01.420', u'02.01.420 - Etil isocianato'),
    ('02.01.421', u'02.01.421 - Etilenoimina'),
    ('02.01.422', u'02.01.422 - Etilnitrosuréias'),
    ('02.01.423', u'02.01.423 - Etion'),
    ('02.01.424', u'02.01.424 - Etoposide'),
    ('02.01.425', u'02.01.425 - Etoposide em associação com cisplatina e bleomicina'),
    ('02.01.426', u'02.01.426 - 2-Etoxietanol'),
    ('02.01.427', u'02.01.427 - Farinha (poeiras)'),
    ('02.01.428', u'02.01.428 - Fenacetina'),
    ('02.01.429', u'02.01.429 - Fenamifos'),
    ('02.01.430', u'02.01.430 - n-Fenil-ß-naftilamina'),
    ('02.01.431', u'02.01.431 - o-Fenileno diamina'),
    ('02.01.432', u'02.01.432 - m-Fenileno diamina'),
    ('02.01.433', u'02.01.433 - p-Fenileno diamina'),
    ('02.01.434', u'02.01.434 - Fenilfosfina'),
    ('02.01.435', u'02.01.435 - Fenilhidrazina'),
    ('02.01.436', u'02.01.436 - Fenil mercaptana'),
    ('02.01.437', u'02.01.437 - Fenol'),
    ('02.01.438', u'02.01.438 - Fenotiazine'),
    ('02.01.439', u'02.01.439 - Fensulfotion'),
    ('02.01.440', u'02.01.440 - Fention'),
    ('02.01.441', u'02.01.441 - Ferbam'),
    ('02.01.442', u'02.01.442 - Ferro, sais solúveis'),
    ('02.01.443', u'02.01.443 - Ferro diciclopentadienila'),
    ('02.01.444', u'02.01.444 - Ferro, óxido (Fe2O3)'),
    ('02.01.445', u'02.01.445 - Ferro pentacarbonila'),
    ('02.01.446', u'02.01.446 - Ferrovanádio, poeira'),
    ('02.01.447', u'02.01.447 - Fibras Vítreas Sintéticas'),
    ('02.01.448', u'02.01.448 - Flúor'),
    ('02.01.449', u'02.01.449 - Fluoracetato de sódio'),
    ('02.01.450', u'02.01.450 - Fluoretos, como F'),
    ('02.01.451', u'02.01.451 - Fluoreto de carbonila'),
    ('02.01.452', u'02.01.452 - Fluoreto de hidrogênio'),
    ('02.01.453', u'02.01.453 - Fluoreto de perclorila'),
    ('02.01.454', u'02.01.454 - Fluoreto de sulfurila'),
    ('02.01.455', u'02.01.455 - Fluoreto de vinila'),
    ('02.01.456', u'02.01.456 - Fluoreto de vinilideno'),
    ('02.01.457', u'02.01.457 - Fonofos'),
    ('02.01.458', u'02.01.458 - Forate'),
    ('02.01.459', u'02.01.459 - Formaldeído'),
    ('02.01.460', u'02.01.460 - Formamida'),
    ('02.01.461', u'02.01.461 - Formiato de etila'),
    ('02.01.462', u'02.01.462 - Formiato de metila'),
    ('02.01.463', u'02.01.463 - Fosfato de dibutila'),
    ('02.01.464', u'02.01.464 - Fosfato de dibutil fenila'),
    ('02.01.465', u'02.01.465 - Fosfato de tributila'),
    ('02.01.466', u'02.01.466 - Fosfato de trifenila'),
    ('02.01.467', u'02.01.467 - Fosfato de triortocresila'),
    ('02.01.468', u'02.01.468 - Fosfina'),
    ('02.01.469', u'02.01.469 - Fosfito de trimetila'),
    ('02.01.470', u'02.01.470 - Fósforo (amarelo)'),
    ('02.01.471', u'02.01.471 - Fosgênio'),
    ('02.01.472', u'02.01.472 - Fluortriclorometano (freon 11)'),
    ('02.01.473', u'02.01.473 - Freon 12'),
    ('02.01.474', u'02.01.474 - Freon 22'),
    ('02.01.475', u'02.01.475 - Freon 113'),
    ('02.01.476', u'02.01.476 - Freon 114'),
    ('02.01.477', u'02.01.477 - Ftalato de dibutila'),
    ('02.01.478', u'02.01.478 - Ftalato de di(2-etilhexila)'),
    ('02.01.479', u'02.01.479 - Ftalato de dietila'),
    ('02.01.480', u'02.01.480 - m-Ftalodinitrila'),
    ('02.01.481', u'02.01.481 - o-Ftalodinitrila'),
    ('02.01.482', u'02.01.482 - Furfural'),
    ('02.01.483', u'02.01.483 - Gás amoníaco'),
    ('02.01.484', u'02.01.484 - Gás carbônico'),
    ('02.01.485', u'02.01.485 - Gás cianídrico'),
    ('02.01.486', u'02.01.486 - Gás clorídrico'),
    ('02.01.487', u'02.01.487 - Gás Mostarda'),
    ('02.01.488', u'02.01.488 - Gás natural'),
    ('02.01.489', u'02.01.489 - Gás sulfídrico'),
    ('02.01.490', u'02.01.490 - Gasolina'),
    ('02.01.491', u'02.01.491 - Glicerina, névoas'),
    ('02.01.492', u'02.01.492 - Glicidol'),
    ('02.01.493', u'02.01.493 - Glioxal'),
    ('02.01.494', u'02.01.494 - GLP (gás liquefeito do petróleo)'),
    ('02.01.495', u'02.01.495 - Glutaraldeído, ativado e não ativado'),
    ('02.01.496', u'02.01.496 - Grafite (todas as formas, exceto fibras de grafite)'),
    ('02.01.497', u'02.01.497 - Grãos, poeira (aveia, trigo, cevada)'),
    ('02.01.498', u'02.01.498 - Háfnio e seus compostos'),
    ('02.01.499', u'02.01.499 - halogenados'),
    ('02.01.500', u'02.01.500 - Halotano'),
    ('02.01.501', u'02.01.501 - Hélio'),
    ('02.01.502', u'02.01.502 - Heptacloro'),
    ('02.01.503', u'02.01.503 - Heptacloro epóxido'),
    ('02.01.504', u'02.01.504 - Heptano, todos os isômeros'),
    ('02.01.505', u'02.01.505 - Hexaclorobenzeno'),
    ('02.01.506', u'02.01.506 - Hexaclorobutadieno'),
    ('02.01.507', u'02.01.507 - Hexaclorociclopentadieno'),
    ('02.01.508', u'02.01.508 - Hexacloroetano'),
    ('02.01.509', u'02.01.509 - Hexacloronaftaleno'),
    ('02.01.510', u'02.01.510 - Hexafluoracetona'),
    ('02.01.511', u'02.01.511 - Hexafluorpropileno'),
    ('02.01.512', u'02.01.512 - Hexafluoreto de enxofre'),
    ('02.01.513', u'02.01.513 - Hexafluoreto de selênio'),
    ('02.01.514', u'02.01.514 - Hexafluoreto de telúrio'),
    ('02.01.515', u'02.01.515 - Hexametileno diisocianato (HDI)'),
    ('02.01.516', u'02.01.516 - Hexametil fosforamida'),
    ('02.01.517', u'02.01.517 - n-Hexano'),
    ('02.01.518', u'02.01.518 - Hexano, outros isômeros que não o n-Hexano'),
    ('02.01.519', u'02.01.519 - 1,6-Hexanodiamina'),
    ('02.01.520', u'02.01.520 - 1-Hexeno'),
    ('02.01.521', u'02.01.521 - Hexileno glicol'),
    ('02.01.522', u'02.01.522 - Hidrazina'),
    ('02.01.523', u'02.01.523 - Hidreto de antimônio (Estibina)'),
    ('02.01.524', u'02.01.524 - Hidreto de lítio'),
    ('02.01.525', u'02.01.525 - Hidrocarbonetos alifáticos gasosos Alcanos'),
    ('02.01.526', u'02.01.526 - Hidrocarbonetos e outros compostos de carbono'),
    ('02.01.527', u'02.01.527 - hidrocarbonetos aromáticos'),
    ('02.01.528', u'02.01.528 - hidrocarbonetos cíclicos'),
    ('02.01.529', u'02.01.529 - Hidrogênio'),
    ('02.01.530', u'02.01.530 - Hidroquinona'),
    ('02.01.531', u'02.01.531 - Hidróxido de cálcio'),
    ('02.01.532', u'02.01.532 - Hidróxido de césio'),
    ('02.01.533', u'02.01.533 - Hidróxido de potássio'),
    ('02.01.534', u'02.01.534 - Hidróxido de sódio'),
    ('02.01.535', u'02.01.535 - Hidroxitolueno butilado'),
    ('02.01.536', u'02.01.536 - Indeno'),
    ('02.01.537', u'02.01.537 - Iodeto de metila'),
    ('02.01.538', u'02.01.538 - Índio e seus compostos'),
    ('02.01.539', u'02.01.539 - Iodo'),
    ('02.01.540', u'02.01.540 - Iodetos'),
    ('02.01.541', u'02.01.541 - Iodofórmio'),
    ('02.01.542', u'02.01.542 - Isobutanol'),
    ('02.01.543', u'02.01.543 - Isobuteno'),
    ('02.01.544', u'02.01.544 - isocianato'),
    ('02.01.545', u'02.01.545 - Isocianato de metila'),
    ('02.01.546', u'02.01.546 - Isoforona'),
    ('02.01.547', u'02.01.547 - Isopropilamina'),
    ('02.01.548', u'02.01.548 - n-Isopropilanilina'),
    ('02.01.549', u'02.01.549 - Isopropil benzeno'),
    ('02.01.550', u'02.01.550 - 2-Isopropoxietanol'),
    ('02.01.551', u'02.01.551 - Ítrio e compostos'),
    ('02.01.552', u'02.01.552 - Lactato de n-butila'),
    ('02.01.553', u'02.01.553 - Lindano'),
    ('02.01.554', u'02.01.554 - Madeira, poeiras'),
    ('02.01.555', u'02.01.555 - Malation'),
    ('02.01.556', u'02.01.556 - Manganês e seus compostos'),
    ('02.01.557', u'02.01.557 - Manganês ciclopentadienil tricarbonila'),
    ('02.01.558', u'02.01.558 - Melfalano'),
    ('02.01.559', u'02.01.559 - Mercaptanos'),
    ('02.01.560', u'02.01.560 - Mercúrio e seus compostos'),
    ('02.01.561', u'02.01.561 - Metabisulfito de sódio'),
    ('02.01.562', u'02.01.562 - Metacrilato de metila'),
    ('02.01.563', u'02.01.563 - Metano'),
    ('02.01.564', u'02.01.564 - Metanol'),
    ('02.01.565', u'02.01.565 - Metil acetileno'),
    ('02.01.566', u'02.01.566 - Metil acetileno-propadieno, mistura (MAPP)'),
    ('02.01.567', u'02.01.567 - Metilacrilonitrila'),
    ('02.01.568', u'02.01.568 - Metilal'),
    ('02.01.569', u'02.01.569 - Metilamina'),
    ('02.01.570', u'02.01.570 - Metil n-amil cetona'),
    ('02.01.571', u'02.01.571 - n-Metil anilina'),
    ('02.01.572', u'02.01.572 - Metil n-butil cetona'),
    ('02.01.573', u'02.01.573 - Metil cellosolve'),
    ('02.01.574', u'02.01.574 - Metilciclohexano'),
    ('02.01.575', u'02.01.575 - Metilciclohexanol'),
    ('02.01.576', u'02.01.576 - o-Metilciclohexanona'),
    ('02.01.577', u'02.01.577 - 2-Metilciclopentadienil manganês tricarbonila'),
    ('02.01.578', u'02.01.578 - Metil clorofórmio'),
    ('02.01.579', u'02.01.579 - Metil demeton'),
    ('02.01.580', u'02.01.580 - Metil etil cetona (MEK)'),
    ('02.01.581', u'02.01.581 - α-Metil estireno'),
    ('02.01.582', u'02.01.582 - Metil hidrazina'),
    ('02.01.583', u'02.01.583 - Metil isoamil cetona'),
    ('02.01.584', u'02.01.584 - Metil isobutil carbinol'),
    ('02.01.585', u'02.01.585 - Metil isobutil cetona'),
    ('02.01.586', u'02.01.586 - Metil isopropil cetona'),
    ('02.01.587', u'02.01.587 - Metil mercaptana'),
    ('02.01.588', u'02.01.588 - 1-Metil naftaleno'),
    ('02.01.589', u'02.01.589 - 2-Metil naftaleno'),
    ('02.01.590', u'02.01.590 - Metil paration'),
    ('02.01.591', u'02.01.591 - Metil propil cetona'),
    ('02.01.592', u'02.01.592 - Metil vinil cetona'),
    ('02.01.593', u'02.01.593 - Metileno-bis-(4-ciclohexilisocianato)'),
    ('02.01.594', u'02.01.594 - 4,4-metileno-bis-(2-cloroanilina) (MOCA®) (MBOCA®)'),
    ('02.01.595', u'02.01.595 - Metileno bisfenil isocianato (MDI)'),
    ('02.01.596', u'02.01.596 - 4,4"-Metileno dianilina'),
    ('02.01.597', u'02.01.597 - Metileno-ortocloroanilina (MOCA)'),
    ('02.01.598', u'02.01.598 - Metomil'),
    ('02.01.599', u'02.01.599 - Metoxicloro'),
    ('02.01.600', u'02.01.600 - 2-Metoxietanol (EGME)'),
    ('02.01.601', u'02.01.601 - (2-Metoximetiletoxi) propanol (DPGME)'),
    ('02.01.602', u'02.01.602 - 4-Metoxifenol'),
    ('02.01.603', u'02.01.603 - 1-Metoxi-2-propanol'),
    ('02.01.604', u'02.01.604 - Metoxsalen associado com radiação ultravioleta A'),
    ('02.01.605', u'02.01.605 - Monometil hidrazina'),
    ('02.01.606', u'02.01.606 - Metribuzin'),
    ('02.01.607', u'02.01.607 - Mevinfos'),
    ('02.01.608', u'02.01.608 - Mica'),
    ('02.01.609', u'02.01.609 - Molibdênio'),
    ('02.01.610', u'02.01.610 - Monocrotofós'),
    ('02.01.611', u'02.01.611 - Monóxido de carbono'),
    ('02.01.612', u'02.01.612 - Morfolina'),
    ('02.01.613', u'02.01.613 - Naftaleno'),
    ('02.01.614', u'02.01.614 - ß-Naftilamina (Betanaftilamina)'),
    ('02.01.615', u'02.01.615 - naftóis'),
    ('02.01.616', u'02.01.616 - Naled'),
    ('02.01.617', u'02.01.617 - Negro de fumo'),
    ('02.01.618', u'02.01.618 - Neônio'),
    ('02.01.619', u'02.01.619 - Nicotina'),
    ('02.01.620', u'02.01.620 - Níquel e seus compostos'),
    ('02.01.621', u'02.01.621 - Nitrapirin'),
    ('02.01.622', u'02.01.622 - Nitrato de n-propila'),
    ('02.01.623', u'02.01.623 - Nitrito de isobutila'),
    ('02.01.624', u'02.01.624 - p-Nitroanilina'),
    ('02.01.625', u'02.01.625 - Nitrobenzeno'),
    ('02.01.626', u'02.01.626 - p-Nitroclorobenzeno'),
    ('02.01.627', u'02.01.627 - nitroderivados'),
    ('02.01.628', u'02.01.628 - 4 - Nitrodifenil'),
    ('02.01.629', u'02.01.629 - 4-Nitrodifenila'),
    ('02.01.630', u'02.01.630 - Nitroetano'),
    ('02.01.631', u'02.01.631 - Nitrogênio'),
    ('02.01.632', u'02.01.632 - Nitroglicerina'),
    ('02.01.633', u'02.01.633 - Nitrometano'),
    ('02.01.634', u'02.01.634 - Nitronaftilamina 4-Dimetil-aminoazobenzeno'),
    ('02.01.635', u'02.01.635 - 1-Nitropropano'),
    ('02.01.636', u'02.01.636 - 2-Nitropropano'),
    ('02.01.637', u'02.01.637 - Nitrosamina'),
    ('02.01.638', u'02.01.638 - n-Nitrosodimetilamina'),
    ('02.01.639', u'02.01.639 - N"-nitrosonornicotina (NNN) e 4-. (metilnitrosamino)-1-(3-piridil)1-butano- na (NNK)'),
    ('02.01.640', u'02.01.640 - Nitrotolueno, todos os isômeros'),
    ('02.01.641', u'02.01.641 - 5-Nitro-o-toluidina'),
    ('02.01.642', u'02.01.642 - Nonano'),
    ('02.01.643', u'02.01.643 - Octacloronaftaleno'),
    ('02.01.644', u'02.01.644 - Octano, todos os isômeros'),
    ('02.01.645', u'02.01.645 - Óleo diesel, como hidrocarbonetos totais'),
    ('02.01.646', u'02.01.646 - Óleo mineral, excluídos os fluídos de trabalho com metais'),
    ('02.01.647', u'02.01.647 - óleo queimado'),
    ('02.01.648', u'02.01.648 - Óleos de xisto'),
    ('02.01.649', u'02.01.649 - Ortotoluidina'),
    ('02.01.650', u'02.01.650 - p,p"-Oxibis(benzeno sulfonila hidrazida)'),
    ('02.01.651', u'02.01.651 - Oxicloreto de fósforo'),
    ('02.01.652', u'02.01.652 - Óxido de boro'),
    ('02.01.653', u'02.01.653 - Óxido de cálcio'),
    ('02.01.654', u'02.01.654 - Óxido de difenila o-clorada'),
    ('02.01.655', u'02.01.655 - Óxido de etileno'),
    ('02.01.656', u'02.01.656 - Óxido de magnésio'),
    ('02.01.657', u'02.01.657 - Óxido de mesitila'),
    ('02.01.658', u'02.01.658 - Óxido de propileno'),
    ('02.01.659', u'02.01.659 - Óxido de zinco'),
    ('02.01.660', u'02.01.660 - Óxido nítrico'),
    ('02.01.661', u'02.01.661 - Óxido nitroso'),
    ('02.01.662', u'02.01.662 - Oxime-talona'),
    ('02.01.663', u'02.01.663 - Ozona'),
    ('02.01.664', u'02.01.664 - Ozônio'),
    ('02.01.665', u'02.01.665 - Parafina, cera (fumos)'),
    ('02.01.666', u'02.01.666 - Paraquat, como o cátion'),
    ('02.01.667', u'02.01.667 - Paration'),
    ('02.01.668', u'02.01.668 - Partículados (insolúveis ou de baixa solubilidade) não especificados de outra maneira (PNOS)'),
    ('02.01.669', u'02.01.669 - Pentaborano'),
    ('02.01.670', u'02.01.670 - Pentacloreto de fósforo'),
    ('02.01.671', u'02.01.671 - 3, 4, 5, 3´, 4" -Pentaclorobifenil (PCB - 126)'),
    ('02.01.672', u'02.01.672 - 2 ,3 ,4 ,7 ,8-Pentaclorodibenzofurano'),
    ('02.01.673', u'02.01.673 - Pentaclorofenol'),
    ('02.01.674', u'02.01.674 - Pentacloronaftaleno'),
    ('02.01.675', u'02.01.675 - Pentacloronitrobenzeno'),
    ('02.01.676', u'02.01.676 - Pentaeritritol'),
    ('02.01.677', u'02.01.677 - Pentafluoreto de bromo'),
    ('02.01.678', u'02.01.678 - Pentafluoreto de enxofre'),
    ('02.01.679', u'02.01.679 - n-Pentano'),
    ('02.01.680', u'02.01.680 - Pentano, todos os isômeros'),
    ('02.01.681', u'02.01.681 - 2,4-Pentanodiona'),
    ('02.01.682', u'02.01.682 - Pentassulfeto de fósforo'),
    ('02.01.683', u'02.01.683 - Pentóxido de vanádio'),
    ('02.01.684', u'02.01.684 - Percloroetileno (Tetracloroetileno)'),
    ('02.01.685', u'02.01.685 - Perclorometil mercaptana'),
    ('02.01.686', u'02.01.686 - Perfluorobutil etileno'),
    ('02.01.687', u'02.01.687 - Perfluorisobutileno'),
    ('02.01.688', u'02.01.688 - Perfluoroctanoato de amônio'),
    ('02.01.689', u'02.01.689 - Peróxido de benzoíla'),
    ('02.01.690', u'02.01.690 - Peróxido de hidrogênio'),
    ('02.01.691', u'02.01.691 - Peróxido de metil etil cetona'),
    ('02.01.692', u'02.01.692 - Persulfatos, como persulfato'),
    ('02.01.693', u'02.01.693 - Petróleo e seus derivados'),
    ('02.01.694', u'02.01.694 - Picloram'),
    ('02.01.695', u'02.01.695 - Pindone'),
    ('02.01.696', u'02.01.696 - Pirperazina e sais, como Piperazia'),
    ('02.01.697', u'02.01.697 - Piretro'),
    ('02.01.698', u'02.01.698 - Piridina'),
    ('02.01.699', u'02.01.699 - Pirofosfato de tetraetila'),
    ('02.01.700', u'02.01.700 - Platina e sais solúveis'),
    ('02.01.701', u'02.01.701 - Plutônio'),
    ('02.01.702', u'02.01.702 - poliisocianetos'),
    ('02.01.703', u'02.01.703 - poliuretanas'),
    ('02.01.704', u'02.01.704 - 3-Poxipro-pano'),
    ('02.01.705', u'02.01.705 - Prata e seus compostos'),
    ('02.01.706', u'02.01.706 - Procarbazina'),
    ('02.01.707', u'02.01.707 - Propano'),
    ('02.01.708', u'02.01.708 - n-propano'),
    ('02.01.709', u'02.01.709 - Propanona'),
    ('02.01.710', u'02.01.710 - Propano sultona'),
    ('02.01.711', u'02.01.711 - Propano sultone'),
    ('02.01.712', u'02.01.712 - Propanosultona'),
    ('02.01.713', u'02.01.713 - n-Propanol'),
    ('02.01.714', u'02.01.714 - iso-Propanol'),
    ('02.01.715', u'02.01.715 - 2-Propanol'),
    ('02.01.716', u'02.01.716 - Propileno'),
    ('02.01.717', u'02.01.717 - Propileno imina'),
    ('02.01.718', u'02.01.718 - ß-Propiolactona (Beta-propiolactona)'),
    ('02.01.719', u'02.01.719 - Propionaldeído'),
    ('02.01.720', u'02.01.720 - Propoxur'),
    ('02.01.721', u'02.01.721 - PVC (poli cloreto de vinila)'),
    ('02.01.722', u'02.01.722 - Querosene combustível de avião, como vapor de hidrocarbonetos totais'),
    ('02.01.723', u'02.01.723 - Quinona'),
    ('02.01.724', u'02.01.724 - Rádio-224 e seus produtos de decaimento'),
    ('02.01.725', u'02.01.725 - Rádio-226 e seus produtos de decaimento'),
    ('02.01.726', u'02.01.726 - Rádio-228 e seus produtos de decaimento'),
    ('02.01.727', u'02.01.727 - Radônio-222 e seus produtos de decaimento'),
    ('02.01.728', u'02.01.728 - Resina de vareta (eletrodo arame) de solda, produtos da decomposição térmica (breu)'),
    ('02.01.729', u'02.01.729 - Resorcinol'),
    ('02.01.730', u'02.01.730 - Ródio e seus compostos'),
    ('02.01.731', u'02.01.731 - Ronel'),
    ('02.01.732', u'02.01.732 - Rotenona (comercial)'),
    ('02.01.733', u'02.01.733 - Sacarose'),
    ('02.01.734', u'02.01.734 - Seleneto de hidrogênio'),
    ('02.01.735', u'02.01.735 - Selênio e seus compostos'),
    ('02.01.736', u'02.01.736 - Semustina [1-(2 -cloroetil) -3-(4-metilciclohexil)-1-nitrosourea, Metil CC- NU]'),
    ('02.01.737', u'02.01.737 - Sesone'),
    ('02.01.738', u'02.01.738 - Sílica Cristalina - α-quartzo e cristobalita'),
    ('02.01.739', u'02.01.739 - Sílica livre'),
    ('02.01.740', u'02.01.740 - Sílica cristobalita'),
    ('02.01.741', u'02.01.741 - Silicato de cálcio, sintético não fibroso'),
    ('02.01.742', u'02.01.742 - Silicato de etila'),
    ('02.01.743', u'02.01.743 - Silicato de metila'),
    ('02.01.744', u'02.01.744 - Silicatos'),
    ('02.01.745', u'02.01.745 - Subtilisins, como enzima cristalina ativa'),
    ('02.01.746', u'02.01.746 - Sulfamato de amônio'),
    ('02.01.747', u'02.01.747 - Sulfato de bário'),
    ('02.01.748', u'02.01.748 - Sulfato de cálcio'),
    ('02.01.749', u'02.01.749 - Sulfato de dimetila'),
    ('02.01.750', u'02.01.750 - Sulfato de carbonila'),
    ('02.01.751', u'02.01.751 - Sulfeto de hidrogênio'),
    ('02.01.752', u'02.01.752 - Sulfeto de dimetila'),
    ('02.01.753', u'02.01.753 - sulfeto de níquel'),
    ('02.01.754', u'02.01.754 - Sulfometuron metil'),
    ('02.01.755', u'02.01.755 - Sulfotep (TEDP)'),
    ('02.01.756', u'02.01.756 - Sulprofos'),
    ('02.01.757', u'02.01.757 - Systox'),
    ('02.01.758', u'02.01.758 - 2,4,5-T'),
    ('02.01.759', u'02.01.759 - Talco'),
    ('02.01.760', u'02.01.760 - Tálio, e compostos, como TI'),
    ('02.01.761', u'02.01.761 - Tamoxifeno (nota: há evidências também conclusivas para seu uso na re- dução do risco de câncer de mama contralateral em pacientes com câncer de mama)'),
    ('02.01.762', u'02.01.762 - Telureto de bismuto'),
    ('02.01.763', u'02.01.763 - Telúrio e compostos (NOS), como Te, excluído telureto de hidrogênio'),
    ('02.01.764', u'02.01.764 - Temefós'),
    ('02.01.765', u'02.01.765 - Terbufos'),
    ('02.01.766', u'02.01.766 - Terebentina e monoterpenos selecionados'),
    ('02.01.767', u'02.01.767 - Terfenilas (o,m,p-isômeros)'),
    ('02.01.768', u'02.01.768 - Terfenilas hidrogenadas (não irradiadas)'),
    ('02.01.769', u'02.01.769 - 1,1,2,2,Tetrabromoetano'),
    ('02.01.770', u'02.01.770 - Tetrabrometo de acetileno (1,1,2,2-Tetrabromoetano)'),
    ('02.01.771', u'02.01.771 - Tetrabrometo de carbono'),
    ('02.01.772', u'02.01.772 - Tetracloreto de carbono'),
    ('02.01.773', u'02.01.773 - 2,3,7,8-Tetraclorodibenzo-para-dioxina'),
    ('02.01.774', u'02.01.774 - 1,1,1,2-Tetracloro-2,2-difluoretano'),
    ('02.01.775', u'02.01.775 - 1,1,2,2-Tetracloro-1,2-difluoretano'),
    ('02.01.776', u'02.01.776 - 1,1,2,2-Tetracloroetano'),
    ('02.01.777', u'02.01.777 - Tetracloroetano'),
    ('02.01.778', u'02.01.778 - Tetracloronaftaleno'),
    ('02.01.779', u'02.01.779 - Tetracloroetileno'),
    ('02.01.780', u'02.01.780 - Tetrafluoretileno'),
    ('02.01.781', u'02.01.781 - Tetrafluoreto de enxofre'),
    ('02.01.782', u'02.01.782 - Tetrahidreto de germânio'),
    ('02.01.783', u'02.01.783 - Tetrahidreto de silício'),
    ('02.01.784', u'02.01.784 - Tetrahidrofurano'),
    ('02.01.785', u'02.01.785 - Tetraquis (hidroximetil) fosfônio, sais - Cloreto de tetraquis (hidroximetil) fosfônio'),
    ('02.01.786', u'02.01.786 - Tetraquis (hidroximetil) fosfônio, sais - Sulfato de tetraquis (hidroximetil) fosfônio'),
    ('02.01.787', u'02.01.787 - Tetrametil succinonitrila'),
    ('02.01.788', u'02.01.788 - Tetranitrometano'),
    ('02.01.789', u'02.01.789 - Tetril'),
    ('02.01.790', u'02.01.790 - Tetróxido de ósmio'),
    ('02.01.791', u'02.01.791 - Thiram'),
    ('02.01.792', u'02.01.792 - Tiotepa'),
    ('02.01.793', u'02.01.793 - Titânio'),
    ('02.01.794', u'02.01.794 - 4,4"-Tiobis (6-terc-butil-m-cresol)'),
    ('02.01.795', u'02.01.795 - o-Tolidina'),
    ('02.01.796', u'02.01.796 - Tolueno'),
    ('02.01.797', u'02.01.797 - Tolueno 2,4 ou 2,6 -diisocianato (ou como mistura)'),
    ('02.01.798', u'02.01.798 - o-Toluidina'),
    ('02.01.799', u'02.01.799 - m-Toluidina'),
    ('02.01.800', u'02.01.800 - p-Toluidina'),
    ('02.01.801', u'02.01.801 - Tório-232 e seus produtos de decaimento'),
    ('02.01.802', u'02.01.802 - Tribrometo de boro'),
    ('02.01.803', u'02.01.803 - Tribromometano'),
    ('02.01.804', u'02.01.804 - Tricloreto de fósforo'),
    ('02.01.805', u'02.01.805 - Tricloreto de vinila'),
    ('02.01.806', u'02.01.806 - Triclorfon'),
    ('02.01.807', u'02.01.807 - Triclorometil benzeno'),
    ('02.01.808', u'02.01.808 - 1,1,2-Tricloro-1,2,2-trifluoretano'),
    ('02.01.809', u'02.01.809 - 1,2,4-Triclorobenzeno'),
    ('02.01.810', u'02.01.810 - 1,1,1 Tricloroetano'),
    ('02.01.811', u'02.01.811 - 1,1,2-Tricloroetano'),
    ('02.01.812', u'02.01.812 - Tricloroetileno'),
    ('02.01.813', u'02.01.813 - Triclorometano'),
    ('02.01.814', u'02.01.814 - Triclorofluormetano'),
    ('02.01.815', u'02.01.815 - Tricloronaftaleno'),
    ('02.01.816', u'02.01.816 - 1,2,3-Tricloropropano'),
    ('02.01.817', u'02.01.817 - Trietanolamina'),
    ('02.01.818', u'02.01.818 - Trietilamina'),
    ('02.01.819', u'02.01.819 - Trifluorbromometano'),
    ('02.01.820', u'02.01.820 - Trifluoreto de boro'),
    ('02.01.821', u'02.01.821 - Trifluoreto de cloro'),
    ('02.01.822', u'02.01.822 - Trifluoreto de nitrogênio'),
    ('02.01.823', u'02.01.823 - Trifluormonobramometano'),
    ('02.01.824', u'02.01.824 - 1,3,5-Triglicidil-s-triazinetriona'),
    ('02.01.825', u'02.01.825 - Trimetilamina'),
    ('02.01.826', u'02.01.826 - Trimetil benzeno (mistura de isômeros)'),
    ('02.01.827', u'02.01.827 - 2,4,6-Trinitrotolueno'),
    ('02.01.828', u'02.01.828 - trióxido de amônio'),
    ('02.01.829', u'02.01.829 - Trióxido de antimônio - Produção'),
    ('02.01.830', u'02.01.830 - Tungstênio e seus compostos'),
    ('02.01.831', u'02.01.831 - Urânio (natural) Compostos solúveis e insolúveis'),
    ('02.01.832', u'02.01.832 - n-Valeraldeído'),
    ('02.01.833', u'02.01.833 - Vinibenzeno'),
    ('02.01.834', u'02.01.834 - 4-Vinilciclohexeno'),
    ('02.01.835', u'02.01.835 - n-Vinil-2-pirrolidone'),
    ('02.01.836', u'02.01.836 - Vinil tolueno'),
    ('02.01.837', u'02.01.837 - Warfarin'),
    ('02.01.838', u'02.01.838 - Xileno (o, m e p isômeros)'),
    ('02.01.839', u'02.01.839 - Xilidina (mistura de isômeros)'),
    ('02.01.840', u'02.01.840 - Xisto betuminoso'),
    ('02.01.841', u'02.01.841 - Zircônio e compostos'),
    ('02.01.999', u'02.01.999 - Outros'),
    ('03.01.001', u'03.01.001 - Trabalho ou operações, em contato permanente com pacientes em isolamento por doenças infecto-contagiosas, bem como objetos de seu uso, não previamente esterilizados'),
    ('03.01.002', u'03.01.002 - Trabalho ou operações, em contato permanente com carnes, glândulas, vísceras, sangue, ossos, couros, pêlos e dejeções de animais portadores de doenças infecto- contagiosas (carbunculose, brucelose, tuberculose)'),
    ('03.01.003', u'03.01.003 - Trabalho ou operações, em contato permanente com esgotos (galerias e tanques)'),
    ('03.01.004', u'03.01.004 - Trabalho ou operações, em contato permanente com lixo urbano (coleta e industrialização)'),
    ('03.01.005', u'03.01.005 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em hospitais, serviços de emergência, enfermarias, ambulatórios, postos de vacinação e outros estabelecimentos destinados aos cuidados da saúde humana (aplica se unicamente ao pessoal que tenha contato com os pacientes, bem como aos que manuseiam objetos de uso desses pacientes, não previamente esterilizados);'),
    ('03.01.006', u'03.01.006 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em hospitais, ambulatórios, postos de vacinação e outros estabelecimentos destinados ao atendimento e tratamento de animais (aplica se apenas ao pessoal que tenha contato com tais animais);'),
    ('03.01.007', u'03.01.007 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em contato em laboratórios, com animais destinados ao preparo de soro, vacinas e outros produtos;'),
    ('03.01.008', u'03.01.008 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em laboratórios de análise clínica e histopatologia (aplica-se tão- só ao pessoal técnico);'),
    ('03.01.009', u'03.01.009 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em gabinetes de autópsias, de anatomia e histoanatomopatologia (aplica-se somente ao pessoal técnico);'),
    ('03.01.010', u'03.01.010 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em cemitérios (exumação de corpos);'),
    ('03.01.011', u'03.01.011 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em estábulos e cavalariças; e'),
    ('03.01.012', u'03.01.012 - Trabalhos e operações em contato permanente com pacientes, animais ou com material infecto-contagiante, em resíduos de animais deteriorados.'),
    ('03.01.013', u'03.01.013 - Trabalho de exumação de corpos e manipulação de resíduos de animais deteriorados;'),
    ('03.01.014', u'03.01.014 - Esvaziamento de biodigestores;'),
    ('03.01.999', u'03.01.999 - Outros'),
    ('04.01.001', u'04.01.001 - Exigência de posturas incômodas ou pouco confortáveis por longos períodos'),
    ('04.01.002', u'04.01.002 - Postura sentada por longos períodos'),
    ('04.01.003', u'04.01.003 - Postura de pé por longos períodos'),
    ('04.01.004', u'04.01.004 - Constante deslocamento a pé durante a jornada de trabalho'),
    ('04.01.005', u'04.01.005 - Exigência de esforço físico intenso'),
    ('04.01.006', u'04.01.006 - Levantamento e transporte manual de cargas ou volumes'),
    ('04.01.007', u'04.01.007 - Frequente ação de puxar/empurrar cargas ou volumes'),
    ('04.01.008', u'04.01.008 - Frequente execução de movimentos repetitivos'),
    ('04.01.009', u'04.01.009 - Manuseio de ferramentas e/ou objetos pesados por períodos prolongados'),
    ('04.01.999', u'04.01.999 - Outros'),
    ('04.02.001', u'04.02.001 - Mobiliário sem meios de regulagem de ajuste'),
    ('04.02.002', u'04.02.002 - Equipamentos e/ou máquinas sem meios de regulagem de ajuste ou sem condições de uso'),
    ('04.02.999', u'04.02.999 - Outros'),
    ('04.03.001', u'04.03.001 - Ausência de pausas para descanso ou não cumprimento destas durante a jornada'),
    ('04.03.002', u'04.03.002 - Necessidade de manter ritmos intensos de trabalho'),
    ('04.03.003', u'04.03.003 - Trabalho com necessidade de variação de turnos'),
    ('04.03.004', u'04.03.004 - Monotonia'),
    ('04.03.005', u'04.03.005 - Ausência de um plano de capacitação, habilitação, reciclagem e atualização dos empregados'),
    ('04.03.006', u'04.03.006 - Cobrança de metas de impossível atingimento'),
    ('04.03.999', u'04.03.999 - Outros'),
    ('04.04.001', u'04.04.001 - Situações de estresse'),
    ('04.04.002', u'04.04.002 - Situações de sobrecarga de trabalho mental'),
    ('04.04.003', u'04.04.003 - Exigência de alto nível de concentração ou atenção'),
    ('04.04.004', u'04.04.004 - Meios de comunicação ineficientes'),
    ('04.04.999', u'04.04.999 - Outros'),
    ('05.01.001', u'05.01.001 - Trabalho em altura'),
    ('05.01.002', u'05.01.002 - Iluminação inadequada'),
    ('05.01.003', u'05.01.003 - Choque elétrico'),
    ('05.01.004', u'05.01.004 - Choque mecânico'),
    ('05.01.005', u'05.01.005 - Arranjo físico inadequado'),
    ('05.01.006', u'05.01.006 - Incêndio e explosão (probabilidade)'),
    ('05.01.007', u'05.01.007 - Máquinas e equipamentos sem proteção'),
    ('05.01.008', u'05.01.008 - Máquinas e equipamentos com proteção inadequada'),
    ('05.01.009', u'05.01.009 - Armazenamento inadequado'),
    ('05.01.010', u'05.01.010 - Ferramentas inadequadas ou defeituosas'),
    ('05.01.011', u'05.01.011 - Soterramento'),
    ('05.01.012', u'05.01.012 - Animais peçonhentos'),
    ('05.01.013', u'05.01.013 - Animais domésticos/Risco a acidentes de ataque'),
    ('05.01.014', u'05.01.014 - Animais selvagens/Risco a acidentes de ataque'),
    ('05.01.015', u'05.01.015 - Cortes e perfurações'),
    ('05.01.016', u'05.01.016 - Queimaduras'),
    ('05.01.017', u'05.01.017 - Acidentes de trânsito'),
    ('05.01.999', u'05.01.999 - Outros'),
    ('06.01.001', u'06.01.001 - Explosivos'),
    ('06.01.002', u'06.01.002 - Inflamáveis'),
    ('06.01.003', u'06.01.003 - Energia elétrica'),
    ('06.01.004', u'06.01.004 - Radiações Ionizantes ou substâncias Radioativas'),
    ('06.01.005', u'06.01.005 - Profissionais de Segurança Pessoal ou Patrimonial'),
    ('06.01.006', u'06.01.006 - As atividades laborais com utilização de motocicleta ou motoneta no deslocamento de trabalhador em vias públicas são consideradas perigosas.'),
    ('06.01.999', u'06.01.999 - Outros'),
    ('07.01.001', u'07.01.001 - Decisão judicial'),
    ('07.01.002', u'07.01.002 - Acordo - Convenção'),
    ('07.01.003', u'07.01.003 - Liberalidade'),
    ('07.01.999', u'07.01.999 - Outros'),
    ('08.01.001', u'08.01.001 - Mineração subterrânea cujas atividades sejam exercidas afastadas das frentes de produção'),
    ('08.01.002', u'08.01.002 - Trabalhos em atividades permanentes no subsolo de minerações subterrâneas em frente de produção'),
    ('08.01.999', u'08.01.999 - Outros'),
    ('09.01.001', u'09.01.001 - Ausência de Fator de Risco'),
)

CHOICES_S2240_ALTEXPRISCO_CONDFUNCTO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_EFICEPC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_EFICEPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_HIGIENIZACAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_MEDPROTECAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_PERIODICTROCA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_PRZVALID = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_UTILIZEPC = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_ALTEXPRISCO_UTILIZEPI = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_INIEXPRISCO_CONDFUNCTO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_EFICEPC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_EFICEPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_HIGIENIZACAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_MEDPROTECAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_PERIODICTROCA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_PRZVALID = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_UTILIZEPC = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_INIEXPRISCO_UTILIZEPI = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

class s2240altExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('eventos.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtaltcondicao)
    #s2240_altexprisco_custom#
    class Meta:
        db_table = r's2240_altexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtaltcondicao']


class s2240altExpRiscoepc(models.Model):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.dscepc) + ' - ' + unicode(self.eficepc)
    #s2240_altexprisco_epc_custom#
    class Meta:
        db_table = r's2240_altexprisco_epc'
        managed = True
        ordering = ['s2240_altexprisco_fatrisco', 'dscepc', 'eficepc']


class s2240altExpRiscoepi(models.Model):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    caepi = models.CharField(max_length=20, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_CONDFUNCTO, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_HIGIENIZACAO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.caepi) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)
    #s2240_altexprisco_epi_custom#
    class Meta:
        db_table = r's2240_altexprisco_epi'
        managed = True
        ordering = ['s2240_altexprisco_fatrisco', 'caepi', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao']


class s2240altExpRiscofatRisco(models.Model):
    s2240_altexprisco_infoamb = models.ForeignKey('s2240altExpRiscoinfoAmb',
        related_name='%(class)s_s2240_altexprisco_infoamb')
    codfatris = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_CODFATRIS, max_length=10)
    intconc = models.CharField(max_length=15, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPC)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.intconc) + ' - ' + unicode(self.tecmedicao) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)
    #s2240_altexprisco_fatrisco_custom#
    class Meta:
        db_table = r's2240_altexprisco_fatrisco'
        managed = True
        ordering = ['s2240_altexprisco_infoamb', 'codfatris', 'intconc', 'tecmedicao', 'utilizepc', 'utilizepi']


class s2240altExpRiscoinfoAmb(models.Model):
    s2240_altexprisco = models.ForeignKey('s2240altExpRisco',
        related_name='%(class)s_s2240_altexprisco')
    codamb = models.CharField(max_length=30)
    dscativdes = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)
    #s2240_altexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_altexprisco_infoamb'
        managed = True
        ordering = ['s2240_altexprisco', 'codamb', 'dscativdes']


class s2240fimExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('eventos.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtfimcondicao)
    #s2240_fimexprisco_custom#
    class Meta:
        db_table = r's2240_fimexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtfimcondicao']


class s2240fimExpRiscoinfoAmb(models.Model):
    s2240_fimexprisco = models.ForeignKey('s2240fimExpRisco',
        related_name='%(class)s_s2240_fimexprisco')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_fimexprisco) + ' - ' + unicode(self.codamb)
    #s2240_fimexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_fimexprisco_infoamb'
        managed = True
        ordering = ['s2240_fimexprisco', 'codamb']


class s2240fimExpRiscorespReg(models.Model):
    s2240_evtexprisco = models.ForeignKey('eventos.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtini = models.DateField()
    dtfim = models.DateField(blank=True, null=True)
    nisresp = models.CharField(max_length=11)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtini) + ' - ' + unicode(self.dtfim) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)
    #s2240_fimexprisco_respreg_custom#
    class Meta:
        db_table = r's2240_fimexprisco_respreg'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtini', 'dtfim', 'nisresp', 'nroc', 'ufoc']


class s2240iniExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('eventos.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtinicondicao)
    #s2240_iniexprisco_custom#
    class Meta:
        db_table = r's2240_iniexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtinicondicao']


class s2240iniExpRiscoepc(models.Model):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.dscepc) + ' - ' + unicode(self.eficepc)
    #s2240_iniexprisco_epc_custom#
    class Meta:
        db_table = r's2240_iniexprisco_epc'
        managed = True
        ordering = ['s2240_iniexprisco_fatrisco', 'dscepc', 'eficepc']


class s2240iniExpRiscoepi(models.Model):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    caepi = models.CharField(max_length=20, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_CONDFUNCTO, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_HIGIENIZACAO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.caepi) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)
    #s2240_iniexprisco_epi_custom#
    class Meta:
        db_table = r's2240_iniexprisco_epi'
        managed = True
        ordering = ['s2240_iniexprisco_fatrisco', 'caepi', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao']


class s2240iniExpRiscofatRisco(models.Model):
    s2240_iniexprisco_infoamb = models.ForeignKey('s2240iniExpRiscoinfoAmb',
        related_name='%(class)s_s2240_iniexprisco_infoamb')
    codfatris = models.CharField(max_length=10)
    intconc = models.CharField(max_length=15, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPC)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.intconc) + ' - ' + unicode(self.tecmedicao) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)
    #s2240_iniexprisco_fatrisco_custom#
    class Meta:
        db_table = r's2240_iniexprisco_fatrisco'
        managed = True
        ordering = ['s2240_iniexprisco_infoamb', 'codfatris', 'intconc', 'tecmedicao', 'utilizepc', 'utilizepi']


class s2240iniExpRiscoinfoAmb(models.Model):
    s2240_iniexprisco = models.ForeignKey('s2240iniExpRisco',
        related_name='%(class)s_s2240_iniexprisco')
    codamb = models.CharField(max_length=30)
    dscativdes = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)
    #s2240_iniexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_iniexprisco_infoamb'
        managed = True
        ordering = ['s2240_iniexprisco', 'codamb', 'dscativdes']


#VIEWS_MODELS
