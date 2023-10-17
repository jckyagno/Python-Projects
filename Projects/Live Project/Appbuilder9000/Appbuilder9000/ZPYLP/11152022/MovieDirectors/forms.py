from django.forms import ModelForm

from .models import Director


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        labels = {
            'name': 'Name',
            'numberOfMovies': 'Number Of Movies Directed',
            'yearOfFirstMovie': 'Release Year of First Movie',
            'primaryGenre': 'Primary Genre',
            'deceased': 'Deceased?',
        }
