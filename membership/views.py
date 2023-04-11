from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file
from .models import Monthly
# from django.core.validators import RegexValidator
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from .models import User
# from .forms import UserForm


# Create your views here.

def index(request):
    return render(request, "membership/index.html", {})

@login_required(login_url='/signin/')
def home(request):
    return render(request, "membership/home.html", {})

@login_required(login_url='/signin/')
def admin_view(request):
    User = get_user_model()
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, "membership/adminpage.html", context)

@login_required(login_url='/signin/')
def monthly_form(request):

    if request.method == "POST":
        # full_name = request.POST['full_name']
        # age = request.POST['age']
        # adress = request.POST.get['adress']
        # contact_no = request.POST['contact_no']
        # weight = request.POST['weight']
        # height = request.POST['height']
        # em_fullname = request.POST['em_fullname']
        # relationship = request.POST['relationship']
        # em_contactno = request.POST['em_contactno']
        # em_email = request.POST['em_email']
        full_name = request.POST.get('fullname')
        age = request.POST.get('age')
        adress = request.POST.get('adress')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        em_fullname = request.POST.get('em_fullname')
        relationship = request.POST.get('relationship')
        em_contactno = request.POST.get('em_contactno')
        em_email = request.POST.get('em_email')
        file = handle_uploaded_file(request.FILES.get('file'))

        monthlyform = Monthly(full_name=full_name, age=age, adress=adress, contact_no=contact_no, email=email, weight=weight, height=height, em_fullname=em_fullname, relationship=relationship, em_contactno=em_contactno, em_email=em_email, file=file)
        monthlyform.save()
        messages.success(request, "Monthly membership subscribed successfully!")
        return redirect('home')
    
    return render(request, "membership/monthlyform.html", {})

def signup_view(request):
    context = {}
    if request.method == "POST":
        email = request.POST['email']
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        context["email"] = email
        context["user_name"] = user_name
        context["first_name"] = first_name
        context["last_name"] = last_name

        User = get_user_model()
        if User.objects.filter(email=email):
            messages.error(request, "Email already exist! Please try a different email.")
            return render (request, 'membership/signup.html', context)

        if User.objects.filter(user_name=user_name):
            messages.error(request, "Username already exist! Please try a different username.")
            return render (request, 'membership/signup.html', context)

        if not user_name.isalnum():
            messages.error(request, "Username must be Alpha-Numerical!")
            return render (request, 'membership/signup.html', context)
        
        if len(user_name)>16:
            messages.error(request, "Username must be under 16 characters.")
            return render (request, 'membership/signup.html', context)

        if password != confirm_password:
            messages.error(request, "Password do not match!") 
            return render (request, 'membership/signup.html', context)

        if len(password)<8:
            messages.error(request, 
            "Password must contain atleast 8 characters. Password must contain at least 1 number. Password must contain at least 1 uppercase letter. Password must contain at least 1 lowercase letter"
            )
            return render (request, 'membership/signup.html', context)
        
        if sum(c.isdigit() for c in password) < 1:
            messages.error(request, 
            "Password must contain atleast 8 characters. Password must contain at least 1 number. Password must contain at least 1 uppercase letter. Password must contain at least 1 lowercase letter"
            )
            return render (request, 'membership/signup.html', context)
        
        if not any(c.isupper() for c in password):
            messages.error(request, 
            "Password must contain atleast 8 characters. Password must contain at least 1 number. Password must contain at least 1 uppercase letter. Password must contain at least 1 lowercase letter"
            )
            return render (request, 'membership/signup.html', context)
        
        if not any(c.islower() for c in password):
            messages.error(request, 
            "Password must contain atleast 8 characters. Password must contain at least 1 number. Password must contain at least 1 uppercase letter. Password must contain at least 1 lowercase letter"
            )
            return render (request, 'membership/signup.html', context)

        myuser = User.objects.create_user(email, user_name, first_name, last_name, password)
        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render(request, "membership/signup.html", {})

def signin_view(request):
    context = {}
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        context["email"] = email
        
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:               
                    return redirect('adminpage')
            elif user.is_superuser==False:
                    first_name = user.first_name
                    return render(request, "membership/home.html", {'first_name': first_name})           
        else:
            messages.error(request, "Incorrect email or password.")
            return render (request, 'membership/signin.html', context)

    return render(request, "membership/signin.html", {})

def signout_view(request):
    
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')



# def register_view(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         password = request.POST["password"]
#         confirmation = request.POST["confirm_password"]
#         if password != confirmation:
#             messages.error(request, "Password must match.")
#             return redirect('register')
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful." )
#             return redirect('login')
#         messages.error(request, "Unsuccessful registration. Invalid information.")

#     form = UserForm()
#     return render(request, 'membership/register.html', {'form': form})


# def login_view(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             # messages.success(request, f"You are now logged in as {first_name}.")
#             return render(request, "membership/home.html", {})
#         else:
#             messages.error(request,"Invalid email or password.")
#     return render(request, "membership/login.html", {})


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'membership/signup.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'membership/login.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('home')
