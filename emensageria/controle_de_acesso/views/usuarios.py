#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

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

import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageria.padrao import *
from emensageria.controle_de_acesso.forms import *
from emensageria.controle_de_acesso.models import *
from emensageria.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageria.mensageiro.models import TransmissorLote
from emensageria.mensageiro.models import TransmissorLote
from emensageria.mensageiro.models import TransmissorLoteOcorrencias
from emensageria.mensageiro.models import TransmissorLoteOcorrencias
from emensageria.eventos.models import s1000evtInfoEmpregadorOcorrencias
from emensageria.eventos.models import s1000evtInfoEmpregadorOcorrencias
from emensageria.eventos.models import s1005evtTabEstabOcorrencias
from emensageria.eventos.models import s1005evtTabEstabOcorrencias
from emensageria.eventos.models import s1010evtTabRubricaOcorrencias
from emensageria.eventos.models import s1010evtTabRubricaOcorrencias
from emensageria.eventos.models import s1020evtTabLotacaoOcorrencias
from emensageria.eventos.models import s1020evtTabLotacaoOcorrencias
from emensageria.eventos.models import s1030evtTabCargoOcorrencias
from emensageria.eventos.models import s1030evtTabCargoOcorrencias
from emensageria.eventos.models import s1035evtTabCarreiraOcorrencias
from emensageria.eventos.models import s1035evtTabCarreiraOcorrencias
from emensageria.eventos.models import s1040evtTabFuncaoOcorrencias
from emensageria.eventos.models import s1040evtTabFuncaoOcorrencias
from emensageria.eventos.models import s1050evtTabHorTurOcorrencias
from emensageria.eventos.models import s1050evtTabHorTurOcorrencias
from emensageria.eventos.models import s1060evtTabAmbienteOcorrencias
from emensageria.eventos.models import s1060evtTabAmbienteOcorrencias
from emensageria.eventos.models import s1070evtTabProcessoOcorrencias
from emensageria.eventos.models import s1070evtTabProcessoOcorrencias
from emensageria.eventos.models import s1080evtTabOperPortOcorrencias
from emensageria.eventos.models import s1080evtTabOperPortOcorrencias
from emensageria.eventos.models import s1200evtRemunOcorrencias
from emensageria.eventos.models import s1200evtRemunOcorrencias
from emensageria.eventos.models import s1202evtRmnRPPSOcorrencias
from emensageria.eventos.models import s1202evtRmnRPPSOcorrencias
from emensageria.eventos.models import s1207evtBenPrRPOcorrencias
from emensageria.eventos.models import s1207evtBenPrRPOcorrencias
from emensageria.eventos.models import s1210evtPgtosOcorrencias
from emensageria.eventos.models import s1210evtPgtosOcorrencias
from emensageria.eventos.models import s1250evtAqProdOcorrencias
from emensageria.eventos.models import s1250evtAqProdOcorrencias
from emensageria.eventos.models import s1260evtComProdOcorrencias
from emensageria.eventos.models import s1260evtComProdOcorrencias
from emensageria.eventos.models import s1270evtContratAvNPOcorrencias
from emensageria.eventos.models import s1270evtContratAvNPOcorrencias
from emensageria.eventos.models import s1280evtInfoComplPer
from emensageria.eventos.models import s1280evtInfoComplPer
from emensageria.eventos.models import s1295evtTotContingOcorrencias
from emensageria.eventos.models import s1295evtTotContingOcorrencias
from emensageria.eventos.models import s1298evtReabreEvPerOcorrencias
from emensageria.eventos.models import s1298evtReabreEvPerOcorrencias
from emensageria.eventos.models import s1299evtFechaEvPerOcorrencias
from emensageria.eventos.models import s1299evtFechaEvPerOcorrencias
from emensageria.eventos.models import s1300evtContrSindPatrOcorrencias
from emensageria.eventos.models import s1300evtContrSindPatrOcorrencias
from emensageria.eventos.models import s2190evtAdmPrelimOcorrencias
from emensageria.eventos.models import s2190evtAdmPrelimOcorrencias
from emensageria.eventos.models import s2200evtAdmissaoOcorrencias
from emensageria.eventos.models import s2200evtAdmissaoOcorrencias
from emensageria.eventos.models import s2205evtAltCadastralOcorrencias
from emensageria.eventos.models import s2205evtAltCadastralOcorrencias
from emensageria.eventos.models import s2206evtAltContratualOcorrencias
from emensageria.eventos.models import s2206evtAltContratualOcorrencias
from emensageria.eventos.models import s2210evtCATOcorrencias
from emensageria.eventos.models import s2210evtCATOcorrencias
from emensageria.eventos.models import s2220evtMonitOcorrencias
from emensageria.eventos.models import s2220evtMonitOcorrencias
from emensageria.eventos.models import s2230evtAfastTempOcorrencias
from emensageria.eventos.models import s2230evtAfastTempOcorrencias
from emensageria.eventos.models import s2240evtExpRiscoOcorrencias
from emensageria.eventos.models import s2240evtExpRiscoOcorrencias
from emensageria.eventos.models import s2241evtInsApoOcorrencias
from emensageria.eventos.models import s2241evtInsApoOcorrencias
from emensageria.eventos.models import s2250evtAvPrevioOcorrencias
from emensageria.eventos.models import s2250evtAvPrevioOcorrencias
from emensageria.eventos.models import s2260evtConvIntermOcorrencias
from emensageria.eventos.models import s2260evtConvIntermOcorrencias
from emensageria.eventos.models import s2298evtReintegrOcorrencias
from emensageria.eventos.models import s2298evtReintegrOcorrencias
from emensageria.eventos.models import s2299evtDesligOcorrencias
from emensageria.eventos.models import s2299evtDesligOcorrencias
from emensageria.eventos.models import s2300evtTSVInicioOcorrencias
from emensageria.eventos.models import s2300evtTSVInicioOcorrencias
from emensageria.eventos.models import s2306evtTSVAltContrOcorrencias
from emensageria.eventos.models import s2306evtTSVAltContrOcorrencias
from emensageria.eventos.models import s2399evtTSVTerminoOcorrencias
from emensageria.eventos.models import s2399evtTSVTerminoOcorrencias
from emensageria.eventos.models import s2400evtCdBenPrRPOcorrencias
from emensageria.eventos.models import s2400evtCdBenPrRPOcorrencias
from emensageria.eventos.models import s3000evtExclusaoOcorrencias
from emensageria.eventos.models import s3000evtExclusaoOcorrencias
from emensageria.eventos.models import s5001evtBasesTrabOcorrencias
from emensageria.eventos.models import s5001evtBasesTrabOcorrencias
from emensageria.eventos.models import s5002evtIrrfBenefOcorrencias
from emensageria.eventos.models import s5002evtIrrfBenefOcorrencias
from emensageria.eventos.models import s5011evtCSOcorrencias
from emensageria.eventos.models import s5011evtCSOcorrencias
from emensageria.eventos.models import s5012evtIrrfOcorrencias
from emensageria.eventos.models import s5012evtIrrfOcorrencias
from emensageria.eventos.models import s1000evtInfoEmpregador
from emensageria.eventos.models import s1000evtInfoEmpregador
from emensageria.eventos.models import s1005evtTabEstab
from emensageria.eventos.models import s1005evtTabEstab
from emensageria.eventos.models import s1010evtTabRubrica
from emensageria.eventos.models import s1010evtTabRubrica
from emensageria.eventos.models import s1020evtTabLotacao
from emensageria.eventos.models import s1020evtTabLotacao
from emensageria.eventos.models import s1030evtTabCargo
from emensageria.eventos.models import s1030evtTabCargo
from emensageria.eventos.models import s1035evtTabCarreira
from emensageria.eventos.models import s1035evtTabCarreira
from emensageria.eventos.models import s1040evtTabFuncao
from emensageria.eventos.models import s1040evtTabFuncao
from emensageria.eventos.models import s1050evtTabHorTur
from emensageria.eventos.models import s1050evtTabHorTur
from emensageria.eventos.models import s1060evtTabAmbiente
from emensageria.eventos.models import s1060evtTabAmbiente
from emensageria.eventos.models import s1070evtTabProcesso
from emensageria.eventos.models import s1070evtTabProcesso
from emensageria.eventos.models import s1080evtTabOperPort
from emensageria.eventos.models import s1080evtTabOperPort
from emensageria.eventos.models import s1200evtRemun
from emensageria.eventos.models import s1200evtRemun
from emensageria.eventos.models import s1202evtRmnRPPS
from emensageria.eventos.models import s1202evtRmnRPPS
from emensageria.eventos.models import s1207evtBenPrRP
from emensageria.eventos.models import s1207evtBenPrRP
from emensageria.eventos.models import s1210evtPgtos
from emensageria.eventos.models import s1210evtPgtos
from emensageria.eventos.models import s1250evtAqProd
from emensageria.eventos.models import s1250evtAqProd
from emensageria.eventos.models import s1260evtComProd
from emensageria.eventos.models import s1260evtComProd
from emensageria.eventos.models import s1270evtContratAvNP
from emensageria.eventos.models import s1270evtContratAvNP
from emensageria.eventos.models import s1280evtInfoComplPer
from emensageria.eventos.models import s1280evtInfoComplPer
from emensageria.eventos.models import s1295evtTotConting
from emensageria.eventos.models import s1295evtTotConting
from emensageria.eventos.models import s1298evtReabreEvPer
from emensageria.eventos.models import s1298evtReabreEvPer
from emensageria.eventos.models import s1299evtFechaEvPer
from emensageria.eventos.models import s1299evtFechaEvPer
from emensageria.eventos.models import s1300evtContrSindPatr
from emensageria.eventos.models import s1300evtContrSindPatr
from emensageria.eventos.models import s2190evtAdmPrelim
from emensageria.eventos.models import s2190evtAdmPrelim
from emensageria.eventos.models import s2200evtAdmissao
from emensageria.eventos.models import s2200evtAdmissao
from emensageria.eventos.models import s2205evtAltCadastral
from emensageria.eventos.models import s2205evtAltCadastral
from emensageria.eventos.models import s2206evtAltContratual
from emensageria.eventos.models import s2206evtAltContratual
from emensageria.eventos.models import s2210evtCAT
from emensageria.eventos.models import s2210evtCAT
from emensageria.eventos.models import s2220evtMonit
from emensageria.eventos.models import s2220evtMonit
from emensageria.eventos.models import s2230evtAfastTemp
from emensageria.eventos.models import s2230evtAfastTemp
from emensageria.eventos.models import s2240evtExpRisco
from emensageria.eventos.models import s2240evtExpRisco
from emensageria.eventos.models import s2241evtInsApo
from emensageria.eventos.models import s2241evtInsApo
from emensageria.eventos.models import s2250evtAvPrevio
from emensageria.eventos.models import s2250evtAvPrevio
from emensageria.eventos.models import s2260evtConvInterm
from emensageria.eventos.models import s2260evtConvInterm
from emensageria.eventos.models import s2298evtReintegr
from emensageria.eventos.models import s2298evtReintegr
from emensageria.eventos.models import s2299evtDeslig
from emensageria.eventos.models import s2299evtDeslig
from emensageria.eventos.models import s2300evtTSVInicio
from emensageria.eventos.models import s2300evtTSVInicio
from emensageria.eventos.models import s2306evtTSVAltContr
from emensageria.eventos.models import s2306evtTSVAltContr
from emensageria.eventos.models import s2399evtTSVTermino
from emensageria.eventos.models import s2399evtTSVTermino
from emensageria.eventos.models import s2400evtCdBenPrRP
from emensageria.eventos.models import s2400evtCdBenPrRP
from emensageria.eventos.models import s3000evtExclusao
from emensageria.eventos.models import s3000evtExclusao
from emensageria.eventos.models import s5001evtBasesTrab
from emensageria.eventos.models import s5001evtBasesTrab
from emensageria.eventos.models import s5002evtIrrfBenef
from emensageria.eventos.models import s5002evtIrrfBenef
from emensageria.eventos.models import s5011evtCS
from emensageria.eventos.models import s5011evtCS
from emensageria.eventos.models import s5012evtIrrf
from emensageria.eventos.models import s5012evtIrrf
from emensageria.s1000.models import s1000inclusao
from emensageria.s1000.models import s1000inclusao
from emensageria.s1000.models import s1000inclusaodadosIsencao
from emensageria.s1000.models import s1000inclusaodadosIsencao
from emensageria.s1000.models import s1000inclusaoinfoOP
from emensageria.s1000.models import s1000inclusaoinfoOP
from emensageria.s1000.models import s1000inclusaoinfoEFR
from emensageria.s1000.models import s1000inclusaoinfoEFR
from emensageria.s1000.models import s1000inclusaoinfoEnte
from emensageria.s1000.models import s1000inclusaoinfoEnte
from emensageria.s1000.models import s1000inclusaoinfoOrgInternacional
from emensageria.s1000.models import s1000inclusaoinfoOrgInternacional
from emensageria.s1000.models import s1000inclusaosoftwareHouse
from emensageria.s1000.models import s1000inclusaosoftwareHouse
from emensageria.s1000.models import s1000inclusaosituacaoPJ
from emensageria.s1000.models import s1000inclusaosituacaoPJ
from emensageria.s1000.models import s1000inclusaosituacaoPF
from emensageria.s1000.models import s1000inclusaosituacaoPF
from emensageria.s1000.models import s1000alteracao
from emensageria.s1000.models import s1000alteracao
from emensageria.s1000.models import s1000alteracaodadosIsencao
from emensageria.s1000.models import s1000alteracaodadosIsencao
from emensageria.s1000.models import s1000alteracaoinfoOP
from emensageria.s1000.models import s1000alteracaoinfoOP
from emensageria.s1000.models import s1000alteracaoinfoEFR
from emensageria.s1000.models import s1000alteracaoinfoEFR
from emensageria.s1000.models import s1000alteracaoinfoEnte
from emensageria.s1000.models import s1000alteracaoinfoEnte
from emensageria.s1000.models import s1000alteracaoinfoOrgInternacional
from emensageria.s1000.models import s1000alteracaoinfoOrgInternacional
from emensageria.s1000.models import s1000alteracaosoftwareHouse
from emensageria.s1000.models import s1000alteracaosoftwareHouse
from emensageria.s1000.models import s1000alteracaosituacaoPJ
from emensageria.s1000.models import s1000alteracaosituacaoPJ
from emensageria.s1000.models import s1000alteracaosituacaoPF
from emensageria.s1000.models import s1000alteracaosituacaoPF
from emensageria.s1035.models import s1035inclusao
from emensageria.s1035.models import s1035inclusao
from emensageria.s1000.models import s1000alteracaonovaValidade
from emensageria.s1000.models import s1000alteracaonovaValidade
from emensageria.s1000.models import s1000exclusao
from emensageria.s1000.models import s1000exclusao
from emensageria.s1005.models import s1005inclusao
from emensageria.s1005.models import s1005inclusao
from emensageria.s1005.models import s1005inclusaoprocAdmJudRat
from emensageria.s1005.models import s1005inclusaoprocAdmJudRat
from emensageria.s1005.models import s1005inclusaoprocAdmJudFap
from emensageria.s1005.models import s1005inclusaoprocAdmJudFap
from emensageria.s1005.models import s1005inclusaoinfoCaepf
from emensageria.s1005.models import s1005inclusaoinfoCaepf
from emensageria.s1005.models import s1005inclusaoinfoObra
from emensageria.s1005.models import s1005inclusaoinfoObra
from emensageria.s1005.models import s1005inclusaoinfoEntEduc
from emensageria.s1005.models import s1005inclusaoinfoEntEduc
from emensageria.s1005.models import s1005inclusaoinfoPCD
from emensageria.s1005.models import s1005inclusaoinfoPCD
from emensageria.s1005.models import s1005alteracao
from emensageria.s1005.models import s1005alteracao
from emensageria.s1005.models import s1005alteracaoprocAdmJudRat
from emensageria.s1005.models import s1005alteracaoprocAdmJudRat
from emensageria.s1005.models import s1005alteracaoprocAdmJudFap
from emensageria.s1005.models import s1005alteracaoprocAdmJudFap
from emensageria.s1005.models import s1005alteracaoinfoCaepf
from emensageria.s1005.models import s1005alteracaoinfoCaepf
from emensageria.s1005.models import s1005alteracaoinfoObra
from emensageria.s1005.models import s1005alteracaoinfoObra
from emensageria.s1005.models import s1005alteracaoinfoEntEduc
from emensageria.s1005.models import s1005alteracaoinfoEntEduc
from emensageria.s1005.models import s1005alteracaoinfoPCD
from emensageria.s1005.models import s1005alteracaoinfoPCD
from emensageria.s1005.models import s1005alteracaonovaValidade
from emensageria.s1005.models import s1005alteracaonovaValidade
from emensageria.s1005.models import s1005exclusao
from emensageria.s1005.models import s1005exclusao
from emensageria.s1010.models import s1010inclusao
from emensageria.s1010.models import s1010inclusao
from emensageria.s1010.models import s1010inclusaoideProcessoCP
from emensageria.s1010.models import s1010inclusaoideProcessoCP
from emensageria.s1010.models import s1010inclusaoideProcessoIRRF
from emensageria.s1010.models import s1010inclusaoideProcessoIRRF
from emensageria.s1010.models import s1010inclusaoideProcessoFGTS
from emensageria.s1010.models import s1010inclusaoideProcessoFGTS
from emensageria.s1010.models import s1010inclusaoideProcessoSIND
from emensageria.s1010.models import s1010inclusaoideProcessoSIND
from emensageria.s1010.models import s1010alteracao
from emensageria.s1010.models import s1010alteracao
from emensageria.s1010.models import s1010alteracaoideProcessoCP
from emensageria.s1010.models import s1010alteracaoideProcessoCP
from emensageria.s1010.models import s1010alteracaoideProcessoIRRF
from emensageria.s1010.models import s1010alteracaoideProcessoIRRF
from emensageria.s1010.models import s1010alteracaoideProcessoFGTS
from emensageria.s1010.models import s1010alteracaoideProcessoFGTS
from emensageria.s1035.models import s1035alteracao
from emensageria.s1035.models import s1035alteracao
from emensageria.s1035.models import s1035alteracaonovaValidade
from emensageria.s1035.models import s1035alteracaonovaValidade
from emensageria.s1010.models import s1010alteracaoideProcessoSIND
from emensageria.s1010.models import s1010alteracaoideProcessoSIND
from emensageria.s1010.models import s1010alteracaonovaValidade
from emensageria.s1010.models import s1010alteracaonovaValidade
from emensageria.s1010.models import s1010exclusao
from emensageria.s1010.models import s1010exclusao
from emensageria.s1020.models import s1020inclusao
from emensageria.s1020.models import s1020inclusao
from emensageria.s1020.models import s1020inclusaoinfoProcJudTerceiros
from emensageria.s1020.models import s1020inclusaoinfoProcJudTerceiros
from emensageria.s1020.models import s1020inclusaoprocJudTerceiro
from emensageria.s1020.models import s1020inclusaoprocJudTerceiro
from emensageria.s1020.models import s1020inclusaoinfoEmprParcial
from emensageria.s1020.models import s1020inclusaoinfoEmprParcial
from emensageria.s1020.models import s1020alteracao
from emensageria.s1020.models import s1020alteracao
from emensageria.s1020.models import s1020alteracaoinfoProcJudTerceiros
from emensageria.s1020.models import s1020alteracaoinfoProcJudTerceiros
from emensageria.s1020.models import s1020alteracaoprocJudTerceiro
from emensageria.s1020.models import s1020alteracaoprocJudTerceiro
from emensageria.s1020.models import s1020alteracaoinfoEmprParcial
from emensageria.s1020.models import s1020alteracaoinfoEmprParcial
from emensageria.s1020.models import s1020alteracaonovaValidade
from emensageria.s1020.models import s1020alteracaonovaValidade
from emensageria.s1020.models import s1020exclusao
from emensageria.s1020.models import s1020exclusao
from emensageria.s1030.models import s1030inclusao
from emensageria.s1030.models import s1030inclusao
from emensageria.s1030.models import s1030inclusaocargoPublico
from emensageria.s1030.models import s1030inclusaocargoPublico
from emensageria.s1030.models import s1030alteracao
from emensageria.s1030.models import s1030alteracao
from emensageria.s1030.models import s1030alteracaocargoPublico
from emensageria.s1030.models import s1030alteracaocargoPublico
from emensageria.s1030.models import s1030alteracaonovaValidade
from emensageria.s1030.models import s1030alteracaonovaValidade
from emensageria.s1030.models import s1030exclusao
from emensageria.s1030.models import s1030exclusao
from emensageria.s1035.models import s1035exclusao
from emensageria.s1035.models import s1035exclusao
from emensageria.s1040.models import s1040inclusao
from emensageria.s1040.models import s1040inclusao
from emensageria.s1040.models import s1040alteracao
from emensageria.s1040.models import s1040alteracao
from emensageria.s1040.models import s1040alteracaonovaValidade
from emensageria.s1040.models import s1040alteracaonovaValidade
from emensageria.s1040.models import s1040exclusao
from emensageria.s1040.models import s1040exclusao
from emensageria.s1050.models import s1050inclusao
from emensageria.s1050.models import s1050inclusao
from emensageria.s1050.models import s1050inclusaohorarioIntervalo
from emensageria.s1050.models import s1050inclusaohorarioIntervalo
from emensageria.s1050.models import s1050alteracao
from emensageria.s1050.models import s1050alteracao
from emensageria.s1050.models import s1050alteracaohorarioIntervalo
from emensageria.s1050.models import s1050alteracaohorarioIntervalo
from emensageria.s1050.models import s1050alteracaonovaValidade
from emensageria.s1050.models import s1050alteracaonovaValidade
from emensageria.s1050.models import s1050exclusao
from emensageria.s1050.models import s1050exclusao
from emensageria.s1060.models import s1060inclusao
from emensageria.s1060.models import s1060inclusao
from emensageria.s1060.models import s1060inclusaofatorRisco
from emensageria.s1060.models import s1060inclusaofatorRisco
from emensageria.s1060.models import s1060alteracao
from emensageria.s1060.models import s1060alteracao
from emensageria.s1060.models import s1060alteracaofatorRisco
from emensageria.s1060.models import s1060alteracaofatorRisco
from emensageria.s1060.models import s1060alteracaonovaValidade
from emensageria.s1060.models import s1060alteracaonovaValidade
from emensageria.s1060.models import s1060exclusao
from emensageria.s1060.models import s1060exclusao
from emensageria.s1070.models import s1070inclusao
from emensageria.s1070.models import s1070inclusao
from emensageria.s1070.models import s1070inclusaodadosProcJud
from emensageria.s1070.models import s1070inclusaodadosProcJud
from emensageria.s1070.models import s1070inclusaoinfoSusp
from emensageria.s1070.models import s1070inclusaoinfoSusp
from emensageria.s1070.models import s1070alteracao
from emensageria.s1070.models import s1070alteracao
from emensageria.s1070.models import s1070alteracaodadosProcJud
from emensageria.s1070.models import s1070alteracaodadosProcJud
from emensageria.s1070.models import s1070alteracaoinfoSusp
from emensageria.s1070.models import s1070alteracaoinfoSusp
from emensageria.s1202.models import s1202infoPerApurdetOper
from emensageria.s1202.models import s1202infoPerApurdetOper
from emensageria.s1070.models import s1070alteracaonovaValidade
from emensageria.s1070.models import s1070alteracaonovaValidade
from emensageria.s1070.models import s1070exclusao
from emensageria.s1070.models import s1070exclusao
from emensageria.s1080.models import s1080inclusao
from emensageria.s1080.models import s1080inclusao
from emensageria.s1080.models import s1080alteracao
from emensageria.s1080.models import s1080alteracao
from emensageria.s1080.models import s1080alteracaonovaValidade
from emensageria.s1080.models import s1080alteracaonovaValidade
from emensageria.s1080.models import s1080exclusao
from emensageria.s1080.models import s1080exclusao
from emensageria.s1200.models import s1200infoMV
from emensageria.s1200.models import s1200infoMV
from emensageria.s1200.models import s1200remunOutrEmpr
from emensageria.s1200.models import s1200remunOutrEmpr
from emensageria.s1200.models import s1200infoComplem
from emensageria.s1200.models import s1200infoComplem
from emensageria.s1200.models import s1200sucessaoVinc
from emensageria.s1200.models import s1200sucessaoVinc
from emensageria.s1200.models import s1200procJudTrab
from emensageria.s1200.models import s1200procJudTrab
from emensageria.s1200.models import s1200infoInterm
from emensageria.s1200.models import s1200infoInterm
from emensageria.s1200.models import s1200dmDev
from emensageria.s1200.models import s1200dmDev
from emensageria.s1200.models import s1200infoPerApur
from emensageria.s1200.models import s1200infoPerApur
from emensageria.s1202.models import s1202infoPerApurdetPlano
from emensageria.s1202.models import s1202infoPerApurdetPlano
from emensageria.s1210.models import s1210detPgtoAnt
from emensageria.s1210.models import s1210detPgtoAnt
from emensageria.s1299.models import s1299ideRespInf
from emensageria.s1299.models import s1299ideRespInf
from emensageria.s1200.models import s1200infoPerApurideEstabLot
from emensageria.s1200.models import s1200infoPerApurideEstabLot
from emensageria.s1200.models import s1200infoPerApurremunPerApur
from emensageria.s1200.models import s1200infoPerApurremunPerApur
from emensageria.s1200.models import s1200infoPerApuritensRemun
from emensageria.s1200.models import s1200infoPerApuritensRemun
from emensageria.s1200.models import s1200infoPerApurinfoSaudeColet
from emensageria.s1200.models import s1200infoPerApurinfoSaudeColet
from emensageria.s1200.models import s1200infoPerApurdetOper
from emensageria.s1200.models import s1200infoPerApurdetOper
from emensageria.s1200.models import s1200infoPerApurdetPlano
from emensageria.s1200.models import s1200infoPerApurdetPlano
from emensageria.s1200.models import s1200infoPerApurinfoAgNocivo
from emensageria.s1200.models import s1200infoPerApurinfoAgNocivo
from emensageria.s1200.models import s1200infoPerApurinfoTrabInterm
from emensageria.s1200.models import s1200infoPerApurinfoTrabInterm
from emensageria.s1200.models import s1200infoPerAnt
from emensageria.s1200.models import s1200infoPerAnt
from emensageria.s1200.models import s1200infoPerAntideADC
from emensageria.s1200.models import s1200infoPerAntideADC
from emensageria.s1200.models import s1200infoPerAntidePeriodo
from emensageria.s1200.models import s1200infoPerAntidePeriodo
from emensageria.s1210.models import s1210detPgtoFerpenAlim
from emensageria.s1210.models import s1210detPgtoFerpenAlim
from emensageria.s1210.models import s1210detPgtoAntinfoPgtoAnt
from emensageria.s1210.models import s1210detPgtoAntinfoPgtoAnt
from emensageria.s1200.models import s1200infoPerAntideEstabLot
from emensageria.s1200.models import s1200infoPerAntideEstabLot
from emensageria.s1200.models import s1200infoPerAntremunPerAnt
from emensageria.s1200.models import s1200infoPerAntremunPerAnt
from emensageria.s1200.models import s1200infoPerAntitensRemun
from emensageria.s1200.models import s1200infoPerAntitensRemun
from emensageria.s1200.models import s1200infoPerAntinfoAgNocivo
from emensageria.s1200.models import s1200infoPerAntinfoAgNocivo
from emensageria.s1200.models import s1200infoPerAntinfoTrabInterm
from emensageria.s1200.models import s1200infoPerAntinfoTrabInterm
from emensageria.s1200.models import s1200infoPerAntinfoComplCont
from emensageria.s1200.models import s1200infoPerAntinfoComplCont
from emensageria.s1202.models import s1202procJudTrab
from emensageria.s1202.models import s1202procJudTrab
from emensageria.s1202.models import s1202dmDev
from emensageria.s1202.models import s1202dmDev
from emensageria.s1202.models import s1202infoPerApur
from emensageria.s1202.models import s1202infoPerApur
from emensageria.s1202.models import s1202infoPerApurideEstab
from emensageria.s1202.models import s1202infoPerApurideEstab
from emensageria.s1202.models import s1202infoPerApurremunPerApur
from emensageria.s1202.models import s1202infoPerApurremunPerApur
from emensageria.s1202.models import s1202infoPerApuritensRemun
from emensageria.s1202.models import s1202infoPerApuritensRemun
from emensageria.s1202.models import s1202infoPerApurinfoSaudeColet
from emensageria.s1202.models import s1202infoPerApurinfoSaudeColet
from emensageria.s1202.models import s1202infoPerAnt
from emensageria.s1202.models import s1202infoPerAnt
from emensageria.s1202.models import s1202infoPerAntideADC
from emensageria.s1202.models import s1202infoPerAntideADC
from emensageria.s1202.models import s1202infoPerAntidePeriodo
from emensageria.s1202.models import s1202infoPerAntidePeriodo
from emensageria.s1202.models import s1202infoPerAntideEstab
from emensageria.s1202.models import s1202infoPerAntideEstab
from emensageria.s1202.models import s1202infoPerAntremunPerAnt
from emensageria.s1202.models import s1202infoPerAntremunPerAnt
from emensageria.s1202.models import s1202infoPerAntitensRemun
from emensageria.s1202.models import s1202infoPerAntitensRemun
from emensageria.s1207.models import s1207dmDev
from emensageria.s1207.models import s1207dmDev
from emensageria.s1207.models import s1207itens
from emensageria.s1207.models import s1207itens
from emensageria.s1210.models import s1210deps
from emensageria.s1210.models import s1210deps
from emensageria.s1210.models import s1210infoPgto
from emensageria.s1210.models import s1210infoPgto
from emensageria.s1210.models import s1210detPgtoFl
from emensageria.s1210.models import s1210detPgtoFl
from emensageria.s1210.models import s1210detPgtoFlretPgtoTot
from emensageria.s1210.models import s1210detPgtoFlretPgtoTot
from emensageria.s1210.models import s1210detPgtoFlpenAlim
from emensageria.s1210.models import s1210detPgtoFlpenAlim
from emensageria.s1210.models import s1210detPgtoFlinfoPgtoParc
from emensageria.s1210.models import s1210detPgtoFlinfoPgtoParc
from emensageria.s1210.models import s1210detPgtoBenPr
from emensageria.s1210.models import s1210detPgtoBenPr
from emensageria.s1210.models import s1210detPgtoBenPrretPgtoTot
from emensageria.s1210.models import s1210detPgtoBenPrretPgtoTot
from emensageria.s1210.models import s1210detPgtoBenPrinfoPgtoParc
from emensageria.s1210.models import s1210detPgtoBenPrinfoPgtoParc
from emensageria.s1210.models import s1210detPgtoFer
from emensageria.s1210.models import s1210detPgtoFer
from emensageria.s1210.models import s1210detPgtoFerdetRubrFer
from emensageria.s1210.models import s1210detPgtoFerdetRubrFer
from emensageria.s1210.models import s1210idePgtoExt
from emensageria.s1210.models import s1210idePgtoExt
from emensageria.s1250.models import s1250tpAquis
from emensageria.s1250.models import s1250tpAquis
from emensageria.s1250.models import s1250ideProdutor
from emensageria.s1250.models import s1250ideProdutor
from emensageria.s1250.models import s1250nfs
from emensageria.s1250.models import s1250nfs
from emensageria.s1250.models import s1250infoProcJud
from emensageria.s1250.models import s1250infoProcJud
from emensageria.s1260.models import s1260tpComerc
from emensageria.s1260.models import s1260tpComerc
from emensageria.s1260.models import s1260ideAdquir
from emensageria.s1260.models import s1260ideAdquir
from emensageria.s1260.models import s1260nfs
from emensageria.s1260.models import s1260nfs
from emensageria.s1260.models import s1260infoProcJud
from emensageria.s1260.models import s1260infoProcJud
from emensageria.s1270.models import s1270remunAvNP
from emensageria.s1270.models import s1270remunAvNP
from emensageria.s1280.models import s1280infoSubstPatr
from emensageria.s1280.models import s1280infoSubstPatr
from emensageria.s1280.models import s1280infoSubstPatrOpPort
from emensageria.s1280.models import s1280infoSubstPatrOpPort
from emensageria.s1280.models import s1280infoAtivConcom
from emensageria.s1280.models import s1280infoAtivConcom
from emensageria.s1295.models import s1295ideRespInf
from emensageria.s1295.models import s1295ideRespInf
from emensageria.s1300.models import s1300contribSind
from emensageria.s1300.models import s1300contribSind
from emensageria.s2200.models import s2200documentos
from emensageria.s2200.models import s2200documentos
from emensageria.s2200.models import s2200CTPS
from emensageria.s2200.models import s2200CTPS
from emensageria.s2200.models import s2200RIC
from emensageria.s2200.models import s2200RIC
from emensageria.s2200.models import s2200RG
from emensageria.s2200.models import s2200RG
from emensageria.s2200.models import s2200RNE
from emensageria.s2200.models import s2200RNE
from emensageria.s2200.models import s2200OC
from emensageria.s2200.models import s2200OC
from emensageria.s2200.models import s2200CNH
from emensageria.s2200.models import s2200CNH
from emensageria.s2200.models import s2200brasil
from emensageria.s2200.models import s2200brasil
from emensageria.s2200.models import s2200exterior
from emensageria.s2200.models import s2200exterior
from emensageria.s2200.models import s2200trabEstrangeiro
from emensageria.s2200.models import s2200trabEstrangeiro
from emensageria.s2200.models import s2200infoDeficiencia
from emensageria.s2200.models import s2200infoDeficiencia
from emensageria.s2200.models import s2200dependente
from emensageria.s2200.models import s2200dependente
from emensageria.s2200.models import s2200aposentadoria
from emensageria.s2200.models import s2200aposentadoria
from emensageria.s2200.models import s2200contato
from emensageria.s2200.models import s2200contato
from emensageria.s2200.models import s2200infoCeletista
from emensageria.s2200.models import s2200infoCeletista
from emensageria.s2200.models import s2200trabTemporario
from emensageria.s2200.models import s2200trabTemporario
from emensageria.s2200.models import s2200ideEstabVinc
from emensageria.s2200.models import s2200ideEstabVinc
from emensageria.s2200.models import s2200ideTrabSubstituido
from emensageria.s2200.models import s2200ideTrabSubstituido
from emensageria.s2200.models import s2200aprend
from emensageria.s2200.models import s2200aprend
from emensageria.s2200.models import s2200infoEstatutario
from emensageria.s2200.models import s2200infoEstatutario
from emensageria.s2200.models import s2200infoDecJud
from emensageria.s2200.models import s2200infoDecJud
from emensageria.s2205.models import s2205trabEstrangeiro
from emensageria.s2205.models import s2205trabEstrangeiro
from emensageria.s2205.models import s2205dependente
from emensageria.s2205.models import s2205dependente
from emensageria.s2200.models import s2200localTrabGeral
from emensageria.s2200.models import s2200localTrabGeral
from emensageria.s2200.models import s2200localTrabDom
from emensageria.s2200.models import s2200localTrabDom
from emensageria.s2200.models import s2200horContratual
from emensageria.s2200.models import s2200horContratual
from emensageria.s2200.models import s2200horario
from emensageria.s2200.models import s2200horario
from emensageria.s2200.models import s2200filiacaoSindical
from emensageria.s2200.models import s2200filiacaoSindical
from emensageria.s2200.models import s2200alvaraJudicial
from emensageria.s2200.models import s2200alvaraJudicial
from emensageria.s2200.models import s2200observacoes
from emensageria.s2200.models import s2200observacoes
from emensageria.s2200.models import s2200sucessaoVinc
from emensageria.s2200.models import s2200sucessaoVinc
from emensageria.s2200.models import s2200transfDom
from emensageria.s2200.models import s2200transfDom
from emensageria.s2200.models import s2200afastamento
from emensageria.s2200.models import s2200afastamento
from emensageria.s2200.models import s2200desligamento
from emensageria.s2200.models import s2200desligamento
from emensageria.s2205.models import s2205documentos
from emensageria.s2205.models import s2205documentos
from emensageria.s2205.models import s2205CTPS
from emensageria.s2205.models import s2205CTPS
from emensageria.s2205.models import s2205RIC
from emensageria.s2205.models import s2205RIC
from emensageria.s2205.models import s2205RG
from emensageria.s2205.models import s2205RG
from emensageria.s2205.models import s2205RNE
from emensageria.s2205.models import s2205RNE
from emensageria.s2205.models import s2205OC
from emensageria.s2205.models import s2205OC
from emensageria.s2205.models import s2205CNH
from emensageria.s2205.models import s2205CNH
from emensageria.s2205.models import s2205brasil
from emensageria.s2205.models import s2205brasil
from emensageria.s2205.models import s2205exterior
from emensageria.s2205.models import s2205exterior
from emensageria.s2205.models import s2205infoDeficiencia
from emensageria.s2205.models import s2205infoDeficiencia
from emensageria.s2205.models import s2205aposentadoria
from emensageria.s2205.models import s2205aposentadoria
from emensageria.s2205.models import s2205contato
from emensageria.s2205.models import s2205contato
from emensageria.s2206.models import s2206infoCeletista
from emensageria.s2206.models import s2206infoCeletista
from emensageria.s2206.models import s2206trabTemp
from emensageria.s2206.models import s2206trabTemp
from emensageria.s2206.models import s2206aprend
from emensageria.s2206.models import s2206aprend
from emensageria.s2206.models import s2206infoEstatutario
from emensageria.s2206.models import s2206infoEstatutario
from emensageria.s2206.models import s2206localTrabGeral
from emensageria.s2206.models import s2206localTrabGeral
from emensageria.s2206.models import s2206localTrabDom
from emensageria.s2206.models import s2206localTrabDom
from emensageria.s2206.models import s2206horContratual
from emensageria.s2206.models import s2206horContratual
from emensageria.s2206.models import s2206horario
from emensageria.s2206.models import s2206horario
from emensageria.s2206.models import s2206filiacaoSindical
from emensageria.s2206.models import s2206filiacaoSindical
from emensageria.s2206.models import s2206alvaraJudicial
from emensageria.s2206.models import s2206alvaraJudicial
from emensageria.s2206.models import s2206observacoes
from emensageria.s2206.models import s2206observacoes
from emensageria.s2206.models import s2206servPubl
from emensageria.s2206.models import s2206servPubl
from emensageria.s2210.models import s2210parteAtingida
from emensageria.s2210.models import s2210parteAtingida
from emensageria.s2210.models import s2210agenteCausador
from emensageria.s2210.models import s2210agenteCausador
from emensageria.s2210.models import s2210atestado
from emensageria.s2210.models import s2210atestado
from emensageria.s2210.models import s2210catOrigem
from emensageria.s2210.models import s2210catOrigem
from emensageria.s2220.models import s2220exame
from emensageria.s2220.models import s2220exame
from emensageria.s2230.models import s2230iniAfastamento
from emensageria.s2230.models import s2230iniAfastamento
from emensageria.s2230.models import s2230infoAtestado
from emensageria.s2230.models import s2230infoAtestado
from emensageria.s2230.models import s2230emitente
from emensageria.s2230.models import s2230emitente
from emensageria.s2230.models import s2230infoCessao
from emensageria.s2230.models import s2230infoCessao
from emensageria.s2230.models import s2230infoMandSind
from emensageria.s2230.models import s2230infoMandSind
from emensageria.s2230.models import s2230infoRetif
from emensageria.s2230.models import s2230infoRetif
from emensageria.s2230.models import s2230fimAfastamento
from emensageria.s2230.models import s2230fimAfastamento
from emensageria.s2240.models import s2240iniExpRisco
from emensageria.s2240.models import s2240iniExpRisco
from emensageria.s2240.models import s2240iniExpRiscoinfoAmb
from emensageria.s2240.models import s2240iniExpRiscoinfoAmb
from emensageria.s2240.models import s2240iniExpRiscofatRisco
from emensageria.s2240.models import s2240iniExpRiscofatRisco
from emensageria.s2240.models import s2240iniExpRiscoepc
from emensageria.s2240.models import s2240iniExpRiscoepc
from emensageria.s2240.models import s2240iniExpRiscoepi
from emensageria.s2240.models import s2240iniExpRiscoepi
from emensageria.s2240.models import s2240altExpRisco
from emensageria.s2240.models import s2240altExpRisco
from emensageria.s2240.models import s2240altExpRiscoinfoAmb
from emensageria.s2240.models import s2240altExpRiscoinfoAmb
from emensageria.s2240.models import s2240altExpRiscofatRisco
from emensageria.s2240.models import s2240altExpRiscofatRisco
from emensageria.s2240.models import s2240altExpRiscoepc
from emensageria.s2240.models import s2240altExpRiscoepc
from emensageria.s2240.models import s2240altExpRiscoepi
from emensageria.s2240.models import s2240altExpRiscoepi
from emensageria.s2240.models import s2240fimExpRisco
from emensageria.s2240.models import s2240fimExpRisco
from emensageria.s2240.models import s2240fimExpRiscoinfoAmb
from emensageria.s2240.models import s2240fimExpRiscoinfoAmb
from emensageria.s2240.models import s2240fimExpRiscorespReg
from emensageria.s2240.models import s2240fimExpRiscorespReg
from emensageria.s2241.models import s2241insalPeric
from emensageria.s2241.models import s2241insalPeric
from emensageria.s2241.models import s2241iniInsalPeric
from emensageria.s2241.models import s2241iniInsalPeric
from emensageria.s2241.models import s2241iniInsalPericinfoAmb
from emensageria.s2241.models import s2241iniInsalPericinfoAmb
from emensageria.s2241.models import s2241iniInsalPericfatRisco
from emensageria.s2241.models import s2241iniInsalPericfatRisco
from emensageria.s2241.models import s2241altInsalPeric
from emensageria.s2241.models import s2241altInsalPeric
from emensageria.s2241.models import s2241altInsalPericinfoamb
from emensageria.s2241.models import s2241altInsalPericinfoamb
from emensageria.s2241.models import s2241altInsalPericfatRisco
from emensageria.s2241.models import s2241altInsalPericfatRisco
from emensageria.s2241.models import s2241fimInsalPeric
from emensageria.s2241.models import s2241fimInsalPeric
from emensageria.s2241.models import s2241fimInsalPericinfoAmb
from emensageria.s2241.models import s2241fimInsalPericinfoAmb
from emensageria.s2241.models import s2241aposentEsp
from emensageria.s2241.models import s2241aposentEsp
from emensageria.s2241.models import s2241iniAposentEsp
from emensageria.s2241.models import s2241iniAposentEsp
from emensageria.s2241.models import s2241iniAposentEspinfoAmb
from emensageria.s2241.models import s2241iniAposentEspinfoAmb
from emensageria.s2241.models import s2241iniAposentEspfatRisco
from emensageria.s2241.models import s2241iniAposentEspfatRisco
from emensageria.s2241.models import s2241altAposentEsp
from emensageria.s2241.models import s2241altAposentEsp
from emensageria.s2241.models import s2241altAposentEspinfoamb
from emensageria.s2241.models import s2241altAposentEspinfoamb
from emensageria.s2241.models import s2241altAposentEspfatRisco
from emensageria.s2241.models import s2241altAposentEspfatRisco
from emensageria.s2241.models import s2241fimAposentEsp
from emensageria.s2241.models import s2241fimAposentEsp
from emensageria.s2241.models import s2241fimAposentEspinfoAmb
from emensageria.s2241.models import s2241fimAposentEspinfoAmb
from emensageria.s2250.models import s2250detAvPrevio
from emensageria.s2250.models import s2250detAvPrevio
from emensageria.s2250.models import s2250cancAvPrevio
from emensageria.s2250.models import s2250cancAvPrevio
from emensageria.s2260.models import s2260localTrabInterm
from emensageria.s2260.models import s2260localTrabInterm
from emensageria.s2299.models import s2299observacoes
from emensageria.s2299.models import s2299observacoes
from emensageria.s2299.models import s2299sucessaoVinc
from emensageria.s2299.models import s2299sucessaoVinc
from emensageria.s2299.models import s2299transfTit
from emensageria.s2299.models import s2299transfTit
from emensageria.s2299.models import s2299verbasResc
from emensageria.s2299.models import s2299verbasResc
from emensageria.s2299.models import s2299dmDev
from emensageria.s2299.models import s2299dmDev
from emensageria.s2299.models import s2299infoPerApur
from emensageria.s2299.models import s2299infoPerApur
from emensageria.s2299.models import s2299infoPerApurideEstabLot
from emensageria.s2299.models import s2299infoPerApurideEstabLot
from emensageria.s2299.models import s2299infoPerApurdetVerbas
from emensageria.s2299.models import s2299infoPerApurdetVerbas
from emensageria.s2299.models import s2299infoPerAntinfoSimples
from emensageria.s2299.models import s2299infoPerAntinfoSimples
from emensageria.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageria.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageria.s2299.models import s2299infoPerApurdetOper
from emensageria.s2299.models import s2299infoPerApurdetOper
from emensageria.s2299.models import s2299infoPerApurdetPlano
from emensageria.s2299.models import s2299infoPerApurdetPlano
from emensageria.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageria.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageria.s2299.models import s2299infoPerApurinfoSimples
from emensageria.s2299.models import s2299infoPerApurinfoSimples
from emensageria.s2299.models import s2299infoPerAnt
from emensageria.s2299.models import s2299infoPerAnt
from emensageria.s2299.models import s2299infoPerAntideADC
from emensageria.s2299.models import s2299infoPerAntideADC
from emensageria.s2299.models import s2299infoPerAntidePeriodo
from emensageria.s2299.models import s2299infoPerAntidePeriodo
from emensageria.s2299.models import s2299infoPerAntideEstabLot
from emensageria.s2299.models import s2299infoPerAntideEstabLot
from emensageria.s2299.models import s2299infoPerAntdetVerbas
from emensageria.s2299.models import s2299infoPerAntdetVerbas
from emensageria.s2299.models import s2299infoPerAntinfoAgNocivo
from emensageria.s2299.models import s2299infoPerAntinfoAgNocivo
from emensageria.s2299.models import s2299infoTrabInterm
from emensageria.s2299.models import s2299infoTrabInterm
from emensageria.s2299.models import s2299infoTrabIntermprocJudTrab
from emensageria.s2299.models import s2299infoTrabIntermprocJudTrab
from emensageria.s2299.models import s2299infoTrabInterminfoMV
from emensageria.s2299.models import s2299infoTrabInterminfoMV
from emensageria.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageria.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageria.s2299.models import s2299infoTrabIntermprocCS
from emensageria.s2299.models import s2299infoTrabIntermprocCS
from emensageria.s2299.models import s2299infoTrabIntermquarentena
from emensageria.s2299.models import s2299infoTrabIntermquarentena
from emensageria.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageria.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageria.s2300.models import s2300documentos
from emensageria.s2300.models import s2300documentos
from emensageria.s2300.models import s2300CTPS
from emensageria.s2300.models import s2300CTPS
from emensageria.s2300.models import s2300RIC
from emensageria.s2300.models import s2300RIC
from emensageria.s2300.models import s2300RG
from emensageria.s2300.models import s2300RG
from emensageria.s2300.models import s2300RNE
from emensageria.s2300.models import s2300RNE
from emensageria.s2300.models import s2300OC
from emensageria.s2300.models import s2300OC
from emensageria.s2300.models import s2300CNH
from emensageria.s2300.models import s2300CNH
from emensageria.s2300.models import s2300brasil
from emensageria.s2300.models import s2300brasil
from emensageria.s2300.models import s2300exterior
from emensageria.s2300.models import s2300exterior
from emensageria.s2300.models import s2300trabEstrangeiro
from emensageria.s2300.models import s2300trabEstrangeiro
from emensageria.s2300.models import s2300infoDeficiencia
from emensageria.s2300.models import s2300infoDeficiencia
from emensageria.s2300.models import s2300dependente
from emensageria.s2300.models import s2300dependente
from emensageria.s2300.models import s2300contato
from emensageria.s2300.models import s2300contato
from emensageria.s2300.models import s2300infoComplementares
from emensageria.s2300.models import s2300infoComplementares
from emensageria.s2300.models import s2300cargoFuncao
from emensageria.s2300.models import s2300cargoFuncao
from emensageria.s2300.models import s2300remuneracao
from emensageria.s2300.models import s2300remuneracao
from emensageria.s2300.models import s2300fgts
from emensageria.s2300.models import s2300fgts
from emensageria.s2300.models import s2300infoDirigenteSindical
from emensageria.s2300.models import s2300infoDirigenteSindical
from emensageria.s2300.models import s2300infoTrabCedido
from emensageria.s2300.models import s2300infoTrabCedido
from emensageria.s2300.models import s2300infoEstagiario
from emensageria.s2300.models import s2300infoEstagiario
from emensageria.s2300.models import s2300ageIntegracao
from emensageria.s2300.models import s2300ageIntegracao
from emensageria.s2300.models import s2300supervisorEstagio
from emensageria.s2300.models import s2300supervisorEstagio
from emensageria.s2300.models import s2300afastamento
from emensageria.s2300.models import s2300afastamento
from emensageria.s2300.models import s2300termino
from emensageria.s2300.models import s2300termino
from emensageria.s2306.models import s2306infoComplementares
from emensageria.s2306.models import s2306infoComplementares
from emensageria.s2306.models import s2306cargoFuncao
from emensageria.s2306.models import s2306cargoFuncao
from emensageria.s2306.models import s2306remuneracao
from emensageria.s2306.models import s2306remuneracao
from emensageria.s2306.models import s2306infoEstagiario
from emensageria.s2306.models import s2306infoEstagiario
from emensageria.s2306.models import s2306ageIntegracao
from emensageria.s2306.models import s2306ageIntegracao
from emensageria.s2306.models import s2306supervisorEstagio
from emensageria.s2306.models import s2306supervisorEstagio
from emensageria.s2399.models import s2399verbasResc
from emensageria.s2399.models import s2399verbasResc
from emensageria.s2399.models import s2399dmDev
from emensageria.s2399.models import s2399dmDev
from emensageria.s2399.models import s2399ideEstabLot
from emensageria.s2399.models import s2399ideEstabLot
from emensageria.s2399.models import s2399detVerbas
from emensageria.s2399.models import s2399detVerbas
from emensageria.s2400.models import s2400fimBeneficio
from emensageria.s2400.models import s2400fimBeneficio
from emensageria.s2399.models import s2399infoSaudeColet
from emensageria.s2399.models import s2399infoSaudeColet
from emensageria.s2399.models import s2399detOper
from emensageria.s2399.models import s2399detOper
from emensageria.s2399.models import s2399detPlano
from emensageria.s2399.models import s2399detPlano
from emensageria.s2399.models import s2399infoAgNocivo
from emensageria.s2399.models import s2399infoAgNocivo
from emensageria.s2399.models import s2399infoSimples
from emensageria.s2399.models import s2399infoSimples
from emensageria.s2399.models import s2399procJudTrab
from emensageria.s2399.models import s2399procJudTrab
from emensageria.s2399.models import s2399infoMV
from emensageria.s2399.models import s2399infoMV
from emensageria.s2399.models import s2399remunOutrEmpr
from emensageria.s2399.models import s2399remunOutrEmpr
from emensageria.s2399.models import s2399quarentena
from emensageria.s2399.models import s2399quarentena
from emensageria.s2400.models import s2400brasil
from emensageria.s2400.models import s2400brasil
from emensageria.s2400.models import s2400exterior
from emensageria.s2400.models import s2400exterior
from emensageria.s2400.models import s2400iniBeneficio
from emensageria.s2400.models import s2400iniBeneficio
from emensageria.s2400.models import s2400iniBeneficioinfoPenMorte
from emensageria.s2400.models import s2400iniBeneficioinfoPenMorte
from emensageria.s2400.models import s2400altBeneficio
from emensageria.s2400.models import s2400altBeneficio
from emensageria.s2400.models import s2400altBeneficioinfoPenMorte
from emensageria.s2400.models import s2400altBeneficioinfoPenMorte
from emensageria.s5011.models import s5011infoEstab
from emensageria.s5011.models import s5011infoEstab
from emensageria.s3000.models import s3000ideTrabalhador
from emensageria.s3000.models import s3000ideTrabalhador
from emensageria.s3000.models import s3000ideFolhaPagto
from emensageria.s3000.models import s3000ideFolhaPagto
from emensageria.s5001.models import s5001procJudTrab
from emensageria.s5001.models import s5001procJudTrab
from emensageria.s5001.models import s5001infoCpCalc
from emensageria.s5001.models import s5001infoCpCalc
from emensageria.s5001.models import s5001ideEstabLot
from emensageria.s5001.models import s5001ideEstabLot
from emensageria.s5001.models import s5001infoCategIncid
from emensageria.s5001.models import s5001infoCategIncid
from emensageria.s5001.models import s5001infoBaseCS
from emensageria.s5001.models import s5001infoBaseCS
from emensageria.s5001.models import s5001calcTerc
from emensageria.s5001.models import s5001calcTerc
from emensageria.s5002.models import s5002infoDep
from emensageria.s5002.models import s5002infoDep
from emensageria.s5002.models import s5002infoIrrf
from emensageria.s5002.models import s5002infoIrrf
from emensageria.s5002.models import s5002basesIrrf
from emensageria.s5002.models import s5002basesIrrf
from emensageria.s5002.models import s5002irrf
from emensageria.s5002.models import s5002irrf
from emensageria.s5002.models import s5002idePgtoExt
from emensageria.s5002.models import s5002idePgtoExt
from emensageria.s5011.models import s5011infoCPSeg
from emensageria.s5011.models import s5011infoCPSeg
from emensageria.s5011.models import s5011infoPJ
from emensageria.s5011.models import s5011infoPJ
from emensageria.s5011.models import s5011infoAtConc
from emensageria.s5011.models import s5011infoAtConc
from emensageria.s5011.models import s5011ideEstab
from emensageria.s5011.models import s5011ideEstab
from emensageria.s5011.models import s5011infoComplObra
from emensageria.s5011.models import s5011infoComplObra
from emensageria.s5011.models import s5011ideLotacao
from emensageria.s5011.models import s5011ideLotacao
from emensageria.s5011.models import s5011infoTercSusp
from emensageria.s5011.models import s5011infoTercSusp
from emensageria.s5011.models import s5011infoEmprParcial
from emensageria.s5011.models import s5011infoEmprParcial
from emensageria.s5011.models import s5011dadosOpPort
from emensageria.s5011.models import s5011dadosOpPort
from emensageria.s5011.models import s5011basesRemun
from emensageria.s5011.models import s5011basesRemun
from emensageria.s5011.models import s5011basesAvNPort
from emensageria.s5011.models import s5011basesAvNPort
from emensageria.s5011.models import s5011infoSubstPatrOpPort
from emensageria.s5011.models import s5011infoSubstPatrOpPort
from emensageria.s5011.models import s5011basesAquis
from emensageria.s5011.models import s5011basesAquis
from emensageria.s5011.models import s5011basesComerc
from emensageria.s5011.models import s5011basesComerc
from emensageria.s5011.models import s5011infoCREstab
from emensageria.s5011.models import s5011infoCREstab
from emensageria.s5011.models import s5011infoCRContrib
from emensageria.s5011.models import s5011infoCRContrib
from emensageria.s5012.models import s5012infoCRContrib
from emensageria.s5012.models import s5012infoCRContrib
from emensageria.mensageiro.forms import form_transmissor_lote
from emensageria.mensageiro.forms import form_transmissor_lote
from emensageria.mensageiro.forms import form_transmissor_lote_ocorrencias
from emensageria.mensageiro.forms import form_transmissor_lote_ocorrencias
from emensageria.eventos.forms import form_s1000_evtinfoempregador_ocorrencias
from emensageria.eventos.forms import form_s1000_evtinfoempregador_ocorrencias
from emensageria.eventos.forms import form_s1005_evttabestab_ocorrencias
from emensageria.eventos.forms import form_s1005_evttabestab_ocorrencias
from emensageria.eventos.forms import form_s1010_evttabrubrica_ocorrencias
from emensageria.eventos.forms import form_s1010_evttabrubrica_ocorrencias
from emensageria.eventos.forms import form_s1020_evttablotacao_ocorrencias
from emensageria.eventos.forms import form_s1020_evttablotacao_ocorrencias
from emensageria.eventos.forms import form_s1030_evttabcargo_ocorrencias
from emensageria.eventos.forms import form_s1030_evttabcargo_ocorrencias
from emensageria.eventos.forms import form_s1035_evttabcarreira_ocorrencias
from emensageria.eventos.forms import form_s1035_evttabcarreira_ocorrencias
from emensageria.eventos.forms import form_s1040_evttabfuncao_ocorrencias
from emensageria.eventos.forms import form_s1040_evttabfuncao_ocorrencias
from emensageria.eventos.forms import form_s1050_evttabhortur_ocorrencias
from emensageria.eventos.forms import form_s1050_evttabhortur_ocorrencias
from emensageria.eventos.forms import form_s1060_evttabambiente_ocorrencias
from emensageria.eventos.forms import form_s1060_evttabambiente_ocorrencias
from emensageria.eventos.forms import form_s1070_evttabprocesso_ocorrencias
from emensageria.eventos.forms import form_s1070_evttabprocesso_ocorrencias
from emensageria.eventos.forms import form_s1080_evttaboperport_ocorrencias
from emensageria.eventos.forms import form_s1080_evttaboperport_ocorrencias
from emensageria.eventos.forms import form_s1200_evtremun_ocorrencias
from emensageria.eventos.forms import form_s1200_evtremun_ocorrencias
from emensageria.eventos.forms import form_s1202_evtrmnrpps_ocorrencias
from emensageria.eventos.forms import form_s1202_evtrmnrpps_ocorrencias
from emensageria.eventos.forms import form_s1207_evtbenprrp_ocorrencias
from emensageria.eventos.forms import form_s1207_evtbenprrp_ocorrencias
from emensageria.eventos.forms import form_s1210_evtpgtos_ocorrencias
from emensageria.eventos.forms import form_s1210_evtpgtos_ocorrencias
from emensageria.eventos.forms import form_s1250_evtaqprod_ocorrencias
from emensageria.eventos.forms import form_s1250_evtaqprod_ocorrencias
from emensageria.eventos.forms import form_s1260_evtcomprod_ocorrencias
from emensageria.eventos.forms import form_s1260_evtcomprod_ocorrencias
from emensageria.eventos.forms import form_s1270_evtcontratavnp_ocorrencias
from emensageria.eventos.forms import form_s1270_evtcontratavnp_ocorrencias
from emensageria.eventos.forms import form_s1280_evtinfocomplper
from emensageria.eventos.forms import form_s1280_evtinfocomplper
from emensageria.eventos.forms import form_s1295_evttotconting_ocorrencias
from emensageria.eventos.forms import form_s1295_evttotconting_ocorrencias
from emensageria.eventos.forms import form_s1298_evtreabreevper_ocorrencias
from emensageria.eventos.forms import form_s1298_evtreabreevper_ocorrencias
from emensageria.eventos.forms import form_s1299_evtfechaevper_ocorrencias
from emensageria.eventos.forms import form_s1299_evtfechaevper_ocorrencias
from emensageria.eventos.forms import form_s1300_evtcontrsindpatr_ocorrencias
from emensageria.eventos.forms import form_s1300_evtcontrsindpatr_ocorrencias
from emensageria.eventos.forms import form_s2190_evtadmprelim_ocorrencias
from emensageria.eventos.forms import form_s2190_evtadmprelim_ocorrencias
from emensageria.eventos.forms import form_s2200_evtadmissao_ocorrencias
from emensageria.eventos.forms import form_s2200_evtadmissao_ocorrencias
from emensageria.eventos.forms import form_s2205_evtaltcadastral_ocorrencias
from emensageria.eventos.forms import form_s2205_evtaltcadastral_ocorrencias
from emensageria.eventos.forms import form_s2206_evtaltcontratual_ocorrencias
from emensageria.eventos.forms import form_s2206_evtaltcontratual_ocorrencias
from emensageria.eventos.forms import form_s2210_evtcat_ocorrencias
from emensageria.eventos.forms import form_s2210_evtcat_ocorrencias
from emensageria.eventos.forms import form_s2220_evtmonit_ocorrencias
from emensageria.eventos.forms import form_s2220_evtmonit_ocorrencias
from emensageria.eventos.forms import form_s2230_evtafasttemp_ocorrencias
from emensageria.eventos.forms import form_s2230_evtafasttemp_ocorrencias
from emensageria.eventos.forms import form_s2240_evtexprisco_ocorrencias
from emensageria.eventos.forms import form_s2240_evtexprisco_ocorrencias
from emensageria.eventos.forms import form_s2241_evtinsapo_ocorrencias
from emensageria.eventos.forms import form_s2241_evtinsapo_ocorrencias
from emensageria.eventos.forms import form_s2250_evtavprevio_ocorrencias
from emensageria.eventos.forms import form_s2250_evtavprevio_ocorrencias
from emensageria.eventos.forms import form_s2260_evtconvinterm_ocorrencias
from emensageria.eventos.forms import form_s2260_evtconvinterm_ocorrencias
from emensageria.eventos.forms import form_s2298_evtreintegr_ocorrencias
from emensageria.eventos.forms import form_s2298_evtreintegr_ocorrencias
from emensageria.eventos.forms import form_s2299_evtdeslig_ocorrencias
from emensageria.eventos.forms import form_s2299_evtdeslig_ocorrencias
from emensageria.eventos.forms import form_s2300_evttsvinicio_ocorrencias
from emensageria.eventos.forms import form_s2300_evttsvinicio_ocorrencias
from emensageria.eventos.forms import form_s2306_evttsvaltcontr_ocorrencias
from emensageria.eventos.forms import form_s2306_evttsvaltcontr_ocorrencias
from emensageria.eventos.forms import form_s2399_evttsvtermino_ocorrencias
from emensageria.eventos.forms import form_s2399_evttsvtermino_ocorrencias
from emensageria.eventos.forms import form_s2400_evtcdbenprrp_ocorrencias
from emensageria.eventos.forms import form_s2400_evtcdbenprrp_ocorrencias
from emensageria.eventos.forms import form_s3000_evtexclusao_ocorrencias
from emensageria.eventos.forms import form_s3000_evtexclusao_ocorrencias
from emensageria.eventos.forms import form_s5001_evtbasestrab_ocorrencias
from emensageria.eventos.forms import form_s5001_evtbasestrab_ocorrencias
from emensageria.eventos.forms import form_s5002_evtirrfbenef_ocorrencias
from emensageria.eventos.forms import form_s5002_evtirrfbenef_ocorrencias
from emensageria.eventos.forms import form_s5011_evtcs_ocorrencias
from emensageria.eventos.forms import form_s5011_evtcs_ocorrencias
from emensageria.eventos.forms import form_s5012_evtirrf_ocorrencias
from emensageria.eventos.forms import form_s5012_evtirrf_ocorrencias
from emensageria.eventos.forms import form_s1000_evtinfoempregador
from emensageria.eventos.forms import form_s1000_evtinfoempregador
from emensageria.eventos.forms import form_s1005_evttabestab
from emensageria.eventos.forms import form_s1005_evttabestab
from emensageria.eventos.forms import form_s1010_evttabrubrica
from emensageria.eventos.forms import form_s1010_evttabrubrica
from emensageria.eventos.forms import form_s1020_evttablotacao
from emensageria.eventos.forms import form_s1020_evttablotacao
from emensageria.eventos.forms import form_s1030_evttabcargo
from emensageria.eventos.forms import form_s1030_evttabcargo
from emensageria.eventos.forms import form_s1035_evttabcarreira
from emensageria.eventos.forms import form_s1035_evttabcarreira
from emensageria.eventos.forms import form_s1040_evttabfuncao
from emensageria.eventos.forms import form_s1040_evttabfuncao
from emensageria.eventos.forms import form_s1050_evttabhortur
from emensageria.eventos.forms import form_s1050_evttabhortur
from emensageria.eventos.forms import form_s1060_evttabambiente
from emensageria.eventos.forms import form_s1060_evttabambiente
from emensageria.eventos.forms import form_s1070_evttabprocesso
from emensageria.eventos.forms import form_s1070_evttabprocesso
from emensageria.eventos.forms import form_s1080_evttaboperport
from emensageria.eventos.forms import form_s1080_evttaboperport
from emensageria.eventos.forms import form_s1200_evtremun
from emensageria.eventos.forms import form_s1200_evtremun
from emensageria.eventos.forms import form_s1202_evtrmnrpps
from emensageria.eventos.forms import form_s1202_evtrmnrpps
from emensageria.eventos.forms import form_s1207_evtbenprrp
from emensageria.eventos.forms import form_s1207_evtbenprrp
from emensageria.eventos.forms import form_s1210_evtpgtos
from emensageria.eventos.forms import form_s1210_evtpgtos
from emensageria.eventos.forms import form_s1250_evtaqprod
from emensageria.eventos.forms import form_s1250_evtaqprod
from emensageria.eventos.forms import form_s1260_evtcomprod
from emensageria.eventos.forms import form_s1260_evtcomprod
from emensageria.eventos.forms import form_s1270_evtcontratavnp
from emensageria.eventos.forms import form_s1270_evtcontratavnp
from emensageria.eventos.forms import form_s1280_evtinfocomplper
from emensageria.eventos.forms import form_s1280_evtinfocomplper
from emensageria.eventos.forms import form_s1295_evttotconting
from emensageria.eventos.forms import form_s1295_evttotconting
from emensageria.eventos.forms import form_s1298_evtreabreevper
from emensageria.eventos.forms import form_s1298_evtreabreevper
from emensageria.eventos.forms import form_s1299_evtfechaevper
from emensageria.eventos.forms import form_s1299_evtfechaevper
from emensageria.eventos.forms import form_s1300_evtcontrsindpatr
from emensageria.eventos.forms import form_s1300_evtcontrsindpatr
from emensageria.eventos.forms import form_s2190_evtadmprelim
from emensageria.eventos.forms import form_s2190_evtadmprelim
from emensageria.eventos.forms import form_s2200_evtadmissao
from emensageria.eventos.forms import form_s2200_evtadmissao
from emensageria.eventos.forms import form_s2205_evtaltcadastral
from emensageria.eventos.forms import form_s2205_evtaltcadastral
from emensageria.eventos.forms import form_s2206_evtaltcontratual
from emensageria.eventos.forms import form_s2206_evtaltcontratual
from emensageria.eventos.forms import form_s2210_evtcat
from emensageria.eventos.forms import form_s2210_evtcat
from emensageria.eventos.forms import form_s2220_evtmonit
from emensageria.eventos.forms import form_s2220_evtmonit
from emensageria.eventos.forms import form_s2230_evtafasttemp
from emensageria.eventos.forms import form_s2230_evtafasttemp
from emensageria.eventos.forms import form_s2240_evtexprisco
from emensageria.eventos.forms import form_s2240_evtexprisco
from emensageria.eventos.forms import form_s2241_evtinsapo
from emensageria.eventos.forms import form_s2241_evtinsapo
from emensageria.eventos.forms import form_s2250_evtavprevio
from emensageria.eventos.forms import form_s2250_evtavprevio
from emensageria.eventos.forms import form_s2260_evtconvinterm
from emensageria.eventos.forms import form_s2260_evtconvinterm
from emensageria.eventos.forms import form_s2298_evtreintegr
from emensageria.eventos.forms import form_s2298_evtreintegr
from emensageria.eventos.forms import form_s2299_evtdeslig
from emensageria.eventos.forms import form_s2299_evtdeslig
from emensageria.eventos.forms import form_s2300_evttsvinicio
from emensageria.eventos.forms import form_s2300_evttsvinicio
from emensageria.eventos.forms import form_s2306_evttsvaltcontr
from emensageria.eventos.forms import form_s2306_evttsvaltcontr
from emensageria.eventos.forms import form_s2399_evttsvtermino
from emensageria.eventos.forms import form_s2399_evttsvtermino
from emensageria.eventos.forms import form_s2400_evtcdbenprrp
from emensageria.eventos.forms import form_s2400_evtcdbenprrp
from emensageria.eventos.forms import form_s3000_evtexclusao
from emensageria.eventos.forms import form_s3000_evtexclusao
from emensageria.eventos.forms import form_s5001_evtbasestrab
from emensageria.eventos.forms import form_s5001_evtbasestrab
from emensageria.eventos.forms import form_s5002_evtirrfbenef
from emensageria.eventos.forms import form_s5002_evtirrfbenef
from emensageria.eventos.forms import form_s5011_evtcs
from emensageria.eventos.forms import form_s5011_evtcs
from emensageria.eventos.forms import form_s5012_evtirrf
from emensageria.eventos.forms import form_s5012_evtirrf
from emensageria.s1000.forms import form_s1000_inclusao
from emensageria.s1000.forms import form_s1000_inclusao
from emensageria.s1000.forms import form_s1000_inclusao_dadosisencao
from emensageria.s1000.forms import form_s1000_inclusao_dadosisencao
from emensageria.s1000.forms import form_s1000_inclusao_infoop
from emensageria.s1000.forms import form_s1000_inclusao_infoop
from emensageria.s1000.forms import form_s1000_inclusao_infoefr
from emensageria.s1000.forms import form_s1000_inclusao_infoefr
from emensageria.s1000.forms import form_s1000_inclusao_infoente
from emensageria.s1000.forms import form_s1000_inclusao_infoente
from emensageria.s1000.forms import form_s1000_inclusao_infoorginternacional
from emensageria.s1000.forms import form_s1000_inclusao_infoorginternacional
from emensageria.s1000.forms import form_s1000_inclusao_softwarehouse
from emensageria.s1000.forms import form_s1000_inclusao_softwarehouse
from emensageria.s1000.forms import form_s1000_inclusao_situacaopj
from emensageria.s1000.forms import form_s1000_inclusao_situacaopj
from emensageria.s1000.forms import form_s1000_inclusao_situacaopf
from emensageria.s1000.forms import form_s1000_inclusao_situacaopf
from emensageria.s1000.forms import form_s1000_alteracao
from emensageria.s1000.forms import form_s1000_alteracao
from emensageria.s1000.forms import form_s1000_alteracao_dadosisencao
from emensageria.s1000.forms import form_s1000_alteracao_dadosisencao
from emensageria.s1000.forms import form_s1000_alteracao_infoop
from emensageria.s1000.forms import form_s1000_alteracao_infoop
from emensageria.s1000.forms import form_s1000_alteracao_infoefr
from emensageria.s1000.forms import form_s1000_alteracao_infoefr
from emensageria.s1000.forms import form_s1000_alteracao_infoente
from emensageria.s1000.forms import form_s1000_alteracao_infoente
from emensageria.s1000.forms import form_s1000_alteracao_infoorginternacional
from emensageria.s1000.forms import form_s1000_alteracao_infoorginternacional
from emensageria.s1000.forms import form_s1000_alteracao_softwarehouse
from emensageria.s1000.forms import form_s1000_alteracao_softwarehouse
from emensageria.s1000.forms import form_s1000_alteracao_situacaopj
from emensageria.s1000.forms import form_s1000_alteracao_situacaopj
from emensageria.s1000.forms import form_s1000_alteracao_situacaopf
from emensageria.s1000.forms import form_s1000_alteracao_situacaopf
from emensageria.s1035.forms import form_s1035_inclusao
from emensageria.s1035.forms import form_s1035_inclusao
from emensageria.s1000.forms import form_s1000_alteracao_novavalidade
from emensageria.s1000.forms import form_s1000_alteracao_novavalidade
from emensageria.s1000.forms import form_s1000_exclusao
from emensageria.s1000.forms import form_s1000_exclusao
from emensageria.s1005.forms import form_s1005_inclusao
from emensageria.s1005.forms import form_s1005_inclusao
from emensageria.s1005.forms import form_s1005_inclusao_procadmjudrat
from emensageria.s1005.forms import form_s1005_inclusao_procadmjudrat
from emensageria.s1005.forms import form_s1005_inclusao_procadmjudfap
from emensageria.s1005.forms import form_s1005_inclusao_procadmjudfap
from emensageria.s1005.forms import form_s1005_inclusao_infocaepf
from emensageria.s1005.forms import form_s1005_inclusao_infocaepf
from emensageria.s1005.forms import form_s1005_inclusao_infoobra
from emensageria.s1005.forms import form_s1005_inclusao_infoobra
from emensageria.s1005.forms import form_s1005_inclusao_infoenteduc
from emensageria.s1005.forms import form_s1005_inclusao_infoenteduc
from emensageria.s1005.forms import form_s1005_inclusao_infopcd
from emensageria.s1005.forms import form_s1005_inclusao_infopcd
from emensageria.s1005.forms import form_s1005_alteracao
from emensageria.s1005.forms import form_s1005_alteracao
from emensageria.s1005.forms import form_s1005_alteracao_procadmjudrat
from emensageria.s1005.forms import form_s1005_alteracao_procadmjudrat
from emensageria.s1005.forms import form_s1005_alteracao_procadmjudfap
from emensageria.s1005.forms import form_s1005_alteracao_procadmjudfap
from emensageria.s1005.forms import form_s1005_alteracao_infocaepf
from emensageria.s1005.forms import form_s1005_alteracao_infocaepf
from emensageria.s1005.forms import form_s1005_alteracao_infoobra
from emensageria.s1005.forms import form_s1005_alteracao_infoobra
from emensageria.s1005.forms import form_s1005_alteracao_infoenteduc
from emensageria.s1005.forms import form_s1005_alteracao_infoenteduc
from emensageria.s1005.forms import form_s1005_alteracao_infopcd
from emensageria.s1005.forms import form_s1005_alteracao_infopcd
from emensageria.s1005.forms import form_s1005_alteracao_novavalidade
from emensageria.s1005.forms import form_s1005_alteracao_novavalidade
from emensageria.s1005.forms import form_s1005_exclusao
from emensageria.s1005.forms import form_s1005_exclusao
from emensageria.s1010.forms import form_s1010_inclusao
from emensageria.s1010.forms import form_s1010_inclusao
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessocp
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessocp
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessoirrf
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessoirrf
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessofgts
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessofgts
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessosind
from emensageria.s1010.forms import form_s1010_inclusao_ideprocessosind
from emensageria.s1010.forms import form_s1010_alteracao
from emensageria.s1010.forms import form_s1010_alteracao
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessocp
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessocp
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessoirrf
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessoirrf
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessofgts
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessofgts
from emensageria.s1035.forms import form_s1035_alteracao
from emensageria.s1035.forms import form_s1035_alteracao
from emensageria.s1035.forms import form_s1035_alteracao_novavalidade
from emensageria.s1035.forms import form_s1035_alteracao_novavalidade
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessosind
from emensageria.s1010.forms import form_s1010_alteracao_ideprocessosind
from emensageria.s1010.forms import form_s1010_alteracao_novavalidade
from emensageria.s1010.forms import form_s1010_alteracao_novavalidade
from emensageria.s1010.forms import form_s1010_exclusao
from emensageria.s1010.forms import form_s1010_exclusao
from emensageria.s1020.forms import form_s1020_inclusao
from emensageria.s1020.forms import form_s1020_inclusao
from emensageria.s1020.forms import form_s1020_inclusao_infoprocjudterceiros
from emensageria.s1020.forms import form_s1020_inclusao_infoprocjudterceiros
from emensageria.s1020.forms import form_s1020_inclusao_procjudterceiro
from emensageria.s1020.forms import form_s1020_inclusao_procjudterceiro
from emensageria.s1020.forms import form_s1020_inclusao_infoemprparcial
from emensageria.s1020.forms import form_s1020_inclusao_infoemprparcial
from emensageria.s1020.forms import form_s1020_alteracao
from emensageria.s1020.forms import form_s1020_alteracao
from emensageria.s1020.forms import form_s1020_alteracao_infoprocjudterceiros
from emensageria.s1020.forms import form_s1020_alteracao_infoprocjudterceiros
from emensageria.s1020.forms import form_s1020_alteracao_procjudterceiro
from emensageria.s1020.forms import form_s1020_alteracao_procjudterceiro
from emensageria.s1020.forms import form_s1020_alteracao_infoemprparcial
from emensageria.s1020.forms import form_s1020_alteracao_infoemprparcial
from emensageria.s1020.forms import form_s1020_alteracao_novavalidade
from emensageria.s1020.forms import form_s1020_alteracao_novavalidade
from emensageria.s1020.forms import form_s1020_exclusao
from emensageria.s1020.forms import form_s1020_exclusao
from emensageria.s1030.forms import form_s1030_inclusao
from emensageria.s1030.forms import form_s1030_inclusao
from emensageria.s1030.forms import form_s1030_inclusao_cargopublico
from emensageria.s1030.forms import form_s1030_inclusao_cargopublico
from emensageria.s1030.forms import form_s1030_alteracao
from emensageria.s1030.forms import form_s1030_alteracao
from emensageria.s1030.forms import form_s1030_alteracao_cargopublico
from emensageria.s1030.forms import form_s1030_alteracao_cargopublico
from emensageria.s1030.forms import form_s1030_alteracao_novavalidade
from emensageria.s1030.forms import form_s1030_alteracao_novavalidade
from emensageria.s1030.forms import form_s1030_exclusao
from emensageria.s1030.forms import form_s1030_exclusao
from emensageria.s1035.forms import form_s1035_exclusao
from emensageria.s1035.forms import form_s1035_exclusao
from emensageria.s1040.forms import form_s1040_inclusao
from emensageria.s1040.forms import form_s1040_inclusao
from emensageria.s1040.forms import form_s1040_alteracao
from emensageria.s1040.forms import form_s1040_alteracao
from emensageria.s1040.forms import form_s1040_alteracao_novavalidade
from emensageria.s1040.forms import form_s1040_alteracao_novavalidade
from emensageria.s1040.forms import form_s1040_exclusao
from emensageria.s1040.forms import form_s1040_exclusao
from emensageria.s1050.forms import form_s1050_inclusao
from emensageria.s1050.forms import form_s1050_inclusao
from emensageria.s1050.forms import form_s1050_inclusao_horariointervalo
from emensageria.s1050.forms import form_s1050_inclusao_horariointervalo
from emensageria.s1050.forms import form_s1050_alteracao
from emensageria.s1050.forms import form_s1050_alteracao
from emensageria.s1050.forms import form_s1050_alteracao_horariointervalo
from emensageria.s1050.forms import form_s1050_alteracao_horariointervalo
from emensageria.s1050.forms import form_s1050_alteracao_novavalidade
from emensageria.s1050.forms import form_s1050_alteracao_novavalidade
from emensageria.s1050.forms import form_s1050_exclusao
from emensageria.s1050.forms import form_s1050_exclusao
from emensageria.s1060.forms import form_s1060_inclusao
from emensageria.s1060.forms import form_s1060_inclusao
from emensageria.s1060.forms import form_s1060_inclusao_fatorrisco
from emensageria.s1060.forms import form_s1060_inclusao_fatorrisco
from emensageria.s1060.forms import form_s1060_alteracao
from emensageria.s1060.forms import form_s1060_alteracao
from emensageria.s1060.forms import form_s1060_alteracao_fatorrisco
from emensageria.s1060.forms import form_s1060_alteracao_fatorrisco
from emensageria.s1060.forms import form_s1060_alteracao_novavalidade
from emensageria.s1060.forms import form_s1060_alteracao_novavalidade
from emensageria.s1060.forms import form_s1060_exclusao
from emensageria.s1060.forms import form_s1060_exclusao
from emensageria.s1070.forms import form_s1070_inclusao
from emensageria.s1070.forms import form_s1070_inclusao
from emensageria.s1070.forms import form_s1070_inclusao_dadosprocjud
from emensageria.s1070.forms import form_s1070_inclusao_dadosprocjud
from emensageria.s1070.forms import form_s1070_inclusao_infosusp
from emensageria.s1070.forms import form_s1070_inclusao_infosusp
from emensageria.s1070.forms import form_s1070_alteracao
from emensageria.s1070.forms import form_s1070_alteracao
from emensageria.s1070.forms import form_s1070_alteracao_dadosprocjud
from emensageria.s1070.forms import form_s1070_alteracao_dadosprocjud
from emensageria.s1070.forms import form_s1070_alteracao_infosusp
from emensageria.s1070.forms import form_s1070_alteracao_infosusp
from emensageria.s1202.forms import form_s1202_infoperapur_detoper
from emensageria.s1202.forms import form_s1202_infoperapur_detoper
from emensageria.s1070.forms import form_s1070_alteracao_novavalidade
from emensageria.s1070.forms import form_s1070_alteracao_novavalidade
from emensageria.s1070.forms import form_s1070_exclusao
from emensageria.s1070.forms import form_s1070_exclusao
from emensageria.s1080.forms import form_s1080_inclusao
from emensageria.s1080.forms import form_s1080_inclusao
from emensageria.s1080.forms import form_s1080_alteracao
from emensageria.s1080.forms import form_s1080_alteracao
from emensageria.s1080.forms import form_s1080_alteracao_novavalidade
from emensageria.s1080.forms import form_s1080_alteracao_novavalidade
from emensageria.s1080.forms import form_s1080_exclusao
from emensageria.s1080.forms import form_s1080_exclusao
from emensageria.s1200.forms import form_s1200_infomv
from emensageria.s1200.forms import form_s1200_infomv
from emensageria.s1200.forms import form_s1200_remunoutrempr
from emensageria.s1200.forms import form_s1200_remunoutrempr
from emensageria.s1200.forms import form_s1200_infocomplem
from emensageria.s1200.forms import form_s1200_infocomplem
from emensageria.s1200.forms import form_s1200_sucessaovinc
from emensageria.s1200.forms import form_s1200_sucessaovinc
from emensageria.s1200.forms import form_s1200_procjudtrab
from emensageria.s1200.forms import form_s1200_procjudtrab
from emensageria.s1200.forms import form_s1200_infointerm
from emensageria.s1200.forms import form_s1200_infointerm
from emensageria.s1200.forms import form_s1200_dmdev
from emensageria.s1200.forms import form_s1200_dmdev
from emensageria.s1200.forms import form_s1200_infoperapur
from emensageria.s1200.forms import form_s1200_infoperapur
from emensageria.s1202.forms import form_s1202_infoperapur_detplano
from emensageria.s1202.forms import form_s1202_infoperapur_detplano
from emensageria.s1210.forms import form_s1210_detpgtoant
from emensageria.s1210.forms import form_s1210_detpgtoant
from emensageria.s1299.forms import form_s1299_iderespinf
from emensageria.s1299.forms import form_s1299_iderespinf
from emensageria.s1200.forms import form_s1200_infoperapur_ideestablot
from emensageria.s1200.forms import form_s1200_infoperapur_ideestablot
from emensageria.s1200.forms import form_s1200_infoperapur_remunperapur
from emensageria.s1200.forms import form_s1200_infoperapur_remunperapur
from emensageria.s1200.forms import form_s1200_infoperapur_itensremun
from emensageria.s1200.forms import form_s1200_infoperapur_itensremun
from emensageria.s1200.forms import form_s1200_infoperapur_infosaudecolet
from emensageria.s1200.forms import form_s1200_infoperapur_infosaudecolet
from emensageria.s1200.forms import form_s1200_infoperapur_detoper
from emensageria.s1200.forms import form_s1200_infoperapur_detoper
from emensageria.s1200.forms import form_s1200_infoperapur_detplano
from emensageria.s1200.forms import form_s1200_infoperapur_detplano
from emensageria.s1200.forms import form_s1200_infoperapur_infoagnocivo
from emensageria.s1200.forms import form_s1200_infoperapur_infoagnocivo
from emensageria.s1200.forms import form_s1200_infoperapur_infotrabinterm
from emensageria.s1200.forms import form_s1200_infoperapur_infotrabinterm
from emensageria.s1200.forms import form_s1200_infoperant
from emensageria.s1200.forms import form_s1200_infoperant
from emensageria.s1200.forms import form_s1200_infoperant_ideadc
from emensageria.s1200.forms import form_s1200_infoperant_ideadc
from emensageria.s1200.forms import form_s1200_infoperant_ideperiodo
from emensageria.s1200.forms import form_s1200_infoperant_ideperiodo
from emensageria.s1210.forms import form_s1210_detpgtofer_penalim
from emensageria.s1210.forms import form_s1210_detpgtofer_penalim
from emensageria.s1210.forms import form_s1210_detpgtoant_infopgtoant
from emensageria.s1210.forms import form_s1210_detpgtoant_infopgtoant
from emensageria.s1200.forms import form_s1200_infoperant_ideestablot
from emensageria.s1200.forms import form_s1200_infoperant_ideestablot
from emensageria.s1200.forms import form_s1200_infoperant_remunperant
from emensageria.s1200.forms import form_s1200_infoperant_remunperant
from emensageria.s1200.forms import form_s1200_infoperant_itensremun
from emensageria.s1200.forms import form_s1200_infoperant_itensremun
from emensageria.s1200.forms import form_s1200_infoperant_infoagnocivo
from emensageria.s1200.forms import form_s1200_infoperant_infoagnocivo
from emensageria.s1200.forms import form_s1200_infoperant_infotrabinterm
from emensageria.s1200.forms import form_s1200_infoperant_infotrabinterm
from emensageria.s1200.forms import form_s1200_infoperant_infocomplcont
from emensageria.s1200.forms import form_s1200_infoperant_infocomplcont
from emensageria.s1202.forms import form_s1202_procjudtrab
from emensageria.s1202.forms import form_s1202_procjudtrab
from emensageria.s1202.forms import form_s1202_dmdev
from emensageria.s1202.forms import form_s1202_dmdev
from emensageria.s1202.forms import form_s1202_infoperapur
from emensageria.s1202.forms import form_s1202_infoperapur
from emensageria.s1202.forms import form_s1202_infoperapur_ideestab
from emensageria.s1202.forms import form_s1202_infoperapur_ideestab
from emensageria.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageria.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageria.s1202.forms import form_s1202_infoperapur_itensremun
from emensageria.s1202.forms import form_s1202_infoperapur_itensremun
from emensageria.s1202.forms import form_s1202_infoperapur_infosaudecolet
from emensageria.s1202.forms import form_s1202_infoperapur_infosaudecolet
from emensageria.s1202.forms import form_s1202_infoperant
from emensageria.s1202.forms import form_s1202_infoperant
from emensageria.s1202.forms import form_s1202_infoperant_ideadc
from emensageria.s1202.forms import form_s1202_infoperant_ideadc
from emensageria.s1202.forms import form_s1202_infoperant_ideperiodo
from emensageria.s1202.forms import form_s1202_infoperant_ideperiodo
from emensageria.s1202.forms import form_s1202_infoperant_ideestab
from emensageria.s1202.forms import form_s1202_infoperant_ideestab
from emensageria.s1202.forms import form_s1202_infoperant_remunperant
from emensageria.s1202.forms import form_s1202_infoperant_remunperant
from emensageria.s1202.forms import form_s1202_infoperant_itensremun
from emensageria.s1202.forms import form_s1202_infoperant_itensremun
from emensageria.s1207.forms import form_s1207_dmdev
from emensageria.s1207.forms import form_s1207_dmdev
from emensageria.s1207.forms import form_s1207_itens
from emensageria.s1207.forms import form_s1207_itens
from emensageria.s1210.forms import form_s1210_deps
from emensageria.s1210.forms import form_s1210_deps
from emensageria.s1210.forms import form_s1210_infopgto
from emensageria.s1210.forms import form_s1210_infopgto
from emensageria.s1210.forms import form_s1210_detpgtofl
from emensageria.s1210.forms import form_s1210_detpgtofl
from emensageria.s1210.forms import form_s1210_detpgtofl_retpgtotot
from emensageria.s1210.forms import form_s1210_detpgtofl_retpgtotot
from emensageria.s1210.forms import form_s1210_detpgtofl_penalim
from emensageria.s1210.forms import form_s1210_detpgtofl_penalim
from emensageria.s1210.forms import form_s1210_detpgtofl_infopgtoparc
from emensageria.s1210.forms import form_s1210_detpgtofl_infopgtoparc
from emensageria.s1210.forms import form_s1210_detpgtobenpr
from emensageria.s1210.forms import form_s1210_detpgtobenpr
from emensageria.s1210.forms import form_s1210_detpgtobenpr_retpgtotot
from emensageria.s1210.forms import form_s1210_detpgtobenpr_retpgtotot
from emensageria.s1210.forms import form_s1210_detpgtobenpr_infopgtoparc
from emensageria.s1210.forms import form_s1210_detpgtobenpr_infopgtoparc
from emensageria.s1210.forms import form_s1210_detpgtofer
from emensageria.s1210.forms import form_s1210_detpgtofer
from emensageria.s1210.forms import form_s1210_detpgtofer_detrubrfer
from emensageria.s1210.forms import form_s1210_detpgtofer_detrubrfer
from emensageria.s1210.forms import form_s1210_idepgtoext
from emensageria.s1210.forms import form_s1210_idepgtoext
from emensageria.s1250.forms import form_s1250_tpaquis
from emensageria.s1250.forms import form_s1250_tpaquis
from emensageria.s1250.forms import form_s1250_ideprodutor
from emensageria.s1250.forms import form_s1250_ideprodutor
from emensageria.s1250.forms import form_s1250_nfs
from emensageria.s1250.forms import form_s1250_nfs
from emensageria.s1250.forms import form_s1250_infoprocjud
from emensageria.s1250.forms import form_s1250_infoprocjud
from emensageria.s1260.forms import form_s1260_tpcomerc
from emensageria.s1260.forms import form_s1260_tpcomerc
from emensageria.s1260.forms import form_s1260_ideadquir
from emensageria.s1260.forms import form_s1260_ideadquir
from emensageria.s1260.forms import form_s1260_nfs
from emensageria.s1260.forms import form_s1260_nfs
from emensageria.s1260.forms import form_s1260_infoprocjud
from emensageria.s1260.forms import form_s1260_infoprocjud
from emensageria.s1270.forms import form_s1270_remunavnp
from emensageria.s1270.forms import form_s1270_remunavnp
from emensageria.s1280.forms import form_s1280_infosubstpatr
from emensageria.s1280.forms import form_s1280_infosubstpatr
from emensageria.s1280.forms import form_s1280_infosubstpatropport
from emensageria.s1280.forms import form_s1280_infosubstpatropport
from emensageria.s1280.forms import form_s1280_infoativconcom
from emensageria.s1280.forms import form_s1280_infoativconcom
from emensageria.s1295.forms import form_s1295_iderespinf
from emensageria.s1295.forms import form_s1295_iderespinf
from emensageria.s1300.forms import form_s1300_contribsind
from emensageria.s1300.forms import form_s1300_contribsind
from emensageria.s2200.forms import form_s2200_documentos
from emensageria.s2200.forms import form_s2200_documentos
from emensageria.s2200.forms import form_s2200_ctps
from emensageria.s2200.forms import form_s2200_ctps
from emensageria.s2200.forms import form_s2200_ric
from emensageria.s2200.forms import form_s2200_ric
from emensageria.s2200.forms import form_s2200_rg
from emensageria.s2200.forms import form_s2200_rg
from emensageria.s2200.forms import form_s2200_rne
from emensageria.s2200.forms import form_s2200_rne
from emensageria.s2200.forms import form_s2200_oc
from emensageria.s2200.forms import form_s2200_oc
from emensageria.s2200.forms import form_s2200_cnh
from emensageria.s2200.forms import form_s2200_cnh
from emensageria.s2200.forms import form_s2200_brasil
from emensageria.s2200.forms import form_s2200_brasil
from emensageria.s2200.forms import form_s2200_exterior
from emensageria.s2200.forms import form_s2200_exterior
from emensageria.s2200.forms import form_s2200_trabestrangeiro
from emensageria.s2200.forms import form_s2200_trabestrangeiro
from emensageria.s2200.forms import form_s2200_infodeficiencia
from emensageria.s2200.forms import form_s2200_infodeficiencia
from emensageria.s2200.forms import form_s2200_dependente
from emensageria.s2200.forms import form_s2200_dependente
from emensageria.s2200.forms import form_s2200_aposentadoria
from emensageria.s2200.forms import form_s2200_aposentadoria
from emensageria.s2200.forms import form_s2200_contato
from emensageria.s2200.forms import form_s2200_contato
from emensageria.s2200.forms import form_s2200_infoceletista
from emensageria.s2200.forms import form_s2200_infoceletista
from emensageria.s2200.forms import form_s2200_trabtemporario
from emensageria.s2200.forms import form_s2200_trabtemporario
from emensageria.s2200.forms import form_s2200_ideestabvinc
from emensageria.s2200.forms import form_s2200_ideestabvinc
from emensageria.s2200.forms import form_s2200_idetrabsubstituido
from emensageria.s2200.forms import form_s2200_idetrabsubstituido
from emensageria.s2200.forms import form_s2200_aprend
from emensageria.s2200.forms import form_s2200_aprend
from emensageria.s2200.forms import form_s2200_infoestatutario
from emensageria.s2200.forms import form_s2200_infoestatutario
from emensageria.s2200.forms import form_s2200_infodecjud
from emensageria.s2200.forms import form_s2200_infodecjud
from emensageria.s2205.forms import form_s2205_trabestrangeiro
from emensageria.s2205.forms import form_s2205_trabestrangeiro
from emensageria.s2205.forms import form_s2205_dependente
from emensageria.s2205.forms import form_s2205_dependente
from emensageria.s2200.forms import form_s2200_localtrabgeral
from emensageria.s2200.forms import form_s2200_localtrabgeral
from emensageria.s2200.forms import form_s2200_localtrabdom
from emensageria.s2200.forms import form_s2200_localtrabdom
from emensageria.s2200.forms import form_s2200_horcontratual
from emensageria.s2200.forms import form_s2200_horcontratual
from emensageria.s2200.forms import form_s2200_horario
from emensageria.s2200.forms import form_s2200_horario
from emensageria.s2200.forms import form_s2200_filiacaosindical
from emensageria.s2200.forms import form_s2200_filiacaosindical
from emensageria.s2200.forms import form_s2200_alvarajudicial
from emensageria.s2200.forms import form_s2200_alvarajudicial
from emensageria.s2200.forms import form_s2200_observacoes
from emensageria.s2200.forms import form_s2200_observacoes
from emensageria.s2200.forms import form_s2200_sucessaovinc
from emensageria.s2200.forms import form_s2200_sucessaovinc
from emensageria.s2200.forms import form_s2200_transfdom
from emensageria.s2200.forms import form_s2200_transfdom
from emensageria.s2200.forms import form_s2200_afastamento
from emensageria.s2200.forms import form_s2200_afastamento
from emensageria.s2200.forms import form_s2200_desligamento
from emensageria.s2200.forms import form_s2200_desligamento
from emensageria.s2205.forms import form_s2205_documentos
from emensageria.s2205.forms import form_s2205_documentos
from emensageria.s2205.forms import form_s2205_ctps
from emensageria.s2205.forms import form_s2205_ctps
from emensageria.s2205.forms import form_s2205_ric
from emensageria.s2205.forms import form_s2205_ric
from emensageria.s2205.forms import form_s2205_rg
from emensageria.s2205.forms import form_s2205_rg
from emensageria.s2205.forms import form_s2205_rne
from emensageria.s2205.forms import form_s2205_rne
from emensageria.s2205.forms import form_s2205_oc
from emensageria.s2205.forms import form_s2205_oc
from emensageria.s2205.forms import form_s2205_cnh
from emensageria.s2205.forms import form_s2205_cnh
from emensageria.s2205.forms import form_s2205_brasil
from emensageria.s2205.forms import form_s2205_brasil
from emensageria.s2205.forms import form_s2205_exterior
from emensageria.s2205.forms import form_s2205_exterior
from emensageria.s2205.forms import form_s2205_infodeficiencia
from emensageria.s2205.forms import form_s2205_infodeficiencia
from emensageria.s2205.forms import form_s2205_aposentadoria
from emensageria.s2205.forms import form_s2205_aposentadoria
from emensageria.s2205.forms import form_s2205_contato
from emensageria.s2205.forms import form_s2205_contato
from emensageria.s2206.forms import form_s2206_infoceletista
from emensageria.s2206.forms import form_s2206_infoceletista
from emensageria.s2206.forms import form_s2206_trabtemp
from emensageria.s2206.forms import form_s2206_trabtemp
from emensageria.s2206.forms import form_s2206_aprend
from emensageria.s2206.forms import form_s2206_aprend
from emensageria.s2206.forms import form_s2206_infoestatutario
from emensageria.s2206.forms import form_s2206_infoestatutario
from emensageria.s2206.forms import form_s2206_localtrabgeral
from emensageria.s2206.forms import form_s2206_localtrabgeral
from emensageria.s2206.forms import form_s2206_localtrabdom
from emensageria.s2206.forms import form_s2206_localtrabdom
from emensageria.s2206.forms import form_s2206_horcontratual
from emensageria.s2206.forms import form_s2206_horcontratual
from emensageria.s2206.forms import form_s2206_horario
from emensageria.s2206.forms import form_s2206_horario
from emensageria.s2206.forms import form_s2206_filiacaosindical
from emensageria.s2206.forms import form_s2206_filiacaosindical
from emensageria.s2206.forms import form_s2206_alvarajudicial
from emensageria.s2206.forms import form_s2206_alvarajudicial
from emensageria.s2206.forms import form_s2206_observacoes
from emensageria.s2206.forms import form_s2206_observacoes
from emensageria.s2206.forms import form_s2206_servpubl
from emensageria.s2206.forms import form_s2206_servpubl
from emensageria.s2210.forms import form_s2210_parteatingida
from emensageria.s2210.forms import form_s2210_parteatingida
from emensageria.s2210.forms import form_s2210_agentecausador
from emensageria.s2210.forms import form_s2210_agentecausador
from emensageria.s2210.forms import form_s2210_atestado
from emensageria.s2210.forms import form_s2210_atestado
from emensageria.s2210.forms import form_s2210_catorigem
from emensageria.s2210.forms import form_s2210_catorigem
from emensageria.s2220.forms import form_s2220_exame
from emensageria.s2220.forms import form_s2220_exame
from emensageria.s2230.forms import form_s2230_iniafastamento
from emensageria.s2230.forms import form_s2230_iniafastamento
from emensageria.s2230.forms import form_s2230_infoatestado
from emensageria.s2230.forms import form_s2230_infoatestado
from emensageria.s2230.forms import form_s2230_emitente
from emensageria.s2230.forms import form_s2230_emitente
from emensageria.s2230.forms import form_s2230_infocessao
from emensageria.s2230.forms import form_s2230_infocessao
from emensageria.s2230.forms import form_s2230_infomandsind
from emensageria.s2230.forms import form_s2230_infomandsind
from emensageria.s2230.forms import form_s2230_inforetif
from emensageria.s2230.forms import form_s2230_inforetif
from emensageria.s2230.forms import form_s2230_fimafastamento
from emensageria.s2230.forms import form_s2230_fimafastamento
from emensageria.s2240.forms import form_s2240_iniexprisco
from emensageria.s2240.forms import form_s2240_iniexprisco
from emensageria.s2240.forms import form_s2240_iniexprisco_infoamb
from emensageria.s2240.forms import form_s2240_iniexprisco_infoamb
from emensageria.s2240.forms import form_s2240_iniexprisco_fatrisco
from emensageria.s2240.forms import form_s2240_iniexprisco_fatrisco
from emensageria.s2240.forms import form_s2240_iniexprisco_epc
from emensageria.s2240.forms import form_s2240_iniexprisco_epc
from emensageria.s2240.forms import form_s2240_iniexprisco_epi
from emensageria.s2240.forms import form_s2240_iniexprisco_epi
from emensageria.s2240.forms import form_s2240_altexprisco
from emensageria.s2240.forms import form_s2240_altexprisco
from emensageria.s2240.forms import form_s2240_altexprisco_infoamb
from emensageria.s2240.forms import form_s2240_altexprisco_infoamb
from emensageria.s2240.forms import form_s2240_altexprisco_fatrisco
from emensageria.s2240.forms import form_s2240_altexprisco_fatrisco
from emensageria.s2240.forms import form_s2240_altexprisco_epc
from emensageria.s2240.forms import form_s2240_altexprisco_epc
from emensageria.s2240.forms import form_s2240_altexprisco_epi
from emensageria.s2240.forms import form_s2240_altexprisco_epi
from emensageria.s2240.forms import form_s2240_fimexprisco
from emensageria.s2240.forms import form_s2240_fimexprisco
from emensageria.s2240.forms import form_s2240_fimexprisco_infoamb
from emensageria.s2240.forms import form_s2240_fimexprisco_infoamb
from emensageria.s2240.forms import form_s2240_fimexprisco_respreg
from emensageria.s2240.forms import form_s2240_fimexprisco_respreg
from emensageria.s2241.forms import form_s2241_insalperic
from emensageria.s2241.forms import form_s2241_insalperic
from emensageria.s2241.forms import form_s2241_iniinsalperic
from emensageria.s2241.forms import form_s2241_iniinsalperic
from emensageria.s2241.forms import form_s2241_iniinsalperic_infoamb
from emensageria.s2241.forms import form_s2241_iniinsalperic_infoamb
from emensageria.s2241.forms import form_s2241_iniinsalperic_fatrisco
from emensageria.s2241.forms import form_s2241_iniinsalperic_fatrisco
from emensageria.s2241.forms import form_s2241_altinsalperic
from emensageria.s2241.forms import form_s2241_altinsalperic
from emensageria.s2241.forms import form_s2241_altinsalperic_infoamb
from emensageria.s2241.forms import form_s2241_altinsalperic_infoamb
from emensageria.s2241.forms import form_s2241_altinsalperic_fatrisco
from emensageria.s2241.forms import form_s2241_altinsalperic_fatrisco
from emensageria.s2241.forms import form_s2241_fiminsalperic
from emensageria.s2241.forms import form_s2241_fiminsalperic
from emensageria.s2241.forms import form_s2241_fiminsalperic_infoamb
from emensageria.s2241.forms import form_s2241_fiminsalperic_infoamb
from emensageria.s2241.forms import form_s2241_aposentesp
from emensageria.s2241.forms import form_s2241_aposentesp
from emensageria.s2241.forms import form_s2241_iniaposentesp
from emensageria.s2241.forms import form_s2241_iniaposentesp
from emensageria.s2241.forms import form_s2241_iniaposentesp_infoamb
from emensageria.s2241.forms import form_s2241_iniaposentesp_infoamb
from emensageria.s2241.forms import form_s2241_iniaposentesp_fatrisco
from emensageria.s2241.forms import form_s2241_iniaposentesp_fatrisco
from emensageria.s2241.forms import form_s2241_altaposentesp
from emensageria.s2241.forms import form_s2241_altaposentesp
from emensageria.s2241.forms import form_s2241_altaposentesp_infoamb
from emensageria.s2241.forms import form_s2241_altaposentesp_infoamb
from emensageria.s2241.forms import form_s2241_altaposentesp_fatrisco
from emensageria.s2241.forms import form_s2241_altaposentesp_fatrisco
from emensageria.s2241.forms import form_s2241_fimaposentesp
from emensageria.s2241.forms import form_s2241_fimaposentesp
from emensageria.s2241.forms import form_s2241_fimaposentesp_infoamb
from emensageria.s2241.forms import form_s2241_fimaposentesp_infoamb
from emensageria.s2250.forms import form_s2250_detavprevio
from emensageria.s2250.forms import form_s2250_detavprevio
from emensageria.s2250.forms import form_s2250_cancavprevio
from emensageria.s2250.forms import form_s2250_cancavprevio
from emensageria.s2260.forms import form_s2260_localtrabinterm
from emensageria.s2260.forms import form_s2260_localtrabinterm
from emensageria.s2299.forms import form_s2299_observacoes
from emensageria.s2299.forms import form_s2299_observacoes
from emensageria.s2299.forms import form_s2299_sucessaovinc
from emensageria.s2299.forms import form_s2299_sucessaovinc
from emensageria.s2299.forms import form_s2299_transftit
from emensageria.s2299.forms import form_s2299_transftit
from emensageria.s2299.forms import form_s2299_verbasresc
from emensageria.s2299.forms import form_s2299_verbasresc
from emensageria.s2299.forms import form_s2299_dmdev
from emensageria.s2299.forms import form_s2299_dmdev
from emensageria.s2299.forms import form_s2299_infoperapur
from emensageria.s2299.forms import form_s2299_infoperapur
from emensageria.s2299.forms import form_s2299_infoperapur_ideestablot
from emensageria.s2299.forms import form_s2299_infoperapur_ideestablot
from emensageria.s2299.forms import form_s2299_infoperapur_detverbas
from emensageria.s2299.forms import form_s2299_infoperapur_detverbas
from emensageria.s2299.forms import form_s2299_infoperant_infosimples
from emensageria.s2299.forms import form_s2299_infoperant_infosimples
from emensageria.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageria.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageria.s2299.forms import form_s2299_infoperapur_detoper
from emensageria.s2299.forms import form_s2299_infoperapur_detoper
from emensageria.s2299.forms import form_s2299_infoperapur_detplano
from emensageria.s2299.forms import form_s2299_infoperapur_detplano
from emensageria.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageria.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageria.s2299.forms import form_s2299_infoperapur_infosimples
from emensageria.s2299.forms import form_s2299_infoperapur_infosimples
from emensageria.s2299.forms import form_s2299_infoperant
from emensageria.s2299.forms import form_s2299_infoperant
from emensageria.s2299.forms import form_s2299_infoperant_ideadc
from emensageria.s2299.forms import form_s2299_infoperant_ideadc
from emensageria.s2299.forms import form_s2299_infoperant_ideperiodo
from emensageria.s2299.forms import form_s2299_infoperant_ideperiodo
from emensageria.s2299.forms import form_s2299_infoperant_ideestablot
from emensageria.s2299.forms import form_s2299_infoperant_ideestablot
from emensageria.s2299.forms import form_s2299_infoperant_detverbas
from emensageria.s2299.forms import form_s2299_infoperant_detverbas
from emensageria.s2299.forms import form_s2299_infoperant_infoagnocivo
from emensageria.s2299.forms import form_s2299_infoperant_infoagnocivo
from emensageria.s2299.forms import form_s2299_infotrabinterm
from emensageria.s2299.forms import form_s2299_infotrabinterm
from emensageria.s2299.forms import form_s2299_infotrabinterm_procjudtrab
from emensageria.s2299.forms import form_s2299_infotrabinterm_procjudtrab
from emensageria.s2299.forms import form_s2299_infotrabinterm_infomv
from emensageria.s2299.forms import form_s2299_infotrabinterm_infomv
from emensageria.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageria.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageria.s2299.forms import form_s2299_infotrabinterm_proccs
from emensageria.s2299.forms import form_s2299_infotrabinterm_proccs
from emensageria.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageria.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageria.s2299.forms import form_s2299_infotrabinterm_consigfgts
from emensageria.s2299.forms import form_s2299_infotrabinterm_consigfgts
from emensageria.s2300.forms import form_s2300_documentos
from emensageria.s2300.forms import form_s2300_documentos
from emensageria.s2300.forms import form_s2300_ctps
from emensageria.s2300.forms import form_s2300_ctps
from emensageria.s2300.forms import form_s2300_ric
from emensageria.s2300.forms import form_s2300_ric
from emensageria.s2300.forms import form_s2300_rg
from emensageria.s2300.forms import form_s2300_rg
from emensageria.s2300.forms import form_s2300_rne
from emensageria.s2300.forms import form_s2300_rne
from emensageria.s2300.forms import form_s2300_oc
from emensageria.s2300.forms import form_s2300_oc
from emensageria.s2300.forms import form_s2300_cnh
from emensageria.s2300.forms import form_s2300_cnh
from emensageria.s2300.forms import form_s2300_brasil
from emensageria.s2300.forms import form_s2300_brasil
from emensageria.s2300.forms import form_s2300_exterior
from emensageria.s2300.forms import form_s2300_exterior
from emensageria.s2300.forms import form_s2300_trabestrangeiro
from emensageria.s2300.forms import form_s2300_trabestrangeiro
from emensageria.s2300.forms import form_s2300_infodeficiencia
from emensageria.s2300.forms import form_s2300_infodeficiencia
from emensageria.s2300.forms import form_s2300_dependente
from emensageria.s2300.forms import form_s2300_dependente
from emensageria.s2300.forms import form_s2300_contato
from emensageria.s2300.forms import form_s2300_contato
from emensageria.s2300.forms import form_s2300_infocomplementares
from emensageria.s2300.forms import form_s2300_infocomplementares
from emensageria.s2300.forms import form_s2300_cargofuncao
from emensageria.s2300.forms import form_s2300_cargofuncao
from emensageria.s2300.forms import form_s2300_remuneracao
from emensageria.s2300.forms import form_s2300_remuneracao
from emensageria.s2300.forms import form_s2300_fgts
from emensageria.s2300.forms import form_s2300_fgts
from emensageria.s2300.forms import form_s2300_infodirigentesindical
from emensageria.s2300.forms import form_s2300_infodirigentesindical
from emensageria.s2300.forms import form_s2300_infotrabcedido
from emensageria.s2300.forms import form_s2300_infotrabcedido
from emensageria.s2300.forms import form_s2300_infoestagiario
from emensageria.s2300.forms import form_s2300_infoestagiario
from emensageria.s2300.forms import form_s2300_ageintegracao
from emensageria.s2300.forms import form_s2300_ageintegracao
from emensageria.s2300.forms import form_s2300_supervisorestagio
from emensageria.s2300.forms import form_s2300_supervisorestagio
from emensageria.s2300.forms import form_s2300_afastamento
from emensageria.s2300.forms import form_s2300_afastamento
from emensageria.s2300.forms import form_s2300_termino
from emensageria.s2300.forms import form_s2300_termino
from emensageria.s2306.forms import form_s2306_infocomplementares
from emensageria.s2306.forms import form_s2306_infocomplementares
from emensageria.s2306.forms import form_s2306_cargofuncao
from emensageria.s2306.forms import form_s2306_cargofuncao
from emensageria.s2306.forms import form_s2306_remuneracao
from emensageria.s2306.forms import form_s2306_remuneracao
from emensageria.s2306.forms import form_s2306_infoestagiario
from emensageria.s2306.forms import form_s2306_infoestagiario
from emensageria.s2306.forms import form_s2306_ageintegracao
from emensageria.s2306.forms import form_s2306_ageintegracao
from emensageria.s2306.forms import form_s2306_supervisorestagio
from emensageria.s2306.forms import form_s2306_supervisorestagio
from emensageria.s2399.forms import form_s2399_verbasresc
from emensageria.s2399.forms import form_s2399_verbasresc
from emensageria.s2399.forms import form_s2399_dmdev
from emensageria.s2399.forms import form_s2399_dmdev
from emensageria.s2399.forms import form_s2399_ideestablot
from emensageria.s2399.forms import form_s2399_ideestablot
from emensageria.s2399.forms import form_s2399_detverbas
from emensageria.s2399.forms import form_s2399_detverbas
from emensageria.s2400.forms import form_s2400_fimbeneficio
from emensageria.s2400.forms import form_s2400_fimbeneficio
from emensageria.s2399.forms import form_s2399_infosaudecolet
from emensageria.s2399.forms import form_s2399_infosaudecolet
from emensageria.s2399.forms import form_s2399_detoper
from emensageria.s2399.forms import form_s2399_detoper
from emensageria.s2399.forms import form_s2399_detplano
from emensageria.s2399.forms import form_s2399_detplano
from emensageria.s2399.forms import form_s2399_infoagnocivo
from emensageria.s2399.forms import form_s2399_infoagnocivo
from emensageria.s2399.forms import form_s2399_infosimples
from emensageria.s2399.forms import form_s2399_infosimples
from emensageria.s2399.forms import form_s2399_procjudtrab
from emensageria.s2399.forms import form_s2399_procjudtrab
from emensageria.s2399.forms import form_s2399_infomv
from emensageria.s2399.forms import form_s2399_infomv
from emensageria.s2399.forms import form_s2399_remunoutrempr
from emensageria.s2399.forms import form_s2399_remunoutrempr
from emensageria.s2399.forms import form_s2399_quarentena
from emensageria.s2399.forms import form_s2399_quarentena
from emensageria.s2400.forms import form_s2400_brasil
from emensageria.s2400.forms import form_s2400_brasil
from emensageria.s2400.forms import form_s2400_exterior
from emensageria.s2400.forms import form_s2400_exterior
from emensageria.s2400.forms import form_s2400_inibeneficio
from emensageria.s2400.forms import form_s2400_inibeneficio
from emensageria.s2400.forms import form_s2400_inibeneficio_infopenmorte
from emensageria.s2400.forms import form_s2400_inibeneficio_infopenmorte
from emensageria.s2400.forms import form_s2400_altbeneficio
from emensageria.s2400.forms import form_s2400_altbeneficio
from emensageria.s2400.forms import form_s2400_altbeneficio_infopenmorte
from emensageria.s2400.forms import form_s2400_altbeneficio_infopenmorte
from emensageria.s5011.forms import form_s5011_infoestab
from emensageria.s5011.forms import form_s5011_infoestab
from emensageria.s3000.forms import form_s3000_idetrabalhador
from emensageria.s3000.forms import form_s3000_idetrabalhador
from emensageria.s3000.forms import form_s3000_idefolhapagto
from emensageria.s3000.forms import form_s3000_idefolhapagto
from emensageria.s5001.forms import form_s5001_procjudtrab
from emensageria.s5001.forms import form_s5001_procjudtrab
from emensageria.s5001.forms import form_s5001_infocpcalc
from emensageria.s5001.forms import form_s5001_infocpcalc
from emensageria.s5001.forms import form_s5001_ideestablot
from emensageria.s5001.forms import form_s5001_ideestablot
from emensageria.s5001.forms import form_s5001_infocategincid
from emensageria.s5001.forms import form_s5001_infocategincid
from emensageria.s5001.forms import form_s5001_infobasecs
from emensageria.s5001.forms import form_s5001_infobasecs
from emensageria.s5001.forms import form_s5001_calcterc
from emensageria.s5001.forms import form_s5001_calcterc
from emensageria.s5002.forms import form_s5002_infodep
from emensageria.s5002.forms import form_s5002_infodep
from emensageria.s5002.forms import form_s5002_infoirrf
from emensageria.s5002.forms import form_s5002_infoirrf
from emensageria.s5002.forms import form_s5002_basesirrf
from emensageria.s5002.forms import form_s5002_basesirrf
from emensageria.s5002.forms import form_s5002_irrf
from emensageria.s5002.forms import form_s5002_irrf
from emensageria.s5002.forms import form_s5002_idepgtoext
from emensageria.s5002.forms import form_s5002_idepgtoext
from emensageria.s5011.forms import form_s5011_infocpseg
from emensageria.s5011.forms import form_s5011_infocpseg
from emensageria.s5011.forms import form_s5011_infopj
from emensageria.s5011.forms import form_s5011_infopj
from emensageria.s5011.forms import form_s5011_infoatconc
from emensageria.s5011.forms import form_s5011_infoatconc
from emensageria.s5011.forms import form_s5011_ideestab
from emensageria.s5011.forms import form_s5011_ideestab
from emensageria.s5011.forms import form_s5011_infocomplobra
from emensageria.s5011.forms import form_s5011_infocomplobra
from emensageria.s5011.forms import form_s5011_idelotacao
from emensageria.s5011.forms import form_s5011_idelotacao
from emensageria.s5011.forms import form_s5011_infotercsusp
from emensageria.s5011.forms import form_s5011_infotercsusp
from emensageria.s5011.forms import form_s5011_infoemprparcial
from emensageria.s5011.forms import form_s5011_infoemprparcial
from emensageria.s5011.forms import form_s5011_dadosopport
from emensageria.s5011.forms import form_s5011_dadosopport
from emensageria.s5011.forms import form_s5011_basesremun
from emensageria.s5011.forms import form_s5011_basesremun
from emensageria.s5011.forms import form_s5011_basesavnport
from emensageria.s5011.forms import form_s5011_basesavnport
from emensageria.s5011.forms import form_s5011_infosubstpatropport
from emensageria.s5011.forms import form_s5011_infosubstpatropport
from emensageria.s5011.forms import form_s5011_basesaquis
from emensageria.s5011.forms import form_s5011_basesaquis
from emensageria.s5011.forms import form_s5011_basescomerc
from emensageria.s5011.forms import form_s5011_basescomerc
from emensageria.s5011.forms import form_s5011_infocrestab
from emensageria.s5011.forms import form_s5011_infocrestab
from emensageria.s5011.forms import form_s5011_infocrcontrib
from emensageria.s5011.forms import form_s5011_infocrcontrib
from emensageria.s5012.forms import form_s5012_infocrcontrib
from emensageria.s5012.forms import form_s5012_infocrcontrib

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        usuarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
    if request.method == 'POST':
        Usuarios.objects.using( db_slug ).filter(id = usuarios_id).update(excluido = True)
        #usuarios_apagar_custom
        #usuarios_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'usuarios_salvar':
            return redirect('usuarios', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
        
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
        
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'usuarios_apagar.html', context)

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #usuarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_config_perfis': 1,
            'show_email': 1,
            'show_nome': 1,
            'show_senha': 0,
            'show_usuario': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'config_perfis': 'config_perfis',
                'email__icontains': 'email__icontains',
                'nome__icontains': 'nome__icontains',
                'usuario__icontains': 'usuario__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'config_perfis': 'config_perfis',
                'email__icontains': 'email__icontains',
                'nome__icontains': 'nome__icontains',
                'usuario__icontains': 'usuario__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        usuarios_lista = Usuarios.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(usuarios_lista) > 100:
            filtrar = True
            usuarios_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
   
        config_perfis_lista = ConfigPerfis.objects.using( db_slug ).filter(excluido = False).all()
        #usuarios_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'usuarios'
        context = {
            'usuarios_lista': usuarios_lista,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
       
            'config_perfis_lista': config_perfis_lista,
        }
        return render(request, 'usuarios_listar.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        usuarios_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if usuarios_id:
        usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if usuarios_id:
            usuarios_form = form_usuarios(request.POST or None, instance = usuarios, slug = db_slug)
        else:
            usuarios_form = form_usuarios(request.POST or None, slug = db_slug, initial={'senha': 'asdkl1231'})
        if request.method == 'POST':
            if usuarios_form.is_valid():
                dados = usuarios_form.cleaned_data
                if usuarios_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #usuarios_campos_multiple_passo1
                    Usuarios.objects.using(db_slug).filter(id=usuarios_id).update(**dados)
                    obj = Usuarios.objects.using(db_slug).get(id=usuarios_id)
                    #usuarios_editar_custom
                    #usuarios_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['senha'] = 'asdkl1231'

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #usuarios_cadastrar_campos_multiple_passo1
                    obj = Usuarios(**dados)
                    obj.save(using = db_slug)
                    #usuarios_cadastrar_custom
                    #usuarios_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('usuarios_apagar', 'usuarios_salvar', 'usuarios'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if usuarios_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('usuarios_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        usuarios_form = disabled_form_fields(usuarios_form, permissao.permite_editar)
        #usuarios_campos_multiple_passo3

        for field in usuarios_form.fields.keys():
            usuarios_form.fields[field].widget.attrs['ng-model'] = 'usuarios_'+field
        if int(dict_hash['print']):
            usuarios_form = disabled_form_for_print(usuarios_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if usuarios_id:
            usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
            pass
        else:
            usuarios = None
        #usuarios_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'usuarios' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'usuarios_salvar'
        context = {
            'usuarios': usuarios,
            'usuarios_form': usuarios_form,
            'mensagem': mensagem,
            'usuarios_id': int(usuarios_id),
            'usuario': usuario,
            
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #usuarios_salvar_custom_variaveis_context#
        }
        return render(request, 'usuarios_salvar.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

