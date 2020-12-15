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
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Name'}),
            'account_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'account_no1': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'account_no2': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the Bank Account No.'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
