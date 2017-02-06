from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import MyRegistrationForm


# from userManagementApp.forms import MyRegistrationForm, UserChangeForm
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test

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
    return HttpResponseRedirect('/admin')


def create_user(request, user_id=None):
    if request.is_ajax():
        if not user_id:
            user = User(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = MyRegistrationForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'error': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404

def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

# Create your views here.
