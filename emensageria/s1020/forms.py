# coding: utf-8
from django import forms
from emensageria.s1020.models import * 
from emensageria.controle_de_acesso.models import Usuarios 
from emensageria.eventos.models import s1020evtTabLotacao 


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



class form_s1020_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_infoemprparcial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_infoemprparcial,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscprop'].widget.attrs['required'] = True
        
        self.fields['tpinscprop'].widget.attrs['required'] = True
        
        self.fields['nrinsccontrat'].widget.attrs['required'] = True
        
        self.fields['tpinsccontrat'].widget.attrs['required'] = True
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoinfoEmprParcial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_procjudterceiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_procjudterceiro,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['codterc'].widget.attrs['required'] = True
        self.fields['s1020_alteracao_infoprocjudterceiros'].queryset = s1020alteracaoinfoProcJudTerceiros.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1020_alteracao_infoprocjudterceiros'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoprocJudTerceiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_infoprocjudterceiros(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_infoprocjudterceiros,self ).__init__(*args,**kwargs)
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoinfoProcJudTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['codtercs'].widget.attrs['required'] = True
        
        self.fields['fpas'].widget.attrs['required'] = True
        
        self.fields['tplotacao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_infoemprparcial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_infoemprparcial,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscprop'].widget.attrs['required'] = True
        
        self.fields['tpinscprop'].widget.attrs['required'] = True
        
        self.fields['nrinsccontrat'].widget.attrs['required'] = True
        
        self.fields['tpinsccontrat'].widget.attrs['required'] = True
        
        self.fields['s1020_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoinfoEmprParcial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_procjudterceiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_procjudterceiro,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['codterc'].widget.attrs['required'] = True
        self.fields['s1020_inclusao_infoprocjudterceiros'].queryset = s1020inclusaoinfoProcJudTerceiros.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1020_inclusao_infoprocjudterceiros'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoprocJudTerceiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_infoprocjudterceiros(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_infoprocjudterceiros,self ).__init__(*args,**kwargs)
        
        self.fields['s1020_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoinfoProcJudTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['codtercs'].widget.attrs['required'] = True
        
        self.fields['fpas'].widget.attrs['required'] = True
        
        self.fields['tplotacao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

