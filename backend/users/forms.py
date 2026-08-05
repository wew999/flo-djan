from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр разрешено."
) # НА ВСЯКИЙ СЛУЧАЙ ОСТАВЛЯЮ



def validate_no_common_words(value):
    if 'login' == value.lower():
        raise ValidationError("Поле не должно содержать слово 'login'.")
    elif 'password' == value.lower():
        raise ValidationError("Поле не должно  содержать слово 'password'.")

class LograForm(forms.Form):
   # username = forms.CharField(required=False)
    login = forms.CharField(max_length=30, error_messages={
       'max_length': 'Логин не может быть длинее 30 символов'
   }, validators=[validate_no_common_words])
    password = forms.CharField(min_length=8, max_length=30, error_messages={
        'min_length': 'Пароль не может быть короче 8 символов',
        'max_length': 'Пароль не может быть длинее 30 символов'
    }, validators=[validate_no_common_words])
    adresl = forms.CharField( validators=[validate_no_common_words])