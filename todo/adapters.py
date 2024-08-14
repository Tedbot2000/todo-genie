# myapp/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages


class MyAccountAdapter(DefaultAccountAdapter):

    def add_message(self, request, level, message_template, message_context=None, extra_tags='', fail_silently=False):
        """
        Utility method to add a message to the user via the messaging framework.
        """
        if message_context is None:
            message_context = {}
        message = self.render_mail(message_template, message_context).message()
        messages.add_message(request, level, message, extra_tags, fail_silently)

    def login(self, request, user):
        # Customize the login message
        messages.success(request, 'You have successfully logged in.')
        return super().login(request, user)

    def logout(self, request):
        # Customize the logout message
        messages.success(request, 'You have successfully logged out.')
        return super().logout(request)

    def post_signup(self, request, user):
        # Customize the signup message
        messages.success(request, 'Signup successful. Welcome!')
        return super().post_signup(request, user)

    def post_reset_password(self, request, user):
        # Customize the password reset message
        messages.success(request, 'Password reset instructions have been sent to your email.')
        return super().post_reset_password(request, user)
