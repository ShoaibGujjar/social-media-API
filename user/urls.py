from django.urls import URLPattern, path
from user import views
# from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('userNearByMe/', views.userNearByMe),
    path('getUserInfo/',views.getUserbyid),
    path('signUp/',views.userMixinView),
    path('deleteAccount/',views.user_delete_view),
    path('edit_profile/',views.user_update_view),
    path('uploadImages/',views.add_image),
    path('deleteImages/',views.profile_delete_view)
]