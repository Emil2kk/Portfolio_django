from django.shortcuts import render
from .models import Experience,Opinion,Portfolio,Blog,Contact,Education
from .forms import NameForm

def index(request):
    experiences=Experience.objects.all()
    opinions=Opinion.objects.all()
    projects=Portfolio.objects.all()
    blogs=Blog.objects.all()
    educations=Education.objects.all()
    form=NameForm()
    context = {'projects': projects, 'blogs': blogs,'form':form, 'experiences':experiences,'opinions':opinions , 'educations':educations}
    return render(request,'app/index.html ',context)

def contact(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ob = Connection()
            ob.your_name = form.cleaned_data['your_name']
            ob.email = form.cleaned_data['email']
            ob.message = form.cleaned_data['message']
            ob.save()
            context={}
            return render(request,'/index.html',context)
    else:
        form = NameForm()

    return render('/index.html')