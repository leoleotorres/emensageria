#coding:utf-8
import psycopg2
import datetime
import os

"""

    eMensageria - Sistema de Gerenciamento de Eventos do eSocial <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

REQUEST_ENVIA_LOTE = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0"><soapenv:Header/><soapenv:Body><v1:EnviarLoteEventos><!--Optional:--><v1:loteEventos><eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/v1_1_1"><envioLoteEventos grupo="1"><ideEmpregador><tpInsc>%(empregador_tpinsc)s</tpInsc><nrInsc>%(empregador_nrinsc)s</nrInsc></ideEmpregador><ideTransmissor><tpInsc>%(transmissor_tpinsc)s</tpInsc><nrInsc>%(transmissor_nrinsc)s</nrInsc></ideTransmissor><eventos><!--You may enter ANY elements at this point--></eventos></envioLoteEventos></eSocial></v1:loteEventos></v1:EnviarLoteEventos></soapenv:Body></soapenv:Envelope>"""

REQUEST_CONSULTA_LOTE = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0"><soapenv:Header/><soapenv:Body><v1:ConsultarLoteEventos><!--Optional:--><v1:consulta><!--You may enter ANY elements at this point--></v1:consulta></v1:ConsultarLoteEventos></soapenv:Body></soapenv:Envelope>"""

BASE_XML_CONSULTA_LOTE = u"""<eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoProcessamento/v1_0_0" xmlns:xs="http://www.w3.org/2001/XMLSchema"><consultaLoteEventos><protocoloEnvio>%s</protocoloEnvio></consultaLoteEventos></eSocial>"""

def criar_diretorio_arquivos():
    lista = [
        'arquivos/',
        'arquivos/WsConsultarLoteEventos/',
        'arquivos/WsEnviarLoteEventos/',
        'arquivos/WsConsultarLoteEventos/header/',
        'arquivos/WsConsultarLoteEventos/request/',
        'arquivos/WsConsultarLoteEventos/response/',
        'arquivos/WsEnviarLoteEventos/header/',
        'arquivos/WsEnviarLoteEventos/request/',
        'arquivos/WsEnviarLoteEventos/response/',
    ]
    for a in lista:
        if not os.path.isdir(a):
            os.system('mkdir %s' % a)

def executar_sql(select, array):
    from emensageria.settings import DATABASES
    database = DATABASES['default']
    try:
        conn = psycopg2.connect("user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s' dbname='%(NAME)s'" % database)
        conn.autocommit = True
    except:
        print "I am unable to connect to the database"
    if select:
        cur = conn.cursor()
        select = select.replace("'Null'", 'Null')
        cur.execute(select)
        if array: lista = cur.fetchall()
        else: lista = None
        cur.close()
        return lista
    else:
        return None

def salvar_arquivo(arquivo, texto):
    file = open(arquivo, "w")
    file.write( texto )
    file.close()
    print arquivo


def ler_arquivo(arquivo):
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto


def create_pem_files():
    import os.path
    from emensageria.settings import CERT_PEM_FILE, KEY_PEM_FILE, CERT_HOST, CERT_PASS
    from OpenSSL import crypto
    pkcs12 = crypto.load_pkcs12(open(CERT_HOST, 'rb').read(), CERT_PASS)
    if not os.path.isfile(CERT_PEM_FILE):
        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
        salvar_arquivo(CERT_PEM_FILE, cert_str)
    if not os.path.isfile(KEY_PEM_FILE):
        key_str = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
        salvar_arquivo(KEY_PEM_FILE, key_str)




def assinar(xml):
    from lxml import etree
    from emensageria.settings import CERT_PEM_FILE, KEY_PEM_FILE, FORCE_PRODUCAO_RESTRITA
    from signxml import XMLSigner, methods
    if FORCE_PRODUCAO_RESTRITA:
        xml = xml.replace('<tpAmb>1</tpAmb>','<tpAmb>2</tpAmb>')
    try:
        create_pem_files()
        cert_str = ler_arquivo(CERT_PEM_FILE)
        key_str = ler_arquivo(KEY_PEM_FILE)
        root = etree.fromstring(xml)
        signed_root = XMLSigner(
            method=methods.enveloped,
            signature_algorithm=u'rsa-sha256',
            digest_algorithm=u'sha256',
            c14n_algorithm=u'http://www.w3.org/TR/2001/REC-xml-c14n-20010315').sign(root, key=key_str, cert=cert_str)
        return etree.tostring(signed_root)
    except:
        return xml





