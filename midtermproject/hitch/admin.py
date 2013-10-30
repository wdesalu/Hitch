from django.contrib import admin
from hitch import models

class DriverAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(models.Driver, DriverAdmin)
admin.site.register(models.Client)
