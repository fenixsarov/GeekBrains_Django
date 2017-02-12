from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import MyRegistrationForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from Shop.forms import UnitsForm
from Shop.models import Unit, Category

# Импортируем классы, на основе которых буду переводить вьюху на ClassBasedView-методологию
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm
    return render(request, 'admin_page.html', {'users': users, 'form': user_form})


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

# @user_passes_test(lambda u: u.is_superuser)
# def admin_units(request):
#     units = Unit.objects.all()
#     return render(request, 'admin_units.html', {'units': units})

class UnitsListView(ListView):
    model = Unit
    template_name = 'admin_units.html'
    paginate_by = 2

# def admin_units_create(request):
#     if request.method == 'POST':
#         form = UnitsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/admin/units/')
#         context = {'form': form}
#         return render(request, 'admin_units_create.html', context)
#     context = {'form': UnitsForm()}
#     return render(request, 'admin_units_create.html', context)

class UnitsCreateView(CreateView):
    model = Unit
    template_name = 'admin_units_create.html'
    success_url = '/admin/units/'
    fields = ('__all__')


# def admin_units_delete(request):
#     units = get_object_or_404(Unit, id=id)
#     units.delete()
#     return HttpResponseRedirect('/admin/units/')

class UnitsDeleteView(DeleteView):
    model = Unit
    success_url = '/admin/units/'
    template_name = 'confirm_delete.html'



# def admin_units_update(request, id):
#     unit = get_object_or_404(Unit, id=id)
#     if request.method == 'POST':
#         form = UnitsForm(request.POST, instance=unit)
#         if form.is_valid():
#             unit.save()
#             return HttpResponseRedirect('/admin/units/')
#         context = {'form': form}
#         return render(request, 'admin_units_update.html', context)
#     context = {'form': UnitsForm(instance=unit)}
#     return render(request, 'admin_units_update.html', context)

class UnitsUpdateView(UpdateView):
    pass


# def admin_units_detail(request, id):
#     unit = get_object_or_404(Unit, id=id)
#     return render(request, 'admin_unit_detail.html', {'unit': unit})

class UnitsDetailView(DetailView):
    model = Unit
    template_name = 'admin_unit_detail.html'

# Create your views here.