def get_transmissor_name(transmissor_id):
    number = str(transmissor_id)
    while len(number) < 9:
        number = '0'+number
    return number




def create_request(dados, transmissor_dados):

    if dados['service'] == 'WsEnviarLoteEventos':

        from emensageria.eventos.views.s1000_evtinfoempregador_verificar import gerar_xml_s1000
        from emensageria.eventos.views.s1005_evttabestab_verificar import gerar_xml_s1005
        from emensageria.eventos.views.s1010_evttabrubrica_verificar import gerar_xml_s1010
        from emensageria.eventos.views.s1020_evttablotacao_verificar import gerar_xml_s1020
        from emensageria.eventos.views.s1030_evttabcargo_verificar import gerar_xml_s1030
        from emensageria.eventos.views.s1035_evttabcarreira_verificar import gerar_xml_s1035
        from emensageria.eventos.views.s1040_evttabfuncao_verificar import gerar_xml_s1040
        from emensageria.eventos.views.s1050_evttabhortur_verificar import gerar_xml_s1050
        from emensageria.eventos.views.s1060_evttabambiente_verificar import gerar_xml_s1060
        from emensageria.eventos.views.s1070_evttabprocesso_verificar import gerar_xml_s1070
        from emensageria.eventos.views.s1080_evttaboperport_verificar import gerar_xml_s1080
        from emensageria.eventos.views.s1200_evtremun_verificar import gerar_xml_s1200
        from emensageria.eventos.views.s1202_evtrmnrpps_verificar import gerar_xml_s1202
        from emensageria.eventos.views.s1207_evtbenprrp_verificar import gerar_xml_s1207
        from emensageria.eventos.views.s1210_evtpgtos_verificar import gerar_xml_s1210
        from emensageria.eventos.views.s1250_evtaqprod_verificar import gerar_xml_s1250
        from emensageria.eventos.views.s1260_evtcomprod_verificar import gerar_xml_s1260
        from emensageria.eventos.views.s1270_evtcontratavnp_verificar import gerar_xml_s1270
        from emensageria.eventos.views.s1280_evtinfocomplper_verificar import gerar_xml_s1280
        from emensageria.eventos.views.s1295_evttotconting_verificar import gerar_xml_s1295
        from emensageria.eventos.views.s1298_evtreabreevper_verificar import gerar_xml_s1298
        from emensageria.eventos.views.s1299_evtfechaevper_verificar import gerar_xml_s1299
        from emensageria.eventos.views.s1300_evtcontrsindpatr_verificar import gerar_xml_s1300
        from emensageria.eventos.views.s2190_evtadmprelim_verificar import gerar_xml_s2190
        from emensageria.eventos.views.s2200_evtadmissao_verificar import gerar_xml_s2200
        from emensageria.eventos.views.s2205_evtaltcadastral_verificar import gerar_xml_s2205
        from emensageria.eventos.views.s2206_evtaltcontratual_verificar import gerar_xml_s2206
        from emensageria.eventos.views.s2210_evtcat_verificar import gerar_xml_s2210
        from emensageria.eventos.views.s2220_evtmonit_verificar import gerar_xml_s2220
        from emensageria.eventos.views.s2230_evtafasttemp_verificar import gerar_xml_s2230
        from emensageria.eventos.views.s2240_evtexprisco_verificar import gerar_xml_s2240
        from emensageria.eventos.views.s2241_evtinsapo_verificar import gerar_xml_s2241
        from emensageria.eventos.views.s2250_evtavprevio_verificar import gerar_xml_s2250
        from emensageria.eventos.views.s2260_evtconvinterm_verificar import gerar_xml_s2260
        from emensageria.eventos.views.s2298_evtreintegr_verificar import gerar_xml_s2298
        from emensageria.eventos.views.s2299_evtdeslig_verificar import gerar_xml_s2299
        from emensageria.eventos.views.s2300_evttsvinicio_verificar import gerar_xml_s2300
        from emensageria.eventos.views.s2306_evttsvaltcontr_verificar import gerar_xml_s2306
        from emensageria.eventos.views.s2399_evttsvtermino_verificar import gerar_xml_s2399
        from emensageria.eventos.views.s2400_evtcdbenprrp_verificar import gerar_xml_s2400
        from emensageria.eventos.views.s3000_evtexclusao_verificar import gerar_xml_s3000
        from emensageria.eventos.views.s5001_evtbasestrab_verificar import gerar_xml_s5001
        from emensageria.eventos.views.s5002_evtirrfbenef_verificar import gerar_xml_s5002
        from emensageria.eventos.views.s5011_evtcs_verificar import gerar_xml_s5011
        from emensageria.eventos.views.s5012_evtirrf_verificar import gerar_xml_s5012
        xml = u''
        eventos = executar_sql("""
          SELECT evento, id, identidade
            FROM public.transmissor_eventos 
           WHERE transmissor_lote_id = %(transmissor_id)s 
           ORDER BY ordem;""" % dados, True)
        for e in eventos:
            evento = {}
            evento['evento'] = e[0]
            evento['id'] = e[1]
            xml += '<evento Id="%s">' % e[2]
            if evento['evento'] == 's1000':
                xml += gerar_xml_s1000(evento['id'], 'default')
            elif evento['evento'] == 's1005':
                xml += gerar_xml_s1005(evento['id'], 'default')
            elif evento['evento'] == 's1010':
                xml += gerar_xml_s1010(evento['id'], 'default')
            elif evento['evento'] == 's1020':
                xml += gerar_xml_s1020(evento['id'], 'default')
            elif evento['evento'] == 's1030':
                xml += gerar_xml_s1030(evento['id'], 'default')
            elif evento['evento'] == 's1035':
                xml += gerar_xml_s1035(evento['id'], 'default')
            elif evento['evento'] == 's1040':
                xml += gerar_xml_s1040(evento['id'], 'default')
            elif evento['evento'] == 's1050':
                xml += gerar_xml_s1050(evento['id'], 'default')
            elif evento['evento'] == 's1060':
                xml += gerar_xml_s1060(evento['id'], 'default')
            elif evento['evento'] == 's1070':
                xml += gerar_xml_s1070(evento['id'], 'default')
            elif evento['evento'] == 's1080':
                xml += gerar_xml_s1080(evento['id'], 'default')
            elif evento['evento'] == 's1200':
                xml += gerar_xml_s1200(evento['id'], 'default')
            elif evento['evento'] == 's1202':
                xml += gerar_xml_s1202(evento['id'], 'default')
            elif evento['evento'] == 's1207':
                xml += gerar_xml_s1207(evento['id'], 'default')
            elif evento['evento'] == 's1210':
                xml += gerar_xml_s1210(evento['id'], 'default')
            elif evento['evento'] == 's1250':
                xml += gerar_xml_s1250(evento['id'], 'default')
            elif evento['evento'] == 's1260':
                xml += gerar_xml_s1260(evento['id'], 'default')
            elif evento['evento'] == 's1270':
                xml += gerar_xml_s1270(evento['id'], 'default')
            elif evento['evento'] == 's1280':
                xml += gerar_xml_s1280(evento['id'], 'default')
            elif evento['evento'] == 's1295':
                xml += gerar_xml_s1295(evento['id'], 'default')
            elif evento['evento'] == 's1298':
                xml += gerar_xml_s1298(evento['id'], 'default')
            elif evento['evento'] == 's1299':
                xml += gerar_xml_s1299(evento['id'], 'default')
            elif evento['evento'] == 's1300':
                xml += gerar_xml_s1300(evento['id'], 'default')
            elif evento['evento'] == 's2190':
                xml += gerar_xml_s2190(evento['id'], 'default')
            elif evento['evento'] == 's2200':
                xml += gerar_xml_s2200(evento['id'], 'default')
            elif evento['evento'] == 's2205':
                xml += gerar_xml_s2205(evento['id'], 'default')
            elif evento['evento'] == 's2206':
                xml += gerar_xml_s2206(evento['id'], 'default')
            elif evento['evento'] == 's2210':
                xml += gerar_xml_s2210(evento['id'], 'default')
            elif evento['evento'] == 's2220':
                xml += gerar_xml_s2220(evento['id'], 'default')
            elif evento['evento'] == 's2230':
                xml += gerar_xml_s2230(evento['id'], 'default')
            elif evento['evento'] == 's2240':
                xml += gerar_xml_s2240(evento['id'], 'default')
            elif evento['evento'] == 's2241':
                xml += gerar_xml_s2241(evento['id'], 'default')
            elif evento['evento'] == 's2250':
                xml += gerar_xml_s2250(evento['id'], 'default')
            elif evento['evento'] == 's2260':
                xml += gerar_xml_s2260(evento['id'], 'default')
            elif evento['evento'] == 's2298':
                xml += gerar_xml_s2298(evento['id'], 'default')
            elif evento['evento'] == 's2299':
                xml += gerar_xml_s2299(evento['id'], 'default')
            elif evento['evento'] == 's2300':
                xml += gerar_xml_s2300(evento['id'], 'default')
            elif evento['evento'] == 's2306':
                xml += gerar_xml_s2306(evento['id'], 'default')
            elif evento['evento'] == 's2399':
                xml += gerar_xml_s2399(evento['id'], 'default')
            elif evento['evento'] == 's2400':
                xml += gerar_xml_s2400(evento['id'], 'default')
            elif evento['evento'] == 's3000':
                xml += gerar_xml_s3000(evento['id'], 'default')
            elif evento['evento'] == 's5001':
                xml += gerar_xml_s5001(evento['id'], 'default')
            elif evento['evento'] == 's5002':
                xml += gerar_xml_s5002(evento['id'], 'default')
            elif evento['evento'] == 's5011':
                xml += gerar_xml_s5011(evento['id'], 'default')
            elif evento['evento'] == 's5012':
                xml += gerar_xml_s5012(evento['id'], 'default')
            xml += '</evento>'
        base_request = REQUEST_ENVIA_LOTE % transmissor_dados

    elif dados['service'] == 'WsConsultarLoteEventos':
        base_request = REQUEST_CONSULTA_LOTE
        a = executar_sql("""
          SELECT protocolo 
            FROM public.transmissor_lote 
           WHERE id= %(transmissor_id)s;""" % dados, True)
        xml = BASE_XML_CONSULTA_LOTE % a[0][0]
        base_request = REQUEST_CONSULTA_LOTE % transmissor_dados

    text = base_request.replace('<!--You may enter ANY elements at this point-->', xml)
    salvar_arquivo(dados['request'], text)



