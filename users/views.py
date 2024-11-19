from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method =='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f' Your Account created , Please Login !')
            return redirect('login')
    else:
        form=UserRegisterForm() # making an instance of default form
    return render(request,'users/register.html',{'form':form}) #passing the instance as context
