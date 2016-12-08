from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from jmbo_search.models import TrivialContent


admin.site.register(TrivialContent, ModelBaseAdmin)
