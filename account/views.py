from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, AccountAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant.models import Restaurant
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        messages.add_message(request, messages.WARNING, f"You are already authenticated as '{user.email}' !")
        return render(request, "account/message_info.html")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            #if destination != None
            if destination:
                return redirect(destination)
            return redirect('profile')
        else:
            context['registration_form'] = form
    return render(request, 'account/register.html', context)


def login_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect(f'/account/profile/{user.id}')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect(f'/account/profile/{user.id}')
        else:
            context['login_form'] = form
    return render(request, 'account/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect



# def login(request):
#      return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request, id):
    if request.user.category == 'Restaurant Manager':
        try:
            restaurant = Restaurant.objects.get(user=id)
            return render(request, 'account/user_profile.html/', {'restaurant': restaurant})
            # restaurant = get_object_or_404(Restaurant, user=id)
        except ObjectDoesNotExist:
            return redirect('create_restaurant')       
    else:
        return render(request, 'account/user_profile.html/')


