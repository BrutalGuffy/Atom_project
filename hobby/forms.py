from django import forms

from hobby.models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    class Meta:
        model = Profile
        fields = ('bio',)