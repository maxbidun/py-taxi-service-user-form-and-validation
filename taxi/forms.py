from .models import Driver, Car
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = (
        forms.CharField(
            max_length=8,
            min_length=8,
            validators=[
                RegexValidator(
                    regex=r"^[A-Z]{3}\d{5}$",
                    message="Format: AAA12345"
                )
            ]
        )
    )

    class Meta:
        model = Driver
        fields = "__all__"


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
