from django import forms

from api.models import ScriptSet


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

    def save(self, commit=True):
        instance = super().save(commit=commit)
        print(instance)
        return instance
