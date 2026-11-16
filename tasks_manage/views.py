from django.shortcuts import render, redirect, get_object_or_404
from .models import TasksModel, CategoryModel
from .forms import TasksModelForm, CategoryModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

# Category views
@login_required(login_url='signin')
def create_cat(request):
    form = CategoryModelForm(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user  # Assign the current user to the category
        category.save()
        messages.success(request, "Category created successfully...")
        return redirect('read_cat')
    return render(request, 'create_cat.html', {'form':form})

@login_required(login_url='signin')
def read_cat(request):
    records = CategoryModel.objects.filter(user=request.user, is_deleted = False)  # Filter categories by the current user
    return render(request, 'read_cat.html', {'context':records})

@login_required(login_url='signin')
def update_cat(request, tid):
    record = get_object_or_404(CategoryModel, id = tid)
    form = CategoryModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Category updated successfully...")
        return redirect('read_cat')
    return render(request, 'update_cat.html', {'form':form})

@login_required(login_url='signin')
def delete_cat(request, tid):
    record = get_object_or_404(CategoryModel, id = tid)
    if request.method == 'POST':
        record.is_deleted = True
        record.save()
        messages.success(request, "Category deleted successfully...")
        return redirect('read_cat')
    return render(request, 'delete_cat.html')

def cat_history(request):
    data = CategoryModel.objects.filter(user = request.user, is_deleted = True)
    return render(request, 'cat_history.html', {'context':data})

def cat_restore(request, cid):
    record = get_object_or_404(CategoryModel, id=cid)
    if request.method == 'POST':
        record.is_deleted = False
        record.save()
        messages.success(request, "Category restored successfully...")
        return redirect('read_cat')
    return render(request, 'cat_restore.html')



# Tasks views
@login_required(login_url='signin')
def create(request):
    form = TasksModelForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user  # Assign the current user to the task
        task.save()
        messages.success(request, "Task added successfully...")
        return redirect('read')
    return render(request, 'create.html', {'form':form})

@login_required(login_url='signin')
def read(request):
    query = request.GET.get('q', '') # skills
    records = TasksModel.objects.filter(user=request.user, is_deleted = False)  # Filter tasks by the current user
    if query:
        records = records.filter(
            Q(tname__icontains = query) |
            Q(cat__cat__icontains = query)
        )
    return render(request, 'read.html', {'context':records, 'q':query})

@login_required(login_url='signin')
def update(request, tid):
    record = get_object_or_404(TasksModel, id = tid)
    form = TasksModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Task updated successfully...")
        return redirect('read')
    return render(request, 'update.html', {'form':form})

@login_required(login_url='signin')
def delete(request, tid):
    record = get_object_or_404(TasksModel, id = tid)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Task deleted successfully...")
        return redirect('read')
    return render(request, 'delete.html')

@login_required(login_url='signin')
def history(request):
    data = TasksModel.objects.filter(user = request.user, is_deleted = True)
    return render(request, 'history.html', {'context':data})

@login_required(login_url='signin')
def restore(request, tid):
    record = get_object_or_404(TasksModel, id=tid)
    if request.method == 'POST':
        record.is_deleted = False
        record.save()
        messages.success(request, "Task restored successfully...")
        return redirect('read')
    return render(request, 'restore.html')
