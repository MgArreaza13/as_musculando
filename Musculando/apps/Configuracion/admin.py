from django.contrib import admin
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_formasDePago
# Register your models here.

admin.site.register(tb_plan)
admin.site.register(tb_formasDePago)