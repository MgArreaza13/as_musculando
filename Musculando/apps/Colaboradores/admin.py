from django.contrib import admin
from apps.Colaboradores.models import tb_colaboradores
from apps.Colaboradores.models import tb_cuentaColaborador
from apps.Colaboradores.models import tb_EntradaSalida

# Register your models here.


admin.site.register(tb_colaboradores)
admin.site.register(tb_cuentaColaborador)
admin.site.register(tb_EntradaSalida)