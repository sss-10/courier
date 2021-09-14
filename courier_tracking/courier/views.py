from django.http.response import HttpResponseRedirect
from courier.models import Login, Signup, Orders
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

user= None
em=None
Admin=False

def index(request):
    return render(request, 'index.html', {"user" : user, "Admin":Admin, "em" : em })

def track(request):
    return render(request, 'track.html')

def sign(request):
    global user, Admin, em
    if request.method == 'POST' :
        u_name = request.POST['uname']
        p_code = request.POST['passcode']
        obj = Login.objects.filter(uname=u_name, password=p_code).first()
        if obj:
            user = str(u_name)
            em = str(u_name)
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
        img = request.FILES["photo"]
        try:
            Signup.objects.create(user=name, mobile=phone, email=email, password=passcode, image=img)
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

def bookorder(request):
    error = False
    if request.method=="POST":
        pname = request.POST['pname'] 
        pmail = request.POST['pemail'] 
        pphone = request.POST['pcontact'] 
        porder = request.POST['porder'] 
        pdate = request.POST['pdate'] 
        psid = request.POST['psid'] 
        psidno = request.POST['psidno'] 
        pweight = request.POST['pweight'] 
        paddress = request.POST['paddress']   
        pstatus = request.POST['pstatus']
        try:
            Orders.objects.create(rname=pname, rmail=pmail, rphone=pphone, rorder=porder, rdate=pdate, rsid=psid, rsidno=psidno, rweight=pweight, raddress=paddress, rstatus=pstatus) 
            error=False
        except:
            error=True
        if error:
            return render(request,'contact.html')
        else:
            return HttpResponseRedirect(reverse('index')) 
    else :
        return render(request,'BookOrder.html')

def vieworder(request):
    data = Orders.objects.all()
    d = {'data' : data}
    if Admin:
        return render(request, 'vieworder.html', d)
    else:
        return HttpResponseRedirect(reverse('index'))

def profile(request):
    global em
    data = Signup.objects.get(email=em)
    return render(request, 'profile.html', {'data':data})