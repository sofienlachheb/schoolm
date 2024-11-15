from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 
                  'teacherName',
                  'teacherFunction', 
                  'teacherPhone', 
                  'teacherEmail', 
                  'profile_image', 
                  'grades',
                  ]
        
        widgets = {
            
            'grades': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-check form-check-inline',  # Adding custom classes
                    'aria-label': 'form-check-label',         # Adding aria-label
                }
            ),
        }
        labels = {
            'teacherName': 'اسم المدرس',
            'teacherFunction': 'المسمى الوظيفي',
            'teacherPhone': 'رقم الهاتف',
            'teacherEmail': 'البريد الالكتروني',
            'profile_image': 'صورة المدرس',
            'grades': 'الصفوف الدراسية',
        }
       # grades = forms.ModelMultipleChoiceField(
       #    queryset=Grade.objects.all(),
      #     widget=forms.SelectMultiple(attrs={
        #    'class': 'form-select',
     #       'aria-label': 'multiple select example'
      #  }),
      #  required=True
   # )
    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        teacherEmail = cleaned_data.get('teacherEmail')
        teacherPhone = cleaned_data.get('teacherPhone')

        # Check if user already exists
        if Teacher.objects.filter(user=user).exists():
            self.add_error('user', "يوجد شخص مسجل بهذا الإسم.")

        # Check if email already exists
        if Teacher.objects.filter(teacherEmail=teacherEmail).exists():
            self.add_error('teacherEmail', "يوجد شحص مسجل بهذا الإميل.")

        # Check if phone already exists
        if Teacher.objects.filter(teacherPhone=teacherPhone).exists():
            self.add_error('teacherPhone', "يوجد شخص أخر بنفس رقم الجوال.")

        return cleaned_data