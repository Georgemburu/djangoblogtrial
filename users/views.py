from django.shortcuts import render
from .forms import UserForm,ProfilePicForm
from django.contrib.auth.views import LoginView
# Create your views here.
def CreateUser(request,*args,**kwargs):
    u_form = UserForm(request.POST or None)
    p_form = ProfilePicForm(request.POST, request.FILES, request.user or None)

    if request.POST:
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()

            u_form = UserForm()
            p_form = ProfilePicForm()

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, 'users/register.html',context)
    

def LoginUser(request,*args,**kwargs):
    return 2
