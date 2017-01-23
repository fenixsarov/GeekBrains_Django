from django.shortcuts import render, render_to_response
from .models import Work, Education

name = 'дмитрий'
surname = 'Кравец'


def main(request):
    page = 'index'
    desc = 'Меня зовут Кравец Дмитрий, работаю в данный момент C++ программистом. Основное направление деятельности сейчас - это разработка интерфесой программных комплексов. Нравится программировать на Python, потому решил освоить фул-стек разработку веб-приложений на GeekBrains. В свободное время увлекаюсь настольным теннисом и покатушками на велосипеде.'
    return render_to_response("index.html", {
        "name": name,
        "surname": surname,
        "desc": desc,
        "page": page,
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
