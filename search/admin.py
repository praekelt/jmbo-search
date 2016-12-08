from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from search.models import IndexedTrivialContent


admin.site.register(IndexedTrivialContent, ModelBaseAdmin)
