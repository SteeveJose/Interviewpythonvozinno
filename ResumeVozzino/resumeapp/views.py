from django.shortcuts import render,redirect
from resumeapp.models import personaldetails
from resumeapp.forms import ResumeCreateForm,ResumeEditForm,Searchform,Registrationform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="loginpage")
def createResume(request):
    form=ResumeCreateForm()
    context={}
    context['form']=form
    data=personaldetails.objects.all()
    context['resume']=data
    if(request.method=="POST"):
        form=ResumeCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return redirect("createresume")
    return render(request,"resumeapp/createResume.html",context)

@login_required(login_url="loginpage")
def ResumeEdit(request,pk):
    obj=personaldetails.objects.get(id=pk)
    form=ResumeEditForm(instance=obj)
    context={}
    context['form'] = form
    if request.method=="POST":
        form=ResumeCreateForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("createresume")
        else:
            context = {}
            context['form'] =ResumeEditForm(request.POST)
            return render(request, "resumeapp/resumeedit.html", context)
    return render(request,"resumeapp/resumeedit.html",context)

@login_required(login_url="loginpage")
def ResumeView(request,pk):
    obj = personaldetails.objects.get(id=pk)
    context = {}
    context['Resume'] = obj
    return render(request, "resumeapp/resumeView.html", context)

@login_required(login_url="loginpage")
def index(request):
    form=personaldetails.objects.all()
    context={}
    context['resume']=form
    form = Searchform()
    context['search'] = form
    if request.method=="POST":
        form=Searchform(request.POST)
        if form.is_valid():
            print("hello")
            Name=form.cleaned_data.get("Full_Name")
            print(Name)
            Resume=personaldetails.objects.filter(Full_Name=Name)
            context['resume']=Resume
            return render(request, "resumeapp/index.html", context)

    return render(request,"resumeapp/index.html",context)

@login_required(login_url="loginpage")
def Resumeoperation(request):
    obj=personaldetails.objects.all()
    context={}
    context['form']=obj
    return render(request, "resumeapp/resumeoperation.html", context)

@login_required(login_url="loginpage")
def ResumeDelete(request,pk):
    entry=personaldetails.objects.get(id=pk)
    entry.delete()
    form = ResumeCreateForm()
    context = {}
    context['form'] = form
    qs = personaldetails.objects.all()
    context["resume"] = qs
    return redirect("resumeOperation")


def register(request):
    form=Registrationform()
    context={}
    context['form']=form
    if request.method=="POST":
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
        else:
            context["form"]=form
            return render(request, "resumeapp/Registration.html", context)

    return render(request,"resumeapp/Registration.html",context)


def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        print(username,",",password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("loginpage")
    return render(request,"resumeapp/login.html")

def logOut(request):
    logout(request)
    return redirect("loginpage")


def userIndex(request):
    form=personaldetails.objects.all()
    context={}
    context['resume']=form
    form = Searchform()
    context['search'] = form
    if request.method=="POST":
        form=Searchform(request.POST)
        if form.is_valid():
            print("hello")
            Name=form.cleaned_data.get("Full_Name")
            print(Name)
            Resume=personaldetails.objects.filter(Full_Name=Name)
            context['resume']=Resume
            return render(request, "resumeapp/userindex.html", context)

    return render(request,"resumeapp/userindex.html",context)

def publicresumeView(request,pk):
    obj = personaldetails.objects.get(id=pk)
    context = {}
    context['Resume'] = obj
    return render(request, "resumeapp/publicResumeView.html", context)








