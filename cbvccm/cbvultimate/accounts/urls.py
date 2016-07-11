from django.conf.urls import url
from django.contrib.auth.views import login as auth_login, logout as auth_logout, password_change, password_change_done
from .views import UserRegistrationView, UserProfileDetailView, UserProfileEditView

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(), name='register'),
    url(r'^login/$', auth_login, name='login'),
    url(r'^logout/$', auth_logout, name='logout',
        kwargs={'template_name': 'registration/logout.html'}),

    # User Profile

    url(r'^profile/(?P<slug>\w+)/$',
        UserProfileDetailView.as_view(), name='profile'),
    url(r'^edit_profile/$', UserProfileEditView.as_view(), name='update_profile'),

    url(r'^change_password/$', password_change, name='password_change',
        kwargs={'template_name': 'accounts/password_change_form.html',
                'post_change_redirect': 'accounts:password_change_done', }),
    url(r'^change_password_done/$', password_change_done, name='password_change_done',
        kwargs={'template_name': 'accounts/change_password_done.html'}),

]
