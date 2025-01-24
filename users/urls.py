from django.urls import path, include

from .custom_jwt_claims import CustomTokenObtainPairView

from users.views import  UserView, NewUserView, UpdateUserStatusView, UpdateUserView, ResetLoginAttemptsView, AdminResetUserPasswordView, ResetUserPasswordView, DeactivateUserView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    path('', include(router.urls)),

    path('users/new', NewUserView.as_view(), name='new_user'),
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('users/delete', DeleteUserView.as_view(), name='delete_user'),
    path('users/update-user-status', UpdateUserStatusView.as_view(), name='update_user_status'),
    path('users/update', UpdateUserView.as_view(), name='update_user'),
    path('users/admin-reset-login-attempts', ResetLoginAttemptsView.as_view(), name='admin_reset_login_attempts'),
    path('users/admin-reset-password', AdminResetUserPasswordView.as_view(), name='admin_reset_password'),
    path('users/user-reset-password', ResetUserPasswordView.as_view(), name='user_reset_password'),
    path('users/deactivate', DeactivateUserView.as_view(), name='deactivate'),
]