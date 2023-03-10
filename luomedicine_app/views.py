from django.shortcuts import render


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
