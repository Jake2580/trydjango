from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title =         forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )

    email =         forms.EmailField()

    description =   forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )

    price =         forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title: str = self.cleaned_data.get('title')
        # if not '2022' in title:
        #     raise forms.ValidationError('This is not a valid title')
        # if not 'news' in title:
        #     raise forms.ValidationError('This is not a valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email: str = self.cleaned_data.get('email')
        # if not email.endswith('edu'):
        #     raise forms.ValidationError('This is not a valid email')
        return email

class RawProductForm(forms.Form):
    title =         forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={"placeholder": "Your title"}
                        )
                    )
    description =   forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-textareas",
                                "rows": 10,
                                "cols": 10
                            }
                        )
                    )
    price =         forms.DecimalField(initial=199.99)
