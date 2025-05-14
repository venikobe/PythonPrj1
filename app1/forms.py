from django import forms

class TaskForm(forms.Form):
    year = forms.Field(label="Года")
    century = forms.IntegerField(label="Столетие", min_value=0)

