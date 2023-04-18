from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Models for the food app.

class Item(models.Model):
    """
    The Item model represents a food item, including its name, description, price, and image URL.

    Attributes:
        user_name (ForeignKey): The User associated with this item, with a CASCADE delete rule.
        item_name (CharField): The name of the item, with a maximum length of 200 characters.
        item_disc (CharField): A description of the item, with a maximum length of 200 characters.
        item_price (IntegerField): The price of the item.
        item_image (CharField): The URL of the item's image, with a maximum length of 500 characters and a default placeholder image.
    """

    def __str__(self):
        """
        Returns a string representation of the Item instance, which is the item's name.
        """
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_disc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def get_absolute_url(self):
        """
        Returns the absolute URL of the item's detail view, using the "food:detail" URL pattern and the item's primary key.
        """
        return reverse("food:detail", kwargs={"pk": self.pk})
