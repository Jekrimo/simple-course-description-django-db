from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    context = {
        "Course" : Course.objects.all()
    }
    print (Course)
    return render(request, 'coursesapp/index.html', context)

def create(request):
    Course.objects.create(course_name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def confirm(request, id):
    confirm = Course.objects.get(id=id)
    print (confirm.course_name)
    context = {
        'confirm' : confirm
    }
    print (confirm.description)
    return render(request, 'coursesapp/die.html', context)

def kill(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
