from django.shortcuts import render, redirect, reverse
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse



def landing_page(request):
    return render(request, 'landing_page.html')

@login_required(login_url='/login')
def show_main(request):

    context = {
        'nama': request.user.username,
        'kelas': "PBP-A",
        'tagline': "Your Daily Dose of Sweetness",
        'description': "Welcome to Butter & Batter — where every bite is a blissful journey of flavors.",
        # 'last_login': request.COOKIES['last_login'],

    }

    return render(request, 'main.html', context)


def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form,
    }
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type='application/xml')

def show_json(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type='application/json')

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {'form': form}
    return render(request, "register.html", context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get the product entry
    product = ProductEntry.objects.get(pk=id)

    # Set product entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save() # simpan form dan kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = ProductEntry.objects.get(pk=id) # Get product berdasarkan id
    product.delete() # hapus product
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    form = ProductEntryForm(request.POST)
    
    if form.is_valid():
        product = form.save(commit=False)  # Save the product without committing yet
        product.user = request.user  # Set the user manually
        product.save()  # Now save it
        return HttpResponse("CREATED", status=201)
    else:
        # Send back an error message with status 400
        error_message = ', '.join([f"{field}: {error[0]}" for field, error in form.errors.items()])
        return HttpResponse(f"Error: {error_message}", status=400)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = ProductEntry.objects.create(
            user=request.user,
            name=data["name"],
            description=data["description"],
            price=int(data["price"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    