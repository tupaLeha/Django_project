from django.shortcuts import render

from .forms import NewForm, AuthenticationForm

from django.http import HttpResponseRedirect

from audioop import reverse

from django.contrib.auth import login


def form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            return HttpResponseRedirect(reverse('well_done'))
        return HttpResponseRedirect(reverse('gtfo'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewForm()

    return render(request, 'form.html', {'form': form})


def new_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            return render(request, 'well_done.html')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NewForm()

    return render(request, 'new_form.html', {'form': form})


def gtfo(request):
    return render(request, 'gtfo.html')


def well_done(request):
    return render(request, 'well_done.html')


def login_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'login_page.html', {'form': form})