from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CloudFile



class FileUploadForm(forms.ModelForm):
    class Meta:
        model = CloudFile
        fields = ['description', 'file']