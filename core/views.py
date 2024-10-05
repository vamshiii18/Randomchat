from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import signupform  # Assuming your form is named SignupForm with capital S

def frontpage(request):
    return render(request, 'core/frontpage.html')

def support_page(request):
    website_details = {
        "name": "Walki Talkie",
        "description": "Walki Talkie is a platform for instant conversations, anytime, anywhere.",
        "contact_email": "support@walkitalkie.com"
    }
    return render(request, 'core/support.html', website_details)

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = signupform()

        
    
    return render(request, 'core/signup.html', {'form': form})

