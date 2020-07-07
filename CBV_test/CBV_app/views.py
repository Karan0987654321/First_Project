from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,DeleteView,CreateView,UpdateView
from . import models
from django.urls import reverse_lazy


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class Comp_List(ListView):
    model = models.Company
    context_object_name = 'comp_list'

class Comp_Detail(DetailView):
    print('k/n')
    model = models.Company
    context_object_name = 'comp_det'
    template_name = 'CBV_app/Company.details.html'

class CreateV(CreateView):
    model = models.Company
    fields = ('__all__')
    template_name = 'CBV_app/Company_create.html'

class DeleteV(DeleteView):
    model = models.Company
    success_url = reverse_lazy('CBV_app:list')
    template_name = 'CBV_app/Company_delete.html'

class UpdateV(UpdateView):
    fields = '__all__'
    model = models.Company
    template_name = 'CBV_app/Company_update.html'

