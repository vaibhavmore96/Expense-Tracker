from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
#from django.contrib.auth.models import User,Expense
#from django.addexpense import Expense
#from APP.models import Expense
#from django.contrib.auth.models import category,auth
from django.template.context_processors import request

from .models import Expense

# Create your views here.


def Index(request):
    return render(request,"APP/Index.html")
# return HttpResponse(Index)

def abount_us(request):
    return render(request,"APP/about.html")

def contact(request):
    return render(request,"APP/contact.html")

def Register(request):
    if request.method =='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cpass')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('User_Name is already taken...')
                return redirect('Register')
            if User.objects.filter(email=email).exists():
                print("Email is already used....")
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print("User created Successfully.....!")
                return redirect('login')
        else:
            print("Password does not match.")
            return redirect('Register')
    else:
        return render(request,"APP/Register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("Invalid Credentials... ")
            return redirect('login')
    else:
         return render(request, "APP/login.html")

def logout(request):
    auth.logout(request)
    print("logout")
    return redirect('/')
    return render(request, "APP/logout.html")


def addexpense(request):
   if request.method == 'POST':
      Category = request.POST.get('Category')
      Items = request.POST.get('Items')
      Amount = request.POST.get('Amount')
      Date = request.POST.get('Date')
      Exp = Expense.objects.create(Category=Category, Items=Items, Amount=Amount, Date=Date)
      Exp.save()
      print("Expense created Successfully.....!")
      return redirect ('addexpense')
   else:
        return render(request, "APP/addexpense.html")
