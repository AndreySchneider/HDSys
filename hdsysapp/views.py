# -*- coding: utf-8 -*-
#Python 2.7################################################

from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from operator import attrgetter
from .forms import hdsysProfessionalForm, hdsysPatientForm, hdsysUserForm, hdsysMeasureForm, hdsysEditUserForm, hdsysGeoPositionForm, hdsysAddressForm
from .models import *
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

@login_required
def home(request):
    patient = hdsysPatient.objects.filter(user=request.user)
    if patient:
        is_patient = True
    else:
        is_patient = False

    professional = hdsysProfessional.objects.filter(user=request.user)
    if professional:
        is_professional = True
    else:
        is_professional = False

    manager = hdsysManager.objects.filter(user=request.user)
    if manager:
        is_manager = True
    else:
        is_manager = False

    return render(request, 'hdsysapp/home.html', {'is_patient': is_patient, 'is_professional': is_professional, 'is_manager': is_manager})

def new_professional(request):
    if request.method == 'POST':
        form1 = hdsysUserForm(request.POST)
        form2 = hdsysAddressForm(request.POST)
        if (form1.is_valid() and form2.is_valid()):
            prof = form1.save(commit=False)
            prof.register_date = timezone.now()
            prof.register_status = False
            prof.is_active = False
            prof.is_admin = False
            prof.psw_temp = False
            prof.save()

            hdsysProfessional.objects.create(user=prof)

            address = form2.save(commit=False)
            address.user = prof

            address.save()
            return redirect('home')
    else:
        form1 = hdsysUserForm()
        form2 = hdsysAddressForm()
    return render(request, 'hdsysapp/new_professional.html', {'form1': form1, 'form2': form2})


def new_patient(request):
    if request.method == "POST":
        form1 = hdsysUserForm(request.POST)
        form2 = hdsysAddressForm(request.POST)
        form3 = hdsysPatientForm(request.POST)
        if (form1.is_valid() and form2.is_valid() and form3.is_valid()):
            usr = form1.save(commit=False)
            usr.register_date = timezone.now()
            usr.register_status = False
            usr.is_active = False
            usr.is_admin = False
            usr.psw_temp = False
            usr.save()

            address = form2.save(commit=False)
            address.user = usr
            address.save()

            patient = form3.save(commit=False)
            patient.user = usr
            patient.save()
            return redirect('home')
    else:
        form1 = hdsysUserForm()
        form2 = hdsysAddressForm()
        form3 = hdsysPatientForm()
    return render(request, 'hdsysapp/new_patient.html', {'form1': form1, 'form2': form2, 'form3': form3})

@login_required
def edit_user(request):
    instance1 = request.user
    instance2 = hdsysAddress.objects.get(user=request.user)
    try:
        instance3 = hdsysPatient.objects.get(user=request.user)

        if request.method == "POST":
            form1 = hdsysEditUserForm(request.POST, instance=instance1)
            form2 = hdsysAddressForm(request.POST, instance=instance2)
            form3 = hdsysPatientForm(request.POST, instance=instance3)
            if (form1.is_valid() and form2.is_valid() and form3.is_valid()):
                usr = form1.save(commit=False)
                usr.register_date = request.user.register_date
                usr.register_status = request.user.register_status
                usr.is_active = request.user.is_active
                usr.is_admin = request.user.is_admin
                usr.psw_temp = request.user.psw_temp
                usr.save()

                address = form2.save(commit=False)
                address.user = usr
                address.save()

                patient = form3.save(commit=False)
                patient.user = usr
                patient.save()

                return redirect('home')
        else:
            form1 = hdsysEditUserForm(instance=instance1)
            form2 = hdsysAddressForm(instance=instance2)
            form3 = hdsysPatientForm(instance=instance3)
        return render(request, 'hdsysapp/edit_user.html', {'form1': form1, 'form2': form2, 'form3': form3})

    except:
        if request.method == "POST":
            form1 = hdsysEditUserForm(request.POST, instance=instance1)
            form2 = hdsysAddressForm(request.POST, instance=instance2)
            if (form1.is_valid() and form2.is_valid()):
                usr = form1.save(commit=False)
                usr.register_date = request.user.register_date
                usr.register_status = request.user.register_status
                usr.is_active = request.user.is_active
                usr.is_admin = request.user.is_admin
                usr.psw_temp = request.user.psw_temp
                usr.save()

                address = form2.save(commit=False)
                address.user = usr
                address.save()

                return redirect('home')
        else:
            form1 = hdsysEditUserForm(instance=instance1)
            form2 = hdsysAddressForm(instance=instance2)
        return render(request, 'hdsysapp/edit_user.html', {'form1': form1, 'form2': form2})

