from django.shortcuts import render
from .models import Watch, Testimonial
from django.shortcuts import get_object_or_404


def product_view(request):
    male_products = Watch.objects.filter(gender='male')
    female_products = Watch.objects.filter(gender='female')
    unisex = Watch.objects.filter(gender='unisex')
    context = {'male_products': male_products,
               'female_products': female_products,
                'electronic_watch': unisex,}    
    return render(request, 'product.html', context)


def watch_detail(request, watch_id):
    watch = get_object_or_404(Watch, pk=watch_id)
    return render(request, 'detail.html', {'watch': watch})


def testimonial_view(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials}
    return render(request, 'testimonial.html', context)

    


