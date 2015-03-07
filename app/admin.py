from django.contrib import admin
from app.models import Label, Article


admin.site.register((Label, Article))
