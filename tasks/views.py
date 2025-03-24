from django.shortcuts import get_object_or_404, redirect, render

from .models import Task
from .forms import TaskForm

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
