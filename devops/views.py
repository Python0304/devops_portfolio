from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')


# main/views.py ichida
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f"Portfolio Contact from {name}",
            message=message,
            from_email=email,
            recipient_list=['youremail@example.com'],
        )
        return redirect('/')
    return render(request, 'devops/index.html')
