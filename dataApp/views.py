from django.shortcuts import render, redirect
from .forms import UserDetailsForm, GroupDetailsForm

from django.http import HttpResponse
 
from .models import UpcomingProgram

def home_view(request):
    return render(request, 'dataApp/home.html')
 
def home_view_upcoming_programs(request):
    upcoming_programs = UpcomingProgram.objects.all().order_by('-id')[:4]  # Get latest 4 programs
    context = {'upcoming_programs': upcoming_programs}
    return render(request, 'dataApp/home_home_view_upcoming_programs.html', context)
 
def data_protection_statement(request):
  context = {}
  return render(request, 'dataApp/data_protection_statement.html', context)


def user_details_view(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page (create later)
    else:
        form = UserDetailsForm()
    return render(request, 'dataApp/user_details.html', {'form': form})

def success_view(request):
    return render(request, 'dataApp/success.html')


def group_details_view(request):
        if request.method == 'POST':
            form = GroupDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')

            else:
                return render(request, 'dataApp/group_details.html', {'form': form})
        else:
            form = GroupDetailsForm()
            return render(request, 'dataApp/group_details.html', {'form': form})
     
   