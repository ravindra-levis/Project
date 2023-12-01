from django.shortcuts import render,redirect
from .forms import AssignmentForm
from .models import Assignment

# Create your views here.
def assignment_list(request):
    assignments=Assignment.objects.all()
    return render(request,'assignment_list.html',{
        'assignments': assignments
    })

def upload_assignment(request):
    if request.method =="POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'upload_assignment.html', {
        'form': form
    })