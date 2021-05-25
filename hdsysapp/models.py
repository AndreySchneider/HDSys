# -*- coding: utf-8 -*-
#Python 2.7################################################

# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from geoposition.fields import GeopositionField

class hdsysUserManager (BaseUserManager):
    def create_user(self, username, cpf, email, password=None):
        if not username:
            raise ValueError('Usuário tem que ter um username')
        if not cpf:
            raise ValueError('Usuário tem que ter um cpf')
        if not email:
            raise ValueError('Usuário tem que ter um email')

        user = self.model(
            username=username,
            cpf=cpf,
            email = hdsysUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, cpf, email, password):
        user = self.create_user(username,
            password=password,
            cpf=cpf,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#verificar https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
#verificar http://procrastinatingdev.com/django/using-configurable-user-models-in-django-1-5/
#verificar http://stackoverflow.com/questions/20192144/creating-custom-user-registration-form-django
class hdsysUser (AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, db_index=True, error_messages={'unique': 'Este nome de usuário já está cadastrado no sistema. Insira um nome de usuário diferente.'}) #Verificar RegexField para este campo!!!
    fullname = models.CharField(max_length=200, blank=True, null=True) #verificar tamanho do campo
    cpf = models.PositiveIntegerField(unique=True, error_messages={'unique': 'Este CPF já está cadastrado no sistema. Insira um CPF diferente.'})
    rg = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=75, unique=True, error_messages={'unique': 'Este e-mail já está cadastrado no sistema. Insira um e-mail diferente.'})

    #address = models.TextField(blank=True, null=True) #verificar tipo do campo
    #position = GeopositionField(blank=True, null=True) #TESTE API GOOGLE MAPS

    register_date = models.DateTimeField(null=True) #verificar blank
    register_status = models.BooleanField(default=False) #verificar redundancia com is_active
    psw_temp = models.BooleanField(default=False) #verificar necessidade deste campo

    is_active = models.BooleanField(default=True) #verificar redundancia com register_status
    is_admin = models.BooleanField(default=False) #verificar necessidade deste campo

    objects = hdsysUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

