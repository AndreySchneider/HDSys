# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-15 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hdsysapp', '0002_auto_20170128_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='hdsysAddress',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('complement', models.CharField(blank=True, max_length=50, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=10, null=True)),
                ('country', models.CharField(blank=True, choices=[('AD', 'Andorra'), ('AE', 'Emirados Árabes Unidos'), ('AF', 'Afeganistão'), ('AG', 'Antígua e Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albânia'), ('AM', 'Armênia'), ('AO', 'Angola'), ('AQ', 'Antártica'), ('AR', 'Argentina'), ('AS', 'Samoa Americana'), ('AT', 'Áustria'), ('AU', 'Austrália'), ('AW', 'Aruba'), ('AZ', 'Azerbaijão'), ('BA', 'Bósnia e Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Bélgica'), ('BF', 'Burkina Faso'), ('BG', 'Bulgária'), ('BH', 'Barém'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BL', 'São Bartolomeu'), ('BM', 'Bermuda'), ('BN', 'Brunei'), ('BO', 'Bolívia'), ('BR', 'Brasil'), ('BS', 'Bahamas'), ('BT', 'Butão'), ('BV', 'Ilha Bouvet'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canadá'), ('CC', 'Ilhas Cocos (Keeling)'), ('CD', 'Congo, República Democrática do'), ('CF', 'República Centro-Africana'), ('CG', 'Congo, República do'), ('CH', 'Suíça'), ('CI', 'Costa do Marfim'), ('CK', 'Ilhas Cook'), ('CL', 'Chile'), ('CM', 'Camarões'), ('CN', 'China'), ('CO', 'Colômbia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cabo Verde'), ('CW', 'Curaçao'), ('CX', 'Ilha Christmas'), ('CY', 'Chipre'), ('CZ', 'República Tcheca'), ('DE', 'Alemanha'), ('DJ', 'Djibuti'), ('DK', 'Dinamarca'), ('DM', 'Dominica'), ('DO', 'República Dominicana'), ('DZ', 'Argélia'), ('EC', 'Equador'), ('EE', 'Estônia'), ('EG', 'Egito'), ('EH', 'Saara Ocidental'), ('ER', 'Eritréia'), ('ES', 'Espanha'), ('ET', 'Etiópia'), ('FI', 'Finlândia'), ('FJ', 'Fiji'), ('FK', 'Ilhas Falkland (Malvinas)'), ('FM', 'Micronésia, Estados Federados da'), ('FO', 'Ilhas Feroe'), ('FR', 'França'), ('FX', 'França Metropolitana'), ('GA', 'Gabão'), ('GB', 'Reino Unido'), ('GD', 'Grenada'), ('GE', 'Geórgia'), ('GF', 'Guiana Francesa'), ('GG', 'Guernsey'), ('GH', 'Gana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gâmbia'), ('GN', 'Guiné'), ('GP', 'Guadelupe'), ('GQ', 'Guiné Equatorial'), ('GR', 'Grécia'), ('GS', 'Geórgia do Sul e Ilhas'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guiné-Bissau'), ('GY', 'Guiana'), ('HK', 'Hong Kong'), ('HM', 'Ilhas Heard and McDonald'), ('HN', 'Honduras'), ('HR', 'Croácia'), ('HT', 'Haiti'), ('HU', 'Hungria'), ('ID', 'Indonésia'), ('IE', 'Irlanda'), ('IL', 'Israel'), ('IM', 'Ilha de Man'), ('IN', 'Índia'), ('IO', 'Território Britânico do Oceano Índico'), ('IQ', 'Iraque'), ('IR', 'Irã'), ('IS', 'Islândia'), ('IT', 'Itália'), ('JE', 'Jersey'), ('JM', 'Jamaica'), ('JO', 'Jordânia'), ('JP', 'Japão'), ('KE', 'Quênia'), ('KG', 'Quirguistão'), ('KH', 'Camboja'), ('KI', 'Kiribati'), ('KM', 'Cômoros'), ('KN', 'São Cristóvão e Nevis'), ('KP', 'Coreia do Norte'), ('KR', 'Coreia do Sul'), ('KW', 'Kuwait'), ('KY', 'Ilhas Caiman'), ('KZ', 'Cazaquistão'), ('LA', 'Laos'), ('LB', 'Líbano'), ('LC', 'Santa Lúcia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Libéria'), ('LS', 'Lesoto'), ('LT', 'Lituânia'), ('LU', 'Luxemburgo'), ('LV', 'Letônia'), ('LY', 'Líbia'), ('MA', 'Marrocos'), ('MC', 'Mônaco'), ('MD', 'Moldova'), ('ME', 'Montenegro'), ('MF', 'Saint Martin'), ('MG', 'Madagascar'), ('MH', 'Ilhas Marshall'), ('MK', 'Macedônia'), ('ML', 'Mali'), ('MM', 'Birmânia'), ('MN', 'Mongólia'), ('MO', 'Macao'), ('MP', 'Ilhas Marianas do Norte'), ('MQ', 'Martinica'), ('MR', 'Mauritânia'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('MU', 'Ilhas Maurício'), ('MV', 'Maldivas'), ('MW', 'Malawi'), ('MX', 'México'), ('MY', 'Malásia'), ('MZ', 'Moçambique'), ('NA', 'Namíbia'), ('NC', 'Nova Caledônia'), ('NE', 'Níger'), ('NF', 'Ilha Norfolk'), ('NG', 'Nigéria'), ('NI', 'Nicarágua'), ('NL', 'Holanda'), ('NO', 'Noruega'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'Nova Zelândia'), ('OM', 'Omã'), ('PA', 'Panamá'), ('PE', 'Peru'), ('PF', 'Polinésia Francesa'), ('PG', 'Papua Nova Guiné'), ('PH', 'Filipinas'), ('PK', 'Paquistão'), ('PL', 'Polônia'), ('PM', 'Saint Pierre e Miquelon'), ('PN', 'Ilhas Pitcairn'), ('PR', 'Porto Rico'), ('PS', 'Faixa de Gaza'), ('PS', 'Cisjordânia'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguai'), ('QA', 'Qatar'), ('RE', 'Reunião'), ('RO', 'Romênia'), ('RS', 'Sérvia'), ('RU', 'Rússia'), ('RW', 'Ruanda'), ('SA', 'Arábia Saudita'), ('SB', 'Ilhas Salomão'), ('SC', 'Seicheles'), ('SD', 'Sudão'), ('SE', 'Suécia'), ('SG', 'Cingapura'), ('SH', 'Santa Helena, Ascensão e Tristão da Cunha'), ('SI', 'Eslovênia'), ('SJ', 'Svalbard'), ('SK', 'Eslováquia'), ('SL', 'Serra Leoa'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somália'), ('SR', 'Suriname'), ('SS', 'Sudão do Sul'), ('ST', 'São Tomé e Príncipe'), ('SV', 'El Salvador'), ('SX', 'São Martinho'), ('SY', 'Síria'), ('SZ', 'Suazilândia'), ('TC', 'Ilhas Turks e Caicos'), ('TD', 'Chad'), ('TF', 'Sul da França e Antártica'), ('TG', 'Togo'), ('TH', 'Tailândia'), ('TJ', 'Tadjiquistão'), ('TK', 'Toquelau'), ('TL', 'Timor-Leste'), ('TM', 'Turcomenistão'), ('TN', 'Tunísia'), ('TO', 'Tonga'), ('TR', 'Turquia'), ('TT', 'Trinidad e Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan'), ('TZ', 'Tanzânia'), ('UA', 'Ucrânia'), ('UG', 'Uganda'), ('UM', 'Ilhas Menores Distantes dos Estados Unidos'), ('US', 'Estados Unidos'), ('UY', 'Uruguai'), ('UZ', 'Uzbequistão'), ('VA', 'Santa Sé (Cidade do Vaticano)'), ('VC', 'São Vicente e Granadinas'), ('VE', 'Venezuela'), ('VG', 'Ilhas Virgens Britânicas'), ('VI', 'Ilhas Virgens Americanas'), ('VN', 'Vietnã'), ('VU', 'Vanuatu'), ('WF', 'Ilhas Wallis e Futuna'), ('WS', 'Samoa'), ('XK', 'Kosovo'), ('YE', 'Iêmen'), ('YT', 'Maiote'), ('ZA', 'África do Sul'), ('ZM', 'Zâmbia'), ('ZW', 'Zimbábue')], max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=9, null=True)),
                ('position', geoposition.fields.GeopositionField(blank=True, max_length=42, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hdsysuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hdsysuser',
            name='position',
        ),
    ]
