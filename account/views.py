from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,'account.html',{'form' : form})


    else : 
        form = LoginForm()
        return render(request,'account.html',{'form' : form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) #우리가 폼으로 받은 데이터를 유저로 만들어야하기 때문에
        if form.is_valid():
            user = form.save()
            login(request,user) # 회원가입 하자마자 로그인 된상태
            return redirect('home')

    else : 
        form = RegisterForm()
        return render(request,'account.html',{'form' : form})
    