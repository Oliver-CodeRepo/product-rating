from django.forms.models import ALL_FIELDS
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.db.models import Avg
# from django.contrib.auth.decorators import login_required

from .models import *
from .forms import RegForm, ReviewForm



def HomePage(request):
    context = {}
    return render(request, 'home.html', context)

def AboutPage(request):
    context = {}
    return render(request, 'about.html', context)

class ProductPage(ListView):
    model = Product
    template_name = 'ratingTemplates/products.html'


def ProductDetailsPage(request, p_slug):
    selected_product = get_object_or_404(Product, slug=p_slug)
    

    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            if selected_product.productReview.filter(user=request.user).exists():
                messages.info(request, 'You Can Only Review Once...')
            else:
                review_form.save()
                messages.success(request, 'Your Review was Submited successfully')
        else:
            messages.warning(request, 'Failed to submit')

    # get average rating
    avgRate  = Review.objects.filter(product=selected_product).aggregate(Avg('rate'))

    context = {'selected_product':selected_product, 'review_form':review_form, 'avgRate':avgRate}
    return render(request, 'ratingTemplates/product-details.html', context)


def regView(request):
    form = RegForm()
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "You've successfully registered as "+ username +", you can now login")
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'ratingTemplates/register.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'Invalid Username or Password')

    context = {}
    return render(request, 'ratingTemplates/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')
