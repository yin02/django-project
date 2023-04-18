from django import forms
from .models import Item

# Forms for the food app.

class ItemForm(forms.ModelForm):
    """
    The ItemForm class is a ModelForm for the Item model, used for creating and updating items.
    
    Attributes:
        Meta: A nested class that defines the model and fields to be used in the form.
    """

    class Meta:
        model = Item
        fields = ['item_name', 'item_disc', 'item_price', 'item_image']
