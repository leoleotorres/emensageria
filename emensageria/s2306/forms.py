# coding: utf-8
from django import forms
from emensageria.s2306.models import * 
from emensageria.controle_de_acesso.models import Usuarios 
from emensageria.eventos.models import s2306evtTSVAltContr 


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



class form_s2306_supervisorestagio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_supervisorestagio,self ).__init__(*args,**kwargs)
        
        self.fields['nmsuperv'].widget.attrs['required'] = True
        
        self.fields['cpfsupervisor'].widget.attrs['required'] = True
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2306supervisorEstagio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_ageintegracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_ageintegracao,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjagntinteg'].widget.attrs['required'] = True
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2306ageIntegracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_infoestagiario(forms.ModelForm):
    vlrbolsa = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_infoestagiario,self ).__init__(*args,**kwargs)
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['dtprevterm'].widget.attrs['required'] = True
        
        self.fields['nivestagio'].widget.attrs['required'] = True
        
        self.fields['natestagio'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306infoEstagiario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_remuneracao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_remuneracao,self ).__init__(*args,**kwargs)
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306remuneracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_cargofuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_cargofuncao,self ).__init__(*args,**kwargs)
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306cargoFuncao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_infocomplementares(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_infocomplementares,self ).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True

    class Meta:
        model = s2306infoComplementares
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

