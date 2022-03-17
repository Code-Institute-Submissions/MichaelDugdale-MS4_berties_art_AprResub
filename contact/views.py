from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Your message is send. '
                + 'We will reply within 48 hours!')
        else:
            messages.error(request, 'Please try again.')
        return redirect(reverse('contact'))
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)