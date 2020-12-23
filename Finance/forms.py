from django import forms
from Finance.models import *


class Level1Form(forms.ModelForm):
    class Meta:
        model = Level1
        fields = ['name', 'is_active']

        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={"class": 'form-control'})
        }


class Level2Form(forms.ModelForm):
    class Meta:
        model = Level2
        fields = ['parent_level', 'name', 'is_active']

        widgets = {
            'parent_level': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of Level 2'}),
            'is_active': forms.CheckboxInput(attrs={"class": 'form-control'})

        }


class Level3Form(forms.ModelForm):
    class Meta:
        model = Level3
        fields = ['parent_level1', 'parent_level', 'name', 'is_active']
        widgets = {
            'parent_level1': forms.Select(attrs={'class': 'form-control'}),
            'parent_level': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of Level 3'}),
            'is_active': forms.CheckboxInput(attrs={"class": 'form-control'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['parent_level'].queryset = Level2.objects.none()
    #
    #     if 'parent_level' in self.data:
    #         try:
    #             parent_level_id = int(self.data.get('parent_level'))
    #             print(parent_level_id)
    #             self.fields['parent_level'].queryset = Level2.objects.filter(parent_level_id=parent_level_id)
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['parent_level'].queryset = Level3.objects.filter(pk=self.instance.pk).order_by('name')


class Level4Form(forms.ModelForm):
    class Meta:
        model = Level4
        fields = ['parent_level1', 'parent_level2', 'parent_level', 'name', 'is_active']

        widgets = {
            'parent_level1': forms.Select(attrs={'class': 'form-control'}),
            'parent_level2': forms.Select(attrs={'class': 'form-control'}),
            'parent_level': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of Level 4'}),
            'is_active': forms.CheckboxInput(attrs={"class": 'form-control'})

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['parent_level'].queryset = Level3.objects.none()
    #
    #     if 'parent_level' in self.data:
    #         try:
    #             parent_level_id = int(self.data.get('parent_level'))
    #             print(parent_level_id)
    #             self.fields['parent_level'].queryset = Level3.objects.filter(parent_level_id=parent_level_id)
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         # self.fields['parent_level'].queryset = self.instance.parent_level_set
    #         self.fields['parent_level'].queryset = Level3.objects.filter(pk=self.instance.pk).order_by('name')
    #
    #
    #     self.fields['parent_level'].queryset = Level3.objects.none()
    #     if 'parent_level1' in self.data:
    #         try:
    #             city_id = int(self.data.get('parent_level1'))
    #             self.fields['parent_level'].queryset = Level3.objects.filter(parent_level_id=city_id)
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         # self.fields['parent_level'].queryset = self.instance.parent_level_set
    #         self.fields['parent_level'].queryset = Level3.objects.filter(pk=self.instance.pk).order_by('name')


class FinancialYearForm(forms.ModelForm):
    class Meta:
        model = FinancialYear
        fields = ['start_date', 'end_date', 'is_active']

    widgets = {
        'start_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'class': 'datepicker'}),
        'end_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'class': 'datepicker'}),
        'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
    }


class OpeningBalanceForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = ['account_name', 'credit', 'debit']

    widgets = {
        'account_name': forms.Select(attrs={"class": 'form-control'}),
        'credit': forms.NumberInput(attrs={"class": 'form-control', 'id':'input1'}),
        'debit': forms.NumberInput(attrs={"class": 'form-control', 'id':'input2'}),
    }


class OpeningBalanceInquiryForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = ['year']

    widgets = {
        'year': forms.SelectDateWidget(attrs={'class': "form-control datepicker", 'id': 'datepicker'})
    }
