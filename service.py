from r4bot_sdk import register_hook_provider, unregister_hook_provider
MODULE_ID = "fortnite"
PROFILE_FIELDS_HOOK = "profile.fields"


class FortniteService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        register_hook_provider(self.module.bot, PROFILE_FIELDS_HOOK, MODULE_ID, self.build_profile_fields)

    def unregister_hooks(self):
        unregister_hook_provider(self.module.bot, PROFILE_FIELDS_HOOK, MODULE_ID)

    def build_profile_fields(self, ctx, member, user_data, server_data):
        account_id = user_data.get("fortnite")
        if not account_id:
            return []

        nickname = self.module.get_fortnite_username_to_profile(account_id) or str(account_id)
        return [{"name": "Профиль Fortnite", "value": nickname}]
