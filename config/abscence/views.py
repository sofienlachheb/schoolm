from django.shortcuts import render,get_object_or_404, redirect
from .models import Abscence
from .forms import AbscenceForm
from django.db import IntegrityError
from main.decorators import allow_user
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
################################## to add  abscence ###################################
@allow_user(['is_superuser', 'is_manager'])
def abscence_add(request):
    
    if request.method == 'POST':
        form = AbscenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abscence:abscence_list')
    else:
        form = AbscenceForm()
    return render(request, 'abscence/abscence_add.html',{'form':form})

#######################################show all students ####################################
@allow_user(['is_superuser', 'is_manager'])
def abscence_list(request):
    abscences=Abscence.objects.all()
    paginator = Paginator(abscences, 7)
    page = request.GET.get('page')
    try:
       abscences = paginator.page(page)
    except PageNotAnInteger:
          abscences= paginator.page(1)
    except EmptyPage:
          abscences = paginator.page(paginator.num_page)
    context = {
              'title': 'قائمةالغيابات',
              'abscences':abscences,
              'page': page,
             } 
    return render(request,'abscence/abscence_list.html',context)
 
################################### To update information sof student ######################
@allow_user(['is_superuser', 'is_manager'])
def abscence_edit(request,pk):
    
    absence = get_object_or_404(Abscence, pk=pk)
    if request.method == 'POST':
        form = AbscenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('abscence:abscence_list')
    else:
        form = AbscenceForm(instance=absence)
    return render(request, 'abscence/abscence_edit.html', {'form': form})
   

################################ To delete a student ####################################
def abscence_delete(request,pk):
    absence = get_object_or_404(Abscence, pk=pk)
    if request.method == 'POST':
        absence.delete()
        return redirect('abscence:abscence_list')
############################################################## 
def absence_view(request, pk):
    absence = get_object_or_404(Abscence, pk=pk)
    return render(request, 'abscence/absence_view.html', {'absence': absence})
############################################################################################# 
