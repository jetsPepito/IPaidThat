from django import forms


class LoginForm(forms.Form):

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    email = forms.CharField(max_length=300)
    password = forms.CharField(widget=forms.PasswordInput())
