from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from account.models import User 
from .models import *
from .forms import SubjectsForm,SiteSettingForm
from django.shortcuts import get_object_or_404
from .forms import UserUploadForm
from django.contrib import messages
import openpyxl
from django.contrib.auth import get_user_model
#################################################################################
def manager_dashboard(request):
     context = {
        
        "User_count": User.objects.first(),
        "page_title": "إدارة الموقع",
     }
     return render(request,'managers/manager_dashboard.html',context)
########################    Subjects       ########################################################
def all_subjects(request):
      subjects=Subjects.objects.all()
    
      return render(request, 'managers/subjects/all_subjects.html', {'subjects': subjects})
    
def subjects_add(request):
    if request.method == 'POST':
      
        form = SubjectsForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            
            form.save()
            return redirect('managers:all_subjects')
        else:
            print("Form errors:", form.errors)
    else:
        form = SubjectsForm()
    return render(request, 'managers/subjects/subjects_add.html', {'form': form})

def subjects_edit(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)
    if request.method == 'POST':
        form = SubjectsForm(request.POST, request.FILES,instance=subject)
        if form.is_valid():
            form.save()
            return redirect('managers:manager_dashboard')
    else:
        form = SubjectsForm(instance=subject)
    
    return render(request, 'managers/subjects/subjects_edit.html', {'form': form})

def subject_delete(request,pk):
   subject=Subjects.objects.get(pk=pk)
   if request.method=='POST':
       subject.delete()
       return redirect('managers:manager_dashboard')
   return render(request, 'managers/subjects/subject_delete.html', {'subject': subject})
############################################# WebSite Setting ##########################
def all_settings(request):
      setting1=SiteSetting.objects.all()
      return render(request,'managers/setting/setting_list.html',setting1)
def setting_add(request):
      if request.method=='POST':
         form=SiteSettingForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
            return redirect('managers:manager_dashboard')
      else:
            form=SiteSettingForm()
      return render(request,'managers/setting/setting_add.html',{'form': form})
   
   
def setting_edit(request,pk):
         setting1=SiteSetting.objects.get(pk=pk)
         if request.methode=='POST':
               form=SiteSettingForm(request.POST,instance=setting1)
               if form.is_valid():
                      form.save()
                      return redirect('managers:all_subjects')
         else:
               form=SiteSettingForm(instance=setting1)
         return render(request,'managers/setting/setting_edit.html',{'form': form})
def setting_delete(request,pk):    
       setting1=SiteSetting.objects.get(pk=pk)
       if request.method=='POST':
              setting1.delete()
              return redirect('managers:all_subjects')
       return render(request,'managers/setting/setting_delete.html',setting1)
##############################   Users Students uploaded ##################################
User = get_user_model()  # Use the custom user model
def upload_users(request):
    if request.method == 'POST':
        form = UserUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data.get('excel_file')

            if excel_file:
                # Open the workbook
                wb = openpyxl.load_workbook(excel_file)
                # Select the active worksheet
                worksheet = wb.active

                # Iterate through the rows in the worksheet
                for row in worksheet.iter_rows(min_row=2):  # Assuming the first row is the header
                    if len(row) >= 3:  # Ensure there are at least 3 columns (username, email, password)
                        email = row[1].value
                        password = row[2].value

                        # Extract the username by removing the domain part (@education.qa)
                        if email:
                            username = email.split('@')[0]

                            # Create or update the user if username is provided
                            user, created = User.objects.get_or_create(username=username)
                            user.email = email
                            user.set_password(password)
                            user.save()

                messages.success(request, 'Users have been successfully uploaded!')
                return redirect('all_users')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserUploadForm()

    return render(request, 'managers/files/upload_users.html', {'form': form})