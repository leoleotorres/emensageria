# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('mensageiro', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='s5012evtirrf',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s5012evtirrf_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcsocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s5011evtcsocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcsocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s5011evtcsocorrencias_evento', to='eventos.s5011evtCS'),
        ),
        migrations.AddField(
            model_name='s5011evtcsocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5011evtcsocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='criado_por',
            field=models.ForeignKey(related_name='s5011evtcs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5011evtcs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s5011evtcs_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenefocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s5002evtirrfbenefocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenefocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s5002evtirrfbenefocorrencias_evento', to='eventos.s5002evtIrrfBenef'),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenefocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5002evtirrfbenefocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='criado_por',
            field=models.ForeignKey(related_name='s5002evtirrfbenef_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5002evtirrfbenef_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s5002evtirrfbenef_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrabocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s5001evtbasestrabocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrabocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s5001evtbasestrabocorrencias_evento', to='eventos.s5001evtBasesTrab'),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrabocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5001evtbasestrabocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='criado_por',
            field=models.ForeignKey(related_name='s5001evtbasestrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='modificado_por',
            field=models.ForeignKey(related_name='s5001evtbasestrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s5001evtbasestrab_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusaoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s3000evtexclusaoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusaoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s3000evtexclusaoocorrencias_evento', to='eventos.s3000evtExclusao'),
        ),
        migrations.AddField(
            model_name='s3000evtexclusaoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s3000evtexclusaoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='criado_por',
            field=models.ForeignKey(related_name='s3000evtexclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='modificado_por',
            field=models.ForeignKey(related_name='s3000evtexclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s3000evtexclusao_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenprrpocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2400evtcdbenprrpocorrencias_evento', to='eventos.s2400evtCdBenPrRP'),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenprrpocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='criado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenprrp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenprrp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2400evtcdbenprrp_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvterminoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2399evttsvterminoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvterminoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2399evttsvterminoocorrencias_evento', to='eventos.s2399evtTSVTermino'),
        ),
        migrations.AddField(
            model_name='s2399evttsvterminoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2399evttsvterminoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='criado_por',
            field=models.ForeignKey(related_name='s2399evttsvtermino_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2399evttsvtermino_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2399evttsvtermino_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2306evttsvaltcontrocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2306evttsvaltcontrocorrencias_evento', to='eventos.s2306evtTSVAltContr'),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2306evttsvaltcontrocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='criado_por',
            field=models.ForeignKey(related_name='s2306evttsvaltcontr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2306evttsvaltcontr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2306evttsvaltcontr_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicioocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2300evttsvinicioocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicioocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2300evttsvinicioocorrencias_evento', to='eventos.s2300evtTSVInicio'),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicioocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2300evttsvinicioocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='criado_por',
            field=models.ForeignKey(related_name='s2300evttsvinicio_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2300evttsvinicio_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2300evttsvinicio_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdesligocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2299evtdesligocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdesligocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2299evtdesligocorrencias_evento', to='eventos.s2299evtDeslig'),
        ),
        migrations.AddField(
            model_name='s2299evtdesligocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2299evtdesligocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='criado_por',
            field=models.ForeignKey(related_name='s2299evtdeslig_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2299evtdeslig_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2299evtdeslig_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegrocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2298evtreintegrocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegrocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2298evtreintegrocorrencias_evento', to='eventos.s2298evtReintegr'),
        ),
        migrations.AddField(
            model_name='s2298evtreintegrocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2298evtreintegrocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='criado_por',
            field=models.ForeignKey(related_name='s2298evtreintegr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2298evtreintegr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2298evtreintegr_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvintermocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2260evtconvintermocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvintermocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2260evtconvintermocorrencias_evento', to='eventos.s2260evtConvInterm'),
        ),
        migrations.AddField(
            model_name='s2260evtconvintermocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2260evtconvintermocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='criado_por',
            field=models.ForeignKey(related_name='s2260evtconvinterm_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2260evtconvinterm_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2260evtconvinterm_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevioocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2250evtavprevioocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevioocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2250evtavprevioocorrencias_evento', to='eventos.s2250evtAvPrevio'),
        ),
        migrations.AddField(
            model_name='s2250evtavprevioocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2250evtavprevioocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='criado_por',
            field=models.ForeignKey(related_name='s2250evtavprevio_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2250evtavprevio_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2250evtavprevio_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2241evtinsapoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2241evtinsapoocorrencias_evento', to='eventos.s2241evtInsApo'),
        ),
        migrations.AddField(
            model_name='s2241evtinsapoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2241evtinsapoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='criado_por',
            field=models.ForeignKey(related_name='s2241evtinsapo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2241evtinsapo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2241evtinsapo_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexpriscoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2240evtexpriscoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexpriscoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2240evtexpriscoocorrencias_evento', to='eventos.s2240evtExpRisco'),
        ),
        migrations.AddField(
            model_name='s2240evtexpriscoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2240evtexpriscoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='criado_por',
            field=models.ForeignKey(related_name='s2240evtexprisco_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2240evtexprisco_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2240evtexprisco_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttempocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2230evtafasttempocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttempocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2230evtafasttempocorrencias_evento', to='eventos.s2230evtAfastTemp'),
        ),
        migrations.AddField(
            model_name='s2230evtafasttempocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2230evtafasttempocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='criado_por',
            field=models.ForeignKey(related_name='s2230evtafasttemp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2230evtafasttemp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2230evtafasttemp_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonitocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2220evtmonitocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonitocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2220evtmonitocorrencias_evento', to='eventos.s2220evtMonit'),
        ),
        migrations.AddField(
            model_name='s2220evtmonitocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2220evtmonitocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='criado_por',
            field=models.ForeignKey(related_name='s2220evtmonit_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2220evtmonit_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2220evtmonit_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcatocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2210evtcatocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcatocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2210evtcatocorrencias_evento', to='eventos.s2210evtCAT'),
        ),
        migrations.AddField(
            model_name='s2210evtcatocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2210evtcatocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='criado_por',
            field=models.ForeignKey(related_name='s2210evtcat_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2210evtcat_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2210evtcat_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratualocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2206evtaltcontratualocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratualocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2206evtaltcontratualocorrencias_evento', to='eventos.s2206evtAltContratual'),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratualocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2206evtaltcontratualocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='criado_por',
            field=models.ForeignKey(related_name='s2206evtaltcontratual_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2206evtaltcontratual_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2206evtaltcontratual_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastralocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2205evtaltcadastralocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastralocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2205evtaltcadastralocorrencias_evento', to='eventos.s2205evtAltCadastral'),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastralocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2205evtaltcadastralocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='criado_por',
            field=models.ForeignKey(related_name='s2205evtaltcadastral_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2205evtaltcadastral_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2205evtaltcadastral_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissaoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2200evtadmissaoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissaoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2200evtadmissaoocorrencias_evento', to='eventos.s2200evtAdmissao'),
        ),
        migrations.AddField(
            model_name='s2200evtadmissaoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2200evtadmissaoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='criado_por',
            field=models.ForeignKey(related_name='s2200evtadmissao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2200evtadmissao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2200evtadmissao_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelimocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s2190evtadmprelimocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelimocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s2190evtadmprelimocorrencias_evento', to='eventos.s2190evtAdmPrelim'),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelimocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2190evtadmprelimocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='criado_por',
            field=models.ForeignKey(related_name='s2190evtadmprelim_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2190evtadmprelim_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s2190evtadmprelim_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatrocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatrocorrencias_evento', to='eventos.s1300evtContrSindPatr'),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatrocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='criado_por',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatr_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevperocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1299evtfechaevperocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevperocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1299evtfechaevperocorrencias_evento', to='eventos.s1299evtFechaEvPer'),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevperocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1299evtfechaevperocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='criado_por',
            field=models.ForeignKey(related_name='s1299evtfechaevper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1299evtfechaevper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1299evtfechaevper_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevperocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1298evtreabreevperocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevperocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1298evtreabreevperocorrencias_evento', to='eventos.s1298evtReabreEvPer'),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevperocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1298evtreabreevperocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='criado_por',
            field=models.ForeignKey(related_name='s1298evtreabreevper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1298evtreabreevper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1298evtreabreevper_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotcontingocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1295evttotcontingocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotcontingocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1295evttotcontingocorrencias_evento', to='eventos.s1295evtTotConting'),
        ),
        migrations.AddField(
            model_name='s1295evttotcontingocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1295evttotcontingocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='criado_por',
            field=models.ForeignKey(related_name='s1295evttotconting_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1295evttotconting_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1295evttotconting_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplperocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1280evtinfocomplperocorrencias_evento', to='eventos.s1280evtInfoComplPer'),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='criado_por',
            field=models.ForeignKey(related_name='s1280evtinfocomplper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1280evtinfocomplper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1280evtinfocomplper_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnpocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1270evtcontratavnpocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnpocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1270evtcontratavnpocorrencias_evento', to='eventos.s1270evtContratAvNP'),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnpocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1270evtcontratavnpocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='criado_por',
            field=models.ForeignKey(related_name='s1270evtcontratavnp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1270evtcontratavnp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1270evtcontratavnp_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprodocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1260evtcomprodocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprodocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1260evtcomprodocorrencias_evento', to='eventos.s1260evtComProd'),
        ),
        migrations.AddField(
            model_name='s1260evtcomprodocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1260evtcomprodocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='criado_por',
            field=models.ForeignKey(related_name='s1260evtcomprod_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1260evtcomprod_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1260evtcomprod_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprodocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1250evtaqprodocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprodocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1250evtaqprodocorrencias_evento', to='eventos.s1250evtAqProd'),
        ),
        migrations.AddField(
            model_name='s1250evtaqprodocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1250evtaqprodocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='criado_por',
            field=models.ForeignKey(related_name='s1250evtaqprod_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1250evtaqprod_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1250evtaqprod_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtosocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1210evtpgtosocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtosocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1210evtpgtosocorrencias_evento', to='eventos.s1210evtPgtos'),
        ),
        migrations.AddField(
            model_name='s1210evtpgtosocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1210evtpgtosocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='criado_por',
            field=models.ForeignKey(related_name='s1210evtpgtos_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1210evtpgtos_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1210evtpgtos_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrpocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1207evtbenprrpocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrpocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1207evtbenprrpocorrencias_evento', to='eventos.s1207evtBenPrRP'),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrpocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1207evtbenprrpocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='criado_por',
            field=models.ForeignKey(related_name='s1207evtbenprrp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1207evtbenprrp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1207evtbenprrp_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrppsocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1202evtrmnrppsocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrppsocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1202evtrmnrppsocorrencias_evento', to='eventos.s1202evtRmnRPPS'),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrppsocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1202evtrmnrppsocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='criado_por',
            field=models.ForeignKey(related_name='s1202evtrmnrpps_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1202evtrmnrpps_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1202evtrmnrpps_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremunocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1200evtremunocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremunocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1200evtremunocorrencias_evento', to='eventos.s1200evtRemun'),
        ),
        migrations.AddField(
            model_name='s1200evtremunocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1200evtremunocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='criado_por',
            field=models.ForeignKey(related_name='s1200evtremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1200evtremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1200evtremun_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperportocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1080evttaboperportocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperportocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1080evttaboperportocorrencias_evento', to='eventos.s1080evtTabOperPort'),
        ),
        migrations.AddField(
            model_name='s1080evttaboperportocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1080evttaboperportocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='criado_por',
            field=models.ForeignKey(related_name='s1080evttaboperport_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1080evttaboperport_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1080evttaboperport_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocessoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1070evttabprocessoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocessoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1070evttabprocessoocorrencias_evento', to='eventos.s1070evtTabProcesso'),
        ),
        migrations.AddField(
            model_name='s1070evttabprocessoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1070evttabprocessoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='criado_por',
            field=models.ForeignKey(related_name='s1070evttabprocesso_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1070evttabprocesso_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1070evttabprocesso_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambienteocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1060evttabambienteocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambienteocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1060evttabambienteocorrencias_evento', to='eventos.s1060evtTabAmbiente'),
        ),
        migrations.AddField(
            model_name='s1060evttabambienteocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1060evttabambienteocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='criado_por',
            field=models.ForeignKey(related_name='s1060evttabambiente_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1060evttabambiente_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1060evttabambiente_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhorturocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1050evttabhorturocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhorturocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1050evttabhorturocorrencias_evento', to='eventos.s1050evtTabHorTur'),
        ),
        migrations.AddField(
            model_name='s1050evttabhorturocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1050evttabhorturocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='criado_por',
            field=models.ForeignKey(related_name='s1050evttabhortur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1050evttabhortur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1050evttabhortur_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncaoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1040evttabfuncaoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncaoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1040evttabfuncaoocorrencias_evento', to='eventos.s1040evtTabFuncao'),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncaoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1040evttabfuncaoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='criado_por',
            field=models.ForeignKey(related_name='s1040evttabfuncao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1040evttabfuncao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1040evttabfuncao_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreiraocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1035evttabcarreiraocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreiraocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1035evttabcarreiraocorrencias_evento', to='eventos.s1035evtTabCarreira'),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreiraocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1035evttabcarreiraocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='criado_por',
            field=models.ForeignKey(related_name='s1035evttabcarreira_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1035evttabcarreira_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1035evttabcarreira_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1030evttabcargoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1030evttabcargoocorrencias_evento', to='eventos.s1030evtTabCargo'),
        ),
        migrations.AddField(
            model_name='s1030evttabcargoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1030evttabcargoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='criado_por',
            field=models.ForeignKey(related_name='s1030evttabcargo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1030evttabcargo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1030evttabcargo_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacaoocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1020evttablotacaoocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacaoocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1020evttablotacaoocorrencias_evento', to='eventos.s1020evtTabLotacao'),
        ),
        migrations.AddField(
            model_name='s1020evttablotacaoocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1020evttablotacaoocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='criado_por',
            field=models.ForeignKey(related_name='s1020evttablotacao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1020evttablotacao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1020evttablotacao_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubricaocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1010evttabrubricaocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubricaocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1010evttabrubricaocorrencias_evento', to='eventos.s1010evtTabRubrica'),
        ),
        migrations.AddField(
            model_name='s1010evttabrubricaocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1010evttabrubricaocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='criado_por',
            field=models.ForeignKey(related_name='s1010evttabrubrica_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1010evttabrubrica_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1010evttabrubrica_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestabocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1005evttabestabocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestabocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1005evttabestabocorrencias_evento', to='eventos.s1005evtTabEstab'),
        ),
        migrations.AddField(
            model_name='s1005evttabestabocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1005evttabestabocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='criado_por',
            field=models.ForeignKey(related_name='s1005evttabestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1005evttabestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1005evttabestab_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='criado_por',
            field=models.ForeignKey(related_name='s1000evtinfoempregadorocorrencias_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='evento',
            field=models.ForeignKey(related_name='s1000evtinfoempregadorocorrencias_evento', to='eventos.s1000evtInfoEmpregador'),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1000evtinfoempregadorocorrencias_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='criado_por',
            field=models.ForeignKey(related_name='s1000evtinfoempregador_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1000evtinfoempregador_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='transmissor_lote',
            field=models.ForeignKey(related_name='s1000evtinfoempregador_transmissor_lote', blank=True, to='mensageiro.TransmissorLote', null=True),
        ),
    ]
