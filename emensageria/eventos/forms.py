# coding: utf-8
from django import forms
from emensageria.eventos.models import * 
from emensageria.controle_de_acesso.models import Usuarios 
from emensageria.mensageiro.models import TransmissorLote 


__author__ = 'marcelovasconcellos'

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

#custom_forms#



class form_s5012_evtirrf_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5012_evtirrf_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s5012evtIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s5012evtIrrfOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s5011_evtcs_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5011_evtcs_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s5011evtCS.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s5011evtCSOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s5002_evtirrfbenef_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_evtirrfbenef_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s5002evtIrrfBenef.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s5002evtIrrfBenefOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s5001_evtbasestrab_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_evtbasestrab_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s5001evtBasesTrab.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s5001evtBasesTrabOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s3000_evtexclusao_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s3000_evtexclusao_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s3000evtExclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s3000evtExclusaoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2400_evtcdbenprrp_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_evtcdbenprrp_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2400evtCdBenPrRP.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2400evtCdBenPrRPOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2399_evttsvtermino_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_evttsvtermino_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2399evtTSVTermino.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2399evtTSVTerminoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2306_evttsvaltcontr_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_evttsvaltcontr_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2306evtTSVAltContr.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2306evtTSVAltContrOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2300_evttsvinicio_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_evttsvinicio_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2300evtTSVInicio.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2300evtTSVInicioOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2299_evtdeslig_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_evtdeslig_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2299evtDesligOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2298_evtreintegr_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2298_evtreintegr_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2298evtReintegr.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2298evtReintegrOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2260_evtconvinterm_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2260_evtconvinterm_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2260evtConvInterm.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2260evtConvIntermOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2250_evtavprevio_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2250_evtavprevio_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2250evtAvPrevio.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2250evtAvPrevioOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2241_evtinsapo_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_evtinsapo_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2241evtInsApo.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2241evtInsApoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2240_evtexprisco_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_evtexprisco_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2240evtExpRiscoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2230_evtafasttemp_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_evtafasttemp_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2230evtAfastTemp.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2230evtAfastTempOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2220_evtmonit_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2220_evtmonit_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2220evtMonit.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2220evtMonitOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2210_evtcat_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_evtcat_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2210evtCAT.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2210evtCATOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2206_evtaltcontratual_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_evtaltcontratual_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2206evtAltContratual.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2206evtAltContratualOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2205_evtaltcadastral_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_evtaltcadastral_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2205evtAltCadastral.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2205evtAltCadastralOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2200_evtadmissao_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_evtadmissao_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2200evtAdmissao.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2200evtAdmissaoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s2190_evtadmprelim_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2190_evtadmprelim_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s2190evtAdmPrelim.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s2190evtAdmPrelimOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1300_evtcontrsindpatr_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1300_evtcontrsindpatr_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1300evtContrSindPatr.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1300evtContrSindPatrOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1299_evtfechaevper_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1299_evtfechaevper_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1299evtFechaEvPer.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1299evtFechaEvPerOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1298_evtreabreevper_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1298_evtreabreevper_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1298evtReabreEvPer.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1298evtReabreEvPerOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1295_evttotconting_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1295_evttotconting_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1295evtTotConting.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1295evtTotContingOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1280_evtinfocomplper_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_evtinfocomplper_ocorrencias,self ).__init__(*args,**kwargs)
        self.fields['evento'].queryset = s1280evtInfoComplPer.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1280evtInfoComplPerOcorrencias
        exclude = [ 
 
        ]