@login_required
def new_user(request):
    if request.method == 'POST':
        if request.user.is_admin:
            form1 = hdsysUserForm(request.POST)
            form2 = hdsysAddressForm(request.POST)
            if (form1.is_valid() and form2.is_valid()):
                manager = form1.save(commit=False)
                manager.register_date = timezone.now()
                manager.register_status = True
                manager.is_active = True
                manager.is_admin = False
                manager.psw_temp = False
                manager.save()

                hdsysManager.objects.create(user=manager)

                address = form2.save(commit=False)
                address.user = manager
                address.save()

                return redirect('home')
        else:
            return redirect('home')
    else:
        if request.user.is_admin:
            form1 = hdsysUserForm()
            form2 = hdsysAddressForm()
            return render(request, 'hdsysapp/new_user.html', {'form1': form1, 'form2': form2})
        else:
            return redirect('home')
    return render(request, 'hdsysapp/new_user.html', {'form1': form1, 'form2': form2})

@login_required
def new_measure(request, pk=None):
    if pk:
        patient = get_object_or_404(hdsysPatient, Q(pk=pk), Q(user=request.user) | Q(professional__user=request.user))
    else:
        patient = get_object_or_404(hdsysPatient, Q(user=request.user))

    if request.method == 'POST':
        form = hdsysMeasureForm(request.POST)
        if form.is_valid():
            measure = form.save(commit=False)
            measure.patient = patient
            measure.measure_author = request.user
            measure.insertion_date = timezone.now()
            measure.save()
            hdsysPublicMeasure.objects.create(measure=measure)
            if (measure.glucose and (measure.glucose>125 or measure.glucose<50) or
                measure.heart_rate and (measure.heart_rate>150 or measure.heart_rate<40) or
                measure.min_pressure and (measure.min_pressure>100 or measure.min_pressure<50) or
                measure.max_pressure and (measure.max_pressure>160 or measure.max_pressure<80)):
                return render(request, 'hdsysapp/measure_alarm.html', {'measure': measure, 'patient': patient})
            else:
                return redirect('list_measures', patient.pk)
    else:
        form = hdsysMeasureForm()
        return render(request, 'hdsysapp/new_measure.html', {'form': form})
    return render(request, 'hdsysapp/new_measure.html', {'form': form})

@login_required
def list_measures(request, pk=None):
    try:
        patient = hdsysPatient.objects.get(user=request.user)
        measures = hdsysPrivateMeasure.objects.filter(hdsyspublicmeasure__measure__patient__user=request.user).order_by('measure_date')
        return render(request, 'hdsysapp/list_measures.html', {'measures': measures, 'patient': patient})
    except:
        professional = hdsysProfessional.objects.filter(user=request.user)
        if professional and pk is not None:
            try:
                patient = hdsysPatient.objects.get(pk=pk)
            except:
                return redirect('home')
            if patient.professional.user == request.user:
                measures = hdsysPrivateMeasure.objects.filter(hdsyspublicmeasure__measure__patient__pk=pk).order_by('measure_date')
                return render(request, 'hdsysapp/list_measures.html', {'measures': measures, 'patient': patient})
            else:
                return redirect('home')
        else:
            return redirect('home')

