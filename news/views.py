from datetime import datetime

from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author, Rubric, New, Comment
from .forms import NewForm


class NewListView(ListView):
    model = New
    template_name = 'news/new_list.html'
    context_object_name = 'news'
    queryset = New.objects.order_by('-created')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.values_list()
        return context


class NewDetailView(DetailView):
    template_name = 'news/new_detail.html'
    queryset = New.objects.all()


class NewCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_new',)
    template_name = 'news/new_create.html'
    form_class = NewForm
    success_url = '/news/'


class NewUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_new',)
    template_name = 'news/new_create.html'
    form_class = NewForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию
    # об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'news/new_delete.html'
    queryset = New.objects.all()
    success_url = '/news/'


