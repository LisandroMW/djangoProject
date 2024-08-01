from django import forms
#from .models import Project
class CreateNewTask(forms.Form):
    title = forms.CharField(label= 'Titulo de la tarea', max_length=200, widget=forms.TextInput)#(attrs={'class': 'input'}))
    description = forms.CharField(label='descripción de la tarea', widget=forms.Textarea)#(attrs={'class': 'input'}))
    #project = forms.ModelChoiceField(queryset=Project.objects.all())
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del projecto', max_length=200)#, widget=forms.TextInput(attrs={'class':'input'}))
    