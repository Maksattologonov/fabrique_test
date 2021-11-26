from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, is_admin=False, is_staff=False, is_active=True):
        if not username:
            raise ValueError(_('The username must be set'))
        user_obj = self.model(
            username=username
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_admin=True,
            is_staff=True,
            is_active=True

        )
        return user
