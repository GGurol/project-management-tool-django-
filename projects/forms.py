from django import forms
from django.forms import inlineformset_factory
from .models import Project, TeamMember, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'email']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'status', 'assigned_to', 'dependencies']

# Inline formset to manage Team Members dynamically
TeamMemberFormSet = inlineformset_factory(
    Project,
    TeamMember,
    form=TeamMemberForm,
    extra=1,
    can_delete=True
)
