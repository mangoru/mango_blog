# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Mango Blog
from mango_blog.utils.models import BaseModel
from mango_blog.users.models import User

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField(_('Autor Biography'))
    photo = models.ImageField(
        _('Photo of Autor.'),
        null=True,
        blank=True,
        upload_to='autors/',
    )