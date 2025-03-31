from django.shortcuts import render, redirect
from App1.models import Portfolio
from App1.forms import PortfolioForm

def index(request):
    return render(request, 'App1/index1.html')

def submit_form(request):
    sentdata = False
    form = PortfolioForm()  # Use the correct form
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            sentdata = True
            form.save()
            return redirect('success')  # Redirect to success page
    
    return render(request, 'App1/index1.html', {'form': form, 'sentdata': sentdata})

def success_view(request):
    return render(request, 'App1/submit.html')  # This renders the success page
