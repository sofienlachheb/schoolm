from django.shortcuts import render

from django.shortcuts import render, redirect
from grades.models import  Grade
from grades.forms import GradeForm

def grade_list(request):
    grades = Grade.objects.all()
    grade_count = Grade.objects.count()
    
    context={ 'grades': grades,
              'grade_count':grade_count,
        
    }
    return render(request, 'grades/grade_list.html', context)

def grade_add(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades:grade_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_add.html', {'form': form})

def grade_edit(request, pk):
    grade = Grade.objects.get(pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades:grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_edit.html', {'form': form})

def grade_delete(request, pk):
    grade = Grade.objects.get(pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grades:grade_list')
    return render(request, 'grades/grade_delete.html', {'grade': grade})