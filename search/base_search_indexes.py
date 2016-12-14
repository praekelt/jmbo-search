import datetime

from haystack import indexes


class IndexMixin(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr="description")
    title = indexes.CharField(model_attr="title")
    pub_date = indexes.DateTimeField(model_attr="publish_on")

    def get_model(self):
        return self.model

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            publish_on__lte=datetime.datetime.now()
        )
