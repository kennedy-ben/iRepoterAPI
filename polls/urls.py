from django.urls import include, path
from . import views
from polls import views as polls_views
from django.contrib.auth.views import LoginView,LogoutView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from polls.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
#    path('', include(router.urls)),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    # path('accounts/register/',Customer_views.register, name='register'),
    # path('signin/',signinView.as_view(next_page='index'), name='login'),
    # path('logout/'signinView,LogoutView.as_view(next_page='index'), name='logout'),

]