def send_xml(transmissor_id, service):
    criar_diretorio_arquivos()
    import os
    from emensageria.settings import CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE, CA_CERT_PEM_FILE, FORCE_PRODUCAO_RESTRITA, TP_AMB
    if TP_AMB == 1: # Produção
        if service == 'WsEnviarLoteEventos':
            URL = "https://webservices.envio.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0/ServicoEnviarLoteEventos/EnviarLoteEventos"
        elif service == 'WsConsultarLoteEventos':
            URL = "https://webservices.consulta.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0/ServicoConsultarLoteEventos/ConsultarLoteEventos"
    elif TP_AMB == 2: # Produção-Restrita
        if service == 'WsEnviarLoteEventos':
            URL = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0/ServicoEnviarLoteEventos/EnviarLoteEventos"
        elif service == 'WsConsultarLoteEventos':
            URL = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0/ServicoConsultarLoteEventos/ConsultarLoteEventos"
    dados = {}
    name = get_transmissor_name(transmissor_id)
    transmissor_dados = {}
    tra = executar_sql("""
    SELECT empregador_tpinsc, empregador_nrinsc,
           transmissor_tpinsc, transmissor_nrinsc
      FROM public.transmissor_lote
     WHERE id=%s;
    """ % transmissor_id, True)
    transmissor_dados['empregador_tpinsc'] = tra[0][0]
    transmissor_dados['empregador_nrinsc'] = tra[0][1]
    transmissor_dados['transmissor_tpinsc'] = tra[0][2]
    transmissor_dados['transmissor_nrinsc'] = tra[0][3]
    dados['transmissor_id'] = transmissor_id
    dados['header'] = 'arquivos/%s/header/%s.xml' % (service, name)
    dados['request'] = 'arquivos/%s/request/%s.xml' % (service, name)
    dados['response'] = 'arquivos/%s/response/%s.xml' % (service, name)
    dados['service'] = service
    dados['url'] = URL
    dados['cert'] = CERT_PEM_FILE
    dados['cacert'] = CA_CERT_PEM_FILE
    dados['key'] = KEY_PEM_FILE
    dados['action'] = ACTION
    create_request(dados, transmissor_dados)
    if os.path.isfile(CERT_PEM_FILE):
        command = '''curl --cert %(cert)s
                          --key %(key)s
                          --cacert %(cacert)s
                          -H "Content-Type: text/xml;charset=UTF-8" 
                          -H "SOAPAction:%(action)s" 
                          --dump-header %(header)s
                          --output %(response)s 
                          -d@%(request)s 
                          %(url)s''' % dados
        command = command.replace('\n', '')
        for n in range(10):
            command = command.replace('  ', ' ')
        os.system(command)
        if service == 'WsEnviarLoteEventos':
            read_envioLoteEventos(dados['response'], transmissor_id)
        elif service == 'WsConsultarLoteEventos':
            read_consultaLoteEventos(dados['response'], transmissor_id)
        return ler_arquivo(dados['header'])
    else:
        return 'Certificado digital não cadastrado!'




