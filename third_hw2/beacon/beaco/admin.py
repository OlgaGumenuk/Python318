from django.contrib import admin
from .models import Beaco


class BeacoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# readonly_fields это поле только для чтения
admin.site.register(Beaco, BeacoAdmin)

