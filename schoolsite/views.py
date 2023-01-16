from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'school_homepage.html')

def facultyStaff(request, fs, settingvar):
    print(fs)
    print(settingvar)
    return render(request, 'school_homepage.html')
