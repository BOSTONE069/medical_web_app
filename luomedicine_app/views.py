from django.shortcuts import render, redirect
from .models import MedicinalPlant, LuoFoods
from .forms import SubscriptionForm
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect



# Create your views here.
def index(request):
    """
    It takes a request object and returns a response object

    :param request: This is the request object that is sent to the view
    :return: The index.html file is being returned.
    """
    return render(request, "luomedicine/index.html")


def contact(request):
    """
    It takes a request, and returns a response

    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The contact.html page is being returned.
    """
    return render(request, "luomedicine/contact.html")

def about(request):
    """
    It takes a request, and returns a response

    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :return: The about page is being returned.
    """
    return render(request, "luomedicine/about.html")

def medicine(request):
    """
    The function "medicine" retrieves all medicinal plants from the database and renders them in a
    template called "medicine.html".

    :param request: The request parameter is an object that represents the HTTP request made by the
    user. It contains information such as the user's browser, IP address, and any data sent with the
    request
    :return: a rendered HTML template called "medicine.html" with a context variable 'medicinal_plants'
    that contains all the objects from the MedicinalPlant model.
    """
    medicinal_plants = MedicinalPlant.objects.all()
    return render(request, "luomedicine/medicine.html", {'medicinal_plants': medicinal_plants})


@csrf_protect
def subscribe(request):
    """
    The `subscribe` function handles a POST request to subscribe a user and saves the subscription form
    data if it is valid, otherwise it renders the subscription form.

    :param request: The `request` parameter is an object that represents the HTTP request made by the
    user. It contains information such as the request method (e.g., GET or POST), the request headers,
    the request body, and other relevant information
    :return: The code is returning a rendered HTML template called 'luomedicine/layout.html' with the
    form variable passed as a context.
    """
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            try:
                form.clean()
            except ValidationError:
                # Handle validation error
                pass
            else:
                form.save()
                return redirect('success', secure=True)  # Redirect to a success page after subscribing
    else:
        form = SubscriptionForm()
    return render(request, 'luomedicine/layout.html', {'form': form})


def plant_view(request, id):
    medicinal_plants = MedicinalPlant.objects.get(id=id)
    return render(request, 'luomedicine/plant.html', {'medicinal_plants': medicinal_plants})

def luo_food(request):
    luo_foods = LuoFoods.objects.all()
    return render(request, 'luomedicine/foods.html', {'luo_foods':luo_foods})