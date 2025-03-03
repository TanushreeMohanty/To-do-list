from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Todo.objects.create(task=task)
        return redirect('todo_list')
    
    return render(request, 'todo_list.html', {'todos': todos})

def toggle_done(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('todo_list')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
