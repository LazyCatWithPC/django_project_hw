from django import forms
from shop.models import Product, Version

block_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'creation_date', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in block_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Недопустимое имя.")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in block_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError("Недопустимое описание.")

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

