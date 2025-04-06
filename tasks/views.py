from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages
import datetime

@login_required
def taskList(request):
    tarefas_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
    paginator = Paginator(tarefas_list, 3)
    page = request.GET.get('page')

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    taskDoneRecently = Task.objects.filter(status='realizado',
    update_at__gt=datetime.datetime.now() - datetime.timedelta(days=30),
    user=request.user).count()

    taskDone = Task.objects.filter(status='realizado', user = request.user).count()
    taskDoing = Task.objects.filter(status='andamento', user = request.user).count()
    if search:
        tarefas = Task.objects.filter(titulo__icontains=search, user = request.user)

    elif filter:
        tarefas = Task.objects.filter(status=filter, user = request.user)
 
    else:
        tarefas = paginator.get_page(page)


    return render(request, 'tasks/list.html', {'tarefas':tarefas, 'taskDoneRecently':taskDoneRecently, 'taskDone':taskDone, 'taskDoing':taskDoing})

@login_required
def taskView(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tarefa':tarefa})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'andamento'

            task.user = request.user
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form':form})

@login_required
def editTask(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=tarefa)

        if(form.is_valid()):
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form':form, 'tarefa':tarefa})
    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'tarefa':tarefa})

@login_required
def deleteTask(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    tarefa.delete()

    messages.info(request, 'Tarefa deletada com sucesso!!!')
    return redirect('/')

@login_required
def changeStatus(request, id):
    tarefa = get_object_or_404(Task, pk=id)

    if(tarefa.status == 'andamento'):
        tarefa.status = 'realizado'
    else:
        tarefa.status = 'andamento'
    
    tarefa.save()

    return redirect('/')