class hdsysAddress (models.Model):
    user = models.OneToOneField(hdsysUser, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=200, blank=True, null=True) #verificar tamanho do campo
    number = models.CharField(max_length=10, blank=True, null=True) #verificar tamanho do campo
    complement = models.CharField(max_length=50, blank=True, null=True) #verificar tamanho do campo
    neighborhood = models.CharField(max_length=50, blank=True, null=True) #verificar tamanho do campo
    city = models.CharField(max_length=50, blank=True, null=True) #verificar tamanho do campo
    #state = models.CharField(max_length=50, blank=True, null=True) #verificar tamanho do campo
    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    state = models.CharField(max_length=10,
                  choices=STATE_CHOICES,
                  blank=True, null=True,
    )

    #country = models.CharField(max_length=50, blank=True, null=True) #verificar tamanho do campo
    COUNTRY_CHOICES = (
        ('AD', 'Andorra'),
        ('AE', 'Emirados Árabes Unidos'),
        ('AF', 'Afeganistão'),
        ('AG', 'Antígua e Barbuda'),
        ('AI', 'Anguilla'),
        ('AL', 'Albânia'),
        ('AM', 'Armênia'),
        ('AO', 'Angola'),
        ('AQ', 'Antártica'),
        ('AR', 'Argentina'),
        ('AS', 'Samoa Americana'),
        ('AT', 'Áustria'),
        ('AU', 'Austrália'),
        ('AW', 'Aruba'),
        ('AZ', 'Azerbaijão'),
        ('BA', 'Bósnia e Herzegovina'),
        ('BB', 'Barbados'),
        ('BD', 'Bangladesh'),
        ('BE', 'Bélgica'),
        ('BF', 'Burkina Faso'),
        ('BG', 'Bulgária'),
        ('BH', 'Barém'),
        ('BI', 'Burundi'),
        ('BJ', 'Benin'),
        ('BL', 'São Bartolomeu'),
        ('BM', 'Bermuda'),
        ('BN', 'Brunei'),
        ('BO', 'Bolívia'),
        ('BR', 'Brasil'),
        ('BS', 'Bahamas'),
        ('BT', 'Butão'),
        ('BV', 'Ilha Bouvet'),
        ('BW', 'Botswana'),
        ('BY', 'Belarus'),
        ('BZ', 'Belize'),
        ('CA', 'Canadá'),
        ('CC', 'Ilhas Cocos (Keeling)'),
        ('CD', 'Congo, República Democrática do'),
        ('CF', 'República Centro-Africana'),
        ('CG', 'Congo, República do'),
        ('CH', 'Suíça'),
        ('CI', 'Costa do Marfim'),
        ('CK', 'Ilhas Cook'),
        ('CL', 'Chile'),
        ('CM', 'Camarões'),
        ('CN', 'China'),
        ('CO', 'Colômbia'),
        ('CR', 'Costa Rica'),
        ('CU', 'Cuba'),
        ('CV', 'Cabo Verde'),
        ('CW', 'Curaçao'),
        ('CX', 'Ilha Christmas'),
        ('CY', 'Chipre'),
        ('CZ', 'República Tcheca'),
        ('DE', 'Alemanha'),
        ('DJ', 'Djibuti'),
        ('DK', 'Dinamarca'),
        ('DM', 'Dominica'),
        ('DO', 'República Dominicana'),
        ('DZ', 'Argélia'),
        ('EC', 'Equador'),
        ('EE', 'Estônia'),
        ('EG', 'Egito'),
        ('EH', 'Saara Ocidental'),
        ('ER', 'Eritréia'),
        ('ES', 'Espanha'),
        ('ET', 'Etiópia'),
        ('FI', 'Finlândia'),
        ('FJ', 'Fiji'),
        ('FK', 'Ilhas Falkland (Malvinas)'),
        ('FM', 'Micronésia, Estados Federados da'),
        ('FO', 'Ilhas Feroe'),
        ('FR', 'França'),
        ('FX', 'França Metropolitana'),
        ('GA', 'Gabão'),
        ('GB', 'Reino Unido'),
        ('GD', 'Grenada'),
        ('GE', 'Geórgia'),
        ('GF', 'Guiana Francesa'),
        ('GG', 'Guernsey'),
        ('GH', 'Gana'),
        ('GI', 'Gibraltar'),
        ('GL', 'Greenland'),
        ('GM', 'Gâmbia'),
        ('GN', 'Guiné'),
        ('GP', 'Guadelupe'),
        ('GQ', 'Guiné Equatorial'),
        ('GR', 'Grécia'),
        ('GS', 'Geórgia do Sul e Ilhas'),
        ('GT', 'Guatemala'),
        ('GU', 'Guam'),
        ('GW', 'Guiné-Bissau'),
        ('GY', 'Guiana'),
        ('HK', 'Hong Kong'),
        ('HM', 'Ilhas Heard and McDonald'),
        ('HN', 'Honduras'),
        ('HR', 'Croácia'),
        ('HT', 'Haiti'),
        ('HU', 'Hungria'),
        ('ID', 'Indonésia'),
        ('IE', 'Irlanda'),
        ('IL', 'Israel'),
        ('IM', 'Ilha de Man'),
        ('IN', 'Índia'),
        ('IO', 'Território Britânico do Oceano Índico'),
        ('IQ', 'Iraque'),
        ('IR', 'Irã'),
        ('IS', 'Islândia'),
        ('IT', 'Itália'),
        ('JE', 'Jersey'),
        ('JM', 'Jamaica'),
        ('JO', 'Jordânia'),
        ('JP', 'Japão'),
        ('KE', 'Quênia'),
        ('KG', 'Quirguistão'),
        ('KH', 'Camboja'),
        ('KI', 'Kiribati'),
        ('KM', 'Cômoros'),
        ('KN', 'São Cristóvão e Nevis'),
        ('KP', 'Coreia do Norte'),
        ('KR', 'Coreia do Sul'),
        ('KW', 'Kuwait'),
        ('KY', 'Ilhas Caiman'),
        ('KZ', 'Cazaquistão'),
        ('LA', 'Laos'),
        ('LB', 'Líbano'),
        ('LC', 'Santa Lúcia'),
        ('LI', 'Liechtenstein'),
        ('LK', 'Sri Lanka'),
        ('LR', 'Libéria'),
        ('LS', 'Lesoto'),
        ('LT', 'Lituânia'),
        ('LU', 'Luxemburgo'),
        ('LV', 'Letônia'),
        ('LY', 'Líbia'),
        ('MA', 'Marrocos'),
        ('MC', 'Mônaco'),
        ('MD', 'Moldova'),
        ('ME', 'Montenegro'),
        ('MF', 'Saint Martin'),
        ('MG', 'Madagascar'),
        ('MH', 'Ilhas Marshall'),
        ('MK', 'Macedônia'),
        ('ML', 'Mali'),
        ('MM', 'Birmânia'),
        ('MN', 'Mongólia'),
        ('MO', 'Macao'),
        ('MP', 'Ilhas Marianas do Norte'),
        ('MQ', 'Martinica'),
        ('MR', 'Mauritânia'),
        ('MS', 'Montserrat'),
        ('MT', 'Malta'),
        ('MU', 'Ilhas Maurício'),
        ('MV', 'Maldivas'),
        ('MW', 'Malawi'),
        ('MX', 'México'),
        ('MY', 'Malásia'),
        ('MZ', 'Moçambique'),
        ('NA', 'Namíbia'),
        ('NC', 'Nova Caledônia'),
        ('NE', 'Níger'),
        ('NF', 'Ilha Norfolk'),
        ('NG', 'Nigéria'),
        ('NI', 'Nicarágua'),
        ('NL', 'Holanda'),
        ('NO', 'Noruega'),
        ('NP', 'Nepal'),
        ('NR', 'Nauru'),
        ('NU', 'Niue'),
        ('NZ', 'Nova Zelândia'),
        ('OM', 'Omã'),
        ('PA', 'Panamá'),
        ('PE', 'Peru'),
        ('PF', 'Polinésia Francesa'),
        ('PG', 'Papua Nova Guiné'),
        ('PH', 'Filipinas'),
        ('PK', 'Paquistão'),
        ('PL', 'Polônia'),
        ('PM', 'Saint Pierre e Miquelon'),
        ('PN', 'Ilhas Pitcairn'),
        ('PR', 'Porto Rico'),
        ('PS', 'Faixa de Gaza'),
        ('PS', 'Cisjordânia'),
        ('PT', 'Portugal'),
        ('PW', 'Palau'),
        ('PY', 'Paraguai'),
        ('QA', 'Qatar'),
        ('RE', 'Reunião'),
        ('RO', 'Romênia'),
        ('RS', 'Sérvia'),
        ('RU', 'Rússia'),
        ('RW', 'Ruanda'),
        ('SA', 'Arábia Saudita'),
        ('SB', 'Ilhas Salomão'),
        ('SC', 'Seicheles'),
        ('SD', 'Sudão'),
        ('SE', 'Suécia'),
        ('SG', 'Cingapura'),
        ('SH', 'Santa Helena, Ascensão e Tristão da Cunha'),
        ('SI', 'Eslovênia'),
        ('SJ', 'Svalbard'),
        ('SK', 'Eslováquia'),
        ('SL', 'Serra Leoa'),
        ('SM', 'San Marino'),
        ('SN', 'Senegal'),
        ('SO', 'Somália'),
        ('SR', 'Suriname'),
        ('SS', 'Sudão do Sul'),
        ('ST', 'São Tomé e Príncipe'),
        ('SV', 'El Salvador'),
        ('SX', 'São Martinho'),
        ('SY', 'Síria'),
        ('SZ', 'Suazilândia'),
        ('TC', 'Ilhas Turks e Caicos'),
        ('TD', 'Chad'),
        ('TF', 'Sul da França e Antártica'),
        ('TG', 'Togo'),
        ('TH', 'Tailândia'),
        ('TJ', 'Tadjiquistão'),
        ('TK', 'Toquelau'),
        ('TL', 'Timor-Leste'),
        ('TM', 'Turcomenistão'),
        ('TN', 'Tunísia'),
        ('TO', 'Tonga'),
        ('TR', 'Turquia'),
        ('TT', 'Trinidad e Tobago'),
        ('TV', 'Tuvalu'),
        ('TW', 'Taiwan'),
        ('TZ', 'Tanzânia'),
        ('UA', 'Ucrânia'),
        ('UG', 'Uganda'),
        ('UM', 'Ilhas Menores Distantes dos Estados Unidos'),
        ('US', 'Estados Unidos'),
        ('UY', 'Uruguai'),
        ('UZ', 'Uzbequistão'),
        ('VA', 'Santa Sé (Cidade do Vaticano)'),
        ('VC', 'São Vicente e Granadinas'),
        ('VE', 'Venezuela'),
        ('VG', 'Ilhas Virgens Britânicas'),
        ('VI', 'Ilhas Virgens Americanas'),
        ('VN', 'Vietnã'),
        ('VU', 'Vanuatu'),
        ('WF', 'Ilhas Wallis e Futuna'),
        ('WS', 'Samoa'),
        ('XK', 'Kosovo'),
        ('YE', 'Iêmen'),
        ('YT', 'Maiote'),
        ('ZA', 'África do Sul'),
        ('ZM', 'Zâmbia'),
        ('ZW', 'Zimbábue'),
    )
    country = models.CharField(max_length=50,
                  choices=COUNTRY_CHOICES,
                  blank=True, null=True,
    )

    zipcode = models.CharField(max_length=9, blank=True, null=True) #verificar tamanho do campo e necessidade do traço
    position = GeopositionField(blank=True, null=True) #TESTE API GOOGLE MAPS

    def __str__(self):
        return self.user.username

