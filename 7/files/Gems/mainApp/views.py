from django.shortcuts import render, render_to_response
from .models import Category, Gem, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories})

def gems(request, category_id):
    gems = Gem.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    return render(request, 'gems_page.html', {'categories': categories, 'gems': gems})

def listing(request):
    contact_list = Contact.objects.all()
        # Show 2 contacts per page
    paginator = Paginator(contact_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {"contacts": contacts})