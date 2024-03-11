from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm
from django.views.generic import DeleteView, UpdateView
from .filters import PostFilter


def index(request):
    staf_all = Service.objects.order_by('id')
    staf = PostFilter(request.GET, queryset=staf_all)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'staf': staf})

def otziv(request):
    return render(request, 'main/otziv.html')

def order(request):
    return render(request, 'main/order.html')


def add(request):
    error = ""
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ServiceForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/add.html', context)


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = '/'
    template_name = 'main/task-delete.html'

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'main/create.html'
    form_class = ServiceForm
    success_url = '/'
