from django.db import models
from django.urls import reverse
from django.utils import timezone
from simditor.fields import RichTextField


class Question(models.Model):
    title = models.CharField(max_length=300, verbose_name='标题')
    #body = models.TextField(blank=True)
    body = RichTextField(verbose_name='详细描述', blank=True)
    #author
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:question_detail', args=[self.id])


class Comment(models.Model):
    question = models.ForeignKey(Question, related_name='comments',
                                 on_delete=models.CASCADE)

    answer = RichTextField(verbose_name="回答")
    #image = models.ImageField(upload_to='comment/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.answer


class Article(models.Model):
    STATUS_CHOICES = (('draft', '草稿'), ('published', '发布'))
    #题图
    image_above = models.ImageField(upload_to='article/%Y/%m/%d', verbose_name="题图", blank=True)
    title = models.CharField(max_length=200, verbose_name="文章标题")
    article = RichTextField(verbose_name="文章")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name="状态",
                              default='draft')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:article_detail', args=[self.id])


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, related_name='article_comment',
                                on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.comment






