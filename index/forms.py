from django import forms

from index.models import WriteToMaster


class NameForm(forms.ModelForm):
    class Meta:
        model = WriteToMaster
        fields = ('username', 'number', 'age')