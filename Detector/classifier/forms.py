from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    IMAGE_TYPES = (
        ('spiral', 'Spiral'),
        ('wave', 'Wave'),
    )
    image_type = forms.ChoiceField(choices=IMAGE_TYPES)

    class Meta:
        model = UserInput
        fields = ['name', 'age', 'email', 'image', 'image_type']
