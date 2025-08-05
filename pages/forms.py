from django import forms

from pages.models import ContactModel


class ContactModelForm(forms.ModelForm):
    phone_number = forms.CharField(required=True)

    class Meta:
        model = ContactModel
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number:
            return phone_number

        if len(phone_number) != 13:
            raise forms.ValidationError("Phone number must be exactly 13 characters long.")

        return phone_number


