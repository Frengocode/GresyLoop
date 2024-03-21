from django.urls import path
from . import views
from .views import ChangePasswordView, MetaViewForm
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login' ),
    path('search/', views.search_view, name='seacrh'),
    path('register/', views.user_register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('users/<int:user_id>/', views.user_view, name='user_view'),
    path('profile_photo/', views.user_photo_upload_form_view, name='profile_photo_uploud'),
    path('content/', views. product_uploud_form_view, name='content'),
    path('subscribe/<int:user_id>/', views.subscribe_view, name='user_subscribe'),
    path('like/<int:user_id>/', views.like_button_view, name='like_button'),
    path('comentarion/<int:content_id>/', views.content_detail, name='commnetrion'),
    path('user_profile/', views.user_profile_view, name='profile'),
    path('comentarion_itmes/<int:pk>/', views.commnetrion_items, name='comment_items'),
    path('comentarion_like/<int:pk>/', views.comment_like_view, name='comment_like'),
    path('content_deleted/', views.content_delete_view, name='delete_uploud_contents'),
    path('content_info<int:pk>/', views.get_uploud_contents, name='get_contents'),
    path('settings/', views.settings_view, name='user_profile_settings'),
    path('get_user_action/', views.get_user_action, name='get_user_values'),
    path('add_to_fiend/<int:pk>/', views.add_user_view, name='add_friend'),
    path('comment_delete/', views.comment_delete_view, name='delete_comment'),
    path('follower_content/', views.subscribed_users_content, name='user_followers'),
    path('subscribers/', views.get_user, name='follow_to_users' ),
    path('ChangePassword/', ChangePasswordView.as_view(), name='user_password_change'),
    path('seceruty_account/', views.seceruty_user_profile, name='seceruty_user_profile'),
    path('profile_change/', views.ProfileUpdateView.as_view(), name='Change_user_profile'),
    path('MetaChanel/', MetaViewForm.as_view(), name='meta' ),
    path('get_other_user_followers/<int:pk>/', views.get_other_user_followers, name='get_user_followers')
]