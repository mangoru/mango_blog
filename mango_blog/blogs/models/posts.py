# Django
from django.utils.translation import gettext_lazy as _
from django.db import models
from ckeditor.fields import RichTextField

# mango_blog
from mango_blog.utils.models import BaseModel
from mango_blog.users.models.profiles import Profile

class Category(BaseModel):
    name = models.CharField(
        _('category name'),
        max_length=35,
        unique=True,
    )

    picture = models.ImageField(
        _('image of category'),
        upload_to='category/',
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class Post(BaseModel):
    """Post model."""
    title = models.CharField(max_length=255)
    slug_name = models.CharField(max_length=35, unique=True)
    description = models.TextField(
        _('Description of post'),
    )
    catetegory = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
    )
    autor = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    content = RichTextField()
    date = models.DateField(
        _('Date of posted.'),
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    is_public = models.BooleanField(
        default=True,
        help_text='Public Posts are listed in the main page so everyone know about their existence.'
    )
    reads = models.ManyToManyField(
        'users.User',
        through='blogs.Read',
        through_fields=('post','user')
    )
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo