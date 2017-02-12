from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')
        # fields = ('__all__')
        def save(self, commit=True):
            user = super(MyRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']

            if commit:
                user.save()
            return user

class UserChangeForm(forms.ModelForm):
    """
        Форма для обновления данных пользователей. Нужна только для того, чтобы не
        видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
        пользователя.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']