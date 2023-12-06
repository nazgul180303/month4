from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password_repeat != password:
            raise forms.ValidationError("Password mamatch")

        cleaned_data.pop('password_repeat')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
