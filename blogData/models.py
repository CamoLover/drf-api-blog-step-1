from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE


# Create your models here.
class Article(Model):
    title = CharField(max_length=512)
    content = TextField()
    # author
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(Model):
    # author
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    article = ForeignKey(Article, on_delete=CASCADE, related_name='comments')