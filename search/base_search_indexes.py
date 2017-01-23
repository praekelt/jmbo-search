import datetime

from haystack import indexes


class ComputedField(indexes.SearchField):
    def prepare(self, obj):
        return " ".join([obj.title, obj.subtitle, obj.slug])


class IndexMixin(indexes.SearchIndex):
    text = ComputedField(document=True)
    description = indexes.CharField(model_attr="description")
    title = indexes.CharField(model_attr="title")
    pub_date = indexes.DateTimeField(model_attr="publish_on", null=True)

    def get_model(self):
        return self.model

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            publish_on__lte=datetime.datetime.now()
        )
