from django import forms
from .models import Category, Material, Customer


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'slug': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'slug': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'job': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'message': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'loadFile(event)'
                }
            ),
        }