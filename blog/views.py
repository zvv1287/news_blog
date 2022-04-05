from datetime import datetime
from django.core.paginator import Paginator

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Category, Post, Comment, Tag
from .forms import CommentForm


class PostListView(View):
    """Вывод статей категории"""

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, slug=None):
        products_on_page = 6
        if category_slug is not None:
            category = Category.objects.filter(slug=category_slug)
            categories = category.get_descendants(include_self=True)
            posts = self.get_queryset().filter(category__in=categories,
                                               category__published=True)
            if category:
                products_on_page = category.first().paginated

        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_queryset()

        if posts.exists():
            template = posts.first().get_category_template()
        else:
            if Category.objects.filter(slug=category_slug):
                template = "blog/post_list.html"
            else:
                raise Http404()

        page = request.GET.get('page', 1)
        paginator = Paginator(posts, products_on_page)

        return render(request, template, {"posts": paginator.page(page)})


class PostDetailView(View):
    """Вывод полной статьи"""

    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        form = CommentForm()
        return render(request, post.template,
                      {"categories": category_list, "post": post, "form": form}
                      )

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get("slug"))
            form.author = request.user
            form.save()
        return redirect(request.path)