@login_required
def list_patients(request):
    try:
        professional = hdsysProfessional.objects.get(user=request.user)
        patients = hdsysPatient.objects.filter(professional__user=request.user, user__is_active=True).order_by('user__username')
        return render(request, 'hdsysapp/list_patients.html', {'patients': patients})
    except:
        return redirect('home')

@login_required
def list_professionals(request):
    try:
        manager = hdsysManager.objects.get(user=request.user)
        professionals = hdsysProfessional.objects.filter(user__is_active=True).order_by('user__username')
        return render(request, 'hdsysapp/list_professionals.html', {'professionals': professionals})
    except:
        return redirect('home')

@login_required
def list_managers(request):
    if request.user.is_admin:
        managers = hdsysManager.objects.filter(user__is_active=True).order_by('user__username')
        return render(request, 'hdsysapp/list_managers.html', {'managers': managers})
    else:
        return redirect('home')

@login_required
def activate_patients(request):
    try:
        professional = hdsysProfessional.objects.get(user=request.user)
        patients = hdsysPatient.objects.filter(professional__user=request.user, user__is_active=False).order_by('user__username')
        
        return render(request, 'hdsysapp/list_activate_patients.html', {'patients': patients})
    except:
        return redirect('home')

@login_required
def patient_details(request, pk):
    try:
        patient = hdsysPatient.objects.get(pk=pk)
        address = hdsysAddress.objects.get(pk=pk)
        #form = hdsysGeoPositionForm(instance=address)
        if patient.professional.user == request.user:
            return render(request, 'hdsysapp/patient_details.html', {'patient': patient, 'address': address})# 'form': form})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def activate_user(request, pk):
    try:
        patient = hdsysPatient.objects.get(pk=pk)
        if patient.professional.user == request.user:
            patient.user.is_active = True
            patient.user.save()
            patients = hdsysPatient.objects.filter(professional__user=request.user, user__is_active=False).order_by('user__username')
            return render(request, 'hdsysapp/list_activate_patients.html', {'patients': patients})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def delete_user(request, pk):
    try:
        patient = hdsysPatient.objects.get(pk=pk)
        if patient.professional.user == request.user:
            patient.user.delete()
            patients = hdsysPatient.objects.filter(professional__user=request.user, user__is_active=False).order_by('user__username')
            return render(request, 'hdsysapp/list_activate_patients.html', {'patients': patients})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def activate_professionals(request):
    try:
        manager = hdsysManager.objects.get(user=request.user)
        professionals = hdsysProfessional.objects.filter(user__is_active=False).order_by('user__username')
        
        return render(request, 'hdsysapp/list_activate_professionals.html', {'professionals': professionals})
    except:
        return redirect('home')

@login_required
def professional_details(request, pk):
    try:
        professional = hdsysProfessional.objects.get(pk=pk)
        address = hdsysAddress.objects.get(pk=pk)
        #form = hdsysGeoPositionForm(instance=address)
        if hdsysManager.objects.filter(user=request.user):
            return render(request, 'hdsysapp/professional_details.html', {'professional': professional, 'address': address})#, 'form': form})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def manager_details(request, pk):
    try:
        manager = hdsysManager.objects.get(pk=pk)
        address = hdsysAddress.objects.get(pk=pk)
        #form = hdsysGeoPositionForm(instance=address)
        if request.user.is_admin:
            return render(request, 'hdsysapp/manager_details.html', {'manager': manager, 'address': address})#, 'form': form})
        else:
            return redirect('home')
    except:
        return redirect('home')

@login_required
def activate_user_professional(request, pk):
    try:
        professional = hdsysProfessional.objects.get(pk=pk)
        if hdsysManager.objects.filter(user=request.user):
            professional.user.is_active = True
            professional.user.save()
            professionals = hdsysProfessional.objects.filter(user__is_active=False).order_by('user__username')
            return render(request, 'hdsysapp/list_activate_professionals.html', {'professionals': professionals})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def delete_user_professional(request, pk):
    try:
        professional = hdsysProfessional.objects.get(pk=pk)
        if hdsysManager.objects.filter(user=request.user):
            professional.user.delete()
            professionals = hdsysProfessional.objects.filter(user__is_active=False).order_by('user__username')
            return render(request, 'hdsysapp/list_activate_professionals.html', {'professionals': professionals})
        else:
            return redirect('home')    
    except:
        return redirect('home')

