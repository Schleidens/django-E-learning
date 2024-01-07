from django.contrib import admin

from .models import coursesModel

# Register your models here.


class courseAdmin(admin.ModelAdmin):
    list_display = ['slug']
    readonly_fields = ['slug']  # Make slug read-only in detail view


admin.site.register(coursesModel, courseAdmin)
