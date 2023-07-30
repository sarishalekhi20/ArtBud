from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields='__all__' #makes  a form with all the values on table room
        exclude=['host', 'participants'] #so that only the person who is logged in can create a room

class UserForm(ModelForm):
    class Meta:
        model = User
        fields =['username', 'email']
        # exclude = ['host', 'participants']