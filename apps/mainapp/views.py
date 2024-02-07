from django.shortcuts import render, redirect
from .models import Contact 
from apps.products.models import Watch, Testimonial
import requests


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(message, name, email, phone)

        # https://api.telegram.org/bot6697315839:AAH08hqQ8FZXr5vKx49Xb_ckltqSPdbPohE/getUpdates
        
        token = '6697315839:AAH08hqQ8FZXr5vKx49Xb_ckltqSPdbPohE'
        chat_id = '-4150953858'
        url = f'https://api.telegram.org/bot{token}/sendMessage'

        params = {'chat_id': chat_id, 
                  'text': f'Вам оставил заявку:{name} с номером: {phone}, email: {email}, сообщение {message}'
                }
        
        requests.post(url, data=params)


        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        return redirect('index')
    
    male_products = Watch.objects.filter(gender='male')
    testimonials = Testimonial.objects.all()
    female_products = Watch.objects.filter(gender='female')
    unisex = Watch.objects.filter(gender='unisex')
    context = {'male_products': male_products,
               'female_products': female_products,
               'electronic_watch': unisex,
               'testimonials': testimonials}    
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(message, name, email, phone)

        # https://api.telegram.org/bot6697315839:AAH08hqQ8FZXr5vKx49Xb_ckltqSPdbPohE/getUpdates
        
        token = '6697315839:AAH08hqQ8FZXr5vKx49Xb_ckltqSPdbPohE'
        chat_id = '-4150953858'
        url = f'https://api.telegram.org/bot{token}/sendMessage'

        params = {'chat_id': chat_id, 
                  'text': f'Вам оставил заявку:{name} с номером: {phone}, email: {email}, сообщение {message}'
                }
        
        requests.post(url, data=params)


        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        return redirect('index')
    return render(request, 'contact.html')


