from django.shortcuts import get_object_or_404, render

from .models import Task

def taskList(request):
    tarefas = Task.objects.all()
    return render(request, 'tasks/list.html', {'tarefas':tarefas})

def taskView(request, id):
    tarefa = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tarefa':tarefa})