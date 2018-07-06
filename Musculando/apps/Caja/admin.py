from django.contrib import admin
from apps.Caja.models import tb_ingreso_mensualidad
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingresos

# Register your models here.

admin.site.register(tb_ingreso_mensualidad)
admin.site.register(tb_egreso)
admin.site.register(tb_ingresos)