from django.shortcuts import render, redirect
from .models import MedicinalPlant, LuoFoods
from .forms import SubscriptionForm
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.http import HttpResponse

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
    try:
        paginator = Paginator(MedicinalPlant.objects.all().order_by('title'), 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        medicinal_plants = page_obj.object_list  # Limiting the number of records to 100
    except Exception as e:
        # Handle the exception or error appropriately
        return render(request, "luomedicine/error.html", {'error_message': str(e)})
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

# This function is responsible for rendering the plant view page for a specific medicinal plantfrom django.http import HttpResponse

def get_medicinal_plant_by_id(request, id):
    # Get the MedicinalPlant object with the specified id
    try:
        medicinal_plant = MedicinalPlant.objects.get(id=id)
    except MedicinalPlant.DoesNotExist:
        error_message = 'The requested MedicinalPlant does not exist.'
        return render(request, 'luomedicine/error.html', {'error_message': error_message}, status=404)
    # Render the plant.html template with the medicinal_plant object passed as context
    return render(request, 'luomedicine/plant.html', {'medicinal_plant': medicinal_plant})

def luo_food(request):
    luo_foods = LuoFoods.objects.all()
    return render(request, 'luomedicine/foods.html', {'luo_foods':luo_foods})