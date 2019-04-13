from django.shortcuts import render
from .models import Question, Comment, Article
from .forms import QuestionPostForm, CommentPostForm, ArticlePostForm,ArticleCommentForm
from django.shortcuts import get_object_or_404

import redis
from django.conf import settings
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)

#提问功能
def question_post(request):
    new_question = None

    if request.method == "POST":
        question_form = QuestionPostForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            #new_question.author = request.user
            new_question.save()
            return render(request, 'question/post_done.html', {'new_question': new_question})

    else:
        question_form = QuestionPostForm()

    return render(request, 'question/question_post.html', {'question_form': question_form})


#文章发布
def article_post(request):
    new_article = None

    if request.method == "POST":
        article_form = ArticlePostForm(data=request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            #new_question.author = request.user
            new_article.save()
            return render(request, 'article/article_post_done.html', {'new_article': new_article})

    else:
        article_form = ArticlePostForm()

    return render(request, 'article/article_post.html', {'article_form': article_form})


#首页
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question/question_list.html', {'questions': questions})


#问题详情页
def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    comments = question.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentPostForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.question = question
            # new_comment.writer = request.user
            new_comment.save()

    else:
        comment_form = CommentPostForm()

    #浏览量
    total_view = r.incr('question:{}:views'.format(question.id))
    r.zincrby('hot_question', question.id, 1)

    return render(request, 'question/question_detail.html', {'question': question,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form,
                                                    'total_view': total_view})


#文章详情页
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.article_comment.all()
    #浏览量
    article_views = r.incr('article:{}:views'.format(article.id))
    new_article_comment = None

    if request.method == "POST":
        article_comment_form = ArticleCommentForm(data=request.POST)
        if article_comment_form.is_valid():
            new_article_comment = article_comment_form.save(commit=False)
            new_article_comment.article = article
            # new_comment.writer = request.user
            new_article_comment.save()

    else:
        article_comment_form = CommentPostForm()

    return render(request, 'question/templates/article/article_detail.html', {'article': article,
                                                            'comments': comments,
                                                            'article_views': article_views,
                                                            'new_article_comment': new_article_comment,
                                                            'article_comment_form': article_comment_form})


def question_hot(request):
    hot_questions = r.zrange('hot_question', 0, -1, desc=True)
    hot_question_ids = [int(id) for id in hot_questions]
    most_viewed = list(Question.objects.filter(id__in=hot_question_ids))
    most_viewed.sort(key=lambda x: hot_question_ids.index(x.id))
    scores = [int(r.zscore('hot_question', id)) for id in hot_question_ids]
    return render(request, 'question/question_hot.html', {'most_viewed': most_viewed,
                                                 'scores': scores})


def article_list(request):
    articles = Article.objects.filter(status='published')
    return render(request, 'article/article_list.html', {'articles': articles})