def read_envioLoteEventos(arquivo, transmissor_lote_id):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.EnviarLoteEventosResponse.EnviarLoteEventosResult.eSocial.retornoEnvioLoteEventos
    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id
    lote['cdResposta'] = child.status.cdResposta.cdata
    lote['descResposta'] = child.status.descResposta.cdata
    executar_sql("""
      DELETE FROM public.transmissor_lote_ocorrencias 
            WHERE transmissor_lote_id=%s;""" % transmissor_lote_id, False)
    if '<ocorrencias>' in xml:
        INSERT_OCORRENCIAS = ''
        for a in child.status.ocorrencias:
            ocorrencias = {}
            ocorrencias['transmissor_lote_id'] = transmissor_lote_id
            ocorrencias['codigo'] = a.ocorrencia.codigo.cdata
            ocorrencias['descricao'] = a.ocorrencia.descricao.cdata
            ocorrencias['descricao'] = ocorrencias['descricao'].replace("'", "''")
            ocorrencias['tipo'] = a.ocorrencia.tipo.cdata
            try:
                ocorrencias['localizacao'] = a.ocorrencia.localizacao.cdata
            except:
                ocorrencias['localizacao'] = ''
            INSERT_OCORRENCIAS += """
            INSERT INTO public.transmissor_lote_ocorrencias (
                        resposta_codigo, descricao, tipo, localizacao, criado_em, 
                        modificado_em, excluido, criado_por_id, modificado_por_id, transmissor_lote_id)
                VALUES ('%(codigo)s', '%(descricao)s', '%(tipo)s', '%(localizacao)s', now(), 
                        Null, False, 1, Null, %(transmissor_lote_id)s);
            """ % ocorrencias
        executar_sql(INSERT_OCORRENCIAS, False)
    if '<dadosRecepcaoLote>' in xml:
        lote['dhRecepcao'] = child.dadosRecepcaoLote.dhRecepcao.cdata
        lote['versaoAplicativoRecepcao'] = child.dadosRecepcaoLote.versaoAplicativoRecepcao.cdata
        lote['protocoloEnvio'] = child.dadosRecepcaoLote.protocoloEnvio.cdata
        UPDATE = """
            UPDATE public.transmissor_lote
               SET resposta_codigo='%(cdResposta)s', 
                   resposta_descricao='%(descResposta)s', 
                   recepcao_data_hora='%(dhRecepcao)s', 
                   recepcao_versao_aplicativo='%(versaoAplicativoRecepcao)s', 
                   protocolo='%(protocoloEnvio)s', modificado_em=now(), modificado_por_id=1
             WHERE id=%(transmissor_lote_id)s;
        """ % lote
    else:
        UPDATE = """
                UPDATE public.transmissor_lote
                   SET resposta_codigo='%(cdResposta)s', 
                       resposta_descricao='%(descResposta)s',
                       modificado_em=now(), modificado_por_id=1
                 WHERE id=%(transmissor_lote_id)s;
                """ % lote
    executar_sql(UPDATE, False)



