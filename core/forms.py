from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import UserProfileSeeModel,ContentUploud_Model, Comment , GetMeta
from django.conf import settings


class MessageForm(forms.Form):
    text = forms.CharField(label='Message', widget=forms.TextInput(attrs={'placeholder': 'Type your message here...'}))


class UserProfileChangeForm(UserChangeForm):
    class Meta (UserChangeForm.Meta) :
        model  = UserProfileSeeModel
        fields = ['username', ]

class CommnetrionForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



class UserContentUpludView(ModelForm):
    class Meta:
        model = ContentUploud_Model
        fields = ['content', 'content_title']

class UserProfilePhoto(ModelForm):
    class Meta:
        model = UserProfileSeeModel
        fields = ['profile_image']

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfileSeeModel
        fields = ['username', 'password1', 'password2']




class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, label='Search...')


class ContentDeleteForm(forms.Form):
    delete = forms.ModelMultipleChoiceField(
        queryset = None,
        widget= forms.CheckboxSelectMultiple,
        label='Delete uploud content'
    )

    def __init__(self, user, *args, **kwargs):
        super(ContentDeleteForm, self).__init__(*args, **kwargs )
        self.fields['delete'].queryset = ContentUploud_Model.objects.filter(user=user)




class CommentDeleteForm(forms.Form):
    comment = forms.ModelMultipleChoiceField(
        queryset=None, 
        widget = forms.CheckboxSelectMultiple,
        label = 'Delete commentary'
    )

    def __init__(self, user, *args, **kwargs):
        super(CommentDeleteForm, self).__init__(*args, **kwargs)
        self.fields['comment'].queryset = Comment.objects.filter(user=user)



class GetMetaForm(ModelForm):
    class Meta:
        model = GetMeta
        fields = '__all__'
        exclude = ('user', 'user_profile',)
