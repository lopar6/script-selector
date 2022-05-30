from django.contrib import admin
from api.forms import AddScriptsForm

from api.models import ScriptSet, Script


@admin.register(Script)
class UserScript(admin.ModelAdmin):
    raw_id_fields = ('script_set',)

@admin.register(ScriptSet)
class UserScriptSet(admin.ModelAdmin):
    form = AddScriptsForm
    # inlines = [ShowPhotoInline]

    def save_model(self, request, obj, form, change) -> None:
        x = super().save_model(request, obj, form, change)
        form.save_scripts(form, obj)

