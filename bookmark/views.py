from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아 동작시킨다. -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import BookMark

class BookmarkListView(ListView):
    model = BookMark

class BookmarkCreatView(CreateView):
    model = BookMark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = BookMark

class BookmarkUpdateView(UpdateView):
    model = BookMark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = BookMark
    success_url = reverse_lazy('list')