from django.shortcuts import render
from .models import Workers, Professions, WorkerProfession
from .forms import WorkersForm, ProfessionsForm
from django.views.generic import DetailView, UpdateView


def workers_home(request):
    w = Workers.objects.all()
    wp = WorkerProfession.objects.all()
    p = Professions.objects.all()
    return render(request, 'workers/workers_home.html', {'worker': w, 'prof': p, 'worker_prof': wp})


class WorkerDetailView(DetailView):
    model = Workers
    template_name = 'workers/detail_view.html'
    context_object_name = 'worker'


class WorkerUpdateView(UpdateView):
    model = Workers
    template_name = 'workers/update.html'
    form_class = WorkersForm


def update(request):
    error = ''
    form = WorkersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'workers/update.html', data)


def add(request):
    error = ''
    if request.method == 'POST':
        form1 = WorkersForm(request.POST)
        form2 = ProfessionsForm(request.POST)
        w = Workers.objects.all()
        if form1.is_valid() and form2.is_valid():
            worker = Workers(name=form1.cleaned_data.get("name"), phone=form1.cleaned_data.get("phone"),
                             email=form1.cleaned_data.get("email"))
            worker_info = [form1.cleaned_data.get("name"), form1.cleaned_data.get("phone"),
                           form1.cleaned_data.get("email")]
            w_list = []
            for el in w:
                w_list.append([el.name, el.phone, el.email])
            if worker_info not in w_list:
                worker.save()
                error += "Пользователь добавлен."
            else:
                for el in w:
                    if worker_info[0] == el.name and worker_info[1] == el.phone and worker_info[2] == el.email:
                        worker = el
                error += "Пользователь уже существует."
            prof_form = Professions(profession=form2.cleaned_data.get("profession"))
            p = Professions.objects.all()
            wp_list = WorkerProfession.objects.all()
            k = 0
            for el in p:
                if prof_form.profession == el.profession:
                    prof_form = el
                    k = 1
            if k == 0:
                prof_form.save()
                error += "Добавлена профессия в список профессий."
            k = 0
            for wp in wp_list:
                if wp.worker.name == worker.name and wp.worker.phone == worker.phone and\
                                wp.prof.profession == prof_form.profession:
                    error += "Такая профессия у данного работника уже существует."
                    k = 1
            if k == 0:
                worker_profession = WorkerProfession(worker=worker, prof=prof_form)
                worker_profession.save()
                error += "Добавлена профессия к данному работнику."
        else:
            error = 'Неверно заполнены данные или такой пользователь уже есть'
    form1 = WorkersForm()
    form2 = ProfessionsForm()
    data = {
        'form1': form1,
        'form2': form2,
        'error': error
    }
    return render(request, 'workers/add.html', data)

