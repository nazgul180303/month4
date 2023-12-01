from django import forms
from .models import Product, Review, Category


class ProductCreateForms(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(Category.objects.all())
    price = forms.FloatField()
    image = forms.ImageField()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if len(name) < 10:
            raise forms.ValidationError("Name to short!")
        return cleaned_data

    def clean_content(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if len(description) < 40:
            raise forms.ValidationError("description to short!")
        if not description:
            raise forms.ValidationError("description is required!")
        return cleaned_data


# class ProductCreateForm2(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'category', 'price', 'image']


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ReviewCreateForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    text = forms.CharField(max_length=70)
