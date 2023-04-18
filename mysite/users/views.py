from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# The register view handles user registration
def register(request):
    """
    Register a new user.

    If the request method is "POST", it validates and saves the new user, sends
    a success message, and redirects the user to the login page. Otherwise, it
    renders an empty registration form.

    Args:
        request: A Django HttpRequest object representing the current request.

    Returns:
        A Django HttpResponse object with either the rendered registration form
        or a redirect to the login page.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# The profilepage view displays the authenticated user's profile
@login_required
def profilepage(request):
    """
    Display the authenticated user's profile page.

    Args:
        request: A Django HttpRequest object representing the current request.

    Returns:
        A Django HttpResponse object with the rendered profile page.
    """
    return render(request, 'users/profile.html')
