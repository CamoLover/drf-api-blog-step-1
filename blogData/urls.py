from django.urls import path

from blogData.views import ArticleListView, ArticleDetailView, CommentListCreateView, CommentDetailView, ConcessionnaireListView, ConcessionnaireDetailView, ConcessionnaireVehiculeListView, ConcessionnaireVehiculeDetailView

#blogData/urls.py

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:article_pk>/comments/', CommentListCreateView.as_view(), name='Comment-list-create'),
    path('articles/<int:article_pk>/comments/<int:pk>', CommentDetailView.as_view(), name='Comment-detail'),
    
    # Endpoints pour les concessionnaires et véhicules
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', ConcessionnaireVehiculeListView.as_view(), name='concessionnaire-vehicule-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:vehicule_pk>/', ConcessionnaireVehiculeDetailView.as_view(), name='concessionnaire-vehicule-detail'),
]