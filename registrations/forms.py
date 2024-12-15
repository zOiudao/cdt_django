from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "nome de usuário",
                # "name": "username",
            }
        )

        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "primeiro nome",
                # "name": "first_name",
            }
        )

        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "sobrenome",
                # "name": "last_name",
            }
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "email",
                # "name": "email",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "senha",
                # "name": "password",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "confirmar senha",
                # "name": "password",
            }
        )


class EmployeeCreate(ModelForm):
    class Meta:
        model = models.Employee
        fields = (
            "first_name",
            "last_name",
            "functional",
            "enterprise",
            "sector",
            "owner",
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Primeiro nome",
            }
        )

        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Sobrenome",
            }
        )

        self.fields["functional"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Funcional",
                "type": "number",
            }
        )

        self.fields["enterprise"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Empresa",
            }
        )

        self.fields["sector"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Setor",
            }
        )

        self.fields["owner"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Cadastrado por",
            }
        )
