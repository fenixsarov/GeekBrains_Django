from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Unit, Category, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    page = 'index'
    return render(request, 'index.html', {"page": page})

def login_page(request):
    page = 'login_page'
    return render(request, "login.html", {"page": page})

def catalog(request):
    page = 'catalog'
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'page': page, 'categories': categories})

def units(request, category_id):
    unitss = Unit.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    return render(request, 'units_page.html', {'categories': categories, 'units': unitss})

def listing(request):
    contact_list = Contact.objects.all()
    #25 контактов
    paginator = Paginator(contact_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # Первую страницу вывести
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'contacts': contacts})
# Create your views here.
