from django.contrib import admin
from apps.Configuracion.models import tb_plan
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoColaborador
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoIngreso
# Register your models here.

admin.site.register(tb_plan)
admin.site.register(tb_formasDePago)
admin.site.register(tb_tipoColaborador)
admin.site.register(tb_tipoEgreso)
admin.site.register(tb_tipoIngreso)