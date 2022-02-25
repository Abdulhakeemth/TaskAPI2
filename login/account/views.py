from django.shortcuts import redirect, render
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexView(request):
    return render(request,'index.html')
      
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()    
    return render(request,'registeration/register.html',{'form':form})
   

