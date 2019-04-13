import datetime
from haystack import indexes
from question.models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='author')
    publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(publish__lte=datetime.datetime.now())

