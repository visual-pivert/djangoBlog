from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Influenceur
from django.contrib.auth.models import User


class InfluenceurForm(UserCreationForm):
    
    class Meta:
        model = Influenceur
        fields = ('username', 'sex', 'email')

    def save(self, commit=True):
        user = super(Influenceur, self).save(commit=True)
        if commit:
            user.save()
        return user
        