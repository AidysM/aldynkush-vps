from datetime import datetime

from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Author, Rubric, New, Comment


class NewList(ListView):
    model = New
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    queryset = New.objects.order_by('-created')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['rubric'] = Rubric.objects.value_list()
        return context