class hdsysAdministrator (models.Model):
    user = models.OneToOneField(hdsysUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class hdsysManager (models.Model):
    user = models.OneToOneField(hdsysUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class hdsysProfessional (models.Model):
    user = models.OneToOneField(hdsysUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.fullname

class hdsysPatient (models.Model):
    user = models.OneToOneField(hdsysUser, on_delete=models.CASCADE, primary_key=True)
    professional = models.ForeignKey(hdsysProfessional, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    PLAN_CHOICES = (
        ('SUS', 'SUS'),
        ('PLAN', 'Plano'),
        ('PARTICULAR', 'Particular'),
    )
    plan = models.CharField(max_length=10,
                  choices=PLAN_CHOICES,
    )
    SEX_CHOICES = (
        ('MALE', 'Masculino'),
        ('FEMALE', 'Feminino'),
    )
    sex = models.CharField(max_length=6,
                  choices=SEX_CHOICES,
    )
    ETHNICITY_CHOICES = (
        ('WHITE', 'Branco'),
        ('BROWN', 'Pardo'),
        ('BLACK', 'Preto'),
        ('YELLOW', 'Amarelo'),
        ('INDIGENOUS', 'Indígena'),
    )
    ethnicity = models.CharField(max_length=10,
                  choices=ETHNICITY_CHOICES,
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(0.10),
                                       MaxValueValidator(300.00)])
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, validators=[MinValueValidator(0.10),
                                       MaxValueValidator(3.00)])

    def __str__(self):
        return self.user.username

class hdsysLogin (models.Model):
    user = models.ForeignKey(hdsysUser, on_delete=models.CASCADE)
    login_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.pk)

class hdsysLogout (models.Model):
    user = models.ForeignKey(hdsysUser, on_delete=models.CASCADE)
    logout_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.pk)

