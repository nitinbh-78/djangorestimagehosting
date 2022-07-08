from django.contrib import admin
from django.contrib.auth.models import User

from app.models import Account, ThumbnailSize, Plan, Image, Thumbnail, TemporalLink

admin.site.register(Account)
admin.site.register(Plan)
admin.site.register(Image)
admin.site.register(ThumbnailSize)
admin.site.register(TemporalLink)
admin.site.register(Thumbnail)