# views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from .models import User

def register(request):
    msg=None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            # Set user type based on selection
            
            form.save()
            msg='تم إنشاء مستخدم جديد بنجاح'
            return redirect('managers:manager_dashboard')
        else:
            msg='هناك خطأ'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form,'user': request.user})



def login_view(request):
    #form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('managers:manager_dashboard')
                elif user.is_teacher:
                    return redirect(reverse_lazy('teachers:teacher_profile'))
                elif user.is_parent:
                    return redirect(reverse_lazy('parents:parent_dashboard'))
                elif user.is_student:
                    return redirect(reverse_lazy('students:student_dashboard'))
                else:
                    msg= 'invalid credentials'
    else:
        msg = 'error validating form'
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



class ChangePasswordView(PasswordChangeView):
    template_name = "managers/persons/change_password.html"
    success_url = reverse_lazy('account:user_password_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "تغيير كلمة المرور"
        return context

@login_required()
def password_change_done(request):
    return render(request, "managers/persons/change_password_done.html", {"page_title": "تم تغيير كلمة المرور بنجاح"})

def logout_view(request):
    logout(request)
    return redirect('login')

def all_users(request):
    users=User.objects.all()
    return render(request,'all_users.html',{'users':users})

def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
    else:
        form = SignUpForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})
@login_required
def user_delete(request, pk):
    if not request.user.is_admin:
        messages.error(request, "You do not have permission to delete users.")
        return redirect('all_users')

    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, f"User {user.username} has been deleted successfully.")
        return redirect('all_users')

    return render(request, 'user_delete.html', {'user': user})