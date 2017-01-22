from django.shortcuts import render, render_to_response

def main(request):
    name = 'дмитрий'
    surname = 'Кравец'
    return render_to_response("index.html", {
            "name": name,
            "surname": surname,
        })

def job(request):
    place_of_work = ['Tele2', 'X5RetailGroup', 'РФЯЦ-ВНИИЭФ']
    date_of_work = ['2008-2011 гг.', '2011-2012 гг', '2012- и по сей день']
    desc_of_work = [
        'Работал на должности продавца-консульта в центре обслуживания клиентов у себя в городе.'
        ' Основной же задачей было общение с абонентами и решение возникающих у них вопросов.',
        'Получил первый опыт работы системным инженером, в обязанности которого входила настройка и'
        'поддержание бесперебойной работы торгового и сервеного оборудования в супермаркетах'
        'нашего города.',
        'Прошел дипломную практику и заступил на должность инженера-программиста, а спустя 2 года меня повысили'
        'до младшего научного сотрудника. За время работы получил навыки разработки сложных программых комплексов,'
        'разработки интерфейсов, построения архитектуры баз данных и многое другое)',
    ]
    return render_to_response("job.html",
        {
            "place_of_work": place_of_work,
            "date_of_work": date_of_work,
            "desc_of_work": desc_of_work
            })

def education(request):
    return render_to_response("education.html")

# Create your views here.
