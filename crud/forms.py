from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control name'}),
        max_length=50)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        max_length=15)
    designation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        max_length=100, required=False)
    is_active = forms.BooleanField(initial=True)

    class Meta:
        model = Member
        fields = "__all__"

    def clean(self):
       clean_all = super().clean()