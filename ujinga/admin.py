from models import *
from django.contrib import admin

class UjingaAdmin(admin.ModelAdmin):
    search_fields = ["content"]

admin.site.register(Ujinga, UjingaAdmin)
