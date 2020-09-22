from django import forms
from .models import Profile #, Room

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','age']

# class RoomForm(forms.ModelRoom):
#     class Meta:
#         model = Room
#         fields = ['content']
