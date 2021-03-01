from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser

OTHER_FIELD = (
    (None, {'fields': ('followers', 'following', 'profile_pic', 'background_img', 'profile_bio', 'location', 'web_url',)}),
)

class CustomUserAdmin(UserAdmin):
    model = TwitterUser
    add_fieldsets = UserAdmin.add_fieldsets + OTHER_FIELD
    fieldsets = UserAdmin.fieldsets + OTHER_FIELD

admin.site.register(TwitterUser)