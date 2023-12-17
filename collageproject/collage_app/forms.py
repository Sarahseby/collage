from django import forms
from .models import Department,Course

class MyForm(forms.Form):
    department=forms.ModelChoiceField(queryset=Department.objects.all())
    course=forms.ModelChoiceField(queryset=Course.objects.all())