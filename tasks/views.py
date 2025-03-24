from django.shortcuts import get_object_or_404, redirect, render

from .models import Task
from .forms import TaskForm
from django.contrib import messages

def taskList(request):
    tarefas = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tarefas':tarefas})

def taskView(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tarefa':tarefa})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'andamento'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form':form})

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

def deleteTask(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    tarefa.delete()

    messages.info(request, 'Tarefa deletada com sucesso!!!')
    return redirect('/')