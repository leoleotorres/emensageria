# coding: utf-8
from django import forms
from emensageria.s1060.models import * 
from emensageria.controle_de_acesso.models import Usuarios 
from emensageria.eventos.models import s1060evtTabAmbiente 


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



class form_s1060_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1060_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1060alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_alteracao_fatorrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_alteracao_fatorrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s1060_alteracao'].queryset = s1060alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1060_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1060alteracaofatorRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['localamb'].widget.attrs['required'] = True
        
        self.fields['dscamb'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_inclusao_fatorrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_inclusao_fatorrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s1060_inclusao'].queryset = s1060inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1060_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1060inclusaofatorRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1060_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['localamb'].widget.attrs['required'] = True
        
        self.fields['dscamb'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        
        self.fields['s1060_evttabambiente'].widget.attrs['required'] = True

    class Meta:
        model = s1060inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

