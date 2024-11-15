from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Teacher
from grades.models import Grade
from .forms import TeacherForm
import pandas as pd
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
##############################################################################
def teacher_dashboard(request):
    return render(request,'teachers/teacher_dashboard.html')
#############################################################################
def teacher_grades(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    grades = teacher.grades.all()
    return render(request, 'teachers/teacher_grades.html', {'teacher': teacher, 'grades': grades})
##############################################################################
#@allow_user(['is_superuser','is_manager'])
def teacher_list(request):
    teachers=Teacher.objects.all()
    paginator = Paginator(teachers, 7)
    page = request.GET.get('page')
    try:
      teachers = paginator.page(page)
    except PageNotAnInteger:
         teachers= paginator.page(1)
    except EmptyPage:
          teachers = paginator.page(paginator.num_page)
    context = {
              'title': 'قائمةالمدرسين',
              'teachers':teachers,
              'page': page,
             } 
    return render(request,'teachers/teacher_list.html',context)
########################################################################
#@allow_user(['is_superuser','is_manager'])
def teacher_add(request):
    
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة المدرس بنجاح!')
            return redirect('teachers:teacher_list')
        
    else:
        form = TeacherForm()
        
    return render(request,'teachers/teacher_form.html', {'form': form})
############################################################################
#@allow_user(['is_superuser','is_manager'])
def teacher_edit(request,pk):
    context={}
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance= teacher)
        if form.is_valid():
            form = form.save(commit=False)
            
            messages.success(request, 'تم تعديل المدرس بنجاح!')
            return redirect('teachers:teacher_list')
    else:
        form =  TeacherForm(instance= teacher)
    context={'form':form}
    return render(request,'teachers/teacher_form.html',context)

##############################################################################   
#@allow_user(['is_superuser','is_manager'])
def teacher_delete(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    if request.method=="POST":
      teacher.delete()
      return redirect('teachers:teacher_list')
    return render(request, 'teachers/teacher_delete.html', {'teacher': teacher})
 ##########################################################################################     
def teacher_profile(request):
    # Get the teacher associated with the current logged-in user
    teacher = get_object_or_404(Teacher, user=request.user)
     # Count the number of grades the teacher teaches
    grades = teacher.grades.all()
    return render(request,'teachers/teacher_profile.html', {'teacher': teacher,'grades':grades})

##########################################################################################     
def import_teachers(request):
 if request.method == "POST":
        excel_file = request.FILES.get("excel_file")

        if not excel_file:
            return render(request, 'teachers/import_teachers.html', {'error': 'No file was uploaded.'})

        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            return render(request, 'teachers/import_teachers.html', {'error': 'Failed to read the Excel file. Please check the format.'})
        
        for index, row in df.iterrows():
            try:
                # الحصول على المستخدم أو إنشاؤه إذا لم يكن موجودًا
                user = User.objects.get_or_create(username=row['username'])

                # إنشاء أو تحديث المعلم
                teacher, created = Teacher.objects.get_or_create(
                    user=user,
                    teacherName=row['teacherName'],
                    defaults={
                        'teacherFunction': row['teacherFunction'],
                        'teacherPhone': row.get('teacherPhone', None),
                        'teacherEmail': row['teacherEmail']
                    }
                )

                # ربط المعلم بالدرجات (grades)
             
                teacher.save()

            except User.DoesNotExist:
                print(f"User {row['username']} does not exist")
                continue  # تخطي السجل إذا كان المستخدم غير موجود

        return redirect('teachers:teacher_list')

 return render(request, 'teachers/import_teachers.html')