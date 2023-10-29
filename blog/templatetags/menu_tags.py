from django import template
from blog.models import Category, Post

register = template.Library()

def get_all_categories():
    return Category.objects.all()    

@register.simple_tag()
def get_sidebar_categories():
    return get_all_categories()
    

@register.inclusion_tag('blog/includes/tags/categories_menu.html')
def get_categories():
    categories = get_all_categories()
    return {'list_categories': categories}


@register.inclusion_tag('blog/includes/tags/posts_menu.html')
def get_last_posts():
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {'list_last_posts': posts}
