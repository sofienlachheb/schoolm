from django.shortcuts import render, redirect
from .models import Student, Grade
from note.models import Note
from .forms import StudentForm
from grades.forms import GradeForm
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile
import openpyxl
import os

def student_list_notes(request):
     grades = Grade.objects.all()  # Fetch all grades for the dropdown
     try:
      selected_grade = int(request.GET.get('grade'))
     except (ValueError, TypeError):
      selected_grade = None
    
     students = Student.objects.filter(grade_id=selected_grade) if selected_grade else []

     notes = Note.objects.filter(student__grade_id=selected_grade) if selected_grade else []
     paginator = Paginator(students, 5) # 3 posts in each page
     page = request.GET.get('page')
     try:
            posts = paginator.page(page)
     except PageNotAnInteger:
    # If page is not an integer deliver the first page
      posts = paginator.page(1)
     except EmptyPage:
           # If page is out of range deliver last page of results
      posts = paginator.page(paginator.num_pages)
     context = {
        'grades': grades,
        'students': students,
        'notes': notes,
        'selected_grade': selected_grade,
        'page': page,
        'posts': posts
    }
     return render(request, 'students/student_list_notes.html', context)
 
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            uploaded_file = UploadedFile(file=file)
            uploaded_file.save()
            # Read Excel data using openpyxl
            wb = openpyxl.load_workbook(file)
            sheet = wb.active
            data = []
            for row in sheet.iter_rows(values_only=True):
                data.append(list(row))
            return render(request, 'students/file_list.html', {'data': data})
    else:
        form = FileUploadForm()
    return render(request, 'students/upload_file.html', {'form': form})

def student_dashboard(request):
    
    grades = Grade.objects.all()
    selected_grade = request.GET.get('grade')
    students = Student.objects.all()
    student_count = students.count() 
    if selected_grade:
        students = students.filter(grade__name=selected_grade)
    
    paginator = Paginator(students, 5) # 3 posts in each page
    page = request.GET.get('page')
    try:
            posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
     posts = paginator.page(1)
    except EmptyPage:
           # If page is out of range deliver last page of results
     posts = paginator.page(paginator.num_pages)
    return render(request, 'students/student_dashboard.html', 
                  {
                   'students': students,
                   'grades': grades,'page': page,
                   'posts': posts,
                   'student_count':student_count,
                   })
    

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الطالب بنجاح!')
            return redirect('students:student_dashboard')
    else:
        form = StudentForm()
    return render(request, 'students/student_add.html', {'form': form})

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:student_dashboard')
    return render(request, 'students/student_delete.html', {'student': student})