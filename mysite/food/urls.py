from . import views
from django.urls import path

# URL configuration for the food app.

app_name = 'food'

# urlpatterns define the routing of the food app by mapping URL patterns to views.
urlpatterns = [
    # /food/ - Index view showing a list of all items.
    path('', views.IndexClassView.as_view(), name='index'),
    
    # /food/1 - Detail view for a specific item identified by its primary key.
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    
    # /food/item/ - Item view (currently returns an HttpResponse with a message).
    path('item/', views.item, name='item'),
    
    # /food/add - Create item view for adding new items.
    path('add', views.CreateItem.as_view(), name='create_item'),
    
    # /food/update/1 - Update item view for editing existing items (identified by id).
    path('update/<int:id>/', views.update_item, name='update_item'),
    
    # /food/delete/1 - Delete item view for removing items (identified by id).
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
