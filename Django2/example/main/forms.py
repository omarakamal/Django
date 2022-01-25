from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    check = forms.BooleanField(
        label="Are you a Saudi Citizen?", required=False)
