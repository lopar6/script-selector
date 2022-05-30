from django import forms

from api.models import Script, ScriptSet


class AddScriptsForm(forms.ModelForm):
    bat_files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label="Bat Files",
        required=True,
    )

    class Meta:
        model = ScriptSet
        fields = (
            "name",
            "bat_files",
        )

    def save_scripts(self, form, scriptSet):
        # TODO validation
        for file in self.files.getlist("bat_files"):
            script = Script()
            script.name = file.name
            script.bat_file = file
            script.script_set = scriptSet
            script.save()
