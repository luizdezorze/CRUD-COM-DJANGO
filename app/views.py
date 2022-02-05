from django.shortcuts import render, redirect
from app.forms import TratametosForm
from app.models import Tratamentos
from django.core.paginator import Paginator


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Tratamentos.objects.filter(paciente__icontains=search)
    else:
        data['db'] = Tratamentos.objects.all()

    # all = Tratamentos.objects.all()
    # paginator = Paginator(all, 7)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, "index.html", data)


def form(request):
    data = {}
    data['form'] = TratametosForm()
    return render(request, 'form.html', data)


def create(request):
    form = TratametosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Tratamentos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Tratamentos.objects.get(pk=pk)
    data['form'] = TratametosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Tratamentos.objects.get(pk=pk)
    form = TratametosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, pk):
    db = Tratamentos.objects.get(pk=pk)
    db.delete()
    return redirect('home')