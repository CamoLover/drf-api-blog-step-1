from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, FloatField, IntegerField
from django.core.exceptions import ValidationError
from apiBlog import settings


def validate_siret(value):
    if len(value) != 14:
        raise ValidationError('Le SIRET doit faire exactement 14 caractères.')


# Create your models here.
class Article(Model):
    title = CharField(max_length=512)
    content = TextField()
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(Model):
    content = TextField()
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    article = ForeignKey(Article, on_delete=CASCADE, related_name='comments')


class Concessionnaire(Model):
    nom = CharField(max_length=64)
    siret = CharField(max_length=14, validators=[validate_siret])

    def __str__(self):
        return self.nom


class Vehicule(Model):
    TYPE_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
    ]
    
    type = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    chevaux = IntegerField()
    prix_ht = FloatField()
    concessionnaire = ForeignKey(Concessionnaire, on_delete=CASCADE, related_name='vehicules')

    def __str__(self):
        return f"{self.marque} ({self.type}) - {self.concessionnaire.nom}"