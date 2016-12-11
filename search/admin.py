from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from search.models import IndexedModelBase


admin.site.register(IndexedModelBase, ModelBaseAdmin)
