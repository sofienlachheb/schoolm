from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassGradeForm, GradeNameFormSet, GradeForm
from .models import ClassGrade, GradeName, Grade


def grade_add(request, pk=None):
    class_grade = get_object_or_404(ClassGrade, pk=pk) if pk else None

    class_grade_form = ClassGradeForm(request.POST or None, instance=class_grade)
    grade_name_formset = GradeNameFormSet(request.POST or None, instance=class_grade)

    if request.method == 'POST':
        if class_grade_form.is_valid():
            class_grade = class_grade_form.save()
            grade_name_formset.instance = class_grade
            if grade_name_formset.is_valid():
                grade_name_formset.save()
                return redirect('grades:grade_list')

    return render(request, 'grades/grade_add.html', {
        'class_grade_form': class_grade_form,
        'grade_name_formset': grade_name_formset,
    })
def grade_list(request):
    classgrades = ClassGrade.objects.all()
    gradenames= GradeName.objects.all()
    grades = Grade.objects.all()
    context={
        'classgrades':classgrades,
        'gradenames':gradenames,
        'grades':grades,
    }
    return render(request,'grades/grade_list.html',context)
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