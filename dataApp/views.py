from django.shortcuts import render, redirect
from .forms import UserDetailsForm

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