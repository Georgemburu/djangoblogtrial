from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
# from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]


class ProfilePicForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_pic'
        ]