from django.shortcuts import render
from bill.forms import *
from .models import RetObject
from .utils import back

# Create your views here.


# THE VIEW
def login(request):
    if request.method == 'POST':
        MyForms = LoginForm(request.POST)
        if MyForms.is_valid():
            back(MyForms.data.get("email"), MyForms.data.get("password"))
            # GET ALL OBJECT OF THE RIGHT EMAIL
            bills_list = RetObject.objects.filter(email=MyForms.data.get("email"))
            context = {'bills_list': bills_list}
            if not bills_list:
                return render(request, 'login.html', {"form": MyForms, "error": "error"})
            return render(request, 'loggedin.html', context)
    else:
        MyForms = LoginForm()
    return render(request, 'login.html', {"form": MyForms})