class hdsysPrivateMeasure (models.Model):
    patient = models.ForeignKey(hdsysPatient, on_delete=models.CASCADE)
    measure_author = models.ForeignKey(hdsysUser, on_delete=models.CASCADE)
    insertion_date = models.DateTimeField(blank=False, null=False)
    measure_date = models.DateTimeField(blank=False, null=False, help_text='Exemplo: 25/10/2016 21:45:00')
    heart_rate = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(200)])
    max_pressure = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(300)])
    min_pressure = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(200)])
    glucose = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(500)])

    def __str__(self):
        return str(self.pk)

class hdsysPublicMeasure (models.Model):
    measure = models.OneToOneField(hdsysPrivateMeasure, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.pk)

class hdsysEditMeasure (models.Model):
    measure = models.ForeignKey(hdsysPrivateMeasure, on_delete=models.CASCADE)
    edit_author = models.ForeignKey(hdsysUser, on_delete=models.CASCADE)
    edit_date = models.DateTimeField(blank=False, null=False)
    previous_measure_date = models.DateTimeField(blank=False, null=False)
    previous_heart_rate = models.PositiveIntegerField(blank=True, null=True)
    previous_max_pressure = models.PositiveIntegerField(blank=True, null=True)
    previous_min_pressure = models.PositiveIntegerField(blank=True, null=True)
    previous_glucose = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class hdsysDeleteMeasure (models.Model):
    measure = models.OneToOneField(hdsysPrivateMeasure, on_delete=models.CASCADE, primary_key=True)
    delete_author = models.ForeignKey(hdsysUser, on_delete=models.CASCADE)
    delete_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.pk)
