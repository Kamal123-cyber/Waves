
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, comment
from django.urls import reverse_lazy
from django.db.models import Q 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render, get_object_or_404

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 10
    ordering = ['-date']

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name = 'blog/post_new.html'
    fields = ['title','body', 'image']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post-update.html'
    fields = ['title','body','image']

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

#class SearchResultView(ListView):
 #   model = Post
  #  template_name = 'blog/search.html'
   # context_object_name = 'search_result'

    #def get_queryset(self):
     #   query = self.request.GET.get('q', default='')
      #  res = Post.objects.filter(Q(title__icontains=query))
       # return res


def search(request):
    template_name = 'blog/search.html'
    query = request.GET.get('q', default = '')
    if query:
        #query example
        results = Post.objects.filter(Q(title__icontains=query))
    else:
         results = []
    return render(
        request, template_name, {'results': results})


def Home(request):
    return render(request, 'blog/home1.html')

def About(request):
    return render(request, 'blog/about.html')

def Comments(request,post_pk):
    comme = comment.objects.filter(post_id=post_pk)
    return render(request, 'blog/comment.html',{'comme':comme})




