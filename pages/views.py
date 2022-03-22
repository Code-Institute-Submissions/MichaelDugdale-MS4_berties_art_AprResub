from django.shortcuts import render

# Create your views here.
def about_us(request):
    """ A view to return the company page """

    return render(request, 'pages/about_us.html')


def faq(request):
    """ A view to return the FAQ page """

    return render(request, 'pages/faq.html')


def return_policy(request):
    """ A view to return the return policy page """

    return render(request, 'pages/return_policy.html')