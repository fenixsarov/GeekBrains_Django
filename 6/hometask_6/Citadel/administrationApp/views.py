from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import MyRegistrationForm

def registration(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        context = {'form': form}
        return render(request, 'registrition.html', context)
    context = {'form': MyRegistrationForm()}

    return render(request, 'registrition.html', context)

def admin_page(request):
    users = User.objects.all()
    return render(request, 'admin_page.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/adminka')
# Create your views here.