class form_s1270_evtcontratavnp_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1270_evtcontratavnp_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1270evtContratAvNP.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1270evtContratAvNPOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1260_evtcomprod_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_evtcomprod_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1260evtComProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1260evtComProdOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1250_evtaqprod_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_evtaqprod_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1250evtAqProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1250evtAqProdOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1210_evtpgtos_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_evtpgtos_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1210evtPgtos.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1210evtPgtosOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1207_evtbenprrp_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1207_evtbenprrp_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1207evtBenPrRP.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1207evtBenPrRPOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1202_evtrmnrpps_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1202_evtrmnrpps_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1202evtRmnRPPS.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1202evtRmnRPPSOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1200_evtremun_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_evtremun_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1200evtRemun.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1200evtRemunOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1080_evttaboperport_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_evttaboperport_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1080evtTabOperPort.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1080evtTabOperPortOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1070_evttabprocesso_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_evttabprocesso_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1070evtTabProcesso.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1070evtTabProcessoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1060_evttabambiente_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_evttabambiente_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1060evtTabAmbiente.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1060evtTabAmbienteOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1050_evttabhortur_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_evttabhortur_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1050evtTabHorTur.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1050evtTabHorTurOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1040_evttabfuncao_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_evttabfuncao_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1040evtTabFuncao.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1040evtTabFuncaoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1035_evttabcarreira_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_evttabcarreira_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1035evtTabCarreira.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1035evtTabCarreiraOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1030_evttabcargo_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_evttabcargo_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1030evtTabCargo.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1030evtTabCargoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1020_evttablotacao_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_evttablotacao_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1020evtTabLotacao.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1020evtTabLotacaoOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1010_evttabrubrica_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_evttabrubrica_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1010evtTabRubrica.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1010evtTabRubricaOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1005_evttabestab_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_evttabestab_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1005evtTabEstab.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1005evtTabEstabOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s1000_evtinfoempregador_ocorrencias(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_evtinfoempregador_ocorrencias,self ).__init__(*args,**kwargs)
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['evento'].queryset = s1000evtInfoEmpregador.objects.using( slug ).filter(excluido=False).all()
        self.fields['evento'].widget.attrs['required'] = True
        self.fields['evento'].widget.attrs['readonly'] = True

    class Meta:
        model = s1000evtInfoEmpregadorOcorrencias
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
 
        ]


