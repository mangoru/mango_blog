"""Circles admin."""

# Django
from django.contrib import admin
from django.http import HttpResponse

# Model
from mango_blog.blogs.models import Post, Category, Read

# Utilities
import csv
from django.utils import timezone
from datetime import datetime, timedelta


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk","name")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = (
        'slug_name',
        'date',
        'catetegory', 
        'autor',
        'title',
        'description',
    )
    search_fields = ('slug_name', 'title', 'date')
    list_filter = (
        'is_public',
        'date',
        'catetegory',
        'autor',
    )

@admin.register(Read)
class ReadAdmin(admin.ModelAdmin):
    """Reads admin."""
    list_display = (
        'user',
        'post',
    )



    # actions = ["download_todays_Posts"]

    # def download_todays_rides(self, request, queryset):
    #     """Return today's rides."""
    #     now = timezone.now()
    #     today = datetime(now.year, now.month, now.day, 0, 0, 0)
    #     posts = Post.objects.filter(
    #         offered_in__in=queryset.values_list('id'),
    #         departure_date=today,
    #     ).order_by('title')

    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = f'attachment; filename="posts{today}.csv"'
    #     writer = csv.writer(response)
    #     writer.writerow([
    #         'id',
    #         'title',
    #         'readers',
    #         'autor',
    #         'catetegory',
    #         'description',
    #     ])
    #     for post in Post:
    #         writer.writerow([
    #             post.pk,
    #             post.title,
    #             post.read.count(),
    #             post.autor,
    #             post.catetegory,
    #             post.description,
    #         ])

    #     return response
    # download_todays_rides.short_description = 'Download todays rides'