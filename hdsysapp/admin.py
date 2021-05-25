from django.contrib import admin
from .models import hdsysUser, hdsysAddress, hdsysAdministrator, hdsysManager, hdsysProfessional, hdsysPatient, hdsysLogin, hdsysLogout, hdsysPrivateMeasure, hdsysPublicMeasure, hdsysEditMeasure, hdsysDeleteMeasure

admin.site.register(hdsysUser)
admin.site.register(hdsysAddress)
admin.site.register(hdsysAdministrator)
admin.site.register(hdsysManager)
admin.site.register(hdsysProfessional)
admin.site.register(hdsysPatient)
admin.site.register(hdsysLogin)
admin.site.register(hdsysLogout)
admin.site.register(hdsysPrivateMeasure)
admin.site.register(hdsysPublicMeasure)
admin.site.register(hdsysEditMeasure)
admin.site.register(hdsysDeleteMeasure)
