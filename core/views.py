from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (render,
                              redirect, 
                              get_object_or_404) 
from django.contrib import messages
from django.contrib.auth import (login,
                                  authenticate,
                                    logout,
                                      update_session_auth_hash)
from .forms import (UserRegisterForm,
                     SearchForm,
                       UserProfilePhoto,
                       UserContentUpludView,
                         UserProfileSeeModel,
                           ContentUploud_Model,
                             CommnetrionForm,
                               Comment,
                                 ContentDeleteForm,
                                   CommentDeleteForm,
                                     UserProfileChangeForm,
                                     GetMeta,
                                     GetMetaForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import (PasswordChangeForm,
                                        UserChangeForm)


from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MetaViewForm(View):


    @method_decorator(login_required)
    def dispath(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        form = GetMetaForm()
        return render(request, 'meta/meta_info.html', {'form':form})

    def post(self, request, *args, **kwrags):
        if request.method == 'POST':
            form = GetMetaForm(request.POST)
            if form.is_valid():
                new_ = form.save(commit=False)
                new_.user = request.user
                new_.user_profile  = request.user
                new_.save()
                return redirect('home')
        else:
            form = GetMetaForm(request.POST)

        return render(request, 'core/meta_info.html', {'form':form})
    


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfileSeeModel
    form_class = UserProfileChangeForm
    template_name = 'user_profile_settings/profile_update.html'
    success_url = reverse_lazy('profile')

    @method_decorator(login_required)
    def dispath(self, request,  *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user




class ChangePasswordView(View):
    form_class = PasswordChangeForm
    template_name = 'password/change_password.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
        return render(request, self.template_name, {'form': form})
    





@login_required
def comment_delete_view(request):
    user = request.user
    comment = Comment.objects.filter(user=user)
    if request.method == 'POST':
        form = CommentDeleteForm(user, request.POST)
        if form.is_valid():
            selected_commentary = form.cleaned_data['comment']
            selected_commentary.delete()
            return redirect('home')
    else:
        form = CommentDeleteForm(user=user,  initial = {'commnet':comment})

    return render(request, 'delete/comment_delete.html', {'form':form})



@login_required
def content_delete_view(request):
    user = request.user
    delete = ContentUploud_Model.objects.filter(user=user)
    if request.method == 'POST':
        form = ContentDeleteForm(user,request.POST)
        if form.is_valid():
            selected_content = form.cleaned_data['delete']
            selected_content.delete()
            return redirect('home')
    else:
        form = ContentDeleteForm(user=user, initial = {'user_content':delete})
    return render(request, 'core/content_delete.html', {"form":form})



@login_required
def user_photo_upload_form_view(request):
    user_profile, created = UserProfileSeeModel.objects.get_or_create(username =  request.user)
    form = UserProfilePhoto(request.POST )

    if not created and user_profile.profile_image:
        messages.success(request, 'Профиль пользователя уже существует.')

    if request.method == 'POST':
        form = UserProfilePhoto(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            new_publish = form.save(commit=False)
            new_publish.user = request.user
            new_publish.save()
            messages.success(request, 'Фотография успешно обновлена.')
            return redirect('home')

    context = {
        "form": form
    }

    return render(request, 'core/photo_uploud.html', context)



@login_required
def home(request):
    content = ContentUploud_Model.objects.all()
    return render(request, 'core/home.html', {'content':content})


@login_required
def search_view(request):
    form = SearchForm(request.GET or None)
    users = None
    if request.method == 'GET':
        if form.is_valid():
            search = form.cleaned_data['search']
            users = UserProfileSeeModel.objects.filter(username__icontains = search)
    return render(request, 'core/search.html', {'form':form, 'users':users})


@login_required
def user_view(request, user_id):
    """

    Этот код для того что бы пользователи могли видеть профиль у друг-друга 

    """
    try:
        user_profile = UserProfileSeeModel.objects.get(pk=user_id)
        username = user_id
        return render(request, 'core/user_view.html', {'user_profile': user_profile, 'username':username })
    except UserProfileSeeModel.DoesNotExist:
        return render(request, 'core/user_view.html', {'users': {user_id}})




def user_register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    return render(request, 'core/user_register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,  password=password, )
        if user is not None:
            login(request, user)
            messages.success(request, 'LOGIN IS SUCCSES')
            return redirect('home')
    return render(request, 'core/login.html', )


@login_required
def product_uploud_form_view(request):
    form = UserContentUpludView()

    if request.method == 'POST':
        form = UserContentUpludView(request.POST, request.FILES)
        if form.is_valid():
            content_instance = form.save(commit=False)
            content_instance.user_profile = request.user
            content_instance.user = request.user

            content_instance.save()
            return redirect('home')

    return render(request, 'core/product_uploud.html', {'form': form})



@login_required
def subscribe_view(request, user_id):
    post = get_object_or_404(UserProfileSeeModel, pk=user_id)

    if request.user not in post.subscribers.all():
        post.subscribers.add(request.user)
        post.save()
        return JsonResponse({'message': 'Subscribe to user is succses'})
    else:
        return JsonResponse({'message': 'You are is subcribed to this user!'})
    

@login_required
def like_button_view(request, user_id):
    post = get_object_or_404(ContentUploud_Model, pk=user_id)

    if request.user not in post.likes.all():
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
        post.save()
    return redirect('home')
    
   
    

@login_required
def comment_like_view(request, pk):
    comment  = Comment.objects.get(pk=pk)
    if request.user not in comment.like.all():
        comment.like.add(request.user)
    else:
        comment.like.remove(request.user)
        comment.save()
    return JsonResponse({'messages':'Ваши действия были успешно сохранены '})
    


@login_required
def content_detail(request, content_id):
    content_object = ContentUploud_Model.objects.get(id=content_id)
    comments = Comment.objects.filter(content=content_id)
    """
    
    This line form line

    """
    comment_form = CommnetrionForm()
    if request.method == 'POST':
        comment_form = CommnetrionForm(request.POST)
        if comment_form.is_valid():
            new = comment_form.save(commit=False)
            new.user_profile = request.user
            new.user = request.user
            new.content = content_object
            new.save()
            return redirect('home')

    return render(request, 'core/commnetrion_view.html', {'content_object': content_object, 'comments': comments, 'comment_form': comment_form})



@login_required
def user_profile_view(request):


    """

    
    Authoficated user can cee his uploud objects end delete his
    Uploud objects but others users dont delete his uploud Objects
    None user dont can't see his profile and His uploud Objects

    

    """
    user = request.user
    profile_image_and_componetns = UserProfileSeeModel.objects.filter(username=user)
    publications = ContentUploud_Model.objects.filter(user=user)
    commnet = Comment.objects.filter(user=user)
    


    sql = {
        "profile_componetns":profile_image_and_componetns,
        'contents':publications,
        'comment':commnet
    }

    return render(request, 'core/user_profile.html', sql)


    

@login_required
def commnetrion_items(request, pk):
    comment = Comment.objects.get(pk=pk)
    return render(request, 'core/commnetrion_view.html', {'comment':comment})


@login_required
def get_uploud_contents(request, pk):
    content = ContentUploud_Model.objects.get(pk=pk)
    return render(request, 'core/content_view.html', {'content':content})


@login_required
def settings_view(request):
    return render(request, 'core/settings.html')


@login_required
def get_user_action(request):
    user = request.user
    actions = Comment.objects.filter(user=user)
    return render(request, 'core/user_actions.html', {"actions":actions})





@login_required
def add_user_view(request, pk):
    add_fiend = UserProfileSeeModel.objects.get(pk=pk)

    if request.user not in add_fiend.add_to_friend.all():
        add_fiend.add_to_friend.add(request.user)
    else:
        add_fiend.add_to_friend.remove(request.user)
        add_fiend.save()

    return JsonResponse({'message': 'Ваши действия были успешно сохранены '})
        

@login_required
def subscribed_users_content(request):

    """
    Get  subscribe user

    """

    user = request.user
    subscribers = user.add_to_friend.all()


    return render(request, 'core/subscribed_users.html', {'content': subscribers, })


@login_required
def get_user(request):
    profiles = UserProfileSeeModel.objects.all()
    return render(request, 'core/get_profile.html', {'profiles':profiles})


@login_required
def seceruty_user_profile(request):
    return render(request, 'core/seceruty.html', )


@login_required
def get_other_user_followers(request, pk):

    """
    Get subscribed users of a given user
    """

    user = UserProfileSeeModel.objects.get(pk=pk)  
    subscribers = user.add_to_friend.all()  

    return render(request, 'core/subscribed_users.html', {'content': subscribers})