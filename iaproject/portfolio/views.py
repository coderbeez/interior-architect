from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Category, Project, Section, Download

# Credit: Class based views Corey https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10

# Create your views here.
def projects(request):
    project_list = Project.objects.filter(exclude=False).order_by('order')
    paginator = Paginator(project_list, 3) # Show 3 blogs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Portfolio', 'page_obj': page_obj}
    return render(request, 'portfolio/projects.html', context)
    # pagination from django docs https://docs.djangoproject.com/en/3.0/topics/pagination/

def project(request, pk):
    project = Project.objects.get(pk=pk)
    sections = Section.objects.filter(project=project)
    downloads = Download.objects.filter(project=project, exclude=False)
    context = {'title': 'Portfolio', 'project': project, 'sections': sections, 'downloads': downloads}
    return render(request, 'portfolio/project.html', context)



class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects' # what u want it to loop over in template
    ordering = ['order']




class ProjectDetailView(DetailView): #expecting pk by default
    model = Project
    template_name = 'portfolio/project.html'
    context_object_name = 'project' # what u want it to loop over in template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sections'] = Section.objects.filter(project=self.object) #OR project=self.kwargs['pk']
        return context

# Credit https://stackoverflow.com/questions/39652109/django-filtering-inside-of-get-context-data


# Credit: Django docs https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/