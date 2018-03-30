from django import forms

from hobby.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'is_organizer', 'profile_image', 'birth_date')

