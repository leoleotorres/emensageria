# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransmissorLote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empregador_tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('empregador_nrinsc', models.CharField(max_length=15)),
                ('transmissor_tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('transmissor_nrinsc', models.CharField(max_length=15)),
                ('grupo', models.IntegerField(choices=[(1, '1 - Eventos de Tabelas'), (2, '2 - Eventos N\xe3o Peri\xf3dicos'), (3, '3 - Eventos Peri\xf3dicos')])),
                ('resposta_codigo', models.IntegerField(default=0, choices=[(0, 'Cadastrado (Aguardando envio)'), (101, '101 - Lote Aguardando Processamento'), (201, '201 - Lote Processado com Sucesso'), (202, '202 - Lote Processado com Advert\xeancias'), (301, '301 - Erro Servidor eSocial'), (401, '401 - Lote Incorreto - Erro preenchimento'), (402, '402 - Lote Incorreto - schema Inv\xe1lido'), (403, '403 - Lote Incorreto - Vers\xe3o do Schema n\xe3o permitida'), (404, '404 - Lote Incorreto - Erro Certificado'), (405, '405 - Lote Incorreto - Lote nulo ou vazio'), (501, '501 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Preenchimento'), (502, '502 - Solicita\xe7\xe3o de Consulta Incorreta - Schema Inv\xe1lido.'), (503, '503 - Solicita\xe7\xe3o de Consulta Incorreta - Vers\xe3o do Schema N\xe3o Permitida.'), (504, '504 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Certificado.'), (505, '505 - Solicita\xe7\xe3o de Consulta Incorreta - Consulta nula ou vazia.')])),
                ('resposta_descricao', models.TextField(null=True, blank=True)),
                ('recepcao_data_hora', models.DateTimeField(max_length=50, null=True, blank=True)),
                ('recepcao_versao_aplicativo', models.CharField(max_length=50, null=True, blank=True)),
                ('protocolo', models.CharField(max_length=50, null=True, blank=True)),
                ('processamento_versao_aplicativo', models.CharField(max_length=50, null=True, blank=True)),
                ('tempo_estimado_conclusao', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='transmissorlote_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='transmissorlote_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'db_table': 'transmissor_lote',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransmissorLoteOcorrencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resposta_codigo', models.IntegerField(choices=[(1, '1 - Erro'), (2, '2 - Advert\xeancia')])),
                ('descricao', models.TextField()),
                ('tipo', models.IntegerField(choices=[(1, '1 - Erro'), (2, '2 - Advert\xeancia')])),
                ('localizacao', models.CharField(max_length=50)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='transmissorloteocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='transmissorloteocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('transmissor_lote', models.ForeignKey(related_name='transmissorloteocorrencias_transmissor_lote', to='mensageiro.TransmissorLote')),
            ],
            options={
                'db_table': 'transmissor_lote_ocorrencias',
                'managed': True,
            },
        ),
    ]
