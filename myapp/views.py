from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject #Esto importa la clase

# Create your views here.
def index(request):
    title = "Django Course!!!!!!!!!!!!"
    return render(request, "index.html", {"title": title})

def hello(request, username):
    return HttpResponse(f"<h1>Hola {username}</h1>")

def about(request):
    username = 'Lisandro'
    return render(request, "about.html", {
        "name": username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "Projects/projects.html", {
        "projects": projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "Tasks/tasks.html",{
        "tasks":tasks
    })

def tasks2(request, title):
    
    try:
        tasks = get_object_or_404(Task, title=title)
        return HttpResponse(f"task: {tasks.title}")
    except:
        return HttpResponse("<h1>No Funco</h1>")
    
def create_task(request):

    if request.method == 'GET':
        #show interface
        return render(request, "Tasks/create_task.html",{
            "form": CreateNewTask() 
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)              
        return redirect('tasks')    

def create_project(request):
    
    if request.method == 'GET':
        return render(request, "Projects/create_project.html",{
            "form": CreateNewProject()  
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'Projects/detail.html', {
        'project':project,
        'tasks':tasks
    })
