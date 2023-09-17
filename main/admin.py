from django import forms
from django.contrib import admin

from main.models import Category, Product, Order, OrderItems


class OrderItemsInlineForm(forms.ModelForm):
    # is_main = forms.BooleanField()

    class Meta:
        model = OrderItems
        fields = ('product', 'quantity')

    # def clean_quantity(self):
    #     quantity = self.cleaned_data.get('quantity')
    #     if quantity <= 0:
    #         raise forms.ValidationError('Количество должно быть больше 0')
    #     return quantity
    #
    # def clean(self):
    #     product = self.cleaned_data.get('product')
    #     quantity = self.cleaned_data.get('quantity')
    #     if product.id == 1 and quantity < 100:
    #         raise forms.ValidationError(...)
    #     return self.cleaned_data


class OrderItemInline(admin.TabularInline):
    model = OrderItems
    form = OrderItemsInlineForm


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItems)
