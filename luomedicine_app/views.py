from django.shortcuts import render, redirect
from .models import MedicinalPlant
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
    medicinal_plants = MedicinalPlant.objects.all()
    return render(request, "luomedicine/medicine.html", {'medicinal_plants': medicinal_plants})


@csrf_protect
def subscribe(request):
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
    """
    The article_view function takes a request and an id, gets the article with the given id, and renders
    the article in the template.

    :param request: The request object is the first parameter to the view function. It contains
    information about the current request, such as the method (GET or POST), the user (if any is logged
    in), and the GET and POST parameters
    :param id: the id of the article
    :return: The article object
    """
    medicinal_plants = MedicinalPlant.objects.get(id=id)
    return render(request, 'luomedicine/plant.html', {'medicinal_plants': medicinal_plants})