from django.contrib import admin
from api.forms import AddScriptsForm

from api.models import ScriptSet, Script

@admin.register(Script)
class UserScript(admin.ModelAdmin):
    pass

@admin.register(ScriptSet)
class UserFolder(admin.ModelAdmin):
    form = AddScriptsForm
    # inlines = [ShowPhotoInline]

    # def save_related(self, request, form, formsets, change):
    #     super().save_related(request, form, formsets, change)
    #     form.save_photos(form.instance)
