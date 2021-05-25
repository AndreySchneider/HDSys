# -*- coding: utf-8 -*-
#Python 2.7################################################

from django import forms
from .models import hdsysProfessional, hdsysPatient, hdsysUser, hdsysPrivateMeasure, hdsysAddress
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class hdsysProfessionalForm(forms.ModelForm):
    class Meta:
        model = hdsysProfessional
        fields = ('user',)
        labels = {
            'user': 'Profissional',
        }

class hdsysPatientForm(forms.ModelForm):
    class Meta:
        model = hdsysPatient
        fields = ('professional', 'birth_date', 'plan', 'sex', 'ethnicity', 'weight', 'height',)
        labels = {
            'professional': 'Profissional',
            'birth_date': 'Data de Nascimento',
            'plan': 'Convênio',
            'sex': 'Sexo',
            'ethnicity': 'Etnia',
            'weight': 'Peso',
            'height': 'Altura',
        }

class hdsysUserForm(UserCreationForm):    
    class Meta:
        model = hdsysUser
        fields = ('username', 'fullname', 'email', 'password1', 'password2', 'cpf', 'rg',)
        labels = {
            'username': 'Nome de usuário',
            'fullname': 'Nome Completo',
            'email': 'E-mail',
            'cpf': 'CPF',
            'rg': 'RG',
        }

class hdsysAddressForm(forms.ModelForm):
    class Meta:
        model = hdsysAddress
        fields = ('street', 'number', 'complement', 'neighborhood', 'city', 'state', 'country', 'zipcode',)# 'position',)
        labels = {
            'street': 'Logradouro',
            'number': 'Número',
            'complement': 'Complemento',
            'neighborhood': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado',
            'country': 'País',
            'zipcode': 'CEP',
            #'position': 'Geolocalização',
        }

class hdsysMeasureForm(forms.ModelForm):
    class Meta:
        model = hdsysPrivateMeasure
        fields = ('measure_date', 'glucose', 'heart_rate', 'max_pressure', 'min_pressure',)
        labels = {
            'measure_date': 'Data e hora da medida',
            'glucose': 'Glicose',
            'heart_rate': 'Batimentos cardíacos',
            'max_pressure': 'Pressão máxima (Sistólica)',
            'min_pressure': 'Pressão mínima (Diastólica)',
        }

class hdsysEditUserForm(forms.ModelForm):
    class Meta:
        model = hdsysUser
        fields = ('username', 'fullname', 'email', 'cpf', 'rg',)
        labels = {
            'username': 'Nome de usuário',
            'fullname': 'Nome Completo',
            'email': 'E-mail',
            'cpf': 'CPF',
            'rg': 'RG',
        }

class hdsysGeoPositionForm(forms.ModelForm):
    class Meta:
        model = hdsysAddress
        fields = ('position',)
        labels = {
            'position': 'Geolocalização',
        }
