from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item
from .views import index, detail, create_item, update_item, delete_item

class FoodAppTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.item = Item.objects.create(item_name='Test Item', item_disc='Test description', item_price=10, user_name=self.user)

    def test_index_view(self):
        request = self.factory.get(reverse('food:index'))
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        request = self.factory.get(reverse('food:detail', args=[self.item.id]))
        request.user = self.user
        response = detail(request, self.item.id)
        self.assertEqual(response.status_code, 200)

    def test_create_item_view(self):
        request = self.factory.post(reverse('food:create_item'), data={
            'item_name': 'New item',
            'item_disc': 'New description',
            'item_price': 15,
        })
        request.user = self.user
        response = create_item(request)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_update_item_view(self):
        request = self.factory.post(reverse('food:update_item', args=[self.item.id]), data={
            'item_name': 'Updated item',
            'item_disc': 'Updated description',
            'item_price': 20,
        })
        request.user = self.user
        response = update_item(request, self.item.id)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_delete_item_view(self):
        request = self.factory.post(reverse('food:delete_item', args=[self.item.id]))
        request.user = self.user
        response = delete_item(request, self.item.id)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
