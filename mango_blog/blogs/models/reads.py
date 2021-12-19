# Django
from django.utils.translation import gettext_lazy as _
from django.db import models

# mango_blog
from mango_blog.utils.models import BaseModel

class Read(BaseModel):
    """ Read Model.
    A Read is the table that holds the relationship between a user and a post.
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE)
    
    is_read_later =  models.BooleanField(
        _('read post later'),
        default=False,
        help_text=_("this field is True if a user wants to read this post later.")
    )

    is_finished = models.BooleanField(
        _('reading is finished'),
        default=False,
        help_text=_("this field is True if a user has finished to read the post.")
    )
