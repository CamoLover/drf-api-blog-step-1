from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from .models import Article, Comment

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['id', 'account_name', 'users', 'created']

class ArticleListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'created_at', 'updated_at']

class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    # Les champs en lecture seule car ils sont gérés automatiquement
    # auteur = StringRelatedField(read_only=True)
    article = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'