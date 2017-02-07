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

def login(request):

    if request.method == 'POST':
        print("POST data= {}".format(request.POST))
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def registration_low(request):
    if request.method == "POST":
        errors = {}

        username = request.POST.get('name')
        email = request.POST.get('email')
        email2 = request.POST.get('confirm_email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        print("REG POST data= {}".format(request.POST))

        if email != email2:
            errors['email'] = 'email-адреса не совпали'
        if password != password2:
            errors['password'] = 'Пароли не совпали'
        user = User(username=username, email=email)
        user.set_password(password)

        try:
            user.validate_unique()
        except ValidationError as er:
            errors.update(er.message_dict)

        if errors:
            return render(request, 'registration_low.html', {'reg_errors': errors})

        user.save()
        return HttpResponseRedirect("/")
    return render(request, "registration_low.html")

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
