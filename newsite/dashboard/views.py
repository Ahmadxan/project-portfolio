from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from maqola.models import GetInTouch

from . import forms


def login_required_decorator(func):
    return login_required(func, login_url='login-page')


def login_page(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index-page')
    return render(request, 'admin/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login-page')


@login_required_decorator
def index_page(request):
    messages = GetInTouch.objects.all()
    ctx = {
        'messages': messages
    }
    return render(request, 'admin/index.html', ctx)


@login_required_decorator
def category_list(request):
    categories = models.Category.objects.all()
    ctx = {
        'categories': categories
    }
    return render(request, 'admin/category/list.html', ctx)


@login_required_decorator
def category_create(request):
    form = forms.CategoryForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category-list')
    ctx = {
        'form': form
    }
    return render(request, 'admin/category/form.html', ctx)


@login_required_decorator
def category_update(request, pk):
    model = models.Category.objects.get(id=pk)
    form = forms.CategoryForm(request.POST or None, request.FILES or None, instance=model)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('category-list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'admin/category/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model = models.Category.objects.get(id=pk)
    model.delete()
    return redirect('category-list')


@login_required_decorator
def material_list(request):
    materiallar = models.Material.objects.all()
    ctx = {
        'materiallar': materiallar
    }
    return render(request, 'admin/material/list.html', ctx)


@login_required_decorator
def material_create(request):
    form = forms.MaterialForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('material-list')
    ctx = {
        'form': form
    }
    return render(request, 'admin/material/form.html', ctx)


@login_required_decorator
def material_update(request, pk):
    model = models.Material.objects.get(id=pk)
    form = forms.MaterialForm(request.POST or None, request.FILES or None, instance=model)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('material-list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'admin/material/form.html', ctx)


@login_required_decorator
def material_delete(request, pk):
    model = models.Material.objects.get(id=pk)
    model.delete()
    return redirect('material-list')


@login_required_decorator
def customer_list(request):
    customers = models.Customer.objects.all()
    ctx = {
        'customers': customers
    }
    return render(request, 'admin/customer/list.html', ctx)


@login_required_decorator
def customer_create(request):
    form = forms.CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('customer-list')
    ctx = {
        'form': form
    }
    return render(request, 'admin/customer/form.html', ctx)


@login_required_decorator
def customer_update(request, pk):
    model = models.Customer.objects.get(id=pk)
    form = forms.CustomerForm(request.POST or None, request.FILES or None, instance=model)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('customer-list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, 'admin/customer/form.html', ctx)


@login_required_decorator
def customer_delete(request, pk):
    model = models.Customer.objects.get(id=pk)
    model.delete()
    return redirect('customer-list')