from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_professional$', views.new_professional, name='new_professional'),
    url(r'^new_patient$', views.new_patient, name='new_patient'),
    url(r'^new_user$', views.new_user, name='new_user'),
    url(r'^new_measure$', views.new_measure, name='new_measure'),
    url(r'^new_measure/(?P<pk>[0-9]+)/$', views.new_measure, name='new_measure'),
    url(r'^list_measures$', views.list_measures, name='list_measures'),
    url(r'^list_measures/(?P<pk>[0-9]+)/$', views.list_measures, name='list_measures'),
    url(r'^list_patients$', views.list_patients, name='list_patients'),
    url(r'^list_professionals$', views.list_professionals, name='list_professionals'),
    url(r'^list_managers$', views.list_managers, name='list_managers'),
    url(r'^activate_patients$', views.activate_patients, name='activate_patients'),
    url(r'^patient_details/(?P<pk>[0-9]+)/$', views.patient_details, name='patient_details'),
    url(r'^activate_user/(?P<pk>[0-9]+)/$', views.activate_user, name='activate_user'),
    url(r'^delete_user/(?P<pk>[0-9]+)/$', views.delete_user, name='delete_user'),
    url(r'^activate_professionals$', views.activate_professionals, name='activate_professionals'),
    url(r'^professional_details/(?P<pk>[0-9]+)/$', views.professional_details, name='professional_details'),
    url(r'^manager_details/(?P<pk>[0-9]+)/$', views.manager_details, name='manager_details'),
    url(r'^activate_user_professional/(?P<pk>[0-9]+)/$', views.activate_user_professional, name='activate_user_professional'),
    url(r'^delete_user_professional/(?P<pk>[0-9]+)/$', views.delete_user_professional, name='delete_user_professional'),
    url(r'^delete_measure/(?P<pk>[0-9]+)/$', views.delete_measure, name='delete_measure'),
    url(r'^edit_measure/(?P<pk>[0-9]+)/$', views.edit_measure, name='edit_measure'),
    url(r'^edit_user$', views.edit_user, name='edit_user'),
    url(r'^delete_register$', views.delete_register, name='delete_register'),
    url(r'^change_password$', views.change_password, name='change_password'),
    url(r'^terms_of_use$', views.terms_of_use, name='terms_of_use'),

    url(r'^reset/password_reset/$', password_reset, {'template_name': 'hdsysapp/password_reset_form.html'}, name='password_reset'),
    url(r'^reset/password_reset/done$', password_reset_done, {'template_name': 'hdsysapp/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'hdsysapp/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, {'template_name': 'hdsysapp/password_reset_complete.html'}, name='password_reset_complete'),
]
