from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogsAppConfig(AppConfig):
    """Blogs app config."""
    name = "mango_blog.blogs"
    verbose_name = _("blogs")

