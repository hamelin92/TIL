from django.shortcuts import *
from .forms import TodoForm
from .models import Todo
from django.views.decorators.http import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    todos = Todo.objects.filter(author=request.user)
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)