def read_consultaLoteEventos(arquivo, transmissor_lote_id):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    child = doc.Envelope.Body.ConsultarLoteEventosResponse.ConsultarLoteEventosResult.eSocial.retornoProcessamentoLoteEventos
    lote = {}
    lote['transmissor_lote_id'] = transmissor_lote_id
    lote['cdResposta'] = child.status.cdResposta.cdata
    lote['descResposta'] = child.status.descResposta.cdata
    if '<tempoEstimadoConclusao>' in xml:
        lote['tempoEstimadoConclusao'] = child.status.tempoEstimadoConclusao.cdata
    else:
        lote['tempoEstimadoConclusao'] = ''

    if '<dadosRecepcaoLote>' in xml:
        lote['dhRecepcao'] = child.dadosRecepcaoLote.dhRecepcao.cdata
        lote['versaoAplicativoRecepcao'] = child.dadosRecepcaoLote.versaoAplicativoRecepcao.cdata
        lote['protocoloEnvio'] = child.dadosRecepcaoLote.protocoloEnvio.cdata
    else:
        lote['dhRecepcao'] = ''
        lote['versaoAplicativoRecepcao'] = ''
        lote['protocoloEnvio'] = ''

    if '<versaoAplicativoProcessamentoLote>' in xml:
        lote['versaoAplicativoProcessamentoLote'] = child.dadosProcessamentoLote.versaoAplicativoProcessamentoLote.cdata
    else:
        lote['versaoAplicativoProcessamentoLote'] = ''

    if '<retornoEvento>' in xml:
        for a in child.retornoEventos:
            evento_dados = executar_sql("""
                SELECT id, tabela
                  FROM public.transmissor_eventos 
                 WHERE identidade='%s';
            """ % a.evento['Id'], True)
            evento = {}
            evento['id'] = evento_dados[0][0]
            evento['tabela'] = evento_dados[0][1]
            evento['tpAmb'] = a.evento.retornoEvento.eSocial.retornoEvento.recepcao.tpAmb.cdata
            evento['dhRecepcao'] = a.evento.retornoEvento.eSocial.retornoEvento.recepcao.dhRecepcao.cdata
            evento['versaoAppRecepcao'] = a.evento.retornoEvento.eSocial.retornoEvento.recepcao.versaoAppRecepcao.cdata
            if '<protocoloEnvioLote>' in xml:
                evento['protocoloEnvioLote'] = a.evento.retornoEvento.eSocial.retornoEvento.recepcao.protocoloEnvioLote.cdata
            else:
                evento['protocoloEnvioLote'] = ''
            evento['cdResposta'] = a.evento.retornoEvento.eSocial.retornoEvento.processamento.cdResposta.cdata
            evento['descResposta'] = a.evento.retornoEvento.eSocial.retornoEvento.processamento.descResposta.cdata
            evento['versaoAppProcessamento'] = a.evento.retornoEvento.eSocial.retornoEvento.processamento.versaoAppProcessamento.cdata
            evento['dhProcessamento'] = a.evento.retornoEvento.eSocial.retornoEvento.processamento.dhProcessamento.cdata
            if '<recibo>' in xml:
                evento['nrRecibo'] = a.evento.retornoEvento.eSocial.retornoEvento.recibo.nrRecibo.cdata
                evento['hash'] = a.evento.retornoEvento.eSocial.retornoEvento.recibo.nrRecibo.cdata
            else:
                evento['nrRecibo'] = ''
                evento['hash'] = ''
            UPDATE = """
                UPDATE public.s1000_evtinfoempregador
                   SET modificado_em=now(), 
                       recepcao_tp_amb=%(tpAmb)s, 
                       recepcao_data_hora='%(dhRecepcao)s', 
                       recepcao_versao_app='%(versaoAppRecepcao)s', 
                       recepcao_protocolo_envio_lote='%(protocoloEnvioLote)s', 
                       processamento_codigo_resposta='%(cdResposta)s', 
                       processamento_descricao_resposta='%(descResposta)s', 
                       processamento_versao_app_processamento='%(versaoAppProcessamento)s', 
                       processamento_data_hora='%(dhProcessamento)s', 
                       recibo_numero='%(nrRecibo)s', 
                       recibo_hash='%(hash)s', 
                       modificado_por_id=1
                 WHERE id=%(id)s;
            """ % evento
            UPDATE = UPDATE.replace("''", 'Null')
            executar_sql(UPDATE, False)
            executar_sql("""
            DELETE FROM public.%(tabela)s_ocorrencias 
                  WHERE evento_id=%(id)s;""" % evento, False)
            INSERT = ''
            for b in a.evento.retornoEvento.eSocial.retornoEvento.processamento.ocorrencias.ocorrencia:
                ocorrencias = {}
                ocorrencias['evento_id'] = evento['id']
                ocorrencias['tabela'] = evento['tabela'] + '_ocorrencias'
                ocorrencias['tipo'] = b.tipo.cdata
                ocorrencias['codigo'] = b.codigo.cdata

                ocorrencias['descricao'] = b.descricao.cdata
                ocorrencias['descricao'] = ocorrencias['descricao'].replace("'", "''")

                try:
                    ocorrencias['localizacao'] = b.localizacao.cdata
                except:
                    ocorrencias['localizacao'] = ''


                INSERT += """
                INSERT INTO public.%(tabela)s (
                        tipo, codigo, descricao, localizacao, criado_em,
                        excluido, criado_por_id, evento_id)
                VALUES ('%(tipo)s', '%(codigo)s', '%(descricao)s', '%(localizacao)s', now(),
                        False, 1, '%(evento_id)s');
                """ % ocorrencias
            if INSERT:
                executar_sql(INSERT, False)

