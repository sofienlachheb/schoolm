from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Parent
from .forms import ParentForm
import pandas as pd
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import Parent
from django.http import HttpResponseRedirect
##############################################################################

def parent_dashboard(request):
    parents=Parent.objects.all()
    parent_count=parents.count()
    context={'parent count':parent_count}
    return render(request,'parents/parent_dashboard.html',context)

#@allow_user(['is_superuser','is_manager'])
def parent_panel(request):
    parents=Parent.objects.all()
    paginator = Paginator(parents, 10)
    page = request.GET.get('page')
    try:
       parents = paginator.page(page)
    except PageNotAnInteger:
       parents= paginator.page(1)
    except EmptyPage:
       parents = paginator.page(paginator.num_page)
    context={'parents':parents,
             'page': page,}
    return render(request,'parents/parent_panel.html',context)
########################################################################
#@allow_user(['is_superuser','is_manager'])
def parent_add(request):
    context={}
    
    if request.method=='POST':
        form =ParentForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'success_message':'parent added successfully!'}
            
            return redirect(reverse('parents:parent_panel'))
    else:
          form=ParentForm()
          context['form'] = form
   
    return render(request,'parents/parent_add.html',context)
############################################################################
#@allow_user(['is_superuser','is_manager'])
def parent_edit(request, pk):
    parent = get_object_or_404(parent, pk=pk)
    if request.method == "POST":
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect(reverse('parents:parent_dashboard'))
    else:
        form = ParentForm(instance=parent)
    return render(request,'parents/parent_edit.html',{'form': form})
##############################################################################   
#@allow_user(['is_superuser','is_manager'])
def parent_delete(request,pk):
     parent = get_object_or_404(Parent,pk=pk)
     parent.delete()
     return HttpResponseRedirect(reverse('parents:parent_dashboard'))
  
 ##########################################################################################     
def parent_profile(request,pk):
    parent = get_object_or_404(parent, pk=pk)
    return render(request,'parents/parent_profile.html',{'parent': parent})

##########################################################################################     
def import_parents(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_excel(file)
        for _, row in df.iterrows():
            parent = Parent(
                parentName=row['parentName'],
                parentPhone=row['parentPhone'],
                
            )
            parent.save()
        return render(request,'parents:parent_dashboard')
    return render(request,'parents/import_parents.html')