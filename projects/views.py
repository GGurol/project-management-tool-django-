from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, TeamMember
from .forms import ProjectForm, TeamMemberFormSet, TeamMemberForm
from .forms import TaskForm



def project_list(request):
    # Fetch all projects to display on the home page
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    # Fetch project details and associated tasks
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()  # Ensure the `tasks` related name is correct in your `Task` model
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})


def create_project(request):
    # Handle the creation of a new project along with its team members
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        formset = TeamMemberFormSet(request.POST, instance=project_form.instance)
        
        if project_form.is_valid() and formset.is_valid():
            # Save the project and its associated team members
            project = project_form.save()  # Save the project
            formset.instance = project  # Associate the formset with the project
            formset.save()  # Save the team members
            return redirect('project_list')  # Redirect to the project list page
    else:
        project_form = ProjectForm()
        formset = TeamMemberFormSet()

    return render(request, 'create_project.html', {
        'project_form': project_form,
        'formset': formset
    })


def create_task(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            form.save_m2m()  # Save Many-to-Many relationships, e.g., dependencies
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm()
    return render(request, 'form.html', {'form': form})


def team_member_list(request):
    # List all team members
    members = TeamMember.objects.all()
    return render(request, 'team_member_list.html', {'members': members})


def create_team_member(request):
    # Handle the creation of a new team member
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list') 

def delete_task(request, project_pk, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return redirect('project_detail', pk=project_pk) 

# Edit Project
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

# Edit Task
def edit_task(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task, 'project': project})
      
