from django.shortcuts import render, redirect
from login.models import details
from django.contrib.auth import authenticate, login
# from login.models import passwords
from django.contrib import messages
# Create your views here.


def log(request):
    val = False
    return render(request, 'TAFlog.html')


def signup(request):
    if request.method == 'POST':
        Uname = request.POST['email']
        if details.objects.filter(username=Uname).exists():
            messages.error(request, 'Email/Username already exixts')
            return redirect('log')
        else:
            pass1 = request.POST['pass']
            pass2 = request.POST['conpass']
            if pass1 != pass2:
                messages.error(request, "Entered passwords didn't match")
                return redirect('log')
            else:
                en = details(username=Uname, pas=pass1)
                en.save()
                messages.success(request, 'Sucessfully created account')
                return redirect('log')

    else:
        return redirect('log')


def loginn(request):

    if request.method == 'POST':
        em = request.POST['email']
        if details.objects.filter(username=em).exists():
            pa = request.POST['pass']
            user = details.objects.get(username=em)
            cp = user.pas
            if pa == cp:
                val = True
                # passes = passwords.objects.filter(username=em).all()
                context = {'em': em, 'val': val}
                return render(request, 'menu.html', context)
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('log')
        else:
            messages.error(request, 'Username does not exist')
            return redirect('log')

    else:
        return redirect('log')
