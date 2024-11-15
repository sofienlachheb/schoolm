from django.shortcuts import render, redirect
from .models import Student, Note
from .forms import NoteForm
from django.contrib import messages
from django.urls import reverse

def st_notes(request,pk):
    student = Student.objects.get(pk=pk)
    notes = Note.objects.filter(student=student)
    messages.success("قائمة ملاحظات الطلاب")
    return render(request,'student_list_notes.html', {'student': student,'notes':notes})


def student_notes(request, pk):
    
    student = Student.objects.get(pk=pk)
    #notes = student.note_set.all()
    notes = Note.objects.filter(student=student)
    
    return render(request,'notes:student_notes.html', {'student': student,'notes':notes,})




def create_note(request,pk):
    student = Student.objects.get(pk=pk)
    notes = Note.objects.filter(student=student)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = student
          
            note.save()
            messages.success(request,"تم إضافة الملاحظة بنجاح")
           
            return redirect('notes:student_notes', pk=pk)
    else:
        form = NoteForm()
        #date = form.cleaned_data['date_field']
    return render(request, 'notes/create_note.html', {'form': form,'notes': notes,})

def update_note(request,pk, note_pk):
    student = Student.objects.get(pk=pk)
    note = Note.objects.get(pk=note_pk)
   
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:student_notes', pk=pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form, 'note': note})


def delete_note(request,pk, note_pk):
    student = Student.objects.get(pk=pk)
    note = Note.objects.get(pk=note_pk)
    if request.method == 'POST':
        note.delete()
        return redirect('student_notes', pk=pk)
    return render(request, 'delete_note.html', {'student':student,'note': note})


