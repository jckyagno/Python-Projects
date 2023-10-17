from django.forms import ModelForm
from .models import Killer, KillerPerk
from .models import Survivor, SurvivorPerk

class KillerForm(ModelForm):
    class Meta:
        model = Killer
        fields = "__all__"

class KillerPerkForm(ModelForm):
    class Meta:
        model = KillerPerk
        fields = "__all__"

class SurvivorForm(ModelForm):
    class Meta:
        model = Survivor
        fields = "__all__"
class SurvivorPerkForm(ModelForm):
    class Meta:
        model = SurvivorPerk
        fields = "__all__"