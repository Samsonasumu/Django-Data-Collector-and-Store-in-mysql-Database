from django.shortcuts import render, redirect
from .forms import UserDetailsForm, GroupDetailsForm, SportsDetailsForm,PersonForm, BusinessForm
from django.http import HttpResponse
from .models import UpcomingProgram, Person
      
def home_view(request):
    return render(request, 'dataApp/home.html')
 
def upcoming_programs(request):
    upcoming_programs = UpcomingProgram.objects.all().order_by('-id')[:4]  # Get latest 4 programs
    context = {'upcoming_programs': upcoming_programs}
    return render(request, 'dataApp/upcoming_programs.html', context)
 
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
     
def sports_details_view(request):
        if request.method == 'POST':
            form = SportsDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')

            else:
                return render(request, 'dataApp/sport.html', {'form': form})
        else:
            form = SportsDetailsForm()
            return render(request, 'dataApp/sport.html', {'form': form})

 
def success(request):
    # Add content to this view as needed, e.g., a success message or a link
    return render(request, 'dataApp/success_url.html')  # Render the success te

 
def successbiz(request):
    pk = 1  # Example pk, this could be dynamically retrieved
    return render(request, 'dataApp/sucess-biz.html', {'pk': pk})

def add_business(request, pk):
  person = Person.objects.get(pk=pk)  # Get the person instance based on ID
  if request.method == 'POST':
    form = BusinessForm(request.POST)
    if form.is_valid():
      business = form.save(commit=False)  # Don't save yet
      business.person = person  # Assign the person to the business
      business.save()
      return redirect('successbiz')
  else:
    form = BusinessForm(initial={'person': person})  # Pre-fill person field
  return render(request, 'dataApp/add_business.html', {'form': form})


def create_person(request):
  if request.method == 'POST':
    form = PersonForm(request.POST)
    if form.is_valid():
      person = form.save()  # Save person first and get the instance
      return redirect('add_business', person.pk)  # Redirect to add_business with person ID
  else:
    form = PersonForm()
  return render(request, 'dataApp/create_person.html', {'form': form})
