from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser
from django import forms
from mainapp.models import Product, ProductCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"


class ProductCategoryEditForm(forms.ModelForm):
    discount = forms.IntegerField(label="скидка", required=False, min_value=-200, max_value=200, initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = Product
        fields = "__all__"
