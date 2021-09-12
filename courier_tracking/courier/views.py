from django.http.response import HttpResponseRedirect
from courier.models import Login, Signup
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

user= None
Admin=False

def index(request):
    return render(request, 'index.html', {"user" : user, "Admin":Admin })

def track(request):
    return render(request, 'track.html')

def sign(request):
    global user, Admin
    if request.method == 'POST' :
        u_name = request.POST['uname']
        p_code = request.POST['passcode']
        obj = Login.objects.filter(uname=u_name, password=p_code).first()
        if obj:
            user = str(u_name)
            user = user[:user.index('@')]
            if user == "admin":
                Admin=True
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'account.html',{"user" : user, "Admin":Admin })
    else:
        return render(request, 'account.html',{"user" : user, "Admin":Admin } )
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
            return render(request, 'account.html',{"user" : user, "Admin":Admin })
        else :
            return HttpResponseRedirect(reverse('index'))
def contact(request):
    return render(request, 'contact.html',{"user" : user, "Admin":Admin })

def viewuser(request):
    data = Signup.objects.all()
    d = {'data' : data}
    if Admin:
        return render(request, 'viewuser.html', d)
    else:
        return HttpResponseRedirect(reverse('index'))

def logout(request):
    global Admin, user
    if Admin or user:
        Admin = False
        user = None
    return HttpResponseRedirect(reverse('index'))

def deleteuser(request, demail):
    global Admin
    if Admin:
        Signup.objects.get(email=demail).delete()
        return HttpResponseRedirect(reverse('viewuser'))
    else:
        return HttpResponseRedirect(reverse('index'))