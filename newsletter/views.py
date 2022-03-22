from django.shortcuts import render, redirect, reverse
from .forms import SubscibersForm
from django.contrib import messages

# Create your views here.


def newsletter(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect(reverse('newsletter'))
    else:
        form = SubscibersForm()
    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
