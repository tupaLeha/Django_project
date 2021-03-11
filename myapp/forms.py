from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class NewForm(forms.Form):
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'IT')
    )

    ENGLISH = (
        (1, 'A1'),
        (2, 'A2'),
        (3, 'B1'),
        (4, 'B2'),
        (5, 'C1'),
        (6, 'C2')
    )

    name = forms.CharField(max_length=50),
    age = forms.IntegerField(min_value=18, max_value=1488)
    gender = forms.ChoiceField(choices=GENDER)
    english = forms.ChoiceField(choices=ENGLISH)

    def clean(self):
        cleaned_data = super().clean()
        if not (cleaned_data.get('gender') == '1' and cleaned_data.get('age') >= 20 and cleaned_data.get('english') >= '4') and not (cleaned_data.get('gender') == '2' and cleaned_data.get('age') >= 23 and cleaned_data.get('english') >= 3):
            raise ValidationError('U faggot')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        self.user = authenticate(username=username, password=password)
        if self.user is None:
            raise forms.ValidationError('Login/Password is incorrect')