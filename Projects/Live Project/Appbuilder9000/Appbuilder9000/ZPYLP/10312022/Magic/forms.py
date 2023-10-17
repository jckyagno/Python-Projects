from django.forms import ModelForm
from .models import Deck, Comment


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
