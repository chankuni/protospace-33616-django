from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import PostPrototype
from comments.forms import CommentForm
from django import forms
from .models import Prototype
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class PrototypeList(ListView):
  template_name = 'prototypes/index.html'
  model = Prototype

class PrototypeCreate(LoginRequiredMixin, CreateView):
  form_class = PostPrototype # 作成した登録用フォームを設定
  template_name = "prototypes/new.html" 
  success_url = reverse_lazy("prototypes:list") # ユーザー作成後のリダイレクト先ページ

  def form_valid(self, form):
      prototype = form.save(commit=False)
      prototype.user = self.request.user
      prototype.save()
      return super().form_valid(form)

class PrototypeDetail(LoginRequiredMixin, DetailView):
  model = Prototype
  template_name = 'prototypes/detail.html'

class PrototypeDetail(View):
    def get(self, request, *args, **kwargs):
        prototype_id = self.kwargs['pk']
        prototype = Prototype.objects.get(pk=prototype_id)
        comments = Comment.objects.filter(prototype__id = prototype_id)
        form = CommentForm()  # コメントフォームを初期化
        return render(request, 'prototypes/detail.html', {'prototype': prototype, 'form': form, 'comments': comments})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
          content = form.cleaned_data['content']
          Comment.objects.create(content=content, user_id=request.user.id, prototype_id=self.kwargs['pk'])
          return redirect('prototypes:detail', self.kwargs['pk'])
        
        # フォームが無効な場合は、フォームにエラーメッセージと共に元のページに戻る
        prototypes = Prototype.objects.all()
        return render(request, 'prototypes/index.html', {'prototypes': prototypes, 'form': form})

class PrototypeUpdate(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
  model = Prototype
  form_class = PostPrototype
  template_name = 'prototypes/update.html'
   
  def get_success_url(self):
    return reverse('prototypes:detail', kwargs={'pk': self.kwargs['pk']})
  
  def test_func(self, **kwargs):
       """アクセスできるユーザーを制限"""
       pk = self.kwargs["pk"]
       prototype = Prototype.objects.get(pk=pk)
       return (prototype.user == self.request.user) 
  
  def handle_no_permission(self):
        return redirect('prototypes:list') 

class PrototypeDelete(LoginRequiredMixin, DeleteView):
  model = Prototype
  success_url = reverse_lazy('prototypes:list')