class form_s5012_evtirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5012_evtirrf,self ).__init__(*args,**kwargs)
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s5012evtIrrf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s5011_evtcs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5011_evtcs,self ).__init__(*args,**kwargs)
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s5011evtCS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s5002_evtirrfbenef(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_evtirrfbenef,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s5002evtIrrfBenef
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s5001_evtbasestrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_evtbasestrab,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s5001evtBasesTrab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s3000_evtexclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s3000_evtexclusao,self ).__init__(*args,**kwargs)
        
        self.fields['nrrecevt'].widget.attrs['required'] = True
        
        self.fields['tpevento'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s3000evtExclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2400_evtcdbenprrp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_evtcdbenprrp,self ).__init__(*args,**kwargs)
        
        self.fields['tpplanrp'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2400evtCdBenPrRP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2399_evttsvtermino(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_evttsvtermino,self ).__init__(*args,**kwargs)
        
        self.fields['dtterm'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2399evtTSVTermino
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2306_evttsvaltcontr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_evttsvaltcontr,self ).__init__(*args,**kwargs)
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2306evtTSVAltContr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2300_evttsvinicio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_evttsvinicio,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cadini'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2300evtTSVInicio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2299_evtdeslig(forms.ModelForm):
    vralim = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    percaliment = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_evtdeslig,self ).__init__(*args,**kwargs)
        
        self.fields['indcumprparc'].widget.attrs['required'] = True
        
        self.fields['pensalim'].widget.attrs['required'] = True
        
        self.fields['indpagtoapi'].widget.attrs['required'] = True
        
        self.fields['dtdeslig'].widget.attrs['required'] = True
        
        self.fields['mtvdeslig'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2299evtDeslig
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2298_evtreintegr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2298_evtreintegr,self ).__init__(*args,**kwargs)
        
        self.fields['indpagtojuizo'].widget.attrs['required'] = True
        
        self.fields['dtefeito'].widget.attrs['required'] = True
        
        self.fields['dtefetretorno'].widget.attrs['required'] = True
        
        self.fields['tpreint'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2298evtReintegr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2260_evtconvinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2260_evtconvinterm,self ).__init__(*args,**kwargs)
        
        self.fields['indlocal'].widget.attrs['required'] = True
        
        self.fields['dtprevpgto'].widget.attrs['required'] = True
        
        self.fields['dtfim'].widget.attrs['required'] = True
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['codconv'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2260evtConvInterm
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2250_evtavprevio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2250_evtavprevio,self ).__init__(*args,**kwargs)
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2250evtAvPrevio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2241_evtinsapo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_evtinsapo,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2241evtInsApo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2240_evtexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_evtexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2240evtExpRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2230_evtafasttemp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_evtafasttemp,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2230evtAfastTemp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2220_evtmonit(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2220_evtmonit,self ).__init__(*args,**kwargs)
        
        self.fields['nmmed'].widget.attrs['required'] = True
        
        self.fields['frmctt'].widget.attrs['required'] = True
        
        self.fields['resaso'].widget.attrs['required'] = True
        
        self.fields['tpaso'].widget.attrs['required'] = True
        
        self.fields['dtaso'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2220evtMonit
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2210_evtcat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_evtcat,self ).__init__(*args,**kwargs)
        
        self.fields['tplocal'].widget.attrs['required'] = True
        
        self.fields['iniciatcat'].widget.attrs['required'] = True
        
        self.fields['indcomunpolicia'].widget.attrs['required'] = True
        
        self.fields['indcatobito'].widget.attrs['required'] = True
        
        self.fields['tpcat'].widget.attrs['required'] = True
        
        self.fields['hrstrabantesacid'].widget.attrs['required'] = True
        
        self.fields['hracid'].widget.attrs['required'] = True
        
        self.fields['tpacid'].widget.attrs['required'] = True
        
        self.fields['dtacid'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['tpregistrador'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2210evtCAT
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2206_evtaltcontratual(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_evtaltcontratual,self ).__init__(*args,**kwargs)
        
        self.fields['tpcontr'].widget.attrs['required'] = True
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['tpregprev'].widget.attrs['required'] = True
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2206evtAltContratual
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2205_evtaltcadastral(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_evtaltcadastral,self ).__init__(*args,**kwargs)
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2205evtAltCadastral
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2200_evtadmissao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_evtadmissao,self ).__init__(*args,**kwargs)
        
        self.fields['tpcontr'].widget.attrs['required'] = True
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cadini'].widget.attrs['required'] = True
        
        self.fields['tpregprev'].widget.attrs['required'] = True
        
        self.fields['tpregtrab'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2200evtAdmissao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s2190_evtadmprelim(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2190_evtadmprelim,self ).__init__(*args,**kwargs)
        
        self.fields['dtadm'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s2190evtAdmPrelim
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1300_evtcontrsindpatr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1300_evtcontrsindpatr,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1300evtContrSindPatr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1299_evtfechaevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1299_evtfechaevper,self ).__init__(*args,**kwargs)
        
        self.fields['evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['evtcontratavnp'].widget.attrs['required'] = True
        
        self.fields['evtcomprod'].widget.attrs['required'] = True
        
        self.fields['evtaqprod'].widget.attrs['required'] = True
        
        self.fields['evtpgtos'].widget.attrs['required'] = True
        
        self.fields['evtremun'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1299evtFechaEvPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1298_evtreabreevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1298_evtreabreevper,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1298evtReabreEvPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1295_evttotconting(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1295_evttotconting,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1295evtTotConting
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1280_evtinfocomplper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_evtinfocomplper,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['localizacao'].widget.attrs['readonly'] = True
        
        self.fields['codigo'].widget.attrs['required'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1280evtInfoComplPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'descricao',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1270_evtcontratavnp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1270_evtcontratavnp,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1270evtContratAvNP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1260_evtcomprod(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_evtcomprod,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscestabrural'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1260evtComProd
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1250_evtaqprod(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_evtaqprod,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscadq'].widget.attrs['required'] = True
        
        self.fields['tpinscadq'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1250evtAqProd
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1210_evtpgtos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_evtpgtos,self ).__init__(*args,**kwargs)
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1210evtPgtos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1207_evtbenprrp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1207_evtbenprrp,self ).__init__(*args,**kwargs)
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1207evtBenPrRP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1202_evtrmnrpps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1202_evtrmnrpps,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1202evtRmnRPPS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1200_evtremun(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_evtremun,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1200evtRemun
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1080_evttaboperport(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_evttaboperport,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1080evtTabOperPort
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1070_evttabprocesso(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_evttabprocesso,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1070evtTabProcesso
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1060_evttabambiente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_evttabambiente,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1060evtTabAmbiente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1050_evttabhortur(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_evttabhortur,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1050evtTabHorTur
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1040_evttabfuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_evttabfuncao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1040evtTabFuncao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1035_evttabcarreira(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_evttabcarreira,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1035evtTabCarreira
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1030_evttabcargo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_evttabcargo,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1030evtTabCargo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1020_evttablotacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_evttablotacao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1020evtTabLotacao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1010_evttabrubrica(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_evttabrubrica,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1010evtTabRubrica
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1005_evttabestab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_evttabestab,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1005evtTabEstab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
 
        ]


class form_s1000_evtinfoempregador(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_evtinfoempregador,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote'].queryset = TransmissorLote.objects.using( slug ).filter(excluido=False).all()

    class Meta:
        model = s1000evtInfoEmpregador
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
 
        ]

