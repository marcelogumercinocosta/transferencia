from django.contrib import admin
from apps.core.models import Antena, Satelite, Sensor, Servidor, Passagem
from apps.core.forms import SensorInLineForm

class SensorInLine(admin.TabularInline):
    model = Sensor
    fields = ["sensor"]
    extra = 0

    def has_add_permission(self, request, obj=None):
        return True

@admin.register(Satelite)
class SateliteAdmin(admin.ModelAdmin):
    search_fields = [ "satelite"]
    list_display = ["satelite"]
    inlines = [SensorInLine]

@admin.register(Antena)
class AntenaAdmin(admin.ModelAdmin):
    search_fields = [ "antena"]
    list_display = ["antena", "metragem", "local"]
    list_filter = ["local"]

@admin.register(Passagem)
class PassagemAdmin(admin.ModelAdmin):
    search_fields = [ "servidor"]
    list_display = ["antena", "servidor","sensor", "inicio", "fim","qt_passagem"]
    list_filter = ["servidor"]
    readonly_fields = ["qt_passagem", "qt_arquivos"]

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    search_fields = [ "servidor"]
    list_display = ["servidor", "montagem"]
