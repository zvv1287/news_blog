from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag, Post, Comment
from pages.admin import ActionPublish


class CategoryAdmin(ActionPublish):
    """Категории блога"""
    list_display = ("id", "name", "parent", "slug", "paginated", "sort", "published")
    list_display_links = ("name", "slug",)
    list_editable = ("published",)
    actions = ['unpublish', 'publish']
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(label="Полное содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = '__all__'


class PostAdmin(ActionPublish):
    """Посты блога"""
    list_display = ("id", "title", "category", "created_date", "published_date", "published")
    list_display_links = ("title",)
    list_editable = ("published",)
    inlines = [CommentsInline]
    form = PostAdminForm
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug'),
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'image'),
        }),
        ('Даты', {
            'fields': ('edit_date', 'published_date'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category'),
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('template', 'published', 'status', 'sort', 'viewed'),
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

admin.site.site_title = "Course django 2"
admin.site.site_header = "Course django 2"
