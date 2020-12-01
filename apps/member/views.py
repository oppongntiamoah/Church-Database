from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Member, Visitor


class MemberList(ListView):
    model = Member
    template_name = "member/list.html"


class MemberDetailView(DetailView):
    model = Member
    template_name = "member/detail.html"


class MemberCreateView(CreateView):
    model = Member
    template_name = "member/create.html"
    fields = '__all__'
