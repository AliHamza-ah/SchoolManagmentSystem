from django import forms
from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Name of Branch'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Email'}),
            'contact_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Contact No.'}),
            'landline': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Contact No.'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Address'}),
            'ntn': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter NTN Number'}),
            'bank_name_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Name'}),
            'account_no_1': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'bank_address_1': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Address: '}),
            'bank_contact_1': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Contact No.'}),
            'bank_name_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Name'}),
            'account_no_2': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'bank_address_2': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Address'}),
            'bank_contact_2': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'bank_name_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Name'}),
            'account_no_3': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'bank_address_3': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Address'}),
            'bank_contact_3': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Contact'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
