from django import forms

class TaskForm(forms.Form):
    overworkInput = forms.Field(label="Запись о переработках")
    dayInput = forms.Field(label="День переработок")

