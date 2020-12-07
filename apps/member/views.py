from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Member, Visitor
from apps.finance.models import Contribution

class MemberList(ListView):
    model = Member
    template_name = "member/list.html"


class MemberDetailView(DetailView):
    model = Member
    template_name = "member/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contributions'] = Contribution.objects.all()
        
        return context


class MemberCreateView(CreateView):
    model = Member
    template_name = "member/create.html"
    fields = '__all__'
