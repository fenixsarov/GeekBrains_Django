from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404

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
# Create your views here.