@login_required
def delete_measure(request, pk):
    publicMeasure = get_object_or_404(hdsysPublicMeasure, Q(pk=pk), Q(measure__patient__user=request.user) | Q(measure__patient__professional__user=request.user))
    hdsysDeleteMeasure.objects.create(measure=publicMeasure.measure, delete_author=request.user, delete_date=timezone.now())
    publicMeasure.delete()
    patient = hdsysPatient.objects.get(hdsysprivatemeasure__pk=pk)
    return redirect('list_measures', patient.pk)
    
@login_required
def edit_measure(request, pk):
    old_measure = get_object_or_404(hdsysPrivateMeasure, Q(pk=pk), Q(patient__user=request.user) | Q(patient__professional__user=request.user))
    measure_instance = get_object_or_404(hdsysPrivateMeasure, Q(pk=pk), Q(patient__user=request.user) | Q(patient__professional__user=request.user)) #redundante mas necessário para separar a instância atual da medida antiga
    if request.method == 'POST':
        form = hdsysMeasureForm(request.POST, instance=measure_instance)
        if form.is_valid():
            hdsysEditMeasure.objects.create(
                measure=old_measure,
                edit_author=request.user,
                edit_date=timezone.now(),
                previous_measure_date=old_measure.measure_date,
                previous_heart_rate=old_measure.heart_rate,
                previous_max_pressure=old_measure.max_pressure,
                previous_min_pressure=old_measure.min_pressure,
                previous_glucose=old_measure.glucose,
                )
            measure = form.save(commit=False)
            measure.patient = hdsysPatient.objects.get(Q(hdsysprivatemeasure__pk=pk), Q(user=request.user) | Q(professional__user=request.user))
            measure.measure_author = request.user
            measure.insertion_date = timezone.now()
            measure.save()
            patient = hdsysPatient.objects.get(hdsysprivatemeasure__pk=pk)
            if (measure.glucose and (measure.glucose>125 or measure.glucose<50) or
                measure.heart_rate and (measure.heart_rate>150 or measure.heart_rate<40) or
                measure.min_pressure and (measure.min_pressure>100 or measure.min_pressure<50) or
                measure.max_pressure and (measure.max_pressure>160 or measure.max_pressure<80)):
                return render(request, 'hdsysapp/measure_alarm.html', {'measure': measure, 'patient': patient})
            else:
                return redirect('list_measures', patient.pk)
    else:
        publicMeasure = get_object_or_404(hdsysPublicMeasure, Q(pk=pk), Q(measure__patient__user=request.user) | Q(measure__patient__professional__user=request.user))
        form = hdsysMeasureForm(instance=measure_instance)
    return render(request, 'hdsysapp/new_measure.html', {'form': form})

@login_required
def delete_register(request):
    if request.method == 'POST':
        if hdsysProfessional.objects.filter(Q(user=request.user), Q(hdsyspatient__professional__user=request.user)) or request.user.is_admin: 
            return render(request, 'hdsysapp/failure_delete_register.html', {})
        else:
            try:
                request.user.delete()
                Session.objects.all().delete()
                return redirect('home')
            except:
                return redirect('home')
    else:
        return render(request, 'hdsysapp/confirm_delete_register.html', {})

@login_required
def change_password(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    return render(request, 'hdsysapp/change_password.html', {'form': form})

def error_404(request):
    return render(request, 'hdsysapp/404.html', {})

def error_500(request):
    return render(request, 'hdsysapp/500.html', {})

def error_403(request):
    return render(request, 'hdsysapp/403.html', {})

def error_400(request):
    return render(request, 'hdsysapp/400.html', {})

def terms_of_use(request):
    return render(request, 'hdsysapp/terms_of_use.html', {})
