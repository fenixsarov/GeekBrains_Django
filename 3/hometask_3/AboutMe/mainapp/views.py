from django.shortcuts import render, render_to_response
from .models import Work, Education, Index

name = 'дмитрий'
surname = 'Кравец'


def main(request):
    page = 'index'
    desc = Index.objects.all()
    return render_to_response("index.html", {
        "name": name,
        "surname": surname,
        "desc": desc,
        "page": page
    })


def job(request):
    page = 'job'
    work_places = Work.objects.all()

    return render_to_response("job.html", {"work_places": work_places,
                                           "name": name,
                                           "surname": surname, "page": page})


def education(request):
    page = 'education'
    education_places = Education.objects.all()

    return render_to_response("education.html", {"education_places": education_places, "name": name,
                                                 "surname": surname, "page": page})

# Create your views here.
