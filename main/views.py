from django.shortcuts import render, redirect 
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    product_entries = ProductEntry.objects.all() # mengambil seuluruh objek dari model ProductEntry yang tersimpan di database


    context = {
        'nama': "Patricia Herningtyas",
        'kelas': "PBP-A",
        'tagline': "Your Daily Dose of Sweetness",
        'description': "Welcome to Butter & Batter — where every bite is a blissful journey of flavors.",
        'product_entries': product_entries
    }

    return render(request, 'main.html', context)


def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'nama': "Patricia Herningtyas",
        'kelas': "PBP-A",
    }
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type='application/xml')

def show_json(request):
    data = ProductEntry.objects.all()
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
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')