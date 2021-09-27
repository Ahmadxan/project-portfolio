from django.shortcuts import render, redirect
from . import models
from . import forms
from dashboard.models import Material, Category, Customer
from django.core.paginator import Paginator


def index_page(request):
    catigories = Category.objects.all()
    fooes = Customer.objects.all()
    videos = Material.objects.filter(category__title="Video")
    books = Material.objects.filter(category__title="Kitob")
    paginator = Paginator(books, 2)
    page_number = 2
    page_obj = paginator.get_page(page_number)
    prezintatsiya = Material.objects.filter(category__title="Prezintatsiya")
    maqola = Material.objects.filter(category__title="Maqola")
    disertatsiya = Material.objects.filter(category__title="Disertatsiya")
    ctx = {
        'catigories': catigories,
        'fooes': fooes,
        'videos': videos,
        'books': books,
        'prezintatsiya': prezintatsiya,
        'maqola': maqola,
        'disertatsiya': disertatsiya,
        'page_obj': page_obj,
    }
    form = forms.GetInTouchForm(request.POST or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('index_page')
    return render(request, 'index.html', ctx)


def maqola_detail(request):
    return render(request, 'maqola/index.html')