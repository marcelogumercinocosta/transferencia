from django.contrib import admin
from apps.core.models import Antena, Satelite, Servidor, Passagem

admin.site.register(Satelite)

@admin.register(Antena)
class AntenaAdmin(admin.ModelAdmin):
    search_fields = [ "antena"]
    list_display = ["antena", "metragem", "local"]
    list_filter = ["local"]

@admin.register(Passagem)
class PassagemAdmin(admin.ModelAdmin):
    search_fields = [ "servidor"]
    list_display = ["antena", "servidor","inicio", "fim","qt_passagem"]
    list_filter = ["servidor"]
    readonly_fields = ("qt_passagem", "qt_arquivos", )

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    search_fields = [ "servidor"]
    list_display = ["servidor", "montagem","satelite"]
    list_filter = ("satelite",)
