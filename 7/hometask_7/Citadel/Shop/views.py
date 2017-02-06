from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Unit, Category

def main(request):
    page = 'index'
    return render(request, "index.html", {"page": page})

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
    return render(request, 'catalog.html', {'page': page})

def units(request, category_id):
    units = Unit.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    return render(request, 'units_page.html', {'categories': categories, 'units': units})

def admin_units(request):
    units = Unit.objects.all()
    return render(request, 'admin_units.html', {'units': units})

def admin_units_create(request):
    if request.method == 'POST':
        form = UnitsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/units/')
        context = {'form': form}
        return render(request, 'admin_units_create.html', context)
    context = {'form': UnitsForm()}
    return render(request, 'admin_units_create.html', context)

def admin_units_delete(request):
    units = get_object_or_404(Unit, id=id)
    units.delete()
    return HttpResponseRedirect('/admin/units/')

def admin_units_update(request, id):
    pass

def admin_units_details(request, id):
    unit = get_object_or_404(Unit, id=id)
    return render(request, 'admin_unit_detail.html', {'unit': unit})
# Create your views here.
