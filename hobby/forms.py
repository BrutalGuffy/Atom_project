from django import forms

from hobby.models import Profile, Message


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'is_organizer', 'profile_image', 'birth_date')


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('comment',)

