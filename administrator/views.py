from django.shortcuts import render




# Create your views here.
def home(request): 
    return render(request, 'admin_homepage.html', {'schoolname' : 'DevSkill'} )

def profile(request):
    return render(request, 'admin_homepage.html')

def rules(request, a):
    print(a)
    return render(request, 'admin_homepage.html')

def invoiveinfo(request):
    return render(request, 'admin_homepage.html')
