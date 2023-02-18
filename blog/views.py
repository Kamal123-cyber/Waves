
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render, get_object_or_404

# Create your views here.



class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name = 'blog/post_new.html'
    fields = ['title','body']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post-update.html'
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


"""def Comments(request):
    cments = Comment.objects.all()
    context = {'cments':cments}
    return render(request, 'blog/comments.html', context)"""
def Home(request):
    return render(request, 'blog/home1.html')





