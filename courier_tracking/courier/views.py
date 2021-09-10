from django.http.response import HttpResponseRedirect
from courier.models import Login, Signup
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

user=None
def index(request):
    return render(request, 'index.html', {"user" : user })

def sign(request):
    global user
    if request.method == 'POST' :
        u_name = request.POST['uname']
        p_code = request.POST['passcode']
        obj = Login.objects.filter(uname=u_name, password=p_code)
        if obj:
            user = str(u_name)
            user = user[:user.index('@')]
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'account.html')
    else:
        return render(request, 'account.html' )
def signup(request):
    error = True
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['uname']
        phone = request.POST['phone']
        passcode = request.POST['passcode']
        try:
            Signup.objects.create(user=name, mobile=phone, email=email, password=passcode)
            Login.objects.create(uname=email, password=passcode)
            error=False
        except:
            error = True
        d = {'error' : error}
        if error:
            return render(request, 'account.html')
        else :
            return HttpResponseRedirect(reverse('index'))
def contact(request):
    return render(request, 'contact.html')