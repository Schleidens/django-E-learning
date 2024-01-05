from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import coursesModel


class coursesForm(forms.ModelForm):

    class Meta:
        model = coursesModel
        description = forms.CharField(widget=CKEditorWidget())
        fields = ['name', 'description', 'cover', 'duration', 'intro_video']
