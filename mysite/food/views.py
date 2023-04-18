from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Views for the food app.

def index(request):
    """
    Function-based view for displaying a list of all items.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered HTML page with the list of items.
    """
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    """
    Class-based view for displaying a list of all items using Django's ListView.
    """
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    """
    Function-based view for an individual item (currently returns only an HttpResponse).
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: An HttpResponse containing an item view message.
    """
    return HttpResponse("<h1>This is an item view.<h1>")


def detail(request, item_id):
    """
    Function-based view for displaying the details of a specific item.
    
    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The primary key of the item to display.
        
    Returns:
        HttpResponse: The rendered HTML page with the item details.
    """
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }

    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    """
    Class-based view for displaying the details of a specific item using Django's DetailView.
    """
    model = Item
    template_name = 'food/detail.html'


def create_item(request):
    """
    Function-based view for creating a new item using a form.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered HTML page with the form or a redirect to the index view after successful form submission.
    """
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})


class CreateItem(CreateView):
    """
    Class-based view for creating a new item using a form and Django's CreateView.
    """
    model = Item
    fields = ['item_name', 'item_disc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        """
        Method called when the form is valid. It sets the user_name field before saving.
        
        Args:
            form (ModelForm): The valid form instance.
            
        Returns:
            HttpResponseRedirect: A redirect to the success URL (usually the index view).
        """
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    """
    Function-based view for updating an existing item using a form.
    
    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The primary key of the item to update.
        
    Returns:
        HttpResponse: The rendered HTML page with the form or a redirect to the index view after successful form submission.
    """
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

