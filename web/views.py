from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message

# Create your views here.

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']      

# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']     
    success_url = reverse_lazy('msg_list')