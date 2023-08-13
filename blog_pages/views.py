from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import CV
from .models import Project


def index(request):
    context = {
        'message': 'Hello',
    }
    return render(request, 'blog_pages/index.html', context)


# def index(request):
#     # Fetch the latest project and findings here
#     latest_project = Project.objects.last()
#     context = {'latest_project': latest_project}
#     return render(request, 'index.html', context)

def cv(request):
    # Retrieve the CV object from the database
    cv = CV.objects.first()  # Assuming you want to retrieve the first CV object
    
    # Pass the CV object to the template
    return render(request, 'blog_pages/cv.html', {'cv': cv})


def projects(request):
    
    return render(request, 'blog_pages/projects.html')
    
# def projects(request):
#     all_projects = Project.objects.all()
#     context = {'projects': all_projects}
#     return render(request, 'myapp/projects.html', context)

# def add_comment(request):
#     if request.method == 'POST':
#         # Handle comment submission here, save to database, etc.
#         pass
#     return redirect('index')
