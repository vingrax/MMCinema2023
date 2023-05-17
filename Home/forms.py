from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter correct username and password"
        ),
        'inactive': _("This account is inactive."),
    }


class MyLoginView(LoginView):
    authentication_form = MyAuthForm