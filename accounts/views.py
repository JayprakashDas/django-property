from django.shortcuts import render, redirect
from django.contrib import messages
#user model by default django creates
from django.contrib.auth.models import User, auth
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method=='POST':
        ##register USER
        #GET FORM VALUES
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        ##Checkif Password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is used')
                    return redirect('register')
                else: 
                    ##finaly register done
                    user = User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    #login after register
                    # auth.login(request,user)
                    # messages.success(request,'You are logged in')
                    # return redirect('index')
                    
                    #to save only
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request,'Password Do not Match ')
            return redirect('register')
    else:       
        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        ##LOGIN USER
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalaid Crdentials')           
    else:   
        return render(request,'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'you are loggred out